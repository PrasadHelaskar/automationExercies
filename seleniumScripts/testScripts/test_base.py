from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from seleniumScripts.utils.jsonOperations import jsonRead
from seleniumScripts.utils.logger import Logger

log=Logger().get_logger(__name__)

class initialTest():
    def initialtest(self,driver):
        driver.get(jsonRead("BASEURL"))

        WebDriverWait(driver,10).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

        log.info("The site is ready to use")

        isImageSeen=driver.find_element(By.CSS_SELECTOR, "img[alt='Website for automation practice']").is_displayed()

        log.info("isImageSeen %s",isImageSeen)

        assert isImageSeen, "Page is not loaded yet can't proceed further"