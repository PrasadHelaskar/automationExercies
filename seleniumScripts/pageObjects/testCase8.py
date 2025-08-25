import time
from selenium.webdriver.common.by import By
from seleniumScripts.utils.baseMethods import baseMethods
from seleniumScripts.utils.logger import Logger

log=Logger().get_logger(__name__)

class testCaseEight(baseMethods):
    __private_productPage=(By.CSS_SELECTOR, "a[href='/products']")
    __private_viewDetailsProduct=(By.CSS_SELECTOR, "a[href='/product_details/1']")
    __private_productName=(By.XPATH, "//img[@alt='ecommerce website products']/..//h2")
    __private_productCategory=(By.XPATH, "(//img[@alt='ecommerce website products']/..//p)[1]")
    __private_productCost=(By.XPATH, "(//img[@alt='ecommerce website products']/../span/..//span)[2]")
    __private_productQuantity=(By.ID, "quantity")
    __private_productAvailibility=(By.XPATH, "(//b[text()='Availability:']/parent::p)")
    __private_productCondition=(By.XPATH, "(//b[text()='Condition:']/parent::p)")
    __private_productBrand=(By.XPATH, "(//b[text()='Brand:']/parent::p)")


    #Action Methods

    def visitProductDetailsPage(self):
        self.click(self.__private_productPage)
        self.click(self.__private_viewDetailsProduct)

    def getProductDetails(self) :
        return {
        "name":self.get_text(self.__private_productName),
        "category":self.get_text(self.__private_productCategory),
        "cost":self.get_text(self.__private_productCost),
        "quantity":self.get_attribute(self.__private_productQuantity,"value"),
        "availibility":self.get_text(self.__private_productAvailibility),
        "condition":self.get_text(self.__private_productCondition),
        "brand":self.get_text(self.__private_productBrand)
        }