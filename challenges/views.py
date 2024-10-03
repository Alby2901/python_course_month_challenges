from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
import datetime

# Create your views here.

monthly_challenges = {
    "january": "Gennaio",
    "february": "Febbraio",
    "march": "Marzo",
    "april": "Aprile",
    "may": "Maggio",
    "jun": "Giugno",
    "julay": "Luglio",
    "august": "Agosto",
    "september": "Settembre",
    "october": "Ottobre",
    "november": "Novembre",
    "december": "Dicembre",
}


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    mounth_redirect = months[month-1]
    return HttpResponseRedirect(mounth_redirect)

    # month_text = datetime.date(1900, month, 1).strftime('%B').lower()
    # return HttpResponseRedirect(month_text)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("Mese inesistente!")

    # if month in monthly_challenges:
    #     return HttpResponse(monthly_challenges[month])
    # else:
    #     return HttpResponseNotFound("Mese inesistente!")
    # return HttpResponse(challenge_text)
