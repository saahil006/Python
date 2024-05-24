import asyncio

import requests

# A few handy JSON types
JSON = int or str or float or bool or None or dict[str, "JSON"] or list["JSON"]
JSONObject = dict[str, JSON]
JSONList = list[JSON]


def http_get_sync(url: str) -> JSONObject:
    response = requests.get(url)
    return response.json()


async def http_get(url: str) -> JSONObject:
    return await asyncio.to_thread(http_get_sync, url)
