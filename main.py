from bs4 import BeautifulSoup
import requests

url = "https://www.nytimes.com/"
response = requests.get(url)

print(response)

soup = BeautifulSoup(response.text, "html.parser")

# raw = (soup.find_all(class_="css-5n6ag4"))
# for n in raw:
#     print(n)
# #

user_input = str(input("What keyword would you like to search the New York Times by?\n").strip())
raw = (soup.find_all("p"))

for n in raw:
    text = n.getText()
    if user_input in text or user_input in text.lower():
        print(text)
    else:
        continue
    print("NYT")