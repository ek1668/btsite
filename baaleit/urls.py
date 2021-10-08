from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('big5/', views.big5, name='big5'),
  path('community/', views.community, name='community'),
  path('learning/', views.learning, name='learning'),
  path('technology/', views.technology, name='technology'),
  path('big5/topic/<str:pk>', views.topic, name='topic'),
  path('community/communitytopic/<str:pk>', views.communitytopic, name='communitytopic'),
  path('learning/learningtopic/<str:pk>', views.learningtopic, name='learningtopic'),
  path('technology/technologytopic/<str:pk>', views.technologytopic, name='technologytopic'),
  # path('btstories/<str:pk>', views.btstories, name='btstories'),
  path('btstories/btone/', views.btone, name='btone'),
  path('btstories/bttwo/', views.bttwo, name='bttwo'),
  path('btstories/btthree/', views.btthree, name='btthree'),
  path('btstories/btone/onepost/<str:pk>', views.onepost, name='onepost'),
  path('btstories/bttwo/twopost/<str:pk>', views.twopost, name='twopost'),
  path('btstories/btthree/threepost/<str:pk>', views.threepost, name='threepost'),
  # path('btstories/post/<str:pk>', views.post, name='post'),
  # path('btstories/post/<slug:name>', views.post, name='post'),
   path('btstories/', views.btstories, name='btstories'),
  path('personalrabbi/', views.personalrabbi, name='personalrabbi')
  
]