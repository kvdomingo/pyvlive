from .schemas import Channel
from .session import BASE_URL, DEFAULT_PARAMS, session


class Search:
    def __init__(self):
        self.session = session

    def channels(self, query: str, max_rows: int = 10):
        res = self.session.get(
            BASE_URL / "search" / "auto" / "channels",
            params={
                **DEFAULT_PARAMS,
                "query": query,
                "maxNumOfRows": max_rows,
            },
        )
        if not res.ok:
            raise ConnectionError(res.text)
        data = res.json()
        channels = [Channel(**d) for d in data]
        return channels


search = Search()
