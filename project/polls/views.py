from django.http import HttpResponse
from django.template import loader
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect


@require_http_methods(["GET", "POST"])
def index(request):
    print(request.method)
    if request.method == 'GET':
        template = loader.get_template('polls/index.html')
        context = {'name': 'milujem simonku', 'orientation': 'simonkofil'}
        return HttpResponse(template.render(context, request))

    elif request.method == 'POST':
        print(request.POST)
        if 'test1' in request.POST:
            return HttpResponse('THIS IS HOW IT WORKS')

        elif 'redirect' in request.POST:
            return redirect('index2')

        else:
            return HttpResponse('SOMETHING WENT WRONG')


@require_http_methods(["GET", "POST"])
def index2(request):
    return HttpResponse('skuska 123')
