import time
from selenium.webdriver.common.by import By
from seleniumScripts.utils.baseMethods import baseMethods
from seleniumScripts.utils.logger import Logger

log=Logger().get_logger(__name__)

class testCaseTwentySix(baseMethods):

    __private_topTitleText=(By.XPATH, "//div[@class='col-sm-6']/h2")
    
    __private_bottomSubscriptionTitleText=(By.XPATH, "//div[@class='single-widget']/h2")

    def getTextForTopTitle(self)-> str:
        text=self.get_text(self.__private_topTitleText)

        return text
    
    def getBottomSubscriptionTitleText(self):
        text=self.get_text(self.__private_bottomSubscriptionTitleText)

        return text