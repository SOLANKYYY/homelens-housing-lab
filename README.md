# HomeLens — Housing Regression Lab

An explainable housing-regression lab with feature contributions, dataset documentation, and reproducible synthetic or California Housing experiments.

**By Solanki Om Narendra · [SOLANKYYY](https://github.com/SOLANKYYY)**

[Original repository](https://github.com/SOLANKYYY/House-Price-Prediction-ML-Project) · [Dataset notes](DATASET.md) · [Deployment](DEPLOYMENT.md) · [Repository settings](REPOSITORY-DETAILS.md)

## Explore the website

Open `OPEN-HomeLens.html` for the self-contained main page, or serve the complete website:

```powershell
python -m http.server 8000
```

Visit http://localhost:8000/docs/ . The exported model is bundled; Python training is not needed to view the site. No npm installation, API key, database or backend is required.

## What you can do

- The included model uses synthetic teaching data. It does not estimate current property prices.
- Inspect dataset facts, evidence and limitations.
- Follow the method from input to output.
- Read the source snapshots and reproduce supported experiments.

## Evidence and evaluation

Included SYNTHETIC run: 600 generated records, 480 train / 120 test, MAE 0.1858 target units and R² 0.9400. These are not California Housing results. The real dataset download timed out in the build environment.

New evaluations use scikit-learn 1.8.0. Full metrics and model conditions, where applicable, are recorded in `research/evaluation.json`. New runs are distinct from historical notebook outputs.

## Tools and architecture

Python, NumPy, scikit-learn LinearRegression. Original plotting: matplotlib and seaborn.

Website: semantic HTML, responsive CSS, vanilla JavaScript and inline SVG. Inference and calculations run inside the browser. User inputs are not stored or uploaded by this code. The hosting provider may retain ordinary access logs.

## Reproduce

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements-showcase.txt
.\.venv\Scripts\python scripts/export_model.py
python scripts/build_standalone.py
```

To replace the synthetic model with California Housing (internet required):

```powershell
.\.venv\Scripts\python scripts/export_model.py --california
python scripts/build_standalone.py
```

The exporter updates the website dataset label, metrics and model. Update any README descriptions that still describe the included synthetic run.

Optional verification (Node.js required):

```powershell
node tests/test.cjs .
```

After editing HTML, CSS, JavaScript or model data, regenerate the one-file preview with `python scripts/build_standalone.py`.

## Project structure

| Path | Purpose |
| --- | --- |
| `docs/` | Deployable website |
| `docs/logic.js` | Pure calculation functions |
| `docs/data.js` | Exported model/data or empty configuration |
| `scripts/` | Reproduction and standalone-page builder |
| `research/original/` | Original code/data snapshots |
| `research/` | Provenance and evaluation notes |
| `tests/` | Numeric parity and interaction checks |
| `OPEN-HomeLens.html` | Self-contained main-page preview |

Original root-level code in your GitHub repository is preserved when this kit is copied over it. The supplied source snapshots are in `research/original/`. Run historical code only with its original dependencies; the showcase requirements cover the new exporters.

## Interpretation and limitations

### Can I value a home with this?

No. The included data is synthetic. Even the original California dataset represents 1990 block-group medians, not current individual home valuations.

### How do I use the real California dataset?

Run python scripts/export_model.py --california, then python scripts/build_standalone.py. This downloads the dataset, trains the model and updates the site data and evaluation report.

### Why can a linear model give a negative value?

OLS is unconstrained and can extrapolate implausibly. The interface keeps the raw result visible instead of silently clamping it. Correlated inputs also limit coefficient interpretation.

## Deploy and present

Deploy `docs` as a static site. Follow [DEPLOYMENT.md](DEPLOYMENT.md), then place the actual deployed URL in the GitHub About panel. Suggested repository name: `homelens-housing-lab`. The name is a suggestion, not a completed rename.

## Attribution and licensing

Original project: SOLANKYYY. Existing code and dataset licenses, where present, continue to apply. This kit does not assign a new license to third-party data or imply that undocumented data is unrestricted. Review upstream provenance before redistributing data independently.
