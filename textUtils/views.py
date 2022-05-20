from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse('<h1>Hello Rohan</h1>  <a href="https://www.google.in">Google</a>')

# def about(request):
#     return HttpResponse('About Rohan')

def index(request):
    # return HttpResponse('Home')
    # params = {'name':'Rohan','place':'Amreli'}
    return render(request, 'index.html')

def analyze(request):
    # return HttpResponse('Analyze')
    djtext = request.POST.get('texts','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    # print(removepunc)
    # print(djtext)
    # analyzed = djtext
    punctuations = '''!()-[]-{};:'"\,<>./?@#$%&*_~'''
    analyzed = ''
    if removepunc == 'on':
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text':analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)
    if fullcaps == 'on':
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Change to Uppercase', 'analyzed_text':analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)
    if newlineremover == 'on':
        analyzed = ''
        for char in djtext:
            if char != '\ n' and char != '\ r': 
                analyzed = analyzed + char  
        params = {'purpose':'New Line Remove', 'analyzed_text':analyzed}
        djtext = analyzed
        # return render(reqdjtext = analyzeduest,'analyze.html',params)
    if extraspaceremover == 'on':
        analyzed = ''
        for index,char in enumerate(djtext):
            if not (djtext[index] == ' ' and djtext[index+1] == ' '):
                analyzed = analyzed + char  
        params = {'purpose':'New Line Remove', 'analyzed_text':analyzed
        # return render(request,'analyze.html',params)
    if (removepunc != 'on' and newlineremover != 'on' and fullcaps != 'on' and extraspaceremover != 'on'):
        return HttpResponse('Please Select Any Operaion.')
    return render(request,'analyze.html',params)

# def capfirst(request):
#     return HttpResponse('Capitalize First')

# def newlineremove(request):
#     return HttpResponse('newlineremove')

# def spaceremove(request):
#     return HttpResponse('Rspaceremove')

# def charcount(request):
#     return HttpResponse('Necharcount')