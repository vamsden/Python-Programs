import re
import urllib.request

# https://www.google.com/finance?q=
# base url stock finance url
url = 'https://www.google.com/finance?q='

stock_name = input("Enter your stock name: ")

# Attch stock name to the url
stock_url = url + stock_name

# Fetch stock page
stock_data = urllib.request.urlopen(stock_url).read()

# Decodes to UTF-8 string format
stock_data_decoded = stock_data.decode("utf-8")

# Search data from 
raw_string1 = re.search('meta itemprop="price"', stock_data_decoded)
start = raw_string1.start()
end = raw_string1.end() + 30

raw_string2 = stock_data_decoded[start: end]

# Final data Fetch
raw_string3 = re.search('content="', raw_string2)
start = raw_string3.end()

final_raw_string = raw_string2[start:]

final_data = re.search('/', final_raw_string)
end = final_data.end() - 3

print("The stock value of " + str(stock_name) + " is: " + final_raw_string[:end])
