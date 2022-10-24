import asyncio, os
import json
from random import Random
import time

class TestMultipleTask:
    def __init__(self):
        self.cache = {}
        self.rnd = Random()

    def pCache(self):
        print(json.dumps(self.cache, indent=4))



test = TestMultipleTask()

async def foo(testUnit, x):
    testUnit.cache[x] = { 'counter': 0, 'delays': [] }

    for i in range(3):
        delay = testUnit.rnd.randint(1, 1)
        testUnit.cache[x]['counter'] += 1
        testUnit.cache[x]['delays'] += [delay]
        testUnit.pCache()
        time.sleep(delay)

background_tasks = set()
for i in range(10):
    print(f'create task {i}')
    task = asyncio.create_task(foo(test, i))

    # Add task to the set. This creates a strong reference.
    background_tasks.add(task)

    # To prevent keeping references to finished tasks forever,
    # make each task remove its own reference from the set after
    # completion:
    task.add_done_callback(background_tasks.discard)