#!/usr/bin/env python3
"""random number wait """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ random wait"""
    delay = random.random() *  max_delay
    await asyncio.sleep(delay)
    return delay
