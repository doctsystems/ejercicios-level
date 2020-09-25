from django.urls import path
from .views import *

urlpatterns=[
	path ('', IndexView, name='home'),
	path ('post/', PersonaViewAjax, name="post_persona"),
]