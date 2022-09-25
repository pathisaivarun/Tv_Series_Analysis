#importing required libraries
from asyncio.windows_events import NULL
from time import sleep
from bs4 import BeautifulSoup
from lxml import etree
import requests
import pdb
import csv
import random

#Intializing required variables
#hardcoding urls in the arrays (movies_genre_urls, series_genre_urls)
movies_genre_urls = []
series_genre_urls = []
domain = ""
final_data = []

#This method takes dom node and xpath. 
#And will search for xpath in dom node and returns the string
#If the xpath is not available then it will return null
def check_xpath_and_return_value(node, xpath):
    value = node.xpath(xpath)
    if value and len(value)>0:
        if str(type(value[0])) == "<class 'lxml.etree._ElementUnicodeResult'>":
            return str(value[0])
        else:
            return str(value[0].text)
    else:
        return NULL


#The below code will fetch the page and extracts the required fields
flag = 0
for url in movies_genre_urls:
    final_data = []
    while True:
        attempt = 0
        try:
            #We may need to fetch a lot of pages. So, given the timeout 10 and retrying 3 times incase the request fails.
            response = requests.get(url, timeout=10)
        except:
            if attempt < 3:
                attempt = attempt+1
                continue
            else:
                break
        print(response.status_code)
        #parsing the page
        soup = BeautifulSoup(response.content, "html.parser")
        #In a page we have 50 series. we are extracting all the 50 series into array. And we will iterate through each one and extract the details.
        result = soup.findAll(class_= 'lister-item mode-advanced')
        for item in result:
            temp = {}
            dom = etree.HTML(str(item))
            temp["title"] = check_xpath_and_return_value(dom, "//div[contains(@class, 'lister-item mode-advanced')]//div[contains(@class, 'lister-item-content')]//h3//a")
            temp["year"] = check_xpath_and_return_value(dom, "//div[contains(@class, 'lister-item mode-advanced')]//div[contains(@class, 'lister-item-content')]//h3//span[contains(@class, 'item-year')]")
            temp["certificate"] = check_xpath_and_return_value(dom, "//div[contains(@class, 'lister-item mode-advanced')]//div[contains(@class, 'lister-item-content')]//p//span[contains(@class, 'certificate')]")
            temp["runtime"] = check_xpath_and_return_value(dom, "//div[contains(@class, 'lister-item mode-advanced')]//div[contains(@class, 'lister-item-content')]//p//span[contains(@class, 'runtime')]")
            temp["genre"] = check_xpath_and_return_value(dom, "//div[contains(@class, 'lister-item mode-advanced')]//div[contains(@class, 'lister-item-content')]//p//span[contains(@class, 'genre')]")
            temp["rating"] = check_xpath_and_return_value(dom, "//div[contains(@class, 'lister-item mode-advanced')]//div[contains(@class, 'lister-item-content')]//div[contains(@class, 'ratings-bar')]//strong")
            temp["votes"] = check_xpath_and_return_value(dom, "//div[contains(@class, 'lister-item mode-advanced')]//div[contains(@class, 'lister-item-content')]//p[contains(@class, 'num_votes')]//span[contains(@name, 'nv')]")
            temp["director"] = check_xpath_and_return_value(dom, "//div[contains(@class, 'lister-item mode-advanced')]//div[contains(@class, 'lister-item-content')]//p[contains(., 'Director')]//a")
            final_data.append(temp)
        dom = etree.HTML(str(soup))
        #checking if next page is available or not
        nxt = check_xpath_and_return_value(dom, "//div[contains(@class, 'desc')]//a[contains(@class, 'next-page')]/@href")

        #If the array length is more than or equal to 1,000 then writing the data to a file.s
        if len(final_data) >= 1000:
            file = open('series_data_action.csv', 'a+', newline ='', encoding='utf-8')
            with file:
                header = ["title", "year", "certificate", "runtime", "genre", "rating", "votes", "director"]
                writer = csv.DictWriter(file, fieldnames = header)
                if flag==0:
                    #writing headers first time
                    writer.writeheader()
                for hsh in final_data:
                    #writing data to csv
                    writer.writerow(hsh)
            flag=1
            final_data = []
        #if next page is available then we will fetch the next page else we will break from the loop
        if nxt:
            url = domain+nxt
            print(url, len(final_data))
            #Sleeping some random time to avoid blocking
            sleep(random.randrange(3))
        else:
            break
    #Writing the remaining data to file
    file = open('series_data_action.csv', 'a+', newline ='', encoding='utf-8')
    with file:
        header = ["title", "year", "certificate", "runtime", "genre", "rating", "votes", "director"]
        writer = csv.DictWriter(file, fieldnames = header)
        if flag==0:
            writer.writeheader()
        for hsh in final_data:
            writer.writerow(hsh)
    
print(len(final_data))
