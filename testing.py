import requests

arg1 = input("anime name: ")

r = requests.get(f"https://api.myanimelist.net/v2/anime?q={arg1}&limit=10", headers={"X-MAL-CLIENT-ID":"21a5395ef35705314be29a385b38716b"})

for obj in r.json()['data']:
        try:
            title = obj['node']['title']
            print(title)

        except KeyError:
            continue  # Ignore and skip to next one.





        