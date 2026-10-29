from typing import Protocol

class CatalogProvider(Protocol):
    """Future external adapters return normalized catalog records; ranking stays local."""
    name: str
    async def search(self, query: str, limit: int = 20) -> list[dict]: ...

PROVIDER_STATUS = {"TMDB": "ertelendi", "Open Library": "ertelendi", "IGDB": "ertelendi"}
