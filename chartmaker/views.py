from django.shortcuts import render
import json
import requests
from random import randrange
# Create your views here.
def home(request):

    r = requests.get('https://api.github.com/search/repositories?q=all+language')
    packages_json = r.json()
    length = len(packages_json['items'])

    language = dict()

    for i in range(length):
        packages_str = json.loads(json.dumps(packages_json['items'][i]['language']))
        if packages_str != None:
            if packages_str in language:
                language[packages_str]+=1
            else:
                language[packages_str] = 1
    data = [['Language Name', 'Count in Repos ']]
    data.extend([[key, value] for key, value in language.items()])
    modified_data = json.dumps(data)
    return render(request, 'charts.html', {'values': modified_data})