from typing import Optional


class User:
    """A model representing a system user with full type annotations."""

    def __init__(
        self, user_id: int, username: str, email: str, role: Optional[str] = "member"
    ) -> None:
        self.user_id: int = user_id
        self.username: str = username
        self.email: str = email
        self.role: Optional[str] = role

    def get_display_name(self) -> str:
        """Return formatted user display name."""
        return f"{self.username} ({self.role})"

    def is_admin(self) -> bool:
        """Check if user has admin privileges."""
        return self.role == "admin"
