import arvestapi
from utils import read_txt

EMAIL = "raymonde.fras@gmail.com"
PASSWORD = read_txt("examples/password.txt")

ar = arvestapi.Arvest(EMAIL, PASSWORD)

# Get your manifests using the get_manifests() method:
my_media = ar.get_manifests()

for item in my_media:
    print(item.title)