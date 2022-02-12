from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from selenium.webdriver.chrome.service import Service

ser = Service('/usr/local/bin/chromedriver')
mesaj_atildimi = False
mesaj_atildimi_dijital = False

def slack_message(messagee):
    slack_token = "SLACK_TOKEN"
    channel = "CHANNEL_ID"
    
    client = WebClient(token=slack_token)
    try:
        result = client.chat_postMessage(
            channel=channel,
            text = messagee
        )
    except SlackApiError as e:
        print(e)
class Bot():
    def __init__(self):
        self.login('USERNAME','PASSWORD')
    def login(self,username,password):
        dijital_secildimi = False
        cevre_secildimi = False
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=ser,options=options)
        self.driver.get('https://obs.atauni.edu.tr')
        delay = 20
        while True:
            try:
                WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="UserName"]')))
                print( "Page is ready!")
                username_input =self.driver.find_element_by_xpath('//*[@id="UserName"]')
                username_input.send_keys(username)
                password_input = self.driver.find_element_by_xpath('//*[@id="Password"]')
                password_input.send_keys(password)
                login_button = self.driver.find_element_by_xpath('//*[@id="btn_giris"]')
                login_button.click()

                break # it will break from the loop once the specific element will be present. 
            except TimeoutException:
                
                print("Loading took too much time!-Try again")
        while True:
            try:
                WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/aside/div[5]/ul/li/ul/li[3]/a')))
                print( "Ogrenim butonu bulundu!")

                ogrenim_button = self.driver.find_element_by_xpath('/html/body/div[1]/aside/div[5]/ul/li/ul/li[3]/a')
                ogrenim_button.click()
                sleep(2)
                break
            except TimeoutException:
                print("Loading took to much time")
        while True:
            try:
                WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/aside/div[5]/ul/li/ul/li[3]/ul/li[2]/a')))
                print( "Ders alma butonu bulundu!")

                dersalma_button = self.driver.find_element_by_xpath('/html/body/div[1]/aside/div[5]/ul/li/ul/li[3]/ul/li[2]/a')

                dersalma_button.click()

                break
            except TimeoutException:
                print("Loading took to much time")
        while True:
            try:
                WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="tablo_karteks"]/div[4]/div[2]/table/tbody/tr[11]/td[1]/input')))
                WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[5]/div/div/div[4]/div[2]/table/tbody/tr[12]/td[1]/input')))
                print("İki dersinde checkboxu bulundu")

                checkbox_butonu_dijital = self.driver.find_element_by_xpath('//*[@id="tablo_karteks"]/div[4]/div[2]/table/tbody/tr[11]/td[1]/input')
                checkbox_butonu_cevre = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[5]/div/div/div[4]/div[2]/table/tbody/tr[12]/td[1]/input')
                if(checkbox_butonu_cevre.is_selected()):
                    cevre_secildimi = True
                    print("cevre basariyla secilmis")
                if(checkbox_butonu_dijital.is_selected()):
                    dijital_secildimi = True
                    print("dijital basariyla secilmis")
                if(dijital_secildimi):

                    print("Dijital ve cevre dersini  zaten almissin")
                    slack_message("Derslerin secilmis-ogzhan")
                    break
                else:
                    
                    i =0
                    while(not(dijital_secildimi)):
                        if(i % 200 == 0):
                            mesaj = "şu kadar denendi" + str(i) 
                            slack_message(mesaj)
                        if(not dijital_secildimi):
                            #checkbox_butonu_dijital.click()
                            self.driver.execute_script('arguments[0].click()', checkbox_butonu_dijital)
                            print("dijital ilk checkbox tiklandı")
                            sleep(2)
                            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[5]/div/div/div[4]/div[2]/table/tbody/tr[11]/td[1]/div/div/div/div[2]/table/tbody/tr[2]/td[1]/input')))
                            checkbox2_dijital = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[5]/div/div/div[4]/div[2]/table/tbody/tr[11]/td[1]/div/div/div/div[2]/table/tbody/tr[2]/td[1]/input')
                            self.driver.execute_script('arguments[0].click()', checkbox2_dijital)
                            print("dijital checkbox2 tiklandi")
                            sleep(2)
                            
                            tamam_butonu = self.driver.find_element_by_xpath('//*[@id="btn_modal_tamam_77742"]')
                            self.driver.execute_script('arguments[0].click()', tamam_butonu)
                            print("tamam1 tiklandi")
                            
                            
                            WebDriverWait(self.driver, delay).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[5]/div/div/div[4]/div[2]/table/tbody/tr[12]/td[1]/input')))
                        WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="tablo_karteks"]/div[4]/div[2]/table/tbody/tr[11]/td[1]/input')))

                            
                            

                        if(checkbox_butonu_dijital.is_selected()):
                                dijital_secildimi = True
                                print("dijital secildi")
                                slack_message("dijital secildi oguzhan")
                                
                                
                        i = i+1
                        print("Deneme sayisi ",i)
                        sleep(5)

                    sleep(1)
                    print("dersler alindi")
                    break
                    
                break
            except TimeoutException:
                print("Loading took to much time")
                slack_message("hata var -oguzhan")
                
        
def main():
    while(True):
        my_bot = Bot()
if __name__ == '__main__':
    main()
