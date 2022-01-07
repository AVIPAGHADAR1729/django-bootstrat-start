from django.urls import path

# views
from app import views

urlpatterns = [

	path('',views.home,name='home')
]