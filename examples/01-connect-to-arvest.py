# Import the arvestapi package
import arvestapi

# Other imports:
from utils import read_txt

# Set you login credentials:
EMAIL = "raymonde.fras@gmail.com"
PASSWORD = read_txt("examples/password.txt")

# Create an instance of the Arvest class and provide your login credentials:
ar = arvestapi.Arvest(EMAIL, PASSWORD)

# Now you can get basic info like your user profile info:
print(ar.profile.name)