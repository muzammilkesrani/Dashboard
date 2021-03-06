# -*- coding: utf-8 -*-

"""
    jqlapilibcontrollers.base_controller

    This file was automatically generated by APIMATIC BETA v2.0 on 06/24/2016
"""

from ..http.requests_client import *
from ..api_exception import APIException

class BaseController(object):

    """All controllers inherit from this base class. It manages shared 
	HTTP clients and global API errors."""
    
    http_call_back = None
    http_client = RequestsClient()

    def __init__(self, client, call_back):
        if client != None:
            self.http_client = client
        if call_back != None:
            self.http_call_back = call_back

    def validate_response(self, response):
        """Validates an HTTP response by checking for global errors.
       
        Args:
            response (HttpResponse): The HttpResponse object to validate.            
            
        """
        if (response.status_code < 200) or (response.status_code > 208): #[200,208] = HTTP OK
            raise APIException("HTTP Response Not OK", response.status_code, response.raw_body)
