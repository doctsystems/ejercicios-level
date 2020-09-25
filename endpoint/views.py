from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .models import *
from .forms import *

def IndexView(request):
	form=PersonaForm()
	personas=Persona.objects.all().order_by('-id')
	return render (request, "endpoint/index.html", {"form": form, "personas": personas})

def PersonaViewAjax(request):
	if request.is_ajax and request.method=="POST":
		form=PersonaForm(request.POST)
		if form.is_valid():
			instance=form.save()
			ser_instance = serializers.serialize('json', [instance,])
			print('todo ok')
			return JsonResponse({"instance": ser_instance}, status=200)
		else:
			print('error de else')
			return JsonResponse({"error": form.errors}, status=300)
	print('error gral')
	return JsonResponse({"error": ""}, status=400)
