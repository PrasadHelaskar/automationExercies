import sys
import pprint
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

class baseMethods:
    def __init__(self, driver):
        """
        Initializes the base page object with a WebDriver instance and sets a default wait time.

        Parameters:
            driver (WebDriver): Selenium WebDriver instance.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=10)

    def find_element_wait(self, locator):
        """
        Waits until the element located by the given locator is visible and returns it.

        Parameters:
            locator (tuple): Locator strategy and locator value, e.g., (By.ID, "element_id").

        Returns:
            WebElement: The visible web element found.
        """
        op = self.wait.until(EC.visibility_of_element_located(locator))
        return op

    def find_elements_wait(self, locator):
        """
        Waits until all elements located by the given locator are visible and returns them.

        Parameters:
            locator (tuple): Locator strategy and locator value, e.g., (By.CLASS_NAME, "element_class").

        Returns:
            list[WebElement]: A list of visible web elements found.
        """
        elements = self.wait.until(EC.visibility_of_all_elements_located(locator))
        return elements
    
    def find_element_wait_presence(self, locator):
        """
        Waits until all elements located by the given locator are visible and returns them.

        Parameters:
            locator (tuple): Locator strategy and locator value, e.g., (By.CLASS_NAME, "element_class").

        Returns:
            list[WebElement]: A list of visible web elements found.
        """
        elements = self.wait.until(EC.presence_of_element_located(locator))
        return elements

    def find_elements_wait_presence(self, locator):
        """
        Waits until all elements located by the given locator are visible and returns them.

        Parameters:
            locator (tuple): Locator strategy and locator value, e.g., (By.CLASS_NAME, "element_class").

        Returns:
            list[WebElement]: A list of visible web elements found.
        """
        elements = self.wait.until(EC.presence_of_all_elements_located(locator))
        return elements
    
    def click(self, locator):
        """
        Waits for visibility of the element and clicks on it.

        Parameters:
            locator (tuple): Locator strategy and locator value.
        """
        element = self.find_element_wait(locator)
        element.click()
    
    def click_presence(self, locator):
        """
        Waits for presence of the element and clicks on it.

        Parameters:
            locator (tuple): Locator strategy and locator value.
        """
        element = self.find_element_wait_presence(locator)
        element.click()

    def send_keys(self, locator, text):
        """
        Waits for the element, clears it, and sends the specified text.

        Parameters:
            locator (tuple): Locator strategy and locator value.
            text (str): Text to input into the element.
        """
        element = self.find_element_wait(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """
        Retrieves the visible text of the located element.

        Parameters:
            locator (tuple): Locator strategy and locator value.

        Returns:
            str: Text content of the element.
        """
        element = self.find_element_wait(locator)
        element_text = element.text
        return element_text

    def is_visible(self, locator):
        """
        Checks whether the element located by the given locator is visible.

        Parameters:
            locator (tuple): Locator strategy and locator value.

        Returns:
            str or bool: "True"/"False" string if found, otherwise False if an exception occurs.
        """
        try:
            element = self.find_element_wait(locator)
            op = element.is_displayed()
            return str(op)
        except Exception:
            return False

    def clear_element(self, locator):
        """
        Waits for the element and clears its content.

        Parameters:
            locator (tuple): Locator strategy and locator value.
        """
        element = self.find_element_wait(locator)
        element.clear()


    def get_url(self):
        """
        Retrieves the current URL of the active browser window.

        Returns:
            str: The current URL loaded in the browser.
        """
        url = self.driver.current_url
        return url
    
    def get_attribute(self,locator,attribute):
        """
        Retrieve the value of a specified attribute from a web element.

        Args:
            locator (tuple): A tuple containing the Selenium By strategy and the locator string.
                            Example: (By.XPATH, "//input[@name='email']")
            attribute (str): The name of the attribute whose value needs to be fetched.
                            Example: "type", "name", "value"

        Returns:
            str: The value of the specified attribute, or None if the attribute is not present.

        Raises:
            TimeoutException: If the element is not found within the wait time defined in `find_element_wait`.
        """
        element = self.find_element_wait(locator)
        value=element.get_attribute(attribute)
        return value
    
    def hoverOnElemet(self,locator):
        """
        Hover the mouse pointer over a web element.

        This method uses Selenium's ActionChains to move the mouse cursor 
        to the specified web element located by the given locator. 
        It is typically used to trigger hover effects such as dropdowns 
        or tooltips.

        Args:
            locator (tuple): A locator tuple (By, value) used to identify the element.

        Returns:
            None
        """
        actions=ActionChains(self.driver)
        actions.move_to_element(self.find_element_wait(locator)).perform()
        
    def DD(self, data=None):
        """
        Debug utility method to pretty-print the provided data and exit the program.

        Parameters:
            data (Any): The data structure to be pretty-printed (e.g., dict, list).

        This method is typically used during development or debugging to inspect
        the structure and content of complex data by halting further execution.
        """
        pprint.pprint(data)
        sys.exit()
    
    def page_wait(self):
        """
        Waits until the page's document.readyState is 'complete'.

        This ensures that the entire page, including all dependent resources,
        has finished loading before proceeding.
        """
        WebDriverWait(self.driver, 10).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
    
    def scrollTillElement(self, locator):
        """
        Scrolls the web page until the specified element is visible in the viewport.

        Args:
            locator (tuple): A tuple containing the locator strategy and locator value 
                            (e.g., (By.ID, "element_id")) used to identify the element.

        Returns:
            None: This method performs a scroll action and does not return a value.

        Raises:
            TimeoutException: If the element is not found within the wait period.
            NoSuchElementException: If the element cannot be located on the page.

        Example:
            self.scrollTillElemet((By.XPATH, "//div[@id='target']"))
        """
        element = self.find_element_wait_presence(locator=locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)