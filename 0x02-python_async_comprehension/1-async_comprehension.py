#!/usr/bin/env python3
''' async comprehension'''

from typing import List
from importlib import import_module as using


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    ''' async comprehension '''
    return [i async for i in async_generator()]
