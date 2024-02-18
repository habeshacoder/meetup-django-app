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


def meetup_detail(request, meetup_slug):
    selected_meeting = {
        "title": "meeting one",
        "location": "NewYork",
        "description": "do not miss this amazing zoom meeting that will happen next Monday",
    }

    return render(
        request,
        "meetup\meetup_details.html",
        {
            "title": selected_meeting["title"],
            "description": selected_meeting["description"],
        },
    )
