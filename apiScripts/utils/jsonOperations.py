import json

__private_filePath="apiScripts/testData/data.json"

def jsonRead(key):
    """For reading the json file"""        
    with open(__private_filePath, 'r',encoding='utf-8') as jsonFile:
        data=json.load(jsonFile)

        return data[key]
    
def jsonWrite(key,value):
    """For updaing the json file"""
    with open(__private_filePath,'r',encoding='utf-8') as jsonFile:
        data=json.load(jsonFile)

        data[key]=value
    
    with open(__private_filePath,'w',encoding='uft-8') as jsonFile:
        json.dump(data,jsonFile,indent=4)

def json_read_array():
    """For reading the json array key"""
  
    with open(__private_filePath, 'r', encoding='utf-8') as json_file:
        data=json.load(json_file)
        cookies=data.get("Array_name")
        return cookies
