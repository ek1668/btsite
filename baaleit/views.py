from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Thebig5, Sublink, BT, BTone, BTtwo, BTthree, Post, BTOnePost, BTTwoPost, BTThreePost, Community, SublinkCommunity, Learning, SublinkLearning, Technology, SublinkTechnology

# Create your views here.

def index(request):
  
  return render(request, 'index.html')

def big5(request):
  thebig5 = Thebig5.objects.all()
  sublink = Sublink.objects.all()
  return render(request, 'big5.html', {'thebig5': thebig5, 'sublink': sublink})

def community(request):
  community = Community.objects.all()
  sublinkcommunity = SublinkCommunity.objects.all()
  return render(request, 'community.html', {'community': community, 'sublinkcommunity': sublinkcommunity})

def learning(request):
  # bt = BT.objects.all()
  learning = Learning.objects.all()
  sublinklearning = SublinkLearning.objects.all()
  return render(request, 'learning.html', {'learning':learning, 'sublinklearning':sublinklearning})

def technology(request):
  technology = Technology.objects.all()
  sublinktechnology = SublinkTechnology.objects.all()
  return render(request, 'technology.html', {'technology': technology, 'sublinktechnology': sublinktechnology})

def topic(request, pk):
  # sublink = Sublink.objects.all()
  sublink = Sublink.objects.filter(name=pk)
  # sublinkcommunity = SublinkCommunity.objects.filter(name=pk)
  return render(request, 'topic.html', {'sublink': sublink})

def communitytopic(request, pk):
  # sublink = Sublink.objects.all()
  # sublink = Sublink.objects.filter(name=pk)
  sublinkcommunity = SublinkCommunity.objects.filter(name=pk)
  return render(request, 'communitytopic.html', {'sublinkcommunity': sublinkcommunity})

def learningtopic(request, pk):
  # sublink = Sublink.objects.all()
  # sublink = Sublink.objects.filter(name=pk)
  sublinklearning = SublinkLearning.objects.filter(name=pk)
  return render(request, 'learningtopic.html', {'sublinklearning': sublinklearning})

def technologytopic(request, pk):
  # sublink = Sublink.objects.all()
  # sublink = Sublink.objects.filter(name=pk)
  sublinktechnology = SublinkTechnology.objects.filter(name=pk)
  return render(request, 'technologytopic.html', {'sublinktechnology': sublinktechnology})

def btstories(request):
  # sublink = Sublink.objects.all()
  # sublink = Sublink.objects.filter(name=pk)
  btone = BTone.objects.all()
  bttwo = BTtwo.objects.all()
  btthree = BTthree.objects.all()
  
  return render(request, 'btstories.html', {'btone': btone, 'bttwo': bttwo, 'btthree': btthree})

def personalrabbi(request):
  if request.method == 'POST':
    bt = BT.objects.all()
    bt = BT()
    firstname = request.POST.get("firstname")
    lastname = request.POST.get("lastname")
    age = request.POST.get("age")
    email = request.POST.get("email")
    phone_number = request.POST.get("phone")
    rstatus = request.POST.get("relationshipstatus")
    rbackground = request.POST.get("background")
    location = request.POST.get("location")
    bt.firstname=firstname
    bt.lastname=lastname
    bt.age=age
    bt.email=email
    bt.phone_number=phone_number
    bt.rstatus=rstatus
    bt.rbackground=rbackground
    bt.location=location
    bt.save()
    # return HttpResponse('<h1>THANKS FOR THE INFO{{bt}}<h1>')
  return render(request, 'personalrabbi.html')

def btone(request):
  btone = BTone.objects.all()
  
# def post(request):
#   return render(request, 'post.html')

def btone(request):
  posts = BTOnePost.objects.all()
  return render(request, 'btone.html', {'posts': posts})

def bttwo(request):
  posts = BTTwoPost.objects.all()
  return render(request, 'bttwo.html', {'posts': posts})

def btthree(request):
  posts = BTThreePost.objects.all()
  return render(request, 'btthree.html', {'posts': posts})

def onepost(request, pk):
  posts = BTOnePost.objects.get(id=pk)
  return render(request, 'onepost.html', {'posts': posts})

def twopost(request, pk):
  posts = BTTwoPost.objects.get(id=pk)
  return render(request, 'twopost.html', {'posts': posts})

def threepost(request, pk):
  posts = BTThreePost.objects.get(id=pk)
  return render(request, 'threepost.html', {'posts': posts})