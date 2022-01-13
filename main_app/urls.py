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
  path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),
  #'finches/int:pk/update/'
  path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='finches_update'),
  #'finches/<int:pk/delete/'
  path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finches_delete'),
  #path for adding feedings, not  CVB so use finch_id
  path('finches/<int:finch_id>/add_feeding/', views.add_feeding, name='add_feeding'),
  #path to a list of all toys
  path('toys/', views.ToyList.as_view(), name='toys_index'),
  #path to associate toys with a finch
  path('finches/<int:finch_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
  #path to a detail of a toy
  path('toys/<int:pk>/detail', views.ToyDetail.as_view(), name='toys_detail'),
  # path to create toys
  path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
  #path to update toys
  path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update')
]