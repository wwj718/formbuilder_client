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

    """Docstring for Client.
    todo
        自动创建表格
        表格地址
        数据地址
        管理地址:  http://ojyphjlrg.bkt.clouddn.com/formbuilder.html
        adminToken 和 userToken 彼此独立，userToken可以单独上传
    """

    def __init__(self,kintoUrl,userToken=None,adminToken=None):
        '''
        kintoUrl : http://localhost:8888/v1
        '''
        self.kintoUrl = kintoUrl
        if adminToken:
            assert len(adminToken) == 32
            self.adminToken = adminToken
            self.userToken = adminToken[:len(adminToken)/2] #userToken is 1/2 adminToken
            #assert self.userToken ==16
        if userToken:
            self.userToken = userToken
            assert len(userToken) == 16
    def get_response(self):
        path = "/buckets/formbuilder/collections/{}/records".format(self.userToken)
        data_url = urlparse.urljoin(self.kintoUrl,path)
        response = requests.get(data_url,auth=HTTPBasicAuth('form', self.adminToken))
        return response
    @property
    def url():
        pass

