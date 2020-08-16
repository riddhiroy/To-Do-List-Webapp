from django.urls import path ,include
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('create',views.create,name='create'),
    path('view/',views.view,name="view"),
    path('<int:id>',views.index, name='index')
]