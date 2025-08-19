import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from seleniumScripts.utils.baseMethods import baseMethods
from seleniumScripts.utils.logger import Logger

log=Logger().get_logger(__name__)

class testCaseFive(baseMethods):
    __private_signUpButton=(By.CSS_SELECTOR, "a[href^='/login']")
    __private_signUpForm=(By.CSS_SELECTOR,"div[class='signup-form']")
    __private_nameTextBox=(By.NAME, "name")
    __private_emailTextBox=(By.CSS_SELECTOR,"input[data-qa='signup-email']")
    __private_createAccount=(By.CSS_SELECTOR, "button[data-qa='signup-button']")
    __private_warningText=(By.XPATH, "//input[@name='form_type']/../p")

    # ACTION METHODS
    def signupActions(self,name,email):
        
        self.click(self.__private_signUpButton)

        if (self.is_visible(self.__private_signUpForm)):
            self.send_keys(self.__private_nameTextBox,name)
            self.send_keys(self.__private_emailTextBox,email)
            self.click(self.__private_createAccount)
            warningText=self.get_text(self.__private_warningText)
            
            assert warningText.lower() == "Email Address already exist!".lower(), "The account doesn't exsist so moving forword"
        else:
            assert self.is_visible(self.__private_signUpForm), "The sign-up from is not visible"
        
        