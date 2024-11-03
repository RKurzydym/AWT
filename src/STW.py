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
        if type(add_data) == tuple:
            for i in range(0,len(add_data)):
                self.data[i].append(add_data[i])
        else:
            self.data.append(add_data)
        
    def print(self):
        print(self.data)
        
    def remove(self,data):
        self.data.remove(data)





list_of_links_internal = Links(([],[]))
list_of_links_external = Links(([],[]))
checked_URLs =  Links(([],[]))
URL_parrent_list = Links(([],[]))
dict_to_save = {}
dict_to_URL_save = {}
def main():
    website = requests.get(url)
    
    #dict_to_save.update({str(website) : url})
    
    
    links_on_website(website)
    flag = True
    i = 0
    while len(list_of_links_internal.data[0]) > 1 and flag:
        #print(i)
        i += 1
        crawl_list(list_of_links_internal.data)
        if i >= 3:
            print("LIMIT REACHED")
            flag = False
            break
    # Serializing json
    
    for i in range(0,len(checked_URLs.data[1])):
        dict_to_save.update({checked_URLs.data[0][i]:checked_URLs.data[1][i]})
    # Writing to sample.json
    json_object = json.dumps(dict_to_save,indent=4)
    print(dict_to_save)
    with open("sample.json", "w") as outfile:
        outfile.write(json_object)
        outfile.close()
    for i in range(0,len(URL_parrent_list.data[1])):
        dict_to_URL_save.update({URL_parrent_list.data[0][i]:URL_parrent_list.data[1][i]})
    # Writing to sample.json
    json_object = json.dumps(dict_to_URL_save,indent=4)
    print(dict_to_URL_save)
    with open("URLParents.json", "w") as outfile:
        outfile.write(json_object)
        outfile.close()


    
    
    
def links_on_website(html):
    parent = html.url
    soup = BeautifulSoup(html.text,'html.parser') 
    for link in soup.find_all('a'):
        path = link.get('href')
        if path and path.startswith('/') and not list_of_links_internal.check_element_in_list(link) and not checked_URLs.check_element_in_list(link): # Check if Link is internal
            list_of_links_internal.append(path,parent)
        elif not list_of_links_external.check_element_in_list(link) and not checked_URLs.check_element_in_list(link):
            list_of_links_external.append(path,parent)
        else:
            continue
    #print(list_of_links_internal.check_element_in_list(""))
    unique_list_checker(list_of_links_internal)
    unique_list_checker(list_of_links_external)
    
def crawl_list(list_to_crawl):
    for i in tqdm(range(0,list_to_crawl[0])):
        website = requests.get(url+list_to_crawl[0][i])
        links_on_website(website.text)
        #dict_to_save.update({str(website) : url+link})
        #print(website)
        #print(link)
        checked_URLs.append((list_to_crawl[0][i],str(website)))
        URL_parrent_list.append((list_to_crawl[0][i],list_to_crawl[1][i]))
        list_to_crawl[0].remove(list_to_crawl[0][i])
        list_to_crawl[1].remove(list_to_crawl[1][i])
        
        
    
    
        
    
    
    
    

def unique_list_checker(Input_list):
    list_set = set(Input_list.data)
    Input_list.data = list(list_set)
    


if __name__ == '__main__':
    main()