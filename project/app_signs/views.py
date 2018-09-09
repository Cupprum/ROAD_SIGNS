from django.http import HttpResponse
from django.template import loader
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect

from app_signs.models import sign_all


@require_http_methods(["GET", "POST"])
def welcome_page(request):
    if request.method == 'GET':
        template = loader.get_template('app_signs/welcome_page.html')
        return HttpResponse(template.render({}, request))

    if request.method == 'POST':
        if 'btn_start' in request.POST:
            return redirect('choose_category')


@require_http_methods(["GET", "POST"])
def choose_category(request):
    if request.method == 'GET':
        template = loader.get_template('app_signs/choose_category.html')
        return HttpResponse(template.render({}, request))


@require_http_methods(["GET", "POST"])
def show_sign(request):
    if request.method == 'GET':
        act_sign = Sign.objects.get(sign_id='001')
        print(act_sign.sign_name)
        template = loader.get_template('app_signs/show_sign.html')
        return HttpResponse(template.render({'act_sign': act_sign}, request))


@require_http_methods(["GET", "POST"])
def add_to_db(request):
    if request.method == 'GET':
        txt_r = open("txt_db.txt", "r").readlines()
        for x in txt_r:
            sign_list = x.split("|")

            s_category = sign_list[0]
            s_id = sign_list[1]
            s_name = sign_list[2]
            s_url = sign_list[3][:-1]

            print(s_category)
            print(s_id)
            print(s_name)
            print(s_url)
            print("\n")

            new_sign = sign_all(sign_category=sign_list[0],
                                sign_id=sign_list[1],
                                sign_name=sign_list[2],
                                sign_url=sign_list[3][:-1])
            new_sign.save()

        return HttpResponse('works')
    elif request.method == 'POST':
        print('POST METHOD USING')

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
