from selenium import webdriver;
from time import sleep;
from credentials import username,password1,password2,password3,password4,password5,password6
class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome();
    
    def login(self):
        self.driver.get('https://tinder.com')
        sleep(2)
        phone_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[1]/button')
        phone_btn.click()

        base_window = self.driver.window_handles[0]
        email_in = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div[2]/div/input')
        email_in.send_keys(username)
        login_btn = bot.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/button')
        login_btn.click()
        password1_in = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div[2]/input[1]')
        password2_in = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div[2]/input[2]')
        password3_in = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div[2]/input[3]')
        password4_in = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div[2]/input[4]')
        password5_in = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div[2]/input[5]')
        password6_in = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div[2]/input[6]')
        password1_in.send_keys(password1)
        password2_in.send_keys(password2)
        password3_in.send_keys(password3)
        password4_in.send_keys(password4)
        password5_in.send_keys(password5)
        password6_in.send_keys(password6)
        login_btn2=self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/button[2]')
        login_btn2.click()

        popup_1 =self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_1.click()
        popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_2.click()
        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[1]')
        popup_3.click()

    def like(self):
       like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/div[4]/button')
       like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/div[2]/button')
        dislike_btn.click()
    def auto_swipe(self):
        while True:
            sleep(0.5)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()


    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()

bot = TinderBot()
bot.login()
    

       