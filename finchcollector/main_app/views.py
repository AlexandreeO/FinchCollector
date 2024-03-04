from django.shortcuts import render

finches = [
    {'name': 'Sunny', 'species': 'Zebra Finch', 'description': 'vibrant colors, cheerful chirps', 'age': 1},
    {'name': 'Pippin', 'species': 'Gouldian Finch', 'description': 'striking plumage, melodious song', 'age': 2},
    {'name': 'Tweetie', 'species': 'Society Finch', 'description': 'friendly and social', 'age': 1},
]


# Create your views here.
def home(request):
    return render(request, 'home.html')