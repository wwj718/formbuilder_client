# -*- coding: utf-8 -*-

import requests
from requests.auth import HTTPBasicAuth
# python2-3
# http://python-future.org/compatible_idioms.html
try:
    import urlparse #python
except:
    import urllib.parse as urlparse

class Client(object):

    """Docstring for Client. """

    def __init__(self,kintoUrl,userToken,adminToken):
        '''
        kintoUrl : http://localhost:8888/v1
        '''
        self.kintoUrl = kintoUrl
        self.userToken = userToken
        self.adminToken = adminToken
    def get_response(self):
        path = "/buckets/formbuilder/collections/{}/records".format(self.userToken)
        data_url = urlparse.urljoin(self.kintoUrl,path)
        response = requests.get(data_url,auth=HTTPBasicAuth('form', self.adminToken))
        return response

