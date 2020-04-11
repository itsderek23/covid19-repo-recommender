# Covid19-Repo-Recommender Web app

This web app creates an HTTP API for model inference.

## Setup

This

```
python3 -m venv covid19-rec-web
source covid19-rec-web/bin/activate
pip install -r requirements.txt
```

## Running the web app

```
uvicorn main:app --reload
```

## Deploying to Heroku

```
heroku create
git push heroku master
heroku buildpacks:set https://github.com/timanovsky/subdir-heroku-buildpack
heroku buildpacks:add heroku/python
heroku config:set PROJECT_PATH=web_app
```

As `web_app` is contained with a mono-repo related to the Covid19-Repo-Recommender project, we need to tell Heroku to set the project path to the `/web_app` directory vs. the default (the root directory). The `subdir` buildpack and `PROJECT_PATH` env var are used for this.
