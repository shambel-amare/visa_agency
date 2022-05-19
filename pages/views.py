from django.shortcuts import redirect, render


def index(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return render(request, 'pages/index.html')


def howto(request):

    return render(request, 'pages/howto.html')
