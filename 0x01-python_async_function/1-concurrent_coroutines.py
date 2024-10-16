#!/usr/bin/env python3i

""" Multiple coroutines at the same time with async """

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Async routine and returns the list of all generated routines
    """

    delays: List[float] = []
    orderList: List[float] = []

    for i in range(n):
        delays.append(wait_random(max_delay))

    for o in asyncio.as_completed(delays):
        orderList.append(await o)

    return orderList
