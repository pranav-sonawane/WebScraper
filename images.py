from bs4 import BeautifulSoup
import requests
import PIL
from io import BytesIO

search = input("Search For:")
params = {"q": search}
r = requests.get("http://www.bing.com/images/search", params=params)

soup = BeautifulSoup(r.text,"html.parser")
links = soup.findAll("a",{"class": "thumb"})

for item in links:
    img_obj = requests.get(item.attrs["href"])
    title = item.attrs["href"].split("/")[-1]
    img = PIL.Image.open(BytesIO(img_obj.content))
    img.save("./scraped_images/" +title, img.format)