from selenium.webdriver.common.by import By
from seleniumScripts.utils.baseMethods import baseMethods
from seleniumScripts.utils.logger import Logger

log=Logger().get_logger(__name__)

class testCaseTwentyOne(baseMethods):
    __private_productPage=(By.CSS_SELECTOR, "a[href='/products']")

    __private_pageTitle=(By.CSS_SELECTOR, "h2[class='title text-center']")

    __private_productViewButtom=(By.CSS_SELECTOR, "a[href='/product_details/3']")

    __private_reviewerName=(By.ID, "name")
    
    __private_reviewerEmail=(By.ID, "email")
    
    __private_reviewerReview=(By.ID, "review")
    
    __private_reviewerReviewSubmit=(By.ID, "button-review")

    # Action Methods 

    def productPage(self)-> str:
        self.click(self.__private_productPage)

        text=self.get_text(self.__private_pageTitle)

        return text
    
    def openProductDetailsPage(self):
        self.click(self.__private_productViewButtom)

    def reviewerActions(self, reviewerdate:dict):
        self.send_keys(self.__private_reviewerName, reviewerdate.get("reviewerName"))
        self.send_keys(self.__private_reviewerEmail, reviewerdate.get("reviewerEmail"))
        self.send_keys(self.__private_reviewerReview, reviewerdate.get("reviewerReview"))
        self.click(self.__private_reviewerReviewSubmit)