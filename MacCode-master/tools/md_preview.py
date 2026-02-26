#!/usr/bin/env python3
import argparse
import os
import sys
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs


def read_file(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except UnicodeDecodeError:
        with open(path, "r", encoding="latin-1") as f:
            return f.read()


class MarkdownPreviewHandler(BaseHTTPRequestHandler):
    md_path: str = ""
    server_started_at: float = time.time()

    def _send_headers(self, status=200, content_type="text/html; charset=utf-8", extra_headers=None):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        if extra_headers:
            for k, v in extra_headers.items():
                self.send_header(k, v)
        self.end_headers()

    def log_message(self, fmt, *args):
        return

    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == "/":
            return self._serve_index()
        elif parsed.path == "/content":
            return self._serve_content()
        elif parsed.path == "/meta":
            return self._serve_meta()
        else:
            self._send_headers(404, "text/plain; charset=utf-8")
            self.wfile.write(b"Not Found")

    def _serve_index(self):
        title = os.path.basename(self.md_path)
        html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Markdown Preview · {title}</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/github-markdown-css@5.5.1/github-markdown-light.min.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/highlight.js@11.9.0/styles/github.min.css">
  <style>
    body {{ margin: 0; padding: 0; background: #f6f8fa; }}
    header {{
      position: sticky; top: 0; z-index: 10;
      display: flex; align-items: center; gap: 12px;
      padding: 10px 16px; background: #fff; border-bottom: 1px solid #eaecef;
      font-family: -apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif;
    }}
    header .file {{ font-weight: 600; }}
    header .status {{ color: #57606a; font-size: 12px; }}
    header .controls {{ margin-left: auto; display: flex; gap: 8px; align-items: center; }}
    #app {{ max-width: 900px; margin: 24px auto; padding: 24px; background: #fff; border: 1px solid #eaecef; border-radius: 8px; }}
    .markdown-body {{ box-sizing: border-box; min-width: 200px; max-width: 100%; }}
    .hidden {{ display: none; }}
  </style>
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/highlight.js@11.9.0/lib/common.min.js"></script>
</head>
<body>
  <header>
    <span class="file">{title}</span>
    <span class="status" id="status">Initializing...</span>
    <div class="controls">
      <label>Refresh interval (ms)
        <input id="interval" type="number" min="250" step="250" value="1000" style="width:100px;">
      </label>
      <button id="toggle">Pause</button>
      <button id="refresh">Refresh Now</button>
    </div>
  </header>
  <main id="app" class="markdown-body">Loading...</main>
  <script>
    marked.setOptions({{ mangle: false, headerIds: true }});
    const statusEl = document.getElementById('status');
    const appEl = document.getElementById('app');
    const intervalEl = document.getElementById('interval');
    const toggleBtn = document.getElementById('toggle');
    const refreshBtn = document.getElementById('refresh');
    let timer = null;
    let running = true;
    let lastVersion = '';

    async function fetchMeta() {{
      try {{
        const r = await fetch('/meta?ts=' + Date.now(), {{ cache: 'no-store' }});
        return await r.json();
      }} catch (e) {{
        return null;
      }}
    }}

    async function render() {{
      try {{
        const meta = await fetchMeta();
        if (meta) {{
          const v = meta.version;
          const updated = meta.updated;
          statusEl.textContent = 'Updated: ' + updated + ' · Version: ' + v;
          if (v === lastVersion && appEl.dataset.loaded === '1') {{
            return;
          }}
          lastVersion = v;
        }}
        const resp = await fetch('/content?ts=' + Date.now(), {{ cache: 'no-store' }});
        const md = await resp.text();
        const html = marked.parse(md);
        appEl.innerHTML = html;
        appEl.dataset.loaded = '1';
        document.querySelectorAll('pre code').forEach((el) => window.hljs.highlightElement(el));
      }} catch (e) {{
        statusEl.textContent = '加载失败: ' + e;
      }}
    }}

    function startLoop() {{
      stopLoop();
      timer = setInterval(render, parseInt(intervalEl.value, 10) || 1000);
      running = true;
      toggleBtn.textContent = 'Pause';
    }}
    function stopLoop() {{
      if (timer) clearInterval(timer);
      running = false;
      toggleBtn.textContent = 'Resume';
    }}
    intervalEl.addEventListener('change', () => running ? startLoop() : null);
    toggleBtn.addEventListener('click', () => running ? stopLoop() : startLoop());
    refreshBtn.addEventListener('click', render);
    render();
    startLoop();
  </script>
</body>
</html>
"""
        self._send_headers(200, "text/html; charset=utf-8")
        self.wfile.write(html.encode("utf-8"))

    def _serve_meta(self):
        try:
            st = os.stat(self.md_path)
            version = f"{int(st.st_mtime)}-{int(st.st_size)}"
            updated = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(st.st_mtime))
            payload = f'{{"version":"{version}","updated":"{updated}"}}'
            self._send_headers(200, "application/json; charset=utf-8")
            self.wfile.write(payload.encode("utf-8"))
        except Exception as e:
            self._send_headers(500, "application/json; charset=utf-8")
            self.wfile.write(f'{{"error":"{e}"}}'.encode("utf-8"))

    def _serve_content(self):
        try:
            md = read_file(self.md_path)
            st = os.stat(self.md_path)
            etag = f'{int(st.st_mtime)}-{int(st.st_size)}'
            self._send_headers(200, "text/plain; charset=utf-8", {"ETag": etag})
            self.wfile.write(md.encode("utf-8"))
        except FileNotFoundError:
            self._send_headers(404, "text/plain; charset=utf-8")
            self.wfile.write(b"# File not found")
        except Exception as e:
            self._send_headers(500, "text/plain; charset=utf-8")
            self.wfile.write(f"# Load failed: {e}".encode("utf-8"))


def main():
    parser = argparse.ArgumentParser(description="Local Markdown live preview server")
    parser.add_argument("path", help="Markdown file path (.md)")
    parser.add_argument("--port", type=int, default=8765, help="Server port, default 8765")
    args = parser.parse_args()

    md_path = os.path.abspath(args.path)
    if not os.path.exists(md_path):
        print(f"Error: file not found -> {md_path}", file=sys.stderr)
        sys.exit(1)
    if not md_path.lower().endswith(".md"):
        print(f"Warning: target is not .md file -> {md_path}", file=sys.stderr)

    handler_cls = MarkdownPreviewHandler
    handler_cls.md_path = md_path
    server = ThreadingHTTPServer(("127.0.0.1", args.port), handler_cls)
    print(f"MD Preview Server: http://localhost:{args.port}/")
    print(f"Previewing file: {md_path}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
