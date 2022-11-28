from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import unittest

class LoginTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=chrome_options)
        cls.driver.maximize_window();
        cls.driver.implicitly_wait(10)

 
    def test_login_valid(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element(By.NAME,"username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//*[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']").click()
        self.driver.find_element(By.CLASS_NAME, "oxd-userdropdown-tab").click()
        self.driver.find_element(By.LINK_TEXT, "Logout").click()
        time.sleep(2)
      
    @classmethod  
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
   
if __name__ == '__main__':
    unittest.main()


