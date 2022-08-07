# created by Shipra
import sys
sys.path.append('OperationCode') 
# from . import textOperation
import textOperation
from django.http import HttpResponse
from django.shortcuts import render

# video 6 codeWith Harry
# def index(request):
#     return HttpResponse('''<h1>Navigation Bar</h1> <a href="https://www.youtube.com/watch?v=AepgWsROO4k&t=58s"> Django first Project</a>
#     <br><a href="https://www.codewithharry.com/videos/python-django-tutorials-hindi-7/"> Django second Project</a><br>
#     <a href ="https://www.codewithharry.com/videos/python-django-tutorials-hindi-8/"> Django third video</a>''')

# def about(request):
#     return HttpResponse("About me")

#video 7 codeWith Harry
def index(request):
    # video 7
    # return HttpResponse('''<h1> Home </h1> <a href ="/removePuntuation"> removepunc</a>
    # <br> <a href ="/captalizedFirst"> Captalized first letter</a>
    # <br> <a href="/newlineremover"> newlineremover </a>
    # <br> <a href="/spaceremover"> spaceremover </a>
    # <br> <a href="http://127.0.0.1:8000/charcount"> charcount </a> 
    # <br> <a href="/usingtempl"> check Template </a>''') # either //charcount or http://127.0.0.1:8000/charcount, both are same
    return render(request, 'index2.html')

def analyze(request):
    dtext= request.POST.get('text', 'dafault')
    removepunc=request.POST.get('removepunc','off')
    capfirst = request.POST.get('capfirst','off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    removeNewLines = request.POST.get('removeNewLines', 'off')
    obj = textOperation.Operation()
    purpose = ""
    try:
        count = 0
        if charcount == "on":
            count = obj.charCount(dtext)
        if removepunc == "on":
            purpose+="Remove Punctuation"
            analyzed = obj.removePunctuation(dtext)
            dtext = analyzed
        if capfirst == "on":
            purpose+=" and capatalized first letter"
            analyzed = obj.captalizedFistLetter(dtext)
            dtext = analyzed
        if spaceremover == "on":
            purpose+=" and Remove space"
            analyzed = obj.spaceremover(dtext)
            dtext = analyzed
        if removeNewLines == "on":
            purpose+=" and Remove new lines"
            analyzed = obj.removeNewLines(dtext)
        if count > 0:
            purpose+=" and count charatcters"
            analyzed=analyzed+"\n Also,char count is "+str(count)
        params = {'purpose': purpose, 'analyzed_text': analyzed}
        return render(request, 'analyze2.html', params)
    except:
        return HttpResponse('''<Strong>Error</Strong> <br> <a href="/"> Home</a> ''') 
def removepunc(request):
    # get the text
    dText = request.POST.get('text', 'default')
    # Analyze the text
    return HttpResponse('''<a href="/"> Home</a> <br>remove puntuation''')

def capfirst(request):
    return HttpResponse('''<a href="/"> Home </a> <br> Captalized first letter''')

def newlineremover(request):
    return HttpResponse(''' <a href="/"> Home </a> <br> newlineremover''')

def spaceremover(request):
    return HttpResponse(''' <a href='/'> Home </a> <br> spaceremover''')

def charcount(request):
    return HttpResponse(''' <a href="http://127.0.0.1:8000/"> Home </a> <br> charcount''') # either / or http://127.0.0.1:8000/ both are same

def usingtempl(request):
    dict_items = {'name': 'Yadu', 'place': 'wonder World'}
    return render(request, 'index.html', dict_items)
