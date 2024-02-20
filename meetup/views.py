from django.shortcuts import render, redirect
from django.http import HttpResponse
from meetup.forms import RegistrationForm

from meetup.models import Meetup


# Create your views here.
def index(request):
    meetings = Meetup.objects.all()
    return render(
        request,
        "meetup\index.html",
        {"show_message": False, "meetings": meetings},
    )


def meetup_detail(request, meetup_slug):
    try:
        selected_meeting = Meetup.objects.get(slug=meetup_slug)
        print("selected_meeting", selected_meeting.slug)
        if request.method == "GET":
            registration_form = RegistrationForm()
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                participant = registration_form.save()
                selected_meeting.participants.add(participant)
                return redirect("meetup:success", meetup_slug=selected_meeting.slug)
        return render(
            request,
            "meetup\meetup_details.html",
            {
                "is_meetup_found": True,
                "meeting": selected_meeting,
                "form": registration_form,
            },
        )
    except Exception as exc:
        print("error:......", exc)
        return render(
            request,
            "meetup\meetup_details.html",
            {"is_meetup_found": False},
        )


def successView(request, meetup_slug):
    meetup = Meetup.objects.get(slug=meetup_slug)
    return render(
        request, "meetup/success.html", {"organizer_email": meetup.organizer_email}
    )
