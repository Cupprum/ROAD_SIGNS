from django.http import HttpResponse
from django.template import loader
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect

from app_signs.models import sign

import random


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
        act_sign = sign.objects.get(sign_id='001')
        print(act_sign.sign_name)
        template = loader.get_template('app_signs/show_sign.html')
        return HttpResponse(template.render({'act_sign': act_sign}, request))


@require_http_methods(["GET", "POST"])
def question(request):
    if request.method == 'GET':
        right_sign = sign.objects.get(sign_id='001')
        fake_sign1 = sign.objects.get(sign_id='002')
        fake_sign2 = sign.objects.get(sign_id='003')
        fake_sign3 = sign.objects.get(sign_id='004')

        list_sign = [right_sign.sign_name,
                     fake_sign1.sign_name,
                     fake_sign2.sign_name,
                     fake_sign3.sign_name]

        random.shuffle(list_sign, random.random)

        template = loader.get_template('app_signs/question.html')
        return HttpResponse(template.render({'right_sign': right_sign,
                                            'list': list_sign}, request))
