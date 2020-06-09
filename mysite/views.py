from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from datetime import datetime
from mysite import models

def index(request):
	now = datetime.now()
	return render(request, "index.html", locals())

def page(request, pno):
	stories = [
		"這是第0頁的內容，別忘了，Python是從0開始算的",
		"這是第一頁的內容，可以放在網站上供人取閱！", 
		"第二頁也有一些故事", 
		"第三頁的內容也不錯"
	]
	if pno >= 0 and pno < len(stories):
		story = stories[pno]
	else:
		story = "None"

	return HttpResponse(story)

def db(request, sno):
	stories = models.Story.objects.filter(sno=sno)
	if len(stories)>=1:
		story = stories[0]
	else:
		story = "None"

	return HttpResponse(story)
