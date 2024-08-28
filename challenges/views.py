from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": None
}

def home_page(request):
    month_list = ""
    months = list(monthly_challenges.keys())
    return render(request,"challenges/index.html",{
        'month_list' : months
    })
    # for month in months:
    #     redirected_path = reverse("monthly-challenges",args=[month])
    #     month_list += f'<li><a href="{redirected_path}">{month}</li>'
    # response_data = f"<ul>{month_list}</ul>"
    # try:
    #     return HttpResponse(response_data)
    # except:
    #     return HttpResponseNotFound("Not Found!")

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html",{
            'text' : challenge_text,
            'month' : month
        })
        # render_data = render_to_string('challenges/challenge.html')
        # return HttpResponse(render_data)
        # return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("Not Found!")


def monthly_challenge_bynumber(request, month):
    try:
        challenge_text = list(monthly_challenges.values())[month-1]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("Incorrect number")


def monthly_challenge_bynumber_redirect(request, month):
    month = list(monthly_challenges.keys())[month-1]
    redirect_path = reverse("monthly-challenges",args=[month])
    return HttpResponseRedirect(redirect_path)

    #return HttpResponseRedirect("/challenges/"+month)
    # The above causes error when the url of the app changes in
    # the main project urls.py file.
    # To over come the issue we use in built function 'reverse'
    # which automatically redirects to the previous or parent address(url)