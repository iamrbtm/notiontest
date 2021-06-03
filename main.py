import requests
from notion import auth, parse_from_URL

page_id = parse_from_URL('https://www.notion.so/notionTest-ed9833176af54b33bd60c45166602798')

headers = {
    'Authorization': f"Bearer " + auth('test'),
    'Notion-Version': '2021-05-13',
}
url = 'https://api.notion.com/v1/pages/'+page_id[1]
response = requests.post(url, headers=headers)

print (response.text)