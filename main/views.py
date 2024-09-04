from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306259963',
        'name': 'Andreas Timothy',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)