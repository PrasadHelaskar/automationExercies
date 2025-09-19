from selenium.webdriver.common.by import By
from seleniumScripts.utils.baseMethods import baseMethods
from seleniumScripts.utils.logger import Logger

log=Logger().get_logger(__name__)

class testCaseNinteen(baseMethods):
    __private_productPage=(By.CSS_SELECTOR, "a[href='/products']")

    __private_brandMadame=(By.CSS_SELECTOR, "a[href='/brand_products/Madame']")

    __private_brandPolo=(By.CSS_SELECTOR, "a[href='/brand_products/Polo']")

    __private_brandTitleText=(By.CSS_SELECTOR, "h2[class='title text-center']")

    # Action Methods

    def clickProductPage(self):
        self.click(self.__private_productPage)

    def clickMadame(self):
        self.click(self.__private_brandMadame)

    def clickPolo(self):
        self.click(self.__private_brandPolo)

    def BreandTitleText(self)-> str:
        text=self.get_text(self.__private_brandTitleText)

        return text