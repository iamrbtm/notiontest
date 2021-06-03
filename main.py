import requests
from notion import auth, parse_from_URL

page_id = parse_from_URL('https://www.notion.so/notionTest-ed9833176af54b33bd60c45166602798')

headers = {
    'Authorization': f"Bearer " + auth('test'),
    'Notion-Version': '2021-05-13',
}
response = requests.get(f'https://api.notion.com/v1/pages/{page_id[1]}', headers=headers)

with open (page_id[1]+".json",'w') as file:
    file.write(response.text)

print (response.text)