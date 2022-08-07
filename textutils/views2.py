# created by Shipra
import sys
sys.path.append('OperationCode') 
# from . import textOperation2
import textOperation
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index3.html')

def analyze(request):
    dtext= request.POST.get('text', 'dafault')
    text1= request.POST.get('text1', 'dafault')
    text2= request.POST.get('text2', 'dafault')
    print(dtext)
    replaceSubstring = request.POST.get('replaceSubstring', 'off')
    obj = textOperation.Operation()
    purpose = ""
    try:
        if replaceSubstring == "on":
            purpose+="Replace substring"
            analyzed = obj.replaceSubstring(dtext,text1,text2)
        params = {'purpose': purpose, 'analyzed_text': analyzed}
        return render(request, 'analyze2.html', params)
    except:
        return HttpResponse('''<Strong>Error</Strong> <br> <a href="/about"> Home</a> ''') 