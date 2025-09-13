import time
from selenium.webdriver.common.by import By
from seleniumScripts.utils.baseMethods import baseMethods
from seleniumScripts.utils.logger import Logger

log=Logger().get_logger(__name__)

class testCaseEleven(baseMethods):
    __private_visitCartPage=(By.CSS_SELECTOR, "a[href^='/view_cart']")
    __private_subscriptionEmailTextBox=(By.ID, "susbscribe_email")
    __private_subscribeButton=(By.ID, "subscribe")
    __private_successMessage=(By.CSS_SELECTOR, "div[class='alert-success alert']")
    
    #Action Methods
    def gotoCartPage(self):
        self.click(self.__private_visitCartPage)
        
    def subscriptionEnrollmentCartPage(self,email):
        self.send_keys(self.__private_subscriptionEmailTextBox, email)
        self.click(self.__private_subscribeButton)

    def successMessageVerfity(self)-> str:
        message=self.get_text(self.__private_successMessage)
        return message