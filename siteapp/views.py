from django.shortcuts import render, get_object_or_404, redirect
from .models import Content, Comment, Recomment, Profile, Board
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib import messages
from django.template.defaulttags import register
# Create your views here.

def home(request):
  contents = Content.objects
  content_list = Content.objects.all()
  paginator = Paginator(content_list,5)
  page = request.GET.get('page')
  posts = paginator.get_page(page)
  board = Board.objects.all()

  return render(request,'home.html',{'contents':contents, 'posts':posts, 'Board':board})

def detail(request, contents_id):
  contents = get_object_or_404(Content, pk=contents_id)
  comments = Comment.objects.filter(post = contents_id)
  contents.comment_count = comments.count()

  if (request.method=="POST"):
    comment = Comment()
    comment.body = request.POST['body']
    comment.post = contents
    comment.writer = request.user
    comment.date = timezone.now()
    contents.comment_count += 1
    comment.save()

  recomments = Recomment.objects.all()
  boards = Board.objects.all()

  return render(request, 'detail.html', {'contents':contents, 'comments':comments, 'recomments':recomments, 'boards':boards})

def create(request):
  global board
  if(request.method=="POST"):
    board = Board.objects.all()
    contents = Content()
    contents.title = request.POST['Title']
    contents.body = request.POST['Body']
    contents.date = timezone.now()
    contents.writer = request.user
    contents.board = Board.objects.get(id=request.POST['Board'])
    try:
      contents.image = request.FILES['Image']
    except:
      contents.image = None
    contents.save()
    return redirect('/detail/'+str(contents.id),{'Board':board})
  else:
    board = Board.objects.all()
    return render(request,'new.html',{'Board':board})

def delete(request, contents_id):
  contents = Content.objects.get(id=contents_id)

  if(request.user == contents.writer):
    contents.delete()
    return redirect('home')
  else:
    return redirect('/detail/'+str(contents.id))

def update(request, contents_id):
  contents = Content.objects.get(id=contents_id)
  global board
  if(request.user ==contents.writer):

    if(request.method=="POST"):
      board = Board.objects.all()
      contents.title = request.POST['Title']
      contents.body = request.POST['Body']
      contents.date = timezone.now()
      contents.writer = request.user
      contents.board = Board.objects.get(id=request.POST['Board'])
      try:
        contents.image = request.FILES['Image']
      except:
        contents.image = None
      contents.save()
      return redirect('/detail/'+str(contents.id),{'Board':board})

    else:
      board = Board.objects.all()
      return render(request, 'update.html',{'Board':board})

  else:
    board = Board.objects.all()
    return redirect('/detail/'+str(contents.id),{'Board':board})

def comment_delete(request, comment_id):
  comment = Comment.objects.get(id=comment_id)
  contents = Content.objects.get(id=comment.post.id)

  if(request.user == comment.writer):
    comment.delete()
    
    return redirect('/detail/'+str(contents.id))
  else:
    return redirect('/detail/'+str(contents.id))

def recomment(request, comment_id):
  comment = get_object_or_404(Comment, pk=comment_id)
  recomments = Recomment.objects.filter(comment=comment_id)

  if(request.method=="POST"):
    recomment = Recomment()
    recomment.comment = comment
    recomment.body = request.POST['body']
    recomment.writer = request.user
    recomment.date = timezone.now()
    recomment.save()
  
  return redirect('/detail/'+str(comment.post.id), {'recomments':recomments})

def recomment_delete(request, recomment_id):
  recomment = Recomment.objects.get(id=recomment_id)
  if(request.user == recomment.writer):
    recomment.delete()
    return redirect('/detail/'+str(recomment.comment.post.id))
  else:
    return redirect('/detail/'+str(recomment.comment.post.id))

def like(request, contents_id):
  contents = get_object_or_404(Content, id=contents_id)
  user = request.user
  profile = Profile.objects.get(user=user)
  like_contents = profile.like_contents.filter(id=contents_id)

  if like_contents.exists():
    profile.like_contents.remove(contents)
    contents.like_count -= 1
    contents.save()
  else:
    profile.like_contents.add(contents)
    contents.like_count += 1
    contents.save()
  
  return redirect('/detail/'+str(contents.id))

def go_board(request):
  boards = Board.objects.all()
  
  return render(request,'go_board.html',{'boards':boards})

def board(request,board_id):
  contents = Content.objects.filter(board = board_id)
  paginator = Paginator(contents,3)
  page = request.GET.get('page')
  posts = paginator.get_page(page)
  boards = Board.objects.all()
  now_board = board_id

  return render(request,'board.html',{'posts':posts,'boards':boards,'now_board':now_board})