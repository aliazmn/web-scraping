from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from unidecode import unidecode

def translate_number(splited_num : str) -> float :
    

    
    num_part1 = unidecode(splited_num[0])
    num_part2 = unidecode(splited_num[1])
    
    price = num_part1 + "." + num_part2

    return float(price)


def get_product_detail (url : str) -> dict:
    colors = []
    url = "https://www.digikala.com"+url

    product_html : BeautifulSoup = initialize(url)

    product_detail = product_html.find("div", class_ = "grow-1 w-min-0")
    

    name = product_detail.find("h1" , class_ = "text-h4 color-900 mb-2").text.strip()

    color = product_detail.find_all("span" , class_ = "d-none-lg mr-2 text-body-2 text-no-wrap" )
    
    for elm in color :
        colors.append(elm.text.strip("\n "))
    
    exist_bar = product_html.find("div" , class_ = "mr-3-lg InfoSection_infoSection__buyBox__6fM_E")
    if "ناموجود" in str(exist_bar) : 
        status = False
        price = "0"
        gurantee = False
    else : 
        status = True
        gurantee = exist_bar.find("p" , class_="text-button-2 color-700").text
    
        if "گارانتی" in gurantee :
            gurantee = True
        else :
            gurantee = False
    
        price = product_html.find("span" , class_ = "text-h4 ml-1 color-800")
        if price :
            price =  translate_number(price.text.strip().split(","))
            
        else : 
            price = product_html.find("span" , class_ = "color-800 ml-1 text-h4").text.strip()
            price = translate_number(price.split(","))
            
        rate  = product_html.find("p" , class_ = "mr-1 text-body-2")
        if rate :
            rate = translate_number(rate.text.strip().split("."))
        else : 
            rate = 0.0

        saler = exist_bar.find("p" , class_ = "color-700 ml-2 text-subtitle").text.strip()
        
        
        discription = product_html.find("article" , 
                                    class_ = "mt-4-lg px-5 px-0-lg pb-5 ProductContent_productContent__sectionBorder__SVCc6")
        if discription:
            discription = discription.find("div" , class_ = "text-body-1 color-800").text.strip()
        else :
            discription = ""


    return {"name" : name , "price":price , "exist":status , "color" : colors ,
            "rate" : rate , "saler" : saler , "discription":discription , "gurantee" : gurantee}
   
   
def get_detail_url(web_page : str) -> None:
    
    web_page  = initialize(web_page)
    
    products = web_page.find_all("a")
    for product in products : 

        if "dkp" in product["href"]:
           result = get_product_detail(product["href"])
           yield result
        else :
            continue
        
                
def initialize(url_path = None) -> BeautifulSoup:
    
    driver = webdriver.Chrome('./chromedriver') #this driver for ubunto chorom v98 
    driver.get(url_path)        
    page = BeautifulSoup(driver.page_source , "html5lib")
    
    return page
    
    
