from multiprocessing import context
from re import template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse

import projects
from .models import Projects

# Create your views here.
def index(request):
    projects = Projects.objects.all().values()
    context = {
        'projects':projects
    }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def add_record(request):
    name = request.POST['name']
    link = request.POST['link']
    project = Projects(name=name, link=link)
    project.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    project = Projects.objects.get(id=id)
    project.delete()
    return HttpResponseRedirect(reverse('index'))

def update(request, id):
    project = Projects.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'project':project
    }
    return HttpResponse(template.render(context, request))

def update_record(request, id):
    name = request.POST['name']
    link = request.POST['link']
    project = Projects.objects.get(id=id)
    project.name = name
    project.link = link
    project.save()
    return HttpResponseRedirect(reverse('index'))

