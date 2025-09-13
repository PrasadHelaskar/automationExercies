import time
from selenium.webdriver.common.by import By
from seleniumScripts.utils.baseMethods import baseMethods
from seleniumScripts.utils.logger import Logger

log=Logger().get_logger(__name__)

class testCaseTwelve(baseMethods):
    __private_productPage=(By.CSS_SELECTOR, "a[href='/products']")
    
    def productHover(self,index):
        xpath=f"(//img[@alt='ecommerce website products'])[{index}]"
        __private_productHover=(By.XPATH,xpath)
        return __private_productHover

    def addToCartAfterHover(self,index):
        xpath=f"(//a[@class='btn btn-default add-to-cart'])[{index}]"
        __private_addToCartAfterHover=(By.XPATH, xpath)
        return __private_addToCartAfterHover
        
    __private_continueShoppingButton=(By.CSS_SELECTOR, "button[class='btn btn-success close-modal btn-block']")

    __private_viewCart=(By.XPATH, "(//a[@href='/view_cart'])[2]")
    
    __private_productCount=(By.XPATH, "//tr[contains(@id,'product')]") # list count

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

    def addToCartOnHover(self,index):
        for iteration in range(2):
            self.hoverOnElemet(self.productHover(index))
            self.click(self.addToCartAfterHover(index*2))
            if index==3 and iteration<2:
                return
            self.clickContinueShopping()

    def clickContinueShopping(self):
        self.click(self.__private_continueShoppingButton)

    def clickViewCart(self):
        self.click(self.__private_viewCart)

    def getProductCount(self) -> int:
        listOfElements=self.find_elements_wait(self.__private_productCount)
        count=len(listOfElements)

        return count
    
    def getDetails(self,index)-> list:
        textPrice=self.get_text(self.productPrice(index))

        finalPrice=int(textPrice.replace("Rs.","").replace(",","").strip())

        textQuantity=self.get_text(self.productQuantity(index))

        finalQuantity=int(textQuantity)

        textTotalPrice=self.get_text(self.productTotalPrice(index))

        finalTotalPrice=int(textTotalPrice.replace("Rs.","").replace(",","").strip())

        return [finalPrice,finalQuantity,finalTotalPrice]

