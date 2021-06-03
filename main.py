import requests
from notion import auth, parse_from_URL, get_database, get_page

page_id = parse_from_URL('https://www.notion.so/testing-9de5b37859c8401196fdc1455cebd063')

data = get_page(page_id[1])
with open (page_id[1]+".json",'w') as file:
    file.write(data.text)

with open ('database.json','w') as file:
           file.write(get_database('40025654-dae0-40c1-baff-270735299090').text)