# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from ngapp.models import ng,upstream
from modules import *

import ConfigParser


def index(request):
    ngs_obj =  ng.objects.order_by('id')
    ngs_list = []
    for ng_obj in ngs_obj:
        ng_info = {"id":ng_obj.id,"ng_name":ng_obj.ng_name}
        ngs_list.append(ng_info)
    ngs_list_sorted = sorted(ngs_list,key=lambda ng: len(ng["ng_name"]))
    return render(request,'ngapp/index.html')


def get_ng_info(request,id):
    ng_summary_info = {}

    try:
        ng_obj = ng.objects.get(id=id)
        upstreams = upstream.objects.filter(ng=ng_obj).order_by('id')
        ng_summary_info['ng'] = ng_obj
        ng_summary_info['upstreams'] = upstreams
        
        host = ng_obj.vip
        port = 8081
        url = "/list"

        try:
            upstream_pool = CallApiGetData(host,port,url).strip("\n").split("\n")
            ng_summary_info["upstream_pool"] = upstream_pool
        except Exception,e:
            ng_summary_info["upstream_pool"] = None

    except upstream.DoesNotExist:
        ng_summary_info['upstreams'] = None

    return render(request,'ngapp/ng.html',ng_summary_info)


def get_upstream_info(request,ng_name,vip,upstream_name):
    upstream_summary_info = {}
    upstream_summary_info["ng_name"] = ng_name
    upstream_summary_info["vip"] = vip
    upstream_summary_info["upstream_name"] = upstream_name

    #get plan's upstreams for the ng
    ng_obj = ng.objects.get(ng_name=ng_name)
    upstreams_obj = upstream.objects.filter(ng=ng_obj)
    upstream_obj = upstreams_obj.filter(service_site_name=upstream_name)

    nodes_list = []
    nodes = upstream_obj[0].plan_service_nodes.split("\n")

    for node in nodes:
        nodes_list.append(node.split("_"))

    upstream_summary_info["plan_service_nodes"] = nodes_list

    return render(request,"ngapp/upstream.html",upstream_summary_info)
    

