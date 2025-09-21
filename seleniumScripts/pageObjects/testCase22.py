from selenium.webdriver.common.by import By
from seleniumScripts.utils.baseMethods import baseMethods
from seleniumScripts.utils.logger import Logger

log=Logger().get_logger(__name__)

class testCaseTwentyTwo(baseMethods):
    __private_recommendedTitle=(By.XPATH, "(//h2[@class='title text-center'])[2]")

    __private_recommendedProductOneAddToCart=(By.XPATH, "(//a[@data-product-id='5'])[3]")

    __private_cartFromModel=(By.XPATH, "(//a[@href='/view_cart'])[2]")

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



    #Action Methods

    def scrollTillRecommendedItem(self)-> str:
        self.scrollTillElement(self.__private_recommendedTitle)

        title=self.get_text(self.__private_recommendedTitle)

        return title

    def addItemToCart(self):
        self.click_presence(self.__private_recommendedProductOneAddToCart)
        self.click(self.__private_cartFromModel)

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