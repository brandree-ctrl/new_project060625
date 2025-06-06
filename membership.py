import requests

url = "https://webexapis.com/v1/memberships" 



#payload is the body
payload={

"roomId" : "Y2lzY29zcGFyazovL3VzL1JPT00vMWUzOWQzMzAtOWQ1MS0xMWViLTgzZmEtNjNlNjBjYTU4ZDYz",
"personEmail" : "brandon.reed81@gmail.com",
"isModerator" : "True"

}

headers = {
  'Authorization': 'Bearer NWNlMGVkMzUtMGE2Zi00MzIxLWI4MDEtNDg5OWQ2YzJjYzBhMDJlYTA1YTMtMzQw_PF84_ecd8c257-2e31-4403-8b40-9ab6ae874ac1',
  'Content-Type' : 'application/json'
}

response = requests.request("POST", url, headers=headers, json=payload)

print(response.json())
 