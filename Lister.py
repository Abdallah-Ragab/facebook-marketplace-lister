from cmath import exp
from selenium import webdriver
import time
import os
from Element import Element
from Helpers import read_json
from datetime import datetime
from colorama import Fore, Style
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait



class Lister:
    def __init__(self):
        self.driver_file = 'chromedriver.exe'
        self.sleep_time = 1
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        chrome_options.add_experimental_option("prefs",prefs)
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--start-maximized")
        
        self.driver = webdriver.Chrome('drivers/%s' % self.driver_file, chrome_options=chrome_options)
        self.driver.implicitly_wait(30)
        
    def read_accounts(self):
        return read_json('accounts')['accounts']
        
    def login(self, account_id):
        registered_accounts = self.read_accounts()
        account_info = list(filter(lambda acc: acc['id'] == account_id, registered_accounts))[0]
        log('Logging in as "%s" ..' % account_info['name'], 'main')
        
        self.driver.get('https://www.facebook.com/login')
        
        
        # entering email
        email_input = Element(self.driver, 'login_email').element
        email_input.clear()
        email_input.send_keys(account_info['email'])
        
        # entering password
        password_input = Element(self.driver, 'login_password').element
        password_input.clear()
        password_input.send_keys(account_info['password'])
        
        # Submitting
        password_button = Element(self.driver, 'login_button').element
        password_button.click()
        
        # Confirm Logged In
        logged = WebDriverWait(self.driver, 60).until(
            lambda driver: "login" not in driver.current_url 
        )
        
        if logged : log('Logged in Successfully.', 'success')
        else : log('Failed To Login.', 'failure')
        
        return logged
    
    def list(self, item):
        self.driver.get('https://www.facebook.com/marketplace/create/item')
        
        listing_item = Item(self.driver, item)
        
        listing_item.upload_images()
        time.sleep(self.sleep_time)
        
        listing_item.enter_title()
        time.sleep(self.sleep_time)
        
        listing_item.enter_price()
        time.sleep(self.sleep_time)
        
        listing_item.choose_category()
        time.sleep(self.sleep_time)
        
        listing_item.choose_condition()
        time.sleep(self.sleep_time)
        
        if 'description' in item.keys() and item['description'] :
            listing_item.enter_description()
            time.sleep(self.sleep_time)
        
        if 'sku' in item.keys() and item['sku'] :
            listing_item.enter_sku()
            time.sleep(self.sleep_time)
        
        listing_item.choose_location()
        time.sleep(self.sleep_time)
        
        if 'hide_from_friends' in item.keys() and item['hide_from_friends'] :        
            listing_item.hide_from_friends()
            time.sleep(self.sleep_time)
        
        listing_item.click_next()
        time.sleep(self.sleep_time)
        
        listing_item.click_publish()
        time.sleep(self.sleep_time)
        
        # Check if Posted
        posted = WebDriverWait(self.driver, 60).until(
            lambda driver: "you" in driver.current_url 
        )
        
        return posted

