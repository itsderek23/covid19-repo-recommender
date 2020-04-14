# Covid19-Repo-Recommender Web app

This is a web app to run model inference. The web app is powered by FastAPI.

## Running the web app

From the project root:

```
honcho -f Procfile.dev start
```

If the application file (`main.py`) is updated or `/models/restart.py` is touched, the app is reloaded automatically in development mode.

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
heroku buildpacks:add heroku/python
heroku config:set AWS_ACCESS_KEY_ID=[INSERT VALUE]
heroku config:set AWS_SECRET_ACCESS_KEY=[INSERT VALUE]
```

The AWS access keys are needed to get the serialized `models/model.pkl` file.
