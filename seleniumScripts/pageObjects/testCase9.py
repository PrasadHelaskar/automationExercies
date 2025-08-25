import time
from selenium.webdriver.common.by import By
from seleniumScripts.utils.baseMethods import baseMethods
from seleniumScripts.utils.logger import Logger

log=Logger().get_logger(__name__)

class testCaseNine(baseMethods):
    __private_productPage=(By.CSS_SELECTOR, "a[href='/products']")
    __private_searchProduct=(By.ID, "search_product")
    __private_searchProductButton=(By.ID, "submit_search")
    __private_productNames=(By.XPATH, "//img[@alt='ecommerce website products']/..//p")

    #Action Methods

    def visitProductDetailsPage(self):
        self.click(self.__private_productPage)
    
    def enterProductDesciption(self,name):
        self.send_keys(self.__private_searchProduct, name)
        self.click(self.__private_searchProductButton)

    def getAllProductNames(self)-> list:
        elements=self.find_elements_wait(self.__private_productNames)
        productsName=[]

        for element in elements:
            name=element.text
            productsName.append(name)
        
        # shorter version of the above loop
        # return [element.text for element in elements]
        return productsName