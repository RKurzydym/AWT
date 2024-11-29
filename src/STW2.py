import requests
from bs4 import BeautifulSoup
import json
from tqdm import tqdm


url = "https://fachr.at"

class NoS:
    def __init__(self,data):
        self.data = data
    def newCurrent(self,data):
        self.data.append(data)
    def print(self): 
        print(self.data)
    def printList(self):
        for x in self.data:
            print(x)
    def __len__(self):
        return len(self.data)
        
        
NoS_list = NoS([[[""],[""],[""],[""]]])



def main():
    begin(url)
    


def begin(url): #O(n*(n-m)) i think i calculatet it wrong but it a lot faster that the v1 version
    website = requests.get(url)
    links = getAllLinks(website) #n
    NoS_list.newCurrent([[website.url],[""],links,[website.status_code]]) #1
    NoS_list.data.pop(0)#1
    NoS_list.print()#1 relativ printin cost alot of time
    checkedLinks = []
    all_Unchecked = getAllNotCheckedLinks(checkedLinks) #n-m
    checkedLinks += beginIter(all_Unchecked) #n*(n-m)
    checkedLinks = list(set(checkedLinks)) #1
    i = 0
    while(checkedLinks != getAllNotCheckedLinks(checkedLinks)): #n
        all_Unchecked = getAllNotCheckedLinks(checkedLinks) #n-m
        checkedLinks += beginIter(all_Unchecked) #n*(n-m)
        checkedLinks = list(set(checkedLinks)) #1
        i += 1
        if(i >= 5):
            break
    NoS_list.print()
    print("___________________________________________________")
    print("Beginn End Calculation")
    printWebsitesVisited()
    
    
def getAllNotCheckedLinks(Checked):
    links = []
    for x in tqdm(range(0,len(NoS_list))):
        links += NoS_list.data[x][2]
    
    links = list(set(links).difference(set(Checked)))
    return links

def beginIter(links):
    if(links == None or links ==[]):
        pass    
    for x in links: #n
        website = requests.get(url+x) #1
        websiteLinks = getAllLinks(website) #n-m
        NoS_list.newCurrent([[website.url],[""],links,[website.status_code]]) #1
    return links
def printWebsitesVisited():
    links = []
    for x in tqdm(range(0,len(NoS_list))):
        links += NoS_list.data[x][0]
    print(links)
def getAllLinks(html):
    soup = BeautifulSoup(html.text,'html.parser') 
    links = [""]
    for link in soup.find_all('a'):
        path = link.get('href')
        if path and path.startswith('/'): # Check if Link is internal
            links.append(path)
        else:
            continue
    
    return list(set(links))


if __name__ == '__main__':
    main()
