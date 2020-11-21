from django.shortcuts import render, get_object_or_404, redirect
from .models import Content, Comment
from django.utils import timezone
from django.core.paginator import Paginator

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
    comment.post = contents_id
    comment.save()

  return render(request, 'detail.html', {'contents_detail':contents_detail, 'comments':comments})

def create(request):
    if(request.method=="POST"):
      contents = Content()
      contents.title = request.POST['Title']
      contents.body = request.POST['Body']
      contents.date = timezone.now()
      contents.save()
      return redirect('/detail/'+str(contents.id))
    else:
      return render(request,'new.html')
