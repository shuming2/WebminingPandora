from django.http import HttpResponse
import json, requests

def collection(request):

    r = requests.get("http://www.pandora.net/en-ca/feeds/products/json/")
    r = r.json()
    gd = r["data"]["groups"]["group"] #groupdata

    col = gd[0]

    response = ""
    for item in col["item"]:
        response += item["@key"] + " " + item["@value"] + "<br>"
    return HttpResponse(response)