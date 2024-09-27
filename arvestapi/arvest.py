from .user import User

class Arvest:
    def __init__(self, username : str, password : str) -> None:
        """
        The Arvest class is your main point of entry. Use it to create an instance of your Arvest account.
        """
        
        self.username = username
        self.password = password
        self.user = User(self.username)

    def get_my_info(self) -> dict:
        """Return info about your Arvest account."""
        return self.user.get_info()