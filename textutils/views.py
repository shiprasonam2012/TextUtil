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
    swapcaseString = request.POST.get('swapcaseString', 'off')
    convertIntoLower = request.POST.get('convertIntoLower', 'off')
    encodeString = request.POST.get('encodeString', 'off')
    splitString = request.POST.get('splitString','off')
    removeWhiteSpaceStartEnd = request.POST.get('removeWhiteSpaceStartEnd', 'off')
    upperCaseString = request.POST.get('upperCaseString', 'off')
    splitStringByLines = request.POST.get('splitStringByLines', 'off')
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
            dtext = analyzed
        if swapcaseString == "on":
            purpose+=" and Swap"
            analyzed = obj.swapcaseString(dtext)
            dtext = analyzed
        if convertIntoLower == "on":
            purpose+=" and convert into lower"
            analyzed = obj.convertIntoLower(dtext)
            dtext = analyzed
        if encodeString == "on":
            purpose+=" and encoded"
            analyzed = obj.encodeString(dtext)
            dtext = analyzed
        if splitString == "on":
            purpose+=" and split"
            analyzed = obj.splitString(dtext)
            dtext = analyzed
        if removeWhiteSpaceStartEnd == "on":
            purpose+=" and remove white space"
            analyzed = obj.removeWhiteSpaceStartEnd(dtext)
            dtext = analyzed
        if upperCaseString == "on":
            purpose+=" and upper case"
            analyzed = obj.upperCaseString(dtext)
            dtext = analyzed
        if splitStringByLines == "on":
            purpose+=" and split by line"
            analyzed = obj.splitStringByLines(dtext)
            dtext = analyzed
        if count > 0:
            purpose+=" and count charatcters"
            analyzed=analyzed+"\n Also,char count is "+str(count)
        params = {'purpose': purpose, 'analyzed_text': analyzed}
        return render(request, 'analyze2.html', params)
    except:
        return HttpResponse('''<Strong>Error</Strong> <br> <a href="/"> Home</a> ''') 
    
def index1(request):
    return render(request, 'index_twoStrings.html')
def textOp2Strings(request):
    text1= request.POST.get('text1', 'dafault')
    text2= request.POST.get('text2', 'dafault')
    checkDiffButton = request.POST.get('checkDiff', 'off')
    splitbywordButton = request.POST.get('splitbyword', 'off')
    findStartIndexButton = request.POST.get('findStartIndex', 'off')
    obj = textOperation.Operation()
    purpose= "Operation done on two strings"
    try:
        if checkDiffButton == "on":
            analyzed = obj.checkDiff(text1,text2)
        if splitbywordButton == "on":
            analyzed = obj.splitbyword(text1,text2)
        if findStartIndexButton == "on":
            analyzed = obj.findStartIndex(text1,text2)
        params = {'purpose': purpose, 'analyzed_text': analyzed}
        return render(request, 'analyze2.html', params)
    except:
        return HttpResponse('''<Strong>Error</Strong> <br> <a href="/about"> Home</a> ''') 
            
    return HttpResponse('''<a href="/"> Home</a> <br>textOp2Strings''')

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
