"""Base specific data provider."""

from mimesis.providers import BaseProvider


class BaseSpecProvider(BaseProvider):
    """Base provider for specific data providers."""

    def __init__(self, *args, **kwargs):
        """Initialize attributes of superclass."""
        super().__init__(*args, **kwargs)
