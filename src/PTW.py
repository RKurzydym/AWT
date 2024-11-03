import json

class Links:
    def __init__(self,data):
        self.data = data
        
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

class LinkTree:
    def __init__(self,data):
        self.data = data
        self.children = []
    def add_children(self,child):
        self.children.append(child)
    def print(self):
        print(self.data,end=" Children are: ")
        for elements in self.children:
            elements.print()
        print(end="|")
    

error_Link = Links([])
URL_link_tree = LinkTree(None)
def get_data(file):
    with open(file,"r") as file_data:
        data_as_dict = json.load(file_data)
        return data_as_dict

def prozess_data(data):
    #print(URL_link_tree.data)
    data = dict(data)
    test = list(data)
    #print(test)
    for x in test:
        if int(str(data[x]).removeprefix("<").removesuffix(">")) != 200:
            error_Link.append(x)
    #error_Link.print()
def find(root,data):
      if data == None:
          return None
      if root.data == data:
          return root
      for child in root.children:
          found = find(child,data)
          if found != None:
              return found
      return None
    
def prozess_URL_Parent_List(data):
    data_as_list = list(data)
    for key in data_as_list:
        if(data[key] == "None" and URL_link_tree.data == None):
              URL_link_tree.data = key
              continue
        location = find(URL_link_tree,data[key])
        if location != None:
            location.add_children(LinkTree(key))
    URL_link_tree.print()
    print("")
            
        
    

def main():
    data = get_data("./sample.json")
    prozess_URL_Parent_List(get_data("./URLParents.json"))
    prozess_data(data)
    #print("Test")
    

if __name__ == '__main__':
    main()
