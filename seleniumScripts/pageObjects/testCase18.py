from selenium.webdriver.common.by import By
from seleniumScripts.utils.baseMethods import baseMethods
from seleniumScripts.utils.logger import Logger

log=Logger().get_logger(__name__)

class testCaseEightteen(baseMethods):
    __private_womenCategory=(By.CSS_SELECTOR, "a[href='#Women']")

    __private_womanSaree=(By.CSS_SELECTOR, "a[href='/category_products/7']")

    __private_categoryTitle=(By.CSS_SELECTOR, "h2[class='title text-center']")

    __private_manCategory=(By.CSS_SELECTOR, "a[href='#Men']")

    __private_manJeans=(By.CSS_SELECTOR, "a[href='/category_products/6']")

    # Action Method

    def clickWomenCategory(self):
        self.click(self.__private_womenCategory)

    def clickWomenSaree(self):
        self.click(self.__private_womanSaree)

    def categoryTitleText(self)->str:
        text=self.get_text(self.__private_categoryTitle)

        return text
    
    def clickManCategory(self):
        self.click(self.__private_manCategory)

    def clickManJeans(self):
        self.click(self.__private_manJeans)
