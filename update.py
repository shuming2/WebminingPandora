import requests
import json

r = requests.get("http://www.pandora.net/en-ca/feeds/products/json/")
r = r.json()

productdata = r["data"]["products"]["product"]
pdf = open("data/productdata.txt", "w")
pdf.write(json.dumps(productdata))
pdf.close()