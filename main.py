import requests
from notion import auth, parse_from_URL, get_database, get_page

page_id = parse_from_URL('https://www.notion.so/Jerem-c82f8aa02273478991123a1738a28ecc')

data = get_page(page_id[1])
with open (page_id[1]+".json",'w') as file:
    file.write(data.text)

with open ('database.json','w') as file:
           file.write(get_database('40025654-dae0-40c1-baff-270735299090').text)