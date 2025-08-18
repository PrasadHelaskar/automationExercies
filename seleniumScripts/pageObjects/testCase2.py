import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from seleniumScripts.utils.baseMethods import baseMethods
from seleniumScripts.utils.logger import Logger

log=Logger().get_logger()

class testCaseTwo(baseMethods):
    __private_signUpButton=(By.CSS_SELECTOR, "a[href^='/login']")
    __private_loginForm=(By.XPATH,"//div[@class='login-form']/..//h2")
    __private_emailTextBox=(By.XPATH, "(//input[@name='email'])[1]")
    __private_passwordTextBox=(By.NAME,"password")
    __private_loginButton=(By.CSS_SELECTOR, "button[data-qa='login-button']")
    __private_loggedinUserNmae=(By.XPATH, "//i[@class='fa fa-user']/..//b")
    __private_deleteAccount=(By.CSS_SELECTOR, "a[href^='/delete_account']")
    __private_deleteConfirmation=(By.XPATH, "//h2[@data-qa='account-deleted']/..//b")

    def loginActions(self,email,password):
        
        self.click(self.__private_signUpButton)
        
        if (self.is_visible(self.__private_loginForm)):
            self.send_keys(self.__private_emailTextBox,email)
            self.send_keys(self.__private_passwordTextBox,password)
            self.click(self.__private_loginButton)
        
        else:
            assert self.is_visible(self.__private_loginForm), "The login from is not visible"

    def loginConfiremationActions(self):

        assert self.get_text(self.__private_loggedinUserNmae).lower() == "reginald neal" , "Account is not verifird as user name is different"

    def postAccountActions(self):
        
        self.click(self.__private_deleteAccount)

        assert self.get_text(self.__private_deleteConfirmation).lower() == "account deleted!" , "Account deletion failed"