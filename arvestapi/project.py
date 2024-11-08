class Project:
    def __init__(self, **kwargs) -> None:
        """Represents an Arvest project."""
        
        self.id = kwargs.get("id", None)
        self.title = kwargs.get("title", None)
        self.owner_id = kwargs.get("owner_id", None)
        self.thumbnail_url = kwargs.get("thumbnail_url", None)
        self.description = kwargs.get("description", None)
        self.user_workspace = kwargs.get("user_workspace", None)
        self.metadata = kwargs.get("metadata", None)
        self.created_at = kwargs.get("created_at", None)

        if "response_body" in kwargs:
            self._parse_response_body(kwargs.get("response_body"))

    def _parse_response_body(self, response_body : dict) -> None:
        """Update the project properties with a request response."""

        self.id = response_body["project"]["id"]
        self.title = response_body["project"]["title"]
        self.description = response_body["project"]["description"]
        self.thumbnail_url = response_body["project"]["thumbnailUrl"]
        self.owner_id = response_body["project"]["ownerId"]
        self.user_workspace = response_body["project"]["userWorkspace"]
        self.metadata = response_body["project"]["metadata"]
        self.created_at = response_body["project"]["created_at"]