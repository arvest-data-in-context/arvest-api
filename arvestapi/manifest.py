class Manifest:
    def __init__(self, **kwargs) -> None:
        """Represents an Arvest project."""
        
        self.id = kwargs.get("id", None)
        self.url = kwargs.get("url", None)
        self.path = kwargs.get("path", None)
        self.thumbnail_url = kwargs.get("thumbnail_url", None)
        self.hash = kwargs.get("hash", None)
        self.title = kwargs.get("title", None)
        self.metadata = kwargs.get("metadata", None)
        self.origin = kwargs.get("origin", None)
        self.description = kwargs.get("description", None)
        self.id_creator = kwargs.get("id_creator", None)
        self.created_at = kwargs.get("created_at", None)
        self.updated_at = kwargs.get("origin", None)

        if "response_body" in kwargs:
            self._parse_response_body(kwargs.get("response_body"))

    def _parse_response_body(self, response_body : dict) -> None:
        """Update the project properties with a request response."""

        self.id = response_body["id"]
        self.url = response_body["url"]
        self.path = response_body["path"]
        self.thumbnail_url = response_body["thumbnailUrl"]
        self.hash = response_body["hash"]
        self.title = response_body["title"]
        self.metadata = response_body["metadata"]
        self.origin = response_body["origin"]
        self.description = response_body["description"]
        self.id_creator = response_body["idCreator"]
        self.created_at = response_body["created_at"]
        self.updated_at = response_body["updated_at"]