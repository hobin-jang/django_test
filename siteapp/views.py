from django.shortcuts import render, get_object_or_404, redirect
from .models import Content, Comment
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def home(request):
  contents = Content.objects
  content_list = Content.objects.all()
  paginator = Paginator(content_list,5)
  page = request.GET.get('page')
  posts = paginator.get_page(page) 
  return render(request,'home.html',{'contents':contents, 'posts':posts})

def detail(request, contents_id):
  contents_detail = get_object_or_404(Content, pk=contents_id)
  comments = Comment.objects.filter(post = contents_id)

  if (request.method=="POST"):
    comment = Comment()
    comment.body = request.POST['body']
    comment.post = contents_detail
    comment.writer = request.user
    comment.date = timezone.now()
    comment.save()

  return render(request, 'detail.html', {'contents_detail':contents_detail, 'comments':comments})

def create(request):
    if(request.method=="POST"):
      contents = Content()
      contents.title = request.POST['Title']
      contents.body = request.POST['Body']
      contents.date = timezone.now()
      contents.writer = request.user
      try:
        contents.image = request.FILES['Image']
      except:
        contents.image = None
      contents.save()
      return redirect('/detail/'+str(contents.id))
    else:
      return render(request,'new.html')

def delete(request, contents_id):
  contents = Content.objects.get(id=contents_id)

  if(request.user == contents.writer):
    contents.delete()
    return redirect('home')
  else:
    return redirect('/detail/'+str(contents.id))

def update(request, contents_id):
  contents = Content.objects.get(id=contents_id)

  if(request.user ==contents.writer):

    if(request.method=="POST"):
      contents.title = request.POST['Title']
      contents.body = request.POST['Body']
      contents.date = timezone.now()
      contents.writer = request.user
      try:
        contents.image = request.FILES['Image']
      except:
        contents.image = None
      contents.save()
      return redirect('/detail/'+str(contents.id))

    else:
      return render(request, 'update.html')

  else:
    return redirect('/detail/'+str(contents.id))

def comment_delete(request, comment_id):
  comment = Comment.objects.get(id=comment_id)
  contents = Content.objects.get(id=comment.post.id)

  if(request.user == comment.writer):
    comment.delete()
    return redirect('/detail/'+str(contents.id))
  else:
    return redirect('/detail/'+str(contents.id))
