from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

class Bot:
    def __init__(self, contact_list, contact_filter):
        self.contact_list = contact_list
        self.contact_filter = contact_filter
        self.dir_path = os.getcwd()
        self.chrome_options = Options()
        self.chrome_options.add_argument('user-data-dir=' + self.dir_path + '/profile')
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get('https://web.whatsapp.com/')
        self.service_started = False

    def get_contact_name(self):
        contact_name_element = self.driver.find_element(By.XPATH, '//*[@id="main"]/header/div[2]/div/div/span')
        contact_name = contact_name_element.text
        return contact_name

    def send_message(self, message):
        xpath_input = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
        send = self.driver.find_element(By.XPATH, xpath_input)
        send.send_keys(message)
        send_message_button = self.driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
        time.sleep(3)
        send_message_button.click()

    def actions_bot(self):
        try:
            notification = self.driver.find_elements(By.CLASS_NAME, 'aumms1qt')

            if notification:
                notification_click = notification[-1]
                notification_action = webdriver.common.action_chains.ActionChains(self.driver)
                notification_action.move_to_element_with_offset(notification_click, 0, -20)
                notification_action.click()
                notification_action.perform()
                notification_action.click()
                notification_action.perform()
                time.sleep(3)
                
                contact_name = self.get_contact_name()

                while True:
                    if self.contact_filter:
                        if contact_name in self.contact_list:
                            if not self.service_started:
                               # Send the options to the user
                                menssage_options = f'Olá {contact_name}, sou a assistente virtual do Jackson. Em que posso ajudar?'
                                self.send_message(menssage_options)
                                self.service_started = True
                                webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()

                            if self.service_started:
                                self.send_message('Certo, deixei tudo anotadinho. Assim que possível, ele estará te respondendo.')
                                webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
                    else:
                        if not self.service_started:
                                # Send the options to the user
                                menssage_options = f'Olá {contact_name}, sou a assistente virtual do Jackson. Em que posso ajudar?'
                                self.send_message(menssage_options)
                                self.service_started = True
                                webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()

                        if self.service_started:
                            self.send_message('Certo, deixei tudo anotadinho. Assim que possível, ele estará te respondendo.')
                            webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()

        except Exception as e:
            print(e)