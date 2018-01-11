# Import the beautiful soup package
import bs4

# Import urlopen from urllib2 which helps us fetch the URL
from urllib2 import urlopen as uReq
from bs4 import BeautifulSoup as soup

# Store the target website URL into a variable
my_url = "https://www.newegg.ca/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card"

# Open the connection and grab the url page's content
uClient = uReq(my_url)

# Offload the content into a variable
page_html = uClient.read()

# Close the client
uClient.close()

# Indicate how to parse it, we could do XML, HTML etc
page_soup = soup(page_html, "html.parser") # Html parsing

#page_soup.h1
#page_soup.p
#page_soup.body.span

# Using the findAll function, find all div tags in the HTML code which
# have the 'class' attribute's text as "item-container".
# This will find all the individual product's HTML code
containers = page_soup.findAll("div",{"class":"item-container"})

# Check how many products are found, for example if it says 12 it means it 
# found that many graphics cards
#len(containers)

#contain = containers[0]
#container = container[0]
#container.div

#container.div.div.a.img["title"]

##
# title_container = container.findAll("a", {"class":"item-title"})
# This is because there is more than one 'a' tag in the html code
##

# Store file name into a variable
filename = "products.csv"
# Open file for writing
f = open(filename, "w")

# Store the CSV file table headers into a variable with a new line
headers = "brand, product_name, shipping\n"

# Write the headers into the CSV file
f.write(headers)

# loop through each individual product in the container
for container in containers:
    
    # Retrieve the product's brand name by selecting from the appropriate HTML tags
    brand = container.div.div.a.img["title"]
    
    # Retrieve the product's name by using findAll to find all 'a' tags that have the class attribute's text as "item-title"
    title_container = container.findAll("a", {"class":"item-title"})
    product_name = title_container[0].text # .text just gets the text description from the particular html tag
    
    # Retrieve the shipping cost by using findAll to find all 'li' tags that have the class attribute's text as "price-ship"
    shipping_container = container.findAll("li", {"class":"price-ship"})
    shipping = shipping_container[0].text.strip() # .text just gets the text description from the particular html tag
    
    print("brand: " + brand)
    print("product_name: " + product_name)
    print("shipping: " + shipping)
    
    # Write the collected product information into the CSV file
    f.write(brand + "," + product_name.replace(",","|") + "," + shipping + "\n")

# Close file
f.close()