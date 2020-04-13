# Covid19 Repo Recommender

This is a data science project created with the [cookiecutter data science project template](https://drivendata.github.io/cookiecutter-data-science/).

The Jupyter Notebook files train a model that recommends GitHub Covid19-related repos based on a programming language and keywords. The [web app](/app) (start via `honcho -f Procfile.dev start`) exposes an HTTP API to run model inference.

## Setup

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements-dev.txt
python -m ipykernel install --user --name=venv
```

## DVC

[Data Version Control](https://dvc.org) is used for model versioning of the `models/model.pkl` file. A remote is pre-configured with:

```
dvc remote add -d s3remote s3://dvc-booklet/covid19-rec
```

To grab the latest:

```
dvc pull
```

After running the Notebook to train the model, commit and push the latest model version:

```
dvc add models/model.pkl
dvc push
```



## Running the web app

```
honcho -f Procfile.dev start
```

See the [/app](app/) folder for more details, including deploy instructions.

## Cookiecutter Project Organization

Below is generated from Cookiecutter.


    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
