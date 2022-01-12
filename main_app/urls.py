from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name= 'home'),
  #about/
  path('about/', views.about, name= 'about'),
  #'finches/ to finches index route
  path('finches/', views.finches_index, name='finches_index'),
  #'finches/<int:finch_id>'
  path('finches/<int:finch_id>/', views.finches_detail, name='finches_detail'),
  #'finches/create- to show form to add a new Finch
  path('finches/create', views.FinchCreate.as_view(), name='finches_create'),
  #'finches/int:pk/update/'
  path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='finches_update'),
  #'finches/<int:pk/delete/'
  path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finches_delete')
]