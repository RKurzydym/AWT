import requests
from bs4 import BeautifulSoup

url = "https://fachr.at"


list_of_links_internal = [""]
list_of_links_external = [""]
checked_URLs = [""]

def main():
    website = requests.get(url)
    
    list_of_links_internal , list_of_links_external = links_on_website(website.text)
    while len(list_of_links_internal) > 1:
        crawl_list(list_of_links_internal)

    
    
    
def links_on_website(html):
    list_1 = []
    list_2 = []
    soup = BeautifulSoup(html,'html.parser') 
    for link in soup.find_all('a'):
        path = link.get('href')
        if path and path.startswith('/') and link not in list_of_links_internal: # Check if Link is internal
            list_1.append(path)
        elif link not in list_of_links_external:
            list_2.append(path)
        else:
            continue

    return unique_list_checker(list_1),unique_list_checker(list_2)
    
def crawl_list(list_to_crawl):
    for link in list_to_crawl:
        website = requests.get(url+link)
        links_on_website(website.text)
        print(website)
        print(link)
        list_of_links_internal.remove(link)
        
    
    
    
    

def unique_list_checker(Input_list):
    list_set = set(Input_list)
    return list(list_set)


if __name__ == '__main__':
    main()