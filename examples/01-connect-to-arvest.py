from arvestapi import Arvest
from utils import read_txt

# Create an instance of the Arvest class:
arv = Arvest(
    "jdchart", # This is your Arvest username
    read_txt("examples/password.txt") # This is your Arvest password
)

# Now you can use the get_user_info() method to see info like your username, number of documents, number of projects etc.
info = arv.get_my_info()
print(info)