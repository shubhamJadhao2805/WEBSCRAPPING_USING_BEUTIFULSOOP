import requests
from bs4 import BeautifulSoup

def ndtvData(response):
    soup = BeautifulSoup(response.text,"lxml")
    tenTopStories = soup.select(".featured_cont")
    print("1. Top ten headLine of NDTV: ")
    print(tenTopStories[0].text)
    print("\n2. Hyperlink to the detailed story page. :\n\n")
    hyperLink = tenTopStories[0].select("h2")
    for i in hyperLink:
        url = i.select("a")[0].get("href")
        print("---------------------------------------")
        print(url)

    print("\n3 Images of the story.\n\n")
    imageUrl = tenTopStories[0].select("div")
    for i in imageUrl:
        imageUrl = i.select("img")[0].get("src")
        print("---------------------------------------")
        print(imageUrl)
   
def timesOfIndia(response):
    soup = BeautifulSoup(response.text,"lxml")
    topStory = soup.select(".top-story")
    print(topStory[0].text)
    print("\nHyperlink to the detailed story page\n\n")
    hyperlink = topStory[0].select("a")
    for i in hyperlink:
        url = i.get("href")
        print("-----------------------------------")
        print("https://timesofindia.indiatimes.com" + url)

def firstPost(response):
    soupFP = BeautifulSoup(response.text,"lxml")
    topHeadLine = soupFP.select(".big-thumb")
    print("Top headLine\n\n")
    for i in topHeadLine:
        title = i.select("a")[0].get("title")
        print(title)
        print("-----------------------------")

    print("\n\nOne paragraph of detail :\n")
    for i in topHeadLine:
        para = i.select("p")
        if len(para) != 0:
            print(para[0].text)
            print("-----------------------------")
    
    
    print("\n\nImage of the story: \n\n")
    for i in topHeadLine:
        image = i.select("img")[0].get("src")
        print(image)
        print("---------------------")
    
    print("\n\n Hyperlink to detail story: \n\n")
    for i in topHeadLine:
        url = i.select("a")[0].get("href")
        print(url)
        print("----------------------")
def indianExpress(response):
    soup = BeautifulSoup(response.text,"lxml")
    data = soup.select(".left-part")
    headLines = data[1].select("img")
    print("Top News HeadLines:\n\n")
    for i in headLines:
        head = i.get("alt")
        print(head)
        print("---------------------------")

    
    print("\n\nsrc of Image of the story : \n\n")
    for i in headLines:
        imageSrc = i.get("src")
        print("https:"+imageSrc)
        print("----------------------------")
    print("\n\n hyperlink to detail story :\n\n")
    hyperlink = data[1].select(".story-image")
    for i in hyperlink:
        url = i.select("a")[0].get("href")
        print(url)
        print("-----------------------------")
    
def economicTimes(response):
    sopeET = BeautifulSoup(response.text,"lxml")
    data = sopeET.select(".tabsContent")
    headLine = data[0].select("a")
    print("Top news HeadLines:\n\n")
    for i in headLine:
        head = i.text
        print(head)
        print("-----------------------")

    print("\n\n HyperLinkes to detail story :\n\n")
    for i in headLine:
        url = i.get("href")
        print("https://economictimes.indiatimes.com/"+url)
        print("-------------------------")
        
def scrollin(response):
    soupSI = BeautifulSoup(response.text,"lxml")
    data = soupSI.select(".latest-homepage")
    print("\n\n Top news headline\n")
    topNews= data[0].select("h1")
    for i in topNews:
        headLine = i.text
        print(headLine)
        print("------------------------------------")
    print("\n\n One paragraph of detail. \n\n")
    para = data[0].select("h2")
    for i in para:
        para = i.text
        print(para)
        print("------------------------------------")

    print("\n\n Image of the story \n\n")
    imageSrc = data[0].select("img")
    for i in imageSrc:
        print(i.get("src"))
        print("-------------------------------------")

    print("\n\n hyperLink of detail page\n\n")
    hyperlink = data[0].select("a")
    for i in hyperlink:
        url = i.get("href")
        print(url)
        print("---------------------------------------")
def livemint(response):
    soupLM = BeautifulSoup(response.text,"lxml")
    topNews = soupLM.select(".mainSec")
    head = topNews[0].select("h2")
    print("\n\n Top Headline ")
    for i in head:
        print(i.text)
        print("------------------------------")

    print("\n\n  One paragraph of detail")
    para = topNews[0].select(".highlights")
    for i in para:
        print(i.text)
        print("-------------------------------")
    print("\n\n Image url of top headlines: \n\n")
    # image = topNews[0].select("figure")[0].select("img")
    image = topNews[0].select("figure")
    for i in image:
        imgURL = i.select("img")[0].get("data-src")
        print(imgURL)
        print("-------------------------------")
while True:
    print("Please select Website :")
    print("1 NDTV")
    print("2 Times of india")
    print("3 First post")
    print("4 The indian Express")
    print("5 Economic Times")
    print("6 Scroll.in")
    print("7 Livemint")
    print("8 close")
    
    opt = int(input())
    if opt == 1:
        print("\nNDTV\n")
        response = requests.get("https://www.ndtv.com")
        ndtvData(response)
    if opt == 2:
        print("\nTOI\n")
        response = requests.get("https://timesofindia.indiatimes.com")
        timesOfIndia(response)
    if opt == 3:
        print("\nFIRSTPOST\n")
        response = requests.get("https://www.firstpost.com")
        firstPost(response)
    if opt == 4:
        print("\nIE\n")
        response = requests.get("https://indianexpress.com/?newsletterVerified=true&redirectFromPopup=true")
        indianExpress(response)
    if opt == 5:
        print("\nET\n")
        response = requests.get("https://economictimes.indiatimes.com/?from=mdr")
        economicTimes(response)
    if opt == 6:
        print("\nSCROLL\n")
        response = requests.get("https://scroll.in/latest/")
        scrollin(response)
    if opt == 7:
        print("\nLIVEMINT\n")
        response = requests.get("https://www.livemint.com")
        livemint(response)
    if opt == 8:
        break;

