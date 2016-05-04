#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from django.http import HttpResponse
from django.shortcuts import render


class JSONResponseMixin(object):
    """
    Mixin used to render a JSON response.
    """
    response_class = HttpResponse

    def render_to_response(self, context, **kwargs):
        kwargs['content_type'] = 'application/json'
        return self.response_class(self.convert_context_to_json(context), **kwargs)

    def convert_context_to_json(self, context):
        return json.dumps(context)


class RenderMixin(object):
    """
    Mixin used to render a HTML response.
    """

    def render(self, request,  *args, **kwargs):
        return render(request, *args, **kwargs)