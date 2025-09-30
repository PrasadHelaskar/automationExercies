import os
import pytest

@pytest.fixture(scope='session')
def base_attribute():
    url=os.getenv("APIURL")
    
    headers={}

    Base_object={
        "url": url,
        "headers": headers
    }

    return Base_object