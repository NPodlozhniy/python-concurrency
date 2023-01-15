import requests
import asyncio

URLS = [
    "facebook.com",
    "apple.com",
    "nvidia.com",
    "google.com",
    "microsoft.com",
    "amazon.com",
    "netflix.com",
]

# fetch all of these recources concurrently

async def async_get(domain:str):
    """
    STEP 1: Create a Worker
    """
    url = f"https://{domain}"
    print(f"fetching {domain}", flush=True)
    loop = asyncio.get_event_loop() # fetch a loop
    future = loop.run_in_executor(None, requests.get, url) # create a future
    response = await future # wait for the future to complete
    print(f"got a response code {response.status_code}", flush=True)

async def fetch(urls: list):
    """
    STEP 2: To run all workers and wait for them
    """
    tasks = []
    for i, url in enumerate(URLS): # create a list of workers
        print(f"i am running number {i}", flush=True)
        worker = async_get(url) # create a coroutine
        task = asyncio.create_task(worker) # (optional) create task from coroutine
        tasks.append(task) # append to list of tasks
    # wait for all
    return await asyncio.gather(*tasks)

# STEP 3: To provide a general loop

coroutines = fetch(URLS)
asyncio.run(coroutines)
