from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    meetings = [
        {
            "title": "meeting one",
            "location": "NewYork",
            "slug": "a-first-meetup",
        },
        {
            "title": "meeting two",
            "location": "America",
            "slug": "a-second-meetup",
        },
    ]
    return render(
        request,
        "meetup\index.html",
        {"show_message": False, "meetings": meetings},
    )
