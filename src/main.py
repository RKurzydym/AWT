import requests
from bs4 import BeautifulSoup
import json
from tqdm import tqdm

url = "https://fachr.at"

class Links:
    def __init__(self,data):
        self.data = data
        
    def check_element_in_list(self,element):
        if element in self.data:
            return True
        else:
            return False
        
    def append(self,add_data):
        self.data.append(add_data)
        
    def print(self):
        print(self.data)
        
    def remove(self,data):
        self.data.remove(data)





list_of_links_internal = Links([""])
list_of_links_external = Links([""])
checked_URLs =  Links([""])
dict_to_save = {}
def main():
    website = requests.get(url)
    
    dict_to_save.update({website : url})
    
    
    links_on_website(website.text)
    flag = True
    i = 0
    while len(list_of_links_internal.data) > 1 and flag:
        print(i)
        i += 1
        crawl_list(list_of_links_internal)
        if i > 4:
            print("LIMIT REACHED")
            flag = False
            break
    # Serializing json
    json_object = json.dumps(dict_to_save, indent=4)
    
    # Writing to sample.json
    with open("sample.json", "w") as outfile:
        outfile.write(json_object)
    #print(checked_URLs)

    
    
    
def links_on_website(html):
    soup = BeautifulSoup(html,'html.parser') 
    for link in soup.find_all('a'):
        path = link.get('href')
        if path and path.startswith('/') and not list_of_links_internal.check_element_in_list(link) and not checked_URLs.check_element_in_list(link): # Check if Link is internal
            list_of_links_internal.append(path)
        elif not list_of_links_external.check_element_in_list(link) and not checked_URLs.check_element_in_list(link):
            list_of_links_external.append(path)
        else:
            continue
    #print(list_of_links_internal.check_element_in_list(""))
    unique_list_checker(list_of_links_internal)
    unique_list_checker(list_of_links_external)
    
def crawl_list(list_to_crawl):
    for link in tqdm(list_to_crawl.data):
        website = requests.get(url+link)
        links_on_website(website.text)
        dict_to_save.update({website : url+link})
        #print(website)
        #print(link)
        list_to_crawl.remove(link)
        checked_URLs.append(link)
    
    
        
    
    
    
    

def unique_list_checker(Input_list):
    list_set = set(Input_list.data)
    Input_list.data = list(list_set)
    


if __name__ == '__main__':
    main()