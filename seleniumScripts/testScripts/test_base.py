import pytest
import time

class Test_initialTest():
    @pytest.mark.order(1)
    def test_initialtest(self,driver):
        driver.get("https://automationexercise.com/")