import json

def parse_from_URL(in_url):
    # parse the id of the page from the URL given
    #from: https://www.notion.so/notionTest-ed9833176af54b33bd60c45166602798
    #to: ed9833176af54b33bd60c45166602798
    #to: ed983317-6af5-4b33-bd60-c45166602798 (8-4-4-4-12)
    
    URL = str(in_url)
    #find last - or /
    res = URL.rfind('-')
    if res == -1:
        res = URL.rfind('/')
    id = URL[res + 1: res + 33]
    formatedID=id[0:8]+"-"+id[8:12]+"-"+id[12:16]+"-"+id[16:20]+"-"+id[20:]
    
    return str(formatedID),str(id)

def auth(auth_name):
    """Gets Authorization key from file key.txt from the auth_name
    key.txt is a dictionary so it is in the keyword:value format where auth_name is the keyword."""
    data = ""
    if data == "":
        with open("key.txt") as file:
            data = file.read()
            keys = json.loads(data)
    key = keys[auth_name]
    return key
auth.__doc__ = "A simple function that says hello... Richie style"