class Item :
    def __init__(self, driver, item):
        self.driver = driver
        self.item = item
        
    def upload_images(self):
        try:
            log('Uploading Images', 'main')
            image_upload = Element(self.driver, 'post_image').element
            self.driver.execute_script("document.querySelector('%s').classList = []" % Element(self.driver, 'post_image_css').xpath)
            log('Showing image input ..', 'main')
            joined_images_path = ' \n '.join([os.path.abspath('images/%s' % image['file']) for image in self.item['images']][:10])
            log('sending images ..', 'main')
            image_upload.send_keys(joined_images_path)
            log('Uploaded Images Successfully .', 'success')
            return True
        except :
            log('FAILED TO UPLOAD IMAGE', 'failure')
            return False
            
    def enter_title(self):
        try:
            log('Entering The Title', 'main')
            title_input = Element(self.driver, 'post_title').element
            title_input.clear()
            title_input.send_keys(self.item['title'])
            log('Entered Title Successfully .', 'success')
            return True
        except :
            log('FAILED TO ENTER THE TITLE', 'failure')
            return False
            
    def enter_price(self):
        try:
            log('Entering The Price', 'main')
            price_input = Element(self.driver, 'post_price').element
            price_input.clear()
            price_input.send_keys(self.item['price'])
            log('Entered Price Successfully .', 'success')
            return True
        except :
            log('FAILED TO ENTER THE PRICE', 'failure')
            return False
    
    def choose_category(self):
        try:
            log('Choosing The Category', 'main')
            category_dropdown = Element(self.driver, 'post_category').element
            category_dropdown.click()
            
            values = self.item['category'] if 'category' in self.item.keys() and self.item['category']  else None
            category_dropdown_option = Element(self.driver, 'post_category_option', values).element
            print(Element(self.driver, 'post_category_option', values).xpath)
            print(Element(self.driver, 'post_category_option', values).xpath)
            print(Element(self.driver, 'post_category_option', values).xpath)
            print(Element(self.driver, 'post_category_option', values).xpath)
            print(Element(self.driver, 'post_category_option', values).xpath)
            log('clicking The Category Dropdown ..', 'sub')
            category_dropdown_option.click()
            
            log('Category Chosen Successfully .', 'success')
            return True
        except :
            log('FAILED TO CHOOSE THE CATEGORY', 'failure')
            return False
    
    def choose_condition(self):
        try:
            log('Choosing The Condition', 'main')
            condition_dropdown = Element(self.driver, 'post_condition').element
            condition_dropdown.click()
            log('clicking The Condition Dropdown ..', 'sub')
        
            values = self.item['condition'] if 'condition'in self.item.keys() and self.item['condition'] else None
            condition_dropdown_option = Element(self.driver, 'post_condition_option', values).element
            condition_dropdown_option.click()
            log('Condition Chosen Successfully .', 'success')
            return True
        except :
            log('FAILED TO CHOOSE THE CATEGORY', 'failure')
            return False
    
    def enter_description(self):
        try:
            log('Entering The Description', 'main')
            description_input = Element(self.driver, 'post_description').element
            description_input.clear()
            description_input.send_keys(self.item['description'])
            log('Entered Description Successfully .', 'success')
            return True
        except :
            log('FAILED TO ENTER THE Description', 'failure')
            return False
        
    def enter_sku(self):
        try:
            log('Entering The SKU', 'main')
            sku_input = Element(self.driver, 'post_sku').element
            sku_input.clear()
            sku_input.send_keys(self.item['sku'])
            log('Entered SKU Successfully .', 'success')
            return True
        except :
            log('FAILED TO ENTER THE SKU', 'failure')
            return False
    
    def choose_location(self):
        try:
            location = self.item['location'] if self.item['location'] else Element(self.driver, 'post_location_option').defaults
            log('Choosing The Location', 'main')
            location_input = Element(self.driver, 'post_location').element
            location_input.click()
            log('Searching Locations ..', 'sub')
            location_input.send_keys(Keys.DELETE)
            location_input.send_keys(location)
            
            log('Choosing Location ..', 'sub')
            values = self.item['location'] if 'location'in self.item.keys() and self.item['location'] else None
            location_input_option = Element(self.driver, 'post_location_option', values).element
            location_input_option.click()
            
            log('Location Chosen Successfully .', 'success')
            return True
        except :
            log('FAILED TO CHOOSE THE Location', 'failure')
            return False
    
    def hide_from_friends(self):
        try:
            log('Checking Hide From Friends', 'main')
            self.click_button('post_hide_from_friends')
            log('Checked Hide From Friends Successfully .', 'success')
            return True
        except :
            log('FAILED TO Check Hide From Friends', 'failure')
            return False

    def click_next(self):
        try:
            log('Clicking Next', 'main')
            self.click_button('post_next_button')
            log('Clicked Next Successfully', 'success')
            return True
        except :
            log('FAILED TO click Next', 'failure')
            return False

    def click_publish(self):
        try:
            log('Clicking Publish', 'main')
            self.click_button('post_publish_button')
            log('Clicked Publish Successfully', 'success')
            return True
        except :
            log('FAILED TO click Publish', 'failure')
            return False

    def click_button(self, button):
        element = Element(self.driver, button).element
        element.click()

def log(msg, type=None):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    msg = "[%s] : %s" % (current_time, msg)
    if type is not None:
        if type == 'failure':
            msg = Fore.RED + "\t- " + msg + Style.RESET_ALL
        elif type == 'success':
            msg = Fore.GREEN + "\t+ " + msg + Style.RESET_ALL
        elif type == 'sub':
            msg = Fore.WHITE + "\t> " + msg + Style.RESET_ALL
        elif type == 'main':
            msg = Fore.WHITE + ">> " + msg + Style.RESET_ALL
        else:
            msg = msg + Style.RESET_ALL
    else:
        msg = msg + Style.RESET_ALL
    print (msg)

