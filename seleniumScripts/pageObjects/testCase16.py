from selenium.webdriver.common.by import By
from seleniumScripts.utils.baseMethods import baseMethods
from seleniumScripts.utils.logger import Logger

log=Logger().get_logger(__name__)

class testCaseSixteen(baseMethods):

    __private_logoutButton=(By.CSS_SELECTOR,"a[href='/logout']")

    __private_proceedCheckout=(By.CSS_SELECTOR, "a[class='btn btn-default check_out']")

    __private_loginButtonModel=(By.XPATH, "(//a[@href='/login'])[2]")

    __private_cartButton= (By.CSS_SELECTOR, "a[href='/view_cart']")

    __private_messageBox=(By.NAME, "message")

    __private_placeOrder=(By.PARTIAL_LINK_TEXT, "Place Order")

    # card
    
    __private_ownerName=(By.NAME, "name_on_card")
    
    __private_cardNumber=(By.NAME, "card_number")
    
    __private_cardCVC=(By.NAME, "cvc")
    
    __private_cardExpiryMonth=(By.NAME, "expiry_month")
    
    __private_cardExpiryYear=(By.NAME, "expiry_year")

    __private_submitCard=(By.ID, "submit")

    __private_deleteAccount=(By.CSS_SELECTOR, "a[href^='/delete_account']")
    
    __private_deleteConfirmation=(By.XPATH, "//h2[@data-qa='account-deleted']/..//b")

    # Action Methods

    def clicklogoutButton(self):
        self.click(self.__private_logoutButton)
        
    def clickProceedCheckout(self):
        self.click(self.__private_proceedCheckout)

    def clickLoginButtonModel(self):
        self.click(self.__private_loginButtonModel)

    def clickCratButton(self):
        self.click(self.__private_cartButton)
    
    def enterMessage(self,message):
        self.scrollTillElement(self.__private_messageBox)

        self.send_keys(self.__private_messageBox,message)

    def clickPlaceOrder(self):
        self.click(self.__private_placeOrder)

    def removeRequiredtag(self):
        variables=[
            self.__private_ownerName,
            self.__private_cardNumber,
            self.__private_cardCVC,
            self.__private_cardExpiryMonth,
            self.__private_cardExpiryYear
            ]

        for locator in variables:
            element=self.find_element_wait(locator)

            self.driver.execute_script("arguments[0].removeAttribute('required')",element)
    
    def clickSubmitCard(self):
        self.click(self.__private_submitCard)

    def postAccountActions(self):
        self.click(self.__private_deleteAccount)

        assert self.get_text(self.__private_deleteConfirmation).lower() == "account deleted!" , "Account deletion failed"
