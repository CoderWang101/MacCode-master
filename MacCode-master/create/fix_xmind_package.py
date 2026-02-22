import zipfile
from datetime import datetime
import os
import sys

def fix(path):
    with zipfile.ZipFile(path, 'a') as z:
        names = set(z.namelist())
        if 'meta.xml' not in names:
            meta = '''<?xml version="1.0" encoding="UTF-8"?>
<meta xmlns="urn:xmind:xmap:xmlns:meta:2.0">
  <Creator>Trae</Creator>
  <Modifier>Trae</Modifier>
  <CreateTime>{ts}</CreateTime>
  <SaveTime>{ts}</SaveTime>
  <Version>1.0</Version>
</meta>
'''.format(ts=datetime.utcnow().isoformat()+"Z")
            z.writestr('meta.xml', meta)
        if 'styles.xml' not in names:
            styles = '''<?xml version="1.0" encoding="UTF-8"?>
<styles xmlns="urn:xmind:xmap:xmlns:style:2.0">
</styles>
'''
            z.writestr('styles.xml', styles)
        if 'META-INF/manifest.xml' not in names:
            manifest = '''<?xml version="1.0" encoding="UTF-8"?>
<manifest xmlns="urn:xmind:xmap:xmlns:manifest:1.0">
  <file-entry full-path="content.xml" media-type="text/xml"/>
  <file-entry full-path="styles.xml" media-type="text/xml"/>
  <file-entry full-path="meta.xml" media-type="text/xml"/>
</manifest>
'''
            z.writestr('META-INF/manifest.xml', manifest)

if __name__ == '__main__':
    p = sys.argv[1] if len(sys.argv) > 1 else '/Users/white/Desktop/Code/MacCode-master/create/BP_Neural_Network_MindMap.xmind'
    if os.path.exists(p):
        fix(p)
        print('fixed', p)
    else:
        print('file not found', p)
