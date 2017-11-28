# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template
from django.utils.safestring import mark_safe
from django.template.base import Node, TemplateSyntaxError
from ngapp.models import ng

register = template.Library()

@register.inclusion_tag("ngapp/ngs_name.html")
def show_ngs_name():
    ngs_obj =  ng.objects.order_by('id')
    ngs_list = []
    for ng_obj in ngs_obj:
        ng_info = {"id":ng_obj.id,"ng_name":ng_obj.ng_name}
        ngs_list.append(ng_info)
    ngs_list_sorted = sorted(ngs_list,key=lambda ng_item: len(ng_item["ng_name"]))
    return {"ngs":ngs_list_sorted}