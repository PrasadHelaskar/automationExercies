import pytest
from selenium.webdriver.support.ui import WebDriverWait
from seleniumScripts.utils.jsonOperations import jsonRead
from seleniumScripts.utils.logger import Logger

log=Logger().get_logger(__name__)

class Test_initialTest():
    @pytest.mark.order(1)
    def test_initialtest(self,driver):
        driver.get(jsonRead("BASEURL"))

        WebDriverWait(driver,10).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

        log.info("The site is ready to use")