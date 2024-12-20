import arvestapi
from utils import read_txt

EMAIL = "raymonde.fras@gmail.com"
PASSWORD = read_txt("examples/password.txt")

ar = arvestapi.Arvest(EMAIL, PASSWORD)

# Get a list of all of your projets using the get_projects() method:
my_projects = ar.get_projects()

for project in my_projects:
    print(project.title)
    print(project.user_workspace)

# Create a new project using the create_project() method:
new_project = ar.create_project(title = "My cool new project")
print(new_project.title)