from django.shortcuts import render

def home(request):
	import json
	import requests

	api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=06320&distance=25&API_KEY=F5B9B468-7698-421C-8A35-3226296AA89F")

	try:
		api = json.loads(api_request.content)

	except Exception as e:
		api = "Error..."

	return render(request, 'home.html', {'api': api})


def about(request):
	return render(request, 'about.html', {})