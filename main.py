from bs4 import BeautifulSoup
import requests

url = "https://www.nytimes.com/"
response = requests.get(url)

print(response)

soup = BeautifulSoup(response.text, "html.parser")

title = (soup.find(name="h3", class_="ee0hn7b0"))
head = (soup.find_all(name="li", class_="summary-class"))

title_text = (title.getText())
print("\n**  " + title_text + "  **\n")
for n in head:
    text = n.getText()
    print(text)


user_input = str(input("\nWhat keyword would you like to search the New York Times by?\n").strip())
raw = (soup.find_all("p"))

for n in raw:
    text = n.getText()
    if user_input in text or user_input in text.lower():
        print(text)
    else:
        continue
    print("per the New York Times")