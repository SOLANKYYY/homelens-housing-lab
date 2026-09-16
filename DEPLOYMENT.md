# Deploy HomeLens

1. Copy this kit into a fresh clone of the original repository, then commit and push (commands in START-HERE.md).
2. Open [Vercel New Project](https://vercel.com/new) and import that GitHub repository.
3. Framework Preset: **Other**.
4. Root Directory: **docs**.
5. Build Command: enable Override and leave it empty.
6. Output Directory: **.** (the docs root).
7. Install Command: leave empty. Environment variables: none.
8. Deploy, open the assigned URL, and paste it into the GitHub About Website field.

The included `docs/vercel.json` declares the static build settings. Deploy only `docs`, not the source snapshots or Python scripts. No server-side inference is needed.

Check the page on desktop and phone: navigation, example selection, inputs, result updates and source links. This environment completed numeric and DOM-harness tests, but did not complete browser visual verification.

For local viewing:

```powershell
python -m http.server 8000
```

Open http://localhost:8000/docs/ . Ctrl+C stops the local server; it does not stop a Vercel deployment.

Future edits: modify files, regenerate `OPEN-HomeLens.html` if desired, commit and push. A connected Vercel project redeploys on pushes to its configured production branch.

[Official Vercel static build instructions](https://vercel.com/docs/builds/configure-a-build#skip-build-step)
