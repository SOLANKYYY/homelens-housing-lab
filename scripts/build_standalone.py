from pathlib import Path
import base64
p=Path(__file__).resolve().parents[1];d=p/"docs"
s=(d/"index.html").read_text(encoding="utf-8")
s=s.replace('<link rel="stylesheet" href="styles.css">','<style>'+(d/"styles.css").read_text(encoding="utf-8")+'</style>')
for name in ["data.js","logic.js","app.js"]:
 code=(d/name).read_text(encoding="utf-8").replace("</script", "<\\/script")
 s=s.replace('<script src="'+name+'"></script>','<script>'+code+'</script>')
s=s.replace('href="favicon.svg"','href="data:image/svg+xml;base64,'+base64.b64encode((d/"favicon.svg").read_bytes()).decode()+'"')
s=s.replace('href="research-notes.html"','href="docs/research-notes.html"')
(p/"OPEN-HomeLens.html").write_text(s,encoding="utf-8")
print("Built OPEN-HomeLens.html")
