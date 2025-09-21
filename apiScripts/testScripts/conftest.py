import pytest

@pytest.fixture(scope='session')
def base_attribute():
    url="https://automationexercise.com/api/"

    headers={}

    Base_object={
        "url": url,
        "headers": headers
    }

    return Base_object