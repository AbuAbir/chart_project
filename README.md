# chart_project

This project is built with the help of google charts, https://developers-dot-devsite-v2-prod.appspot.com/chart
and Django 3 as backend framework to visualize language used in repositories collected from github API in an interactive 
form of pie chart, bar chart and table form.

# Installation:
['corechart'] and ‘table’ package needs to be used

I used the Django framework as a backend to work with the github API. In order to work with Python3, I used pip3 to install all the package dependencies.

I created a virtual environment with the help of “conda” to keep all my works separate irrespective of base system configuration.

I provided a “requirements.txt” in which all necessary python packages are compiled with their working version, I had to run 
pip3 install -r requirements.txt inside the django project directory.

# Woking Method:
Called the API in views.py and since this is the controller of the Django architecture, and then passed the result in JSON to the template with 
template tagging and with necessary adjustments, showed the charts.


Host to Heroku:

Make changes in the settings.py file to resolve the error of “collectstatic --noinput”
This line needs to be added:
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
Setup the heroku with the help of git and github and push the changes for deployment
git push heroku master


We need to write a “Procfile” at the project level. Inside the file, process name “web” needs to be written, followed by gunicorn, the project name.wsgi 
to talk to the server
web: gunicorn chart_project.wsgi

Now, in the settings, we need to add the heroku url in the allowed host array.

In production, debug should be false and the secret key should be different than what we use in the local system.


At this step, the environment variable was causing some problems and so the deployment was not successful.


