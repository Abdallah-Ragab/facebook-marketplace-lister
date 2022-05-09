

# Installation :

## 1. Add credentials :
 1. create **accounts.json** file at the main directory.
 2. add your facebook account's credentials as follows:

        "accounts" : [
			{ "id" : "...",
			"name" : "...",
			"email" : "...",
			"password" : "..."
			},
			...
		]

## 2.  Install a driver suitable for your browser :
 1. Follow The [official Instructions by selenium](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/) to download a suitable driver for your browser.
 2. Add the driver to the `drivers` folder.
 3. Make sure to add the driver's filename to the `__init__` function of the `Lister Class` like the following : `self.driver_file = 'chromedriver.exe'`  and set the driver's options.

>**NOTICE :**  I have set everything for the **chrome driver**  so if you are using chrome browser you will have to just download the driver and add it to the **drivers** folder,
## 3. Install Required Packages :
  navigate to the main directory and run `pip install -r requirements.txt` on your terminal.
 
# Usage:
you can check `examples.py` file for example usage.

## ****IMPORTANT**** | Product Object Structure :

 1. **title : string | Required | required by facebook.** 
 example:
	 `{'title' : 'Cool Product'}`
 2. **price : string | Required | required by facebook.**
  example:
 	 `{'price' : '25'}`
 3. **images : list | Required | required by facebook.** 
	 
	- at least one image required.
	 - images must be placed at the `images` directory.
 example:
	 `{'images' : [
	 {"file" : "cool_image.png"},
	 ... 
	 ]}`
  4. **location : string | Required | required by facebook.** 
		
		- when left empty, default values will be used.
		- you can change default values at the `elements.json` file.

			example:
			 `{'location' : 'Cairo, Egypt'}`
	 
  5. **category :  string | Optional | required by facebook.** 
		
		- when left empty, default values will be used.
		- you can change default values at the `elements.json` file.

			example:
	 `{'category' : 'Electronics & computers'}`
	 
  6. **condition :  string | Optional | required by facebook.** 
		
		- when left empty, default values will be used.
		- you can change default values at the `elements.json` file.

			example:
	 `{'category' : 'New'}`

  7. **sku :  string | Optional.** 
			example:
	 `{'sku' : '564646154'}`
	 
  8. **hide_from_friends :  boolean | Optional.** 
	  set to `True` to hide the listing from your facebook friends.
			example:
	 `{'hide_from_friends' : True}`

## Listing a single product :

 - create a new instance from `Lister Class` and run `login`  function passing the id of one of the accounts registered at `accounts.json`
 - `login` function will return `True` on a successful login.
 - run list function passing a `product` dictionary.
 

Example :

    from  Lister  import  Lister
    
	product = {
		'title': '...', 
		'price': '...', 
		'images': '[
			{'file' : '/image.jpg'},
		]',
	} 
    
    lister = Lister()
	my_account_id = 'ma'
	if  lister.login('ma') :
		lister.list(product)


## Listing multiple products :

 - create a new instance from `Lister Class` and run `login`  function passing the id of one of the accounts registered at `accounts.json`
 - `login` function will return `True` on a successful login.
 

Example :

    from  Lister  import  Lister
    import json
    
    my_json_file = open('products.json', 'r')
    products = json.load(my_json_file)['products']
    
    lister = Lister()
	my_account_id = 'ma'
	if  lister.login('ma') :
		for product in products : 
			result = lister.list(product)
			if result: print('Success!')