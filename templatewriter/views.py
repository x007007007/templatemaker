# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.conf import settings
from django.shortcuts import render, Http404
import json
import os
import glob


class HomePage(View):
    def get(self, request):
        name = [os.path.basename(i) for i in glob.iglob('{}/statics/report/*'.format(settings.BASE_DIR)) if os.path.isdir(i)]
        return render(request, 'homepage.html', {"names": name})


class Show(View):
    def get(self, request, page_id):
        query_type = request.GET.get('type', None)
        if query_type == 'schema':
            schema_path = "{}/templates/{}/schema.json".format(settings.BASE_DIR, page_id)
            if os.path.exists(schema_path):
                return JsonResponse(json.load(open(schema_path)))
            return JsonResponse({})
        else:
            template_path = "{}/templates/{}/index.tpl".format(settings.BASE_DIR, page_id)
            if os.path.exists(template_path):
                return render(request, template_path, {})
            else:
                raise Http404

    @method_decorator(csrf_exempt)
    def post(self, request, page_id):
        template_path = "{}/templates/{}/index.tpl".format(settings.BASE_DIR, page_id)
        content = json.loads(request.POST.get('content', ''))
        if os.path.exists(template_path):
            return render(request, template_path, content)
        else:
            raise Http404


class Index(View):
    def get(self, request):
        pass