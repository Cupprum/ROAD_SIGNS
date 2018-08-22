from django.http import HttpResponse
from django.template import loader
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect


@require_http_methods(["GET", "POST"])
def welcome_page(request):
    if request.method == 'GET':
        template = loader.get_template('app_signs/welcome_page.html')
        return HttpResponse(template.render({}, request))

    if request.method == 'POST':
        if 'btn_start' in request.POST:
            template = loader.get_template('app_signs/choose_category.html')
            return HttpResponse(template.render({}, request))


@require_http_methods(["GET", "POST"])
def choose_category(request):
    if request.method == 'GET':
        return HttpResponse('SOUNDS GOOD TO ME')


@require_http_methods(["GET", "POST"])
def index(request):
    if request.method == 'GET':
        template = loader.get_template('app_signs/index.html')
        context = {'name': 'milujem simonku', 'orientation': 'simonkofil'}
        return HttpResponse(template.render(context, request))

    elif request.method == 'POST':
        if 'test1' in request.POST:
            return HttpResponse('THIS IS HOW IT WORKS')

        elif 'redirect' in request.POST:
            return redirect('index2')

        else:
            return HttpResponse('SOMETHING WENT WRONG')


@require_http_methods(["GET", "POST"])
def index2(request):
    return HttpResponse('skuska 123')
