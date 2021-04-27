from django.shortcuts import redirect


def backhome(request):
    return redirect ('/landing/home/')