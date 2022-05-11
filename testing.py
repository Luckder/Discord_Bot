import requests
import pandas as pd

url = "https://zenquotes.io/api/random"

r = requests.get(url)
df = pd.json_normalize(r.json())

print(df)
print("\n")
print(df.at[0,'q'])