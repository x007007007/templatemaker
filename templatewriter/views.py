# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import View
from django.conf import settings
from django.shortcuts import render
import json


class Show(View):
    def get(self, request):
        path = request.get('file', '')
        return render(request, path)

    def post(self):
        path = request.get('file', '')
        context = json.loads(request.get('date', "{}"))
        return render(request, path, context)


class Index(View):
    def get(self, request):
        pass