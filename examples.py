
"""
test_product = {
    'title': String, # Required
    'price': String, # Required
    'images' : [
        {"file": "xxx.jpg"}و
        {"file": "xxx.jpg"}و
        ...
        ...
    ]و # Required
    'location': String, # Optional : Required by facebook. If left empty the default value will be used. Default value can be changed at elements.json file.
    'category': String,  # Optional : Required by facebook. If left empty the default value will be used. Default value can be changed at elements.json file.
    'condition': String,  # Optional : Required by facebook. If left empty the default value will be used. Default value can be changed at elements.json file.
    'hide_from_friends' : Boolean, # Optional : Optional for facebook. Default value is False.
    'sku': String, # Optional : Optional for facebook. Default value is None.
}
"""

from  Lister  import  Lister
import json

my_account_id = '...'

product = {
	'title': '...', 
	'price': '...', 
	'images': [
		{'file' : '/image.jpg'},
	],
}

def publish_single_product():
    lister = Lister()
    if lister.login(my_account_id) :
        lister.list(product)
        
def publish_multi_products():
    my_json_file = open('products.json', 'r')
    products = json.load(my_json_file)['products']

    lister = Lister()
    if  lister.login(my_account_id) :
        for product in products : 
            result = lister.list(product)
            if result: print('Success!')