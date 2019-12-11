from django.shortcuts import render

# Create your views here.


def test_request(request):
    print(request.session.session_key)
    return 1
