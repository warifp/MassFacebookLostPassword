# @@Author    : Wahyu Arif P
# @@Github    : https://www.github.com/warifp
# @@Facebook  : https://www.facebook.com/warifp
# @@Twitter   : https://www.twitter.com/wahyuarifp 
# @@Instagram : https://www.instagram.com/warifp  
# @@Update    : 1 Juni 2019 06:49
# Please don't change or recode.


from urllib2 import Request, urlopen, URLError, HTTPError
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Delete --headless to Visibility Browser
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--headless")
# chrome_options = webdriver.Chrome(chrome_options=chrome_options)
chrome_options = webdriver.Chrome(options=options)

def randWahyuArifP(j):
    i = 0
    while i<=j:
        print " ",
        i+=1

def FacebookLost():
        input_email = open("list.txt","r");
        while True:
                emailWahyuArifP = input_email.readline()
                if not emailWahyuArifP:
                        break
                        browser = webdriver.Chrome(options=options)
                        # browser = webdriver.Chrome(chrome_options=chrome_options)
                        browser.get('https://m.facebook.com/login/identify/')
                        
                        email_in=browser.find_element_by_name("email")
                        email_in.send_keys(emailWahyuArifP)

                        submit=browser.find_element_by_name("reset_action")
                        submit.submit()
                        
                        print "Email Facebook => ",emailWahyuArifP

                        browser.quit()
            
def bannerWahyuArifP():
    randWahyuArifP(9); print "Facebook Lost Password with List by Wahyu Arif P"

bannerWahyuArifP()
FacebookLost()
