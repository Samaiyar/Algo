

#AUTHORIZATION:
from fyers_api import fyersModel
from fyers_api import accessToken
from fyers_api import fyersModel
import webbrowser
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from pyotp import TOTP
import time

redirect_uri= "http://www.google.com"  ## redircet_uri you entered while creating APP.
client_id = "E8UJZULTSC-100"                                          ## Client_id here refers to APP_ID of the created app
secret_key = "WVULOP7GU7"                                           ## app_secret key which you got after creating the app

username="XA57020"
totp='NVEX2LCFLAYD6WTZPGMUAVCQNW45PVR6'
pin1='4'
pin2='2'
pin3='6'
pin4='2'

session=accessToken.SessionModel(client_id=client_id,
                                 secret_key=secret_key,redirect_uri=redirect_uri,
                                 response_type='code', grant_type='authorization_code',)


response = session.generate_authcode()
response

def generate_auth_code():
    session=accessToken.SessionModel(client_id=client_id,
                                     secret_key=secret_key,redirect_uri=redirect_uri,
                                     response_type='code', grant_type='authorization_code',)
    response = session.generate_authcode()
    driver=webdriver.Chrome()
    driver.get(response)
    time.sleep(5)
    driver.execute_script(f"document.querySelector('[id=fy_client_id]').value = '{username}'")
    driver.execute_script("document.querySelector('[id=clientIdSubmit]').click()")
    time.sleep(4)

    t=TOTP(totp).now()
    print(t)
    print(t[0])
    print(t[5])

    driver.find_element(By.XPATH,'//*[@id="first"]').send_keys(t[0])

    driver.find_element(By.XPATH, '//*[@id="second"]').send_keys(t[1])
    driver.find_element(By.XPATH,'//*[@id="third"]').send_keys(t[2])
    driver.find_element(By.XPATH,'//*[@id="fourth"]').send_keys(t[3])
    driver.find_element(By.XPATH,'//*[@id="fifth"]').send_keys(t[4])
    driver.find_element(By.XPATH,'//*[@id="sixth"]').send_keys(t[5])
    driver.find_element(By.XPATH,'//*[@id="confirmOtpSubmit"]').click()
    time.sleep(4)

    driver.find_element(By.ID,"verify-pin-page").find_element(By.ID,"first").send_keys(pin1)
    driver.find_element(By.ID,"verify-pin-page").find_element(By.ID,"second").send_keys(pin2)
    driver.find_element(By.ID,"verify-pin-page").find_element(By.ID,"third").send_keys(pin3)
    driver.find_element(By.ID,"verify-pin-page").find_element(By.ID,"fourth").send_keys(pin4)
    driver.find_element(By.XPATH,'//*[@id="verifyPinSubmit"]').click()
    time.sleep(4)
    newurl = driver.current_url
    auth_code = newurl[newurl.index('auth_code=')+10:newurl.index('&state')]
    driver.quit()
    return auth_code


auth_code = generate_auth_code()
print(auth_code)

session.set_token(auth_code)
response = session.generate_token()

access_token = response["access_token"]
a=open("access.text",'w')
a.write(access_token)
a.close()
print(access_token)
