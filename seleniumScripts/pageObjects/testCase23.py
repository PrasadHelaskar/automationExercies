from selenium.webdriver.common.by import By
from seleniumScripts.utils.baseMethods import baseMethods
from seleniumScripts.utils.logger import Logger

log=Logger().get_logger(__name__)

class testCaseTwentyThree(baseMethods):
    __private_ProceedToCheckoutButton=(By.LINK_TEXT, "Proceed To Checkout")

    __priavte_DeliveryAddressLineOne=(By.XPATH, "(//li[@class='address_address1 address_address2'])[2]")
    
    __priavte_DeliveryAddressLineTwo=(By.XPATH, "(//li[@class='address_city address_state_name address_postcode'])[1]")

    __priavte_BilingAddressLineOne=(By.XPATH, "(//li[@class='address_address1 address_address2'])[5]")

    __priavte_BilingAddressLineTwo=(By.XPATH, "(//li[@class='address_city address_state_name address_postcode'])[2]")

    __private_deleteAccount=(By.CSS_SELECTOR, "a[href^='/delete_account']")
    
    __private_deleteConfirmation=(By.XPATH, "//h2[@data-qa='account-deleted']/..//b")

    __private_Continuebutton=(By.CSS_SELECTOR, "a[data-qa='continue-button']")

    #Action Methods

    def clickProceedToCheckoutButton(self):
        self.click(self.__private_ProceedToCheckoutButton)

    def deliveryAddress(self)-> str:
        deliveryAddressLineOne=self.get_text(self.__priavte_DeliveryAddressLineOne)
        deliveryAddressLineTwo=self.get_text(self.__priavte_DeliveryAddressLineTwo)

        return (deliveryAddressLineOne+" "+deliveryAddressLineTwo)
    
    def bilingAddress(self)-> str:
        bilingAddressLineOne=self.get_text(self.__priavte_BilingAddressLineOne)
        bilingAddressLineTwo=self.get_text(self.__priavte_BilingAddressLineTwo)

        return (bilingAddressLineOne+" "+bilingAddressLineTwo)

    def postAccountActions(self):
        self.click(self.__private_deleteAccount)

        assert self.get_text(self.__private_deleteConfirmation).lower() == "account deleted!" , "Account deletion failed"

        self.click(self.__private_Continuebutton)
