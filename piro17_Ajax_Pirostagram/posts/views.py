from django.shortcuts import render, redirect
from .forms import CommentForm
from .models import Comment

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def comment_list(request):
  comments = Comment.objects.all()
  if request.method == "POST":
    form = CommentForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('posts:comment_list')
    else:
      context = {
        'form': form,
        'comments': comments,
      }
      return render(request, template_name='posts/comment_list.html', context=context)
  else: # GET
    form = CommentForm()
    context = {
      'form': form,
      'comments': comments,
    }
    return render(request, template_name='posts/comment_list.html', context=context) 

@csrf_exempt
def like_ajax(request):
  req = json.loads(request.body)
  comment_id = req['id']
  comment = Comment.objects.get(id=comment_id)

  if comment.like == True:
    comment.like = False
  else:
    comment.like = True
  comment.save()
  return JsonResponse({ 'id': comment_id })

@csrf_exempt
def delete_ajax(request):
  req = json.loads(request.body)
  comment_id = req['id']
  comment = Comment.objects.get(id=comment_id)

  comment.delete()
  return JsonResponse({ 'id': comment_id })