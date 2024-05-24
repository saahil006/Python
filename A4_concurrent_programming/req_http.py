import asyncio

import requests

# A few handy JSON types
from typing import Dict, List

JSON = int or str or float or bool or None or Dict[str, "JSON"] or List["JSON"]
JSONObject = Dict[str, JSON]
JSONList = List[JSON]


def http_get_sync(url: str) -> JSONObject:
    response = requests.get(url)
    return response.json()


async def http_get(url: str) -> JSONObject:
    return await asyncio.to_thread(http_get_sync, url)
