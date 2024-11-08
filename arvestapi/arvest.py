import requests
from .profile import Profile
from .group import Group
from .project import Project

class Arvest:
    def __init__(self, email : str, password : str, **kwargs) -> None:
        """
        The Arvest class is your main point of entry. Use it to create an instance of your Arvest account.
        """
        
        self.email = email
        self.password = password
        self.access_token = kwargs.get("access_token", None)
        self._arvest_prefix = kwargs.get("arvest_prefix", "https://arvest-backend.tetras-libre.fr")
        self._auth_header = None

        if self.access_token == None:
            self.access_token = self._login()
            if self.access_token != None:
                self._auth_header = {"Authorization" : f"Bearer {self.access_token}"}

        self.profile = self._get_profile()
        self._personal_group = self._get_personal_group()

    def _login(self) -> None:
        """Connect to the Arvest account and get the user's access token."""

        url = f"{self._arvest_prefix}/auth/login"
        body = {"mail" : self.email, "password" : self.password}

        response = requests.post(url, json = body)
        
        if response.status_code == 200:
            return response.json()["access_token"]
        else:
            print("Unable to connect to Arvest and collect access token. Please check your login credentials.")
            return None

    def _get_profile(self) -> Profile:
        """Return the user profile info."""

        url = f"{self._arvest_prefix}/auth/profile"
        response = requests.get(url, headers = self._auth_header)

        if response.status_code == 200:
            return Profile(response_body = response.json())
        else:
            print("Unable to get user profile.")
            return None
        
    def _get_personal_group(self) -> Group:
        """Return the user's personal group."""
        
        if self.profile != None:
            url = f"{self._arvest_prefix}/link-user-group/user-personal-group/{str(self.profile.id)}"
            
            response = requests.get(url, headers = self._auth_header)
            
            if response.status_code == 200:
                return Group(response_body = response.json())
            else:
                print("Unable to get user personal group.")
                return None
        else:
            print("Unable to get personal user group because the user profile was not found.")
            return None
        
    def get_projects(self, **kwargs) -> list[Project]:
        """
        Return a list of the user's projects.
        
        ## kwargs
        - group_id (int) : the id of the group's projects (by default, the user's personal group)
        """

        if self._personal_group != None:
            url = f"{self._arvest_prefix}/link-group-project/{str(kwargs.get("group_id", self._personal_group.id))}"
            response = requests.get(url, headers = self._auth_header)
            if response.status_code == 200:
                ret = []
                for item in response.json():
                    ret.append(Project(response_body = item))
                return ret
            else:
                print("Unable to get projects.")
                return None
        else:
            print("Unable to get projects because unable to find personal user group.")
            return None
        
    def create_project(self, **kwargs) -> Project:
        """
        Create a new arvest project.
        
        ## kwargs
        - title (str) : project title
        - user_workspace (dict) : mirador workspace
        - metadata (dict) : ad hoc metadata
        - owner_id (int) : the group owner of the project (by default, the user's personal group)
        """

        if self._personal_group != None:
            url = f"{self._arvest_prefix}/link-group-project/project"
            
            body = {
                "title" : kwargs.get("title", ""),
                "userWorkspace" : kwargs.get("user_workspace", None),
                "ownerId" : kwargs.get("owner_id", self.profile.id),
                "metadata" : kwargs.get("metadata", {})
            }
            response = requests.post(url, json = body, headers = self._auth_header)
            
            if response.status_code == 201:
                return Project(response_body = response.json())
            else:
                print("Unable to create project.")
                return None