from django.shortcuts import redirect, render

# Create your views here.
#-*- coding: utf-8 -*-
from  django.http import HttpResponse, Http404
def home(request):
  text = """<h1>Bienvenue sur mon blog !</h1>
<p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>"""

  return HttpResponse(text)

def articleById(request, id):
  text= '''<h1>Nous voulons l'article n°{}</h1>'''.format(id)
  return HttpResponse(text)

def article(request):
  articleId = request.GET.get('id')
  if articleId is not None:
    text = '''<h1>Nous voulons l'article n°{}</h1> Mais là nous avons precisé le id en parametre'''.format(articleId)
  else:
    text = '''<h1>Nous voulons tous les articles car </h1> nous n'avons pas précisé le id en paramètre'''
  return HttpResponse(text)

def view_article(request, id_article):
    if int(id_article) > 100: #Si l'ID est supérieur à 100, nous considérons que l'article n'existe pas
      raise Http404
    return redirect('articleById', id = 900)
    # return HttpResponse('<h1>Mon article ici</h1>')
def redirect_view(request):
  return HttpResponse('Vous etes sur une nouvelle page')