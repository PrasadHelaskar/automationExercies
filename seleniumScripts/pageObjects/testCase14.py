import time
from selenium.webdriver.common.by import By
from seleniumScripts.utils.baseMethods import baseMethods
from seleniumScripts.utils.logger import Logger

log=Logger().get_logger(__name__)

class testCaseFourteen(baseMethods):
    __private_addProductToCart=(By.XPATH, "(//a[@data-product-id='1'])[1]")

    __private_viewCartModel=(By.XPATH, "(//a[@href='/view_cart'])[2]")
    
    __private_proceedCheckout=(By.CSS_SELECTOR, "a[class='btn btn-default check_out']")

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