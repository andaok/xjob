# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
import json
import urllib
import httplib

def CallApiGetData(Host,Port,ReqUrlSuffix):
    """
    Call api interface for get docker and container information
    """
    httpClient = None
    try:
        httpClient = httplib.HTTPConnection(Host,Port,timeout=2)
        httpClient.request('GET',ReqUrlSuffix)
        response = httpClient.getresponse()
        if response.status == 200:
            resp_string = response.read()
            try:
            	resp_format_data = json.loads(resp_string)
            	return resp_format_data
            except ValueError:
            	return resp_string
        else:
            print("return code %s"%response.status)
            return None
    except Exception,e:
        print("call api error!,%s"%e)
        return None
    finally:
        if httpClient:
            httpClient.close()


if __name__ == "__main__":

	print CallApiGetData("192.168.1.101",8081,"/list")