# mlops-course

MLOps for AI Engineers and Data Scientists

# Session 3

- python -m venv venv
- pip install fastapi uvicorn gunicorn
- touch \_\_init.py
- touch Procfile
- Install the Heroku CLI
  - `npm i -g heroku`
  - heroku login
- create Procfile
- add this `web: gunicorn __init__:app`
- Create a new Git repository
  ````bash
  git init
  $ heroku git:remote -a mlops-flask-heroku```
  ````
- Deploy your application

````bash
$ git add .
$ git commit -am "make it better"
$ git push heroku master```
````

https://github.com/JosephItopa/My_Best_Projects/tree/MLOps-for-AI-Engineers-and-Data-Scientist/Solar_Energy_Project/solar-app
