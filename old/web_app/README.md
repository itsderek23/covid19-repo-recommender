# Covid19-Repo-Recommender Web app

This web app creates an HTTP API for model inference.

## Setup

```
python3 -m venv covid19-rec-web
source covid19-rec-web/bin/activate
pip install -r requirements.txt
```

The web app has a different set of requirements than training.

## Running the web app

```
uvicorn main:app --reload
```

## Model Inference API

```
curl --location --request POST 'http://localhost:8000/predict' \
--header 'Content-Type: application/json' \
--data-raw '{"columns":[0,1],"index":[0],"data":[["Python","Data"]]}'
```

## Deploying to Heroku

```
heroku create
git push heroku master
heroku buildpacks:set https://github.com/timanovsky/subdir-heroku-buildpack
heroku buildpacks:add heroku/python
heroku config:set PROJECT_PATH=app
```

As `web_app` is contained within a mono-repo related to the Covid19-Repo-Recommender project, we need to tell Heroku to set the project path to the `/web_app` directory vs. the default (the root directory). The `subdir` buildpack and `PROJECT_PATH` env var are used for this. Setup based on [this SO response](https://stackoverflow.com/questions/39197334/automated-heroku-deploy-from-subfolder).
