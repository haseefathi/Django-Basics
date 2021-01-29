from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World</h1>") 
    return render(request, 'home.html', {})

def contact_view(request, *args, **kwargs):
    my_context = {
        "name": "Haseeba",
        "age": 21,
        "phone": "+971559135140",
        "family": ["vapa","umma","sudy","random",123],
        "my_html": "<h5>Random heading</h5>"
    }
    return render(request, 'contact.html', my_context)