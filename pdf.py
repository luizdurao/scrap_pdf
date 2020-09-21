import requests
import pandas as pd

def download_pdf(lnk):

    from selenium import webdriver

    from time import sleep

    options = webdriver.ChromeOptions()     

    print("Downloading file from link: {}".format(lnk))

    driver = webdriver.Chrome('./chromedriver.exe',chrome_options = options)

    driver.get(lnk)

    imp_by1 = driver.find_elements_by_css_selector("div.buttons")
    
    form_element = driver.find_element_by_xpath('//*[@id="buttons"]/ul/li/a')
    
    form_element.click()

    print("Status: Download Complete.")

    sleep(6)

    driver.close()


df = pd.read_csv("artigos2.csv", sep=";")
df["baixou"]=""
j=1

for i in df.iterrows():
    
    print(j)
    url = 'https://sci-hub.tw/' + str(i[1]["DI"])
    print(url)
    try:
        download_pdf(url)
        i[1]["baixou"]=1
    except:
        i[1]["baixou"]=0
    j=j+1
pd.to_csv("novo.csv", sep=";")

