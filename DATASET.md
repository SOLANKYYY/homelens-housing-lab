# HomeLens: dataset and evidence

Included SYNTHETIC run: 600 generated records, 480 train / 120 test, MAE 0.1858 target units and R² 0.9400. These are not California Housing results. The real dataset download timed out in the build environment.

### Can I value a home with this?

No. The included data is synthetic. Even the original California dataset represents 1990 block-group medians, not current individual home valuations.

### How do I use the real California dataset?

Run python scripts/export_model.py --california, then python scripts/build_standalone.py. This downloads the dataset, trains the model and updates the site data and evaluation report.

### Why can a linear model give a negative value?

OLS is unconstrained and can extrapolate implausibly. The interface keeps the raw result visible instead of silently clamping it. Correlated inputs also limit coefficient interpretation.

## Sources

- [Original repository](https://github.com/SOLANKYYY/House-Price-Prediction-ML-Project)
- [scikit-learn California Housing](https://scikit-learn.org/stable/datasets/real_world.html#california-housing-dataset)
