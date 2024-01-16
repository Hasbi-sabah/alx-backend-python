#!/usr/bin/env python3
""" module for the function async_generator """
import asyncio
from random import uniform
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine called async_generator that takes no arguments.
    The coroutine will loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
