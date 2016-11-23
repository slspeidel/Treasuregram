from django.shortcuts import render
from pymongo import MongoClient
#from django.http import HttpResponse

# Create your views here.
def index(request):
    #name = 'Gold Nugget'
    #value = 1000.00
    #context = {'treasure_name': name, 'treasure_value': value}

    return render(request, 'index.html', {'treasures': treasures})

#Create a class to hold the treasure properties
class Treasure:
    def __init__ (self, name, value, material, location, img_url):
        self.name = name
        self.value = value
        self.material = material
        self.location = location
        self.img_url = img_url

client = MongoClient()
db = client.treasuregram
cols = db.treasures

treasures = []
for item in cols.find():
    treasures.append(Treasure(item['name'], item['value'], item['material'], item['location'], item['img_url']))
    

##treasures = [
##    Treasure("Gold Nugget", 1000.00, 'gold', "Curly's Creek, NM", 'example.com/nugget.jpg'),
##    Treasure("Fool's Gold", 0, "pyrite", "Fool's Falls, CO", 'example.com/fools-gold.jpg'),
##    Treasure("Coffee Can", 20.00, "tin", "Acme, CA", 'example.com/coffee-can.jpg')
##]
