from django.shortcuts import render, redirect
from .models import Idea, Tool
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

@csrf_exempt
def IdeaHome(request):
  if(request.method == "POST"):
    req = json.loads(request.body)
    Idea.objects.filter(id = req["id"]).update(interest = req["interest"])

  ideas = Idea.objects.all()
  sort = request.GET.get("sort", "")
  if sort == "like":
    ideas = ideas.order_by("-like")
  elif sort == "createAt":
    ideas = ideas.order_by("created_at")
  elif sort == "updateAt":
    ideas = ideas.order_by("-updated_at")
  elif sort == "title":
    ideas = ideas.order_by("title")

  context = {
    "ideas": ideas
  }
  return render(request, template_name='ideas/IdeaHome.html', context=context)

def IdeaCreate(request):
  if request.method == "POST":
    title = request.POST["title"]
    req_image = request.FILES["image"]
    content = request.POST["content"]
    interest = request.POST["interest"]
    devtool = Tool.objects.get(name = request.POST["devtool"])

    Idea.objects.create(
      title=title,
      image=req_image,
      content=content,
      interest=interest,
      devtool=devtool
    )
    return redirect("/")

  devtools = Tool.objects.all()

  context = {"devtools": devtools}
  return render(request, template_name='ideas/IdeaCreate.html', context=context)

def IdeaDetail(request, id):
  idea = Idea.objects.get(id=id)
  context = {
    "idea": idea,
  }
  return render(request, template_name="ideas/IdeaDetail.html", context=context)

def IdeaUpdate(request, id):
  if request.method == "POST":
    idea = Idea.objects.get(id=id)
    idea.title = request.POST["title"]
    idea.content = request.POST["content"]
    idea.interest = request.POST["interest"]
    idea.devtool = Tool.objects.get(id = request.POST["devtool"])
    if request.FILES.get("image"):
      idea.image = request.FILES.get("image")
    else:
      idea.image = idea.image
    idea.save()
    return redirect(f"/IdeaDetail/{id}")

  idea = Idea.objects.get(id=id)
  devtools = Tool.objects.all()
  context = {
    "idea": idea,
    "devtools": devtools
  }
  return render(request, template_name='ideas/IdeaUpdate.html', context=context)

def IdeaDelete(request, id):
  if request.method == "POST":
    Idea.objects.filter(id=id).delete()
    return redirect('/')

def likes(request):
  if request.is_ajax():
    idea_id = request.GET["idea_id"]
    idea = Idea.objects.get(id=idea_id)

    if not request.user.is_authenticated:
      message = "로그인이 필요합니다."
      context = {"like_count": idea.like.count(), "message": message}
      return HttpResponse(json.dumps(context), content_type="application/json")
    
    user = request.user
    if idea.like.filter(id=user.id).exists():
      idea.like.remove(user)
      message = "좋아요 취소되었습니다."
    else:
      idea.like.add(user)
      message = "좋아요 되었습니다."

    context = {"like_count": idea.like.count(), "message": message}
    return HttpResponse(json.dumps(context), content_type="application/json")
      
def ToolHome(request):
  tools = Tool.objects.all()
  context = {
    "tools": tools
  }
  return render(request, template_name='ideas/ToolHome.html', context=context)

def ToolCreate(request):
  if request.method == "POST":
    name = request.POST["name"]
    kind = request.POST["kind"]
    content = request.POST["content"]

    Tool.objects.create(
      name=name,
      kind=kind,
      content=content
    )
  return render(request, template_name='ideas/ToolCreate.html')

def ToolDetail(request, id):
  tool = Tool.objects.get(id=id)
  context = {
    "tool": tool,
    "ideas": Idea.objects.filter(devtool=tool)
  }
  return render(request, template_name="ideas/ToolDetail.html", context=context)

def ToolUpdate(request, id):
  tool = Tool.objects.get(id=id)
  if request.method == "POST":
    name = request.POST["name"]
    kind = request.POST["kind"]
    content = request.POST["content"]

    Tool.objects.filter(id=id).update(
      name = name,
      kind = kind,
      content = content,
    )
    return redirect(f"/ToolDetail/{id}")

  elif request.method == "GET":
    tool = Tool.objects.get(id=id)
    context = {
      "tool": tool
    }
  return render(request, 'ideas/ToolUpdate.html', context=context)

def ToolDelete(request, id):
  if request.method == "POST":
    Tool.objects.filter(id=id).delete()
    return redirect('/')

