class Group:
    def __init__(self, **kwargs) -> None:
        """Represents an Arvest group."""
        
        self.id = kwargs.get("id", None)
        self.title = kwargs.get("title", None)
        self.owner_id = kwargs.get("owner_id", None)
        self.thumbnail_url = kwargs.get("thumbnail_url", None)
        self.description = kwargs.get("description", None)
        self.type = kwargs.get("type", None)

        if "response_body" in kwargs:
            self._parse_response_body(kwargs.get("response_body"))

    def _parse_response_body(self, response_body : dict) -> None:
        """Update the group properties with a request response."""

        self.id = response_body["id"]
        self.title = response_body["title"]
        self.owner_id = response_body["ownerId"]
        self.thumbnail_url = response_body["thumbnailUrl"]
        self.description = response_body["description"]
        self.type = response_body["type"]