import json
import sys
import os
import xmind
from xmind.core.topic import TopicElement

def build_topic(root, data):
    root.setTitle(data.get("title",""))
    notes=data.get("notes")
    if isinstance(notes,dict):
        if "html" in notes:
            root.setPlainNotes(notes["html"])
        elif "plain" in notes:
            root.setPlainNotes(notes["plain"])
    elif isinstance(notes,str):
        root.setPlainNotes(notes)
    # 跳过 labels/markers 以提升兼容性
    children=data.get("children",[])
    for ch in children:
        t = root.addSubTopic()
        build_topic(t, ch)

def main():
    in_path=sys.argv[1] if len(sys.argv)>1 else "bp_mindmap.json"
    with open(in_path,"r",encoding="utf-8") as f:
        data=json.load(f)
    out_path=data["path"]
    wb = xmind.load(out_path)
    sheet = wb.getPrimarySheet()
    sheet.setTitle(data["sheets"][0].get("title","Sheet"))
    root = sheet.getRootTopic()
    # 先设置根主题标题，避免空根导致文件结构异常
    root.setTitle(data["sheets"][0]["rootTopic"].get("title","Root"))
    build_topic(root, data["sheets"][0]["rootTopic"])
    xmind.save(wb, out_path)
    print(out_path)

if __name__=="__main__":
    main()
