class Profile:
    def __init__(self, **kwargs) -> None:
        """Represents an Arvest user profile."""
        
        self.id = kwargs.get("id", None)
        self.mail = kwargs.get("mail", None)
        self.name = kwargs.get("name", None)

        if "response_body" in kwargs:
            self._parse_response_body(kwargs.get("response_body"))

    def _parse_response_body(self, response_body : dict) -> None:
        """Update the profile properties with a request response."""

        self.id = response_body["id"]
        self.mail = response_body["mail"]
        self.name = response_body["name"]
