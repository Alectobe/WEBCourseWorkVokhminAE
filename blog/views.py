from django.shortcuts import render


def app1(request):
    return render(request, 'blog/comfort_form.html')
