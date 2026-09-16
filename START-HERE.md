# Start with HomeLens

1. Open `OPEN-HomeLens.html`, or run `python -m http.server 8000` and visit http://localhost:8000/docs/ .
2. Read README.md, DATASET.md and REPOSITORY-DETAILS.md.
3. Upload from a fresh Git clone with the commands below. They preserve repository history and the original root-level code.

Assumes the extracted archive is at `C:\Users\omnso\Downloads\Five-Project-Showcases`:

```powershell
cd "$env:USERPROFILE\Downloads"
git clone https://github.com/SOLANKYYY/House-Price-Prediction-ML-Project.git HomeLens-GitHub
if ($LASTEXITCODE -ne 0) { throw "Clone failed; stop here." }
cd HomeLens-GitHub
Copy-Item "$env:USERPROFILE\Downloads\Five-Project-Showcases\HomeLens\*" . -Recurse -Force
git add .
git diff --cached --stat
git commit -m "Add HomeLens interactive showcase and research documentation"
git push
```

If `HomeLens-GitHub` already exists, use a different new folder name. If a Git command fails, stop and resolve that error before continuing. Do not force-push.

Rename only after the first successful push; see REPOSITORY-DETAILS.md. Then deploy using DEPLOYMENT.md.
