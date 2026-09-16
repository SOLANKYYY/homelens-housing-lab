# GitHub repository details

Display name: **HomeLens — Housing Regression Lab**

Suggested repository name: `homelens-housing-lab`

Description (paste in About):

An explainable housing-regression lab with feature contributions, dataset documentation, and reproducible synthetic or California Housing experiments.

Topics (enter separately):

`machine-learning regression explainable-ai california-housing scikit-learn data-visualization javascript`

Website: paste your actual Vercel deployment URL after deploying. A suggested slug is not a reserved or deployed domain.

In About, keep Deployments enabled. Show Releases or Packages only if you use those features.

## Rename after pushing

In the existing GitHub repository, open Settings → General → Repository name. Enter `homelens-housing-lab` and choose Rename. Then, inside your local Git clone:

```powershell
git remote set-url origin https://github.com/SOLANKYYY/homelens-housing-lab.git
python scripts/update_repo_links.py homelens-housing-lab
python scripts/build_standalone.py
git add .
git commit -m "Update repository links after rename"
git push
```

Update the connected repository in Vercel if necessary and check the live Source link. This package has not changed your remote repository.
