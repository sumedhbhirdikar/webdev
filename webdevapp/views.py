from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse




def home(request):
    return render(request, 'Codewithharry.html')


def about(request):
    return HttpResponse('This is an about page')


def recent_websites(request):
    return render(request,'webhtml.html')


def analyze(request):
    djtext = (request.POST.get('text', 'Default'))
    remove_punc = request.POST.get('remove_punc', 'Default')
    Uppercase = request.POST.get('uppercase', 'Default')
    newlinerremove = request.POST.get('newlinerremove', 'Default')
    spaceremover = request.POST.get('spaceremover', 'Default')
    character_counter = request.POST.get('Charactercounter', 'Default')
    calc = request.POST.get('calc' ,'default')
    analyzed = djtext


    if remove_punc == 'on':
        tober = ''
        punctuations = '~,!@#$%^&*()_-+:;\'?/\;><*.~`"'
        for i in djtext:
            if i not in punctuations:
                tober = tober + i
        params = {'analyzed': analyzed, 'tober': tober}
        return render(request, 'analyzer.html', params)
    if Uppercase == 'on':
        a = djtext.upper()
        params = {'analyzed': analyzed, 'a': a}
        return render(request, 'analyzer.html', params)

    if newlinerremove == 'on':
        removed = ''
        for char in djtext:
             if char != '\n':
                removed = removed + char
        params = {'analyzed': analyzed, 'removed' : removed}
        return render(request, 'analyzer.html', params)

    if spaceremover == 'on':
        spaced = ''
        for char in djtext:
            if char != ' ':
                spaced = spaced + char
        params = {'analyzed': analyzed, 'spaced': spaced}
        return render(request, 'analyzer.html', params)

    if character_counter == 'on':
        count = 0
        for char in djtext:
            count += 1
        params = {'analyzed': analyzed, 'count': count}
        return render(request, 'analyzer.html', params)

    if calc == 'on':
        try:
            answer = eval((analyzed))
            params = {'analyzed': analyzed, 'answer': answer}
            return render(request, 'analyzer.html', params)
        except :
            return HttpResponse('error')

    else:
        return HttpResponse('User input Expected')


def capitalize(request):
    return HttpResponse('capitalize')


def newlinerremove(request):
    return HttpResponse('New Line Remover')


def demo_page(request):
    return render(request, 'codewithharry.html')


