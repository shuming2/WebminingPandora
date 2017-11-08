import urllib

from django.http import HttpResponse

import requests
import os
import shutil
from datetime import datetime
import base64
import json

from .models import *

def test(request):
    properties = []
    return HttpResponse("<br>".join(properties))


def updateGroupData(request):
    backupDB()

    updateDic = {"Collection": Collection,
                 "Category": Category,
                 "SubCategory": SubCategory,
                 "Metal": Metal,
                 "Material": Material,
                 "Color": Color,
                 "Stone": Stone,
                 "Theme": Theme
                 }

    r = getDataFromOfficialWebsite()
    gd = r["data"]["groups"]["group"]

    for dic in gd:
        groupName = dic["@key"]
        if groupName in updateDic.keys():
            groupModel = updateDic[groupName]
            #groupModel.objects.all().delete() # Clear the old data
            for itemDic in dic["item"]:
                groupModel.objects.update_or_create(
                    key=itemDic["@key"],
                    default={"value": itemDic["@value"]}
                )

    response = "Group data has been updated successfully"
    return HttpResponse(response)

def updateProductData(request):
    backupDB()

    r = getDataFromOfficialWebsite()
    pd = r["data"]["products"]["product"]

    #Product.objects.all().delete()
    i=0
    for prod in pd:
        id = prod["@id"]
        downloadImage(id)

        processRaw(prod)
        i+=1
        if i==10:
            break

    response = str(Product.objects.count()) + " product data has been updated successfully"
    return HttpResponse(response)


# Help Function
def getDataFromOfficialWebsite():
    ###################TODO  delete following code
    if 1:
        data = open("../data/data.txt", "r").readline()
        return json.loads(data)
    ####################
    r = requests.get("http://www.pandora.net/en-ca/feeds/products/json/")
    return r.json()


def backupDB():
    ###################TODO  delete following code
    if 1:
        return
    ####################
    if not os.path.exists(os.getcwd() + "/backup"):
        os.makedirs(os.getcwd() + "/backup")

    currentPath = os.getcwd() + "/db.sqlite3"
    newPath = os.getcwd() + "/backup/" + str(datetime.now()) + ".sqlite3"
    shutil.copy(currentPath, newPath)


def downloadImage(id):
    if not os.path.exists(os.getcwd() + "/images"):
        os.makedirs(os.getcwd() + "/images")

    if os.path.exists(os.getcwd() + "/images/" + id + ".jpg"):
        return

    # Download images using requests
    # From Martijn Pieters
    # https://stackoverflow.com/questions/13137817/how-to-download-image-using-requests
    imgurlstart = "https://estore-ca.pandora.net/dw/image/v2/AAVX_PRD/on/demandware.static/-/Sites-pandora-master-catalog/default/dw781c0df0/images/productimages/"
    imgurlend = "-1.jpg?sw=450&sh=450&sm=fit"

    imgurl = imgurlstart + id + imgurlend
    imgpath = "images/" + id + ".jpg"

    r = requests.get(imgurl, stream=True)
    if r.status_code == 200:
        with open(imgpath, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)


def processRaw(prod):
    # Possible multiple values
    # subcol stone theme

    Product.objects.update_or_create(
        id=prod["@id"],
        defaults={'name': prod["@name"],
                  'baseid': prod["@baseid"],
                  'state': prod["@state"],
                  'url': prod["@url"],
                  'collection': Collection.objects.get(key=prod["@col"]).value,
                  'category': Category.objects.get(key=prod["@cat"]).value,
                  'subcollection': handleMultipleInputs(prod, "@subcol", Collection),
                  'subcategory': SubCategory.objects.get(key=prod["@subcat"]).value,
                  'metal': Metal.objects.get(key=prod["@metal"]).value,
                  'material': Material.objects.get(key=prod["@material"]).value,
                  'color': Color.objects.get(key=prod["@color"]).value,
                  'theme': handleMultipleInputs(prod, "@theme", Theme),
                  'stone': handleMultipleInputs(prod, "@stone", Stone),
                  'price': int(prod["@price"]),
                  'newest': True if prod["@newest"] == "true" else False,
                  'description': prod["desc"]["#cdata-section"],
                  'image': prod["@id"] + ".jpg"
                  },
    )


def handleMultipleInputs(prod, key, groupModel):
    result = []
    if prod[key]:
        for num in prod[key].split("|"):
            object = groupModel.objects.get(key=num)
            result.append(object.value)
    return ", ".join(result)
