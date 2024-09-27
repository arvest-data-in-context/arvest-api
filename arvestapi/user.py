class User:
    def __init__(self, username : str) -> None:
        """
        A class to represent an Arvest user account.
        """
        self.username = username

    def get_info(self) -> dict:
        """Return a dictionary of info about the user."""
        return {}