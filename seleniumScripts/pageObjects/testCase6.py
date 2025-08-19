import time
from selenium.webdriver.common.by import By
from seleniumScripts.utils.baseMethods import baseMethods
from seleniumScripts.utils.logger import Logger

log=Logger().get_logger(__name__)

class testCaseSix(baseMethods):
    __private_contaactUsLink=(By.CSS_SELECTOR, "a[href^='/contact_us']")
    __private_confirmationText=(By.XPATH, "(//h2[@class='title text-center'])[2]")
    __private_nameText=(By.NAME, "name")
    __private_emailText=(By.NAME, "email")
    __private_subjectText=(By.NAME, "subject")
    __private_messageText=(By.NAME, "message")
    __private_submitButton=(By.NAME, "submit")
    __private_successText=(By.CSS_SELECTOR, "div[class='status alert alert-success']") 
    __private_homeButton=(By.CSS_SELECTOR, "a[class='btn btn-success']")


    # Action Methods

    def openContactUsPage(self):
        self.click(self.__private_contaactUsLink)
        confirmationText=self.get_text(self.__private_confirmationText)

        assert confirmationText.lower() == "Get In Touch".lower(), "The Contact Us page is not loaded Properly"

    def formFill(self,name,email,subject,message):
        self.send_keys(self.__private_nameText,name)
        self.send_keys(self.__private_emailText,email)
        self.send_keys(self.__private_subjectText,subject)
        self.send_keys(self.__private_messageText,message)

        self.click(self.__private_submitButton)

    def messageSentConfirmation(self):
        postConfirmationText=self.get_text(self.__private_successText)

        assert postConfirmationText.lower() == "Success! Your details have been submitted successfully.".lower() , "The contact Us message is not submitted Properly"

        self.click(self.__private_homeButton)