from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name= 'home'),
  #about/
  path('about/', views.about, name= 'about'),
  #'finches/ to finches index route
  path('finches/', views.finches_index, name='finches_index'),
  #'finches/<int:finch_id>'
  path('finches/<int:finch_id>/', views.finches_detail, name='finches_detail')
]