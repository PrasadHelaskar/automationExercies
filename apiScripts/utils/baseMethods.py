import requests

class BaseMethod():
    def get_method(self,url,header=None,params=None,time:int=10):
        
        apiCall=requests.get(url,headers=header,params=params,timeout=time)

        return apiCall
    
    def post_method(self,url,header=None,body=None,time:int=10):

        # if body is None:
        #     raise ValueError("POST request requires a body")
        
        apiCall=requests.post(url,headers=header,data=body,timeout=time)

        return apiCall
    
    def put_method(self,url,header=None,body=None,time:int=10):

        if body is None:
            raise ValueError("POST request requires a body")
        
        apiCall=requests.put(url,headers=header,data=body,timeout=time)

        return apiCall
    
    def delete_method(self,url,header=None,body=None,time:int=10):

        if body is None:
            raise ValueError("POST request requires a body")
        
        apiCall=requests.delete(url,headers=header,data=body,timeout=time)

        return apiCall
    