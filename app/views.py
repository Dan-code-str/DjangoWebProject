"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def WebPage1(request):
    """Renders the test page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/WebPage1.html',
        {
            'title':'WebPage1',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def feed(request):
    """Renders the feed page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/feed.html',
        {
            'title':'feed',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def dashboard(request):
    """Renders the dashboard page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/dashboard.html',
        {
            'title':'dashboard',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
