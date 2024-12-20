import arvestapi
from utils import read_txt

EMAIL = "raymonde.fras@gmail.com"
PASSWORD = read_txt("examples/password.txt")

ar = arvestapi.Arvest(EMAIL, PASSWORD)

# Get your media using the get_media() method:
my_media = ar.get_media()

for item in my_media:
    print(item.title)


# media_url = "https://i.pinimg.com/originals/fd/3b/78/fd3b78ab6e60a8a9b3d45073c4b8fb95.jpg"
# media_url = "https://hatrabbits.com/wp-content/uploads/2017/01/random.jpg"