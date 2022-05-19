from django.shortcuts import render, redirect
from .form import ApplicationForm
from .models import Application
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.core.paginator import Paginator


@login_required(login_url='login')
def search_application(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        if request.user.is_superuser:
            target = Application.objects.all()
        else:
            target = Application.objects.filter(owner=request.user)
        applications = target.filter(
            first_name__contains=searched).order_by('first_name')
        context = {'searched': searched, 'applications': applications}
        return render(request, 'application/search_app.html', context)

    else:
        return render(request, 'application/search_app.html', context)


@login_required(login_url='login')
def see_application(request, application_id):
    application = Application.objects.get(pk=int(application_id))
    context = {'form': application}
    return render(request, 'application/see_application.html', context)


@login_required(login_url='login')
def edit_application(request, application_id):
    application = Application.objects.get(pk=int(application_id))
    owner = application.owner
    form = ApplicationForm(
        request.POST or None, instance=application)
    if request.method == 'POST':
        form = ApplicationForm(
            request.POST, request.FILES, instance=application)
        if form.is_valid():
            application = form.save(commit=False)
            application.owner = owner
            application.save()
            # form.save()
            messages.success(
                request, "Application Succesfully Updated!")
            return redirect('admin_approval')
    context = {'form': form}
    return render(request, 'application/edit_application.html', context)


@login_required(login_url='login')
def start_application(request):
    form = ApplicationForm()
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():

            application = form.save(commit=False)
            application.owner = request.user
            application.save()
            # form.save()
            messages.success(
                request, "Application Succesfully Created!")
            return redirect('dashboard')

    context = {'form': form}
    return render(request, 'application/application.html', context)


@login_required(login_url='login')
def dashboard(request):
    if request.user.is_authenticated and request.user.is_superuser:
        savedApplications = Application.objects.all().order_by('first_name')
        context = {'applications': savedApplications}
        return render(request, 'application/index.html', context)
    else:
        owner = request.user
        savedApplications = Application.objects.filter(
            owner=owner).order_by('first_name')
        context = {'applications': savedApplications}
        return render(request, 'application/index.html', context)


@login_required(login_url='login')
def admin_approval(request):
    if request.user.is_superuser and request.user.is_authenticated:
        allApplications = Application.objects.all().order_by('first_name')
        context = {'applications': allApplications}
        return render(request, 'application/admin_approval.html', context)
    else:
        messages.success(request, "You are not Allowed to access this Page!")
        return render(request, 'application/index.html', context)
