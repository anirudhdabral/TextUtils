from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.POST.get("text", "default")  # get the text
    # checking empty string

    if djtext.strip() == '':
        params = {'error': 'Please enter some text.'}
        return render(request, 'error.html', params)

    # check checkbox values
    removepunc = request.POST.get("remove_punc", 'off')
    fullcaps = request.POST.get("fullcaps", 'off')
    newlineremover = request.POST.get("newlineremover", 'off')
    extraspaceremover = request.POST.get("extraspaceremover", 'off')
    charactercounter = request.POST.get("charactercounter", 'off')
    purpose = []

    # which checkbox is on
    if removepunc == 'on':
        analyzed = ''
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        purpose.append('punctuations removed')
        djtext = analyzed
    if fullcaps == 'on':
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.upper()
        purpose.append('changed to uppercase')
        djtext = analyzed
    if newlineremover == 'on':
        analyzed = ''
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        purpose.append('new lines removed')
        djtext = analyzed
    if extraspaceremover == 'on':
        analyzed = ''
        for index, char in enumerate(djtext):
            if not (djtext[index] == ' ' and djtext[index + 1] == ' '):
                analyzed = analyzed + char
        purpose.append('extra spaces removed')
        djtext = analyzed
    if charactercounter == 'on':
        analyzed = analyzed + '\nNo. of characters = ' + str(len(djtext))

    # check if no option is selected
    if removepunc != 'on' and fullcaps != 'on' and newlineremover != 'on' and extraspaceremover != 'on' and charactercounter != 'on':
        params = {'error': 'Please select an operation first.'}
        return render(request, 'error.html', params)

    # joining purposes
    purpose = ', '.join(purpose) + '.'
    params = {'purpose': purpose, 'analyzed_text': analyzed}
    return render(request, 'analyze.html', params)


def about(request):
    return render(request, 'about.html')