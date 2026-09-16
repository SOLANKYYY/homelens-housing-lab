from pathlib import Path
import re,sys
p=Path(__file__).resolve().parents[1]
if len(sys.argv)!=2 or not re.fullmatch(r"[A-Za-z0-9_.-]+",sys.argv[1]):raise SystemExit("Usage: python scripts/update_repo_links.py NEW-REPO-NAME")
old="https://github.com/SOLANKYYY/House-Price-Prediction-ML-Project"
new="https://github.com/SOLANKYYY/"+sys.argv[1]
for f in list(p.glob("*.md"))+list((p/"docs").glob("*.html")):
 f.write_text(f.read_text(encoding="utf-8").replace(old,new),encoding="utf-8")
print("Updated current showcase links; historical source notes retained.")
