import requests as rq

all_classes = list()
page: int = 0
page_end: int = 10
udemy_url_endpoint: str = "https://www.udemy.com/api-2.0"
udemy_url_classes: str = f"courses/?page={page}"
headers: dict = {
  "Accept": "application/json, text/plain, */*",
  "Authorization": "Basic R0JNb2ZFMHVKUVgwM20yeWhrVFp5R3ZYOUhrOGxndHduYmxUQnE3NTptczZxVzZiNkgyWVNTNUY0MTlJbXVRMkF4aFVIS2c4VXpJMmZZMWdoaENnaGlHZFFkSzA3V211WXQ4Y21uUFVkVWptdlExREs3VlFZdk9FUzdRMjYyTEJ3WHAxQnBDYnJYUmlZMWFPdTdiOEw5TW1ia0FFRVAxbnR5SmtmV2NYMA==",
  "Content-Type": "application/json"
}

while page < 10:
    classes_response = rq.get(f"{udemy_url_endpoint}/{udemy_url_classes}", headers=headers)
    classes_list = classes_response.json()
    if 'results' in classes_list[0]:
        all_classes.append([x['results'] for x in classes_list])
    page += 1
    udemy_url_classes = f"courses/?page={page}"
    print(f"page: {page}")

print(f"len all_classes: {len(all_classes)}")
