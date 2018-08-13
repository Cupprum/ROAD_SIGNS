from django.http import HttpResponse
from django.template import loader


def index(request):
    print(request.method)
    if request.method == 'GET':
        template = loader.get_template('polls/index.html')
        context = {'name': 'milujem simonku', 'orientation': 'simonkofil'}
        return HttpResponse(template.render(context, request))


def index2(request):
    return HttpResponse('skuska 123')
