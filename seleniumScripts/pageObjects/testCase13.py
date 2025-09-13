import time
from selenium.webdriver.common.by import By
from seleniumScripts.utils.baseMethods import baseMethods
from seleniumScripts.utils.logger import Logger

log=Logger().get_logger(__name__)

class testCaseThirteen(baseMethods):
    __private_productPage=(By.CSS_SELECTOR, "a[href='/products']")

    __private_openProductDetails=(By.CSS_SELECTOR, "a[href='/product_details/3']")

    __private_productQunatityDetialPage=(By.NAME, "quantity")

    __private_addToCartButton=(By.CSS_SELECTOR, "button[class='btn btn-default cart']")
    
    __private_viewCart=(By.XPATH, "(//a[@href='/view_cart'])[2]")
    
    def productPrice(self,index):
        xpath=f"(//td[@class='cart_price'])[{index}]/p"
        __private_productPrice=(By.XPATH, xpath)
        
        return __private_productPrice
    
    def productQuantity(self,index):
        xpath=f"(//button[@class='disabled'])[{index}]"
        __private_productQuantity=(By.XPATH, xpath)
        
        return __private_productQuantity
    
    def productTotalPrice(self,index):
        xpath=f"(//p[@class='cart_total_price'])[{index}]"
        __private_productTotalPrice=(By.XPATH, xpath)
        
        return __private_productTotalPrice
    
    # Action Methosds
    
    def openProductPage(self):
        self.click(self.__private_productPage)

    def openProductDetailsPage(self):
        self.click(self.__private_openProductDetails)

    def productCountAddition(self, count:int):
        self.clear_element(self.__private_productQunatityDetialPage)
        self.send_keys(self.__private_productQunatityDetialPage, count)

    def clickAddToCart(self):
        self.click(self.__private_addToCartButton)
        
    def clickViewCart(self):
        self.click(self.__private_viewCart)
     
    def getDetails(self,index)-> list:
        textPrice=self.get_text(self.productPrice(index))

        finalPrice=int(textPrice.replace("Rs.","").replace(",","").strip())

        textQuantity=self.get_text(self.productQuantity(index))

        finalQuantity=int(textQuantity)

        textTotalPrice=self.get_text(self.productTotalPrice(index))

        finalTotalPrice=int(textTotalPrice.replace("Rs.","").replace(",","").strip())

        return [finalPrice,finalQuantity,finalTotalPrice]

