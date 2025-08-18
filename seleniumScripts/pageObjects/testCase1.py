import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from seleniumScripts.utils.baseMethods import baseMethods
from seleniumScripts.utils.logger import Logger

log=Logger().get_logger(__name__)

class testCaseOne(baseMethods):
    __private_signUpButton=(By.CSS_SELECTOR, "a[href^='/login']")
    __private_signUpForm=(By.CSS_SELECTOR,"div[class='signup-form']")
    __private_nameTextBox=(By.NAME, "name")
    __private_emailTextBox=(By.CSS_SELECTOR,"input[data-qa='signup-email']")
    __private_createAccount=(By.CSS_SELECTOR, "button[data-qa='signup-button']")
    __private_genderTItle=(By.XPATH, "(//input[@type='radio'])[1]")
    __private_nameTestField=(By.ID,"name")
    __private_passwordTextField=(By.ID, "password")
    
    # Select class
    __private_daySelection=(By.ID,"days")
    __private_monthSelection=(By.ID,"months")
    __private_yearSelection=(By.ID,"years")

    __private_newLetterConsent=(By.ID, "newsletter")
    __private_specialOffers=(By.ID, "optin")

    # Address Info
    __private_addressFirstName=(By.ID,"first_name")
    __private_addressLastName=(By.ID,"last_name")
    __private_addressLineOne=(By.ID,"address1")

    # Select class
    __private_addressCountry=(By.ID,"country")

    __private_addressState=(By.ID,"state")
    __private_addressCity=(By.ID,"city")
    __private_addressZipCode=(By.ID,"zipcode")
    __private_addressMobileNumber=(By.ID,"mobile_number")

    __private_creatAccountButton=(By.CSS_SELECTOR,"button[data-qa='create-account']")
    __private_accountConfirmation=(By.XPATH, "//h2[@data-qa='account-created']/..//b")
    __private_Continuebutton=(By.CSS_SELECTOR, "a[data-qa='continue-button']")
    __private_loggedinUserNmae=(By.XPATH, "//i[@class='fa fa-user']/..//b")
    __private_deleteAccount=(By.CSS_SELECTOR, "a[href^='/delete_account']")
    __private_deleteConfirmation=(By.XPATH, "//h2[@data-qa='account-deleted']/..//b")


    # ACTION METHODS
    def signupActions(self,name,email):
        
        self.click(self.__private_signUpButton)

        if (self.is_visible(self.__private_signUpForm)):
            self.send_keys(self.__private_nameTextBox,name)
            self.send_keys(self.__private_emailTextBox,email)
            self.click(self.__private_createAccount)
        
        else:
            assert self.is_visible(self.__private_signUpForm), "The sign-up from is not visible"
        
    def genderNamePasswordActions(self,name,passwrod):

        self.click(self.__private_genderTItle)
        self.clear_element(self.__private_nameTestField)
        self.send_keys(self.__private_nameTestField,name)
        self.clear_element(self.__private_passwordTextField)
        self.send_keys(self.__private_passwordTextField,passwrod)

    def birthDayselection(self,day,month,year):
        selectdays=Select(self.find_element_wait(self.__private_daySelection))
        selectdays.select_by_value(str(day))

        selectMonths=Select(self.find_element_wait(self.__private_monthSelection))
        selectMonths.select_by_value(str(month))

        selectyear=Select(self.find_element_wait(self.__private_yearSelection))
        selectyear.select_by_value(str(year))
    
    def consentsActions(self):
        self.click(self.__private_newLetterConsent)
        self.click(self.__private_specialOffers)
    
    def addressActions(self,firstName,lastName,addressLineOne,state,city,zipCode,mobileNumber):
        self.send_keys(self.__private_addressFirstName,firstName)
        self.send_keys(self.__private_addressLastName,lastName)
        self.send_keys(self.__private_addressLineOne,addressLineOne)

        selectCountry=Select(self.find_element_wait(self.__private_addressCountry))
        selectCountry.select_by_value("United States")

        self.send_keys(self.__private_addressState,state)
        self.send_keys(self.__private_addressCity,city)
        self.send_keys(self.__private_addressZipCode,zipCode)
        self.send_keys(self.__private_addressMobileNumber,mobileNumber)
    
    def CreatAccountActions(self,name):
        self.click(self.__private_creatAccountButton)

        log.info(self.get_text(self.__private_accountConfirmation))

        assert self.get_text(self.__private_accountConfirmation).lower() == "account created!" , "Account creation failed"

        self.click(self.__private_Continuebutton)

        assert self.get_text(self.__private_loggedinUserNmae).lower() == name.lower() , "Account is not verifird as user name is different"

    def postAccountActions(self):
        self.click(self.__private_deleteAccount)

        assert self.get_text(self.__private_deleteConfirmation).lower() == "account deleted!" , "Account deletion failed"

        self.click(self.__private_Continuebutton)