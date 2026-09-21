import threading
import asyncio
import time
from rich import print

def make_coffee_sync():
    print(f"\tMaking coffee..., Thread name = {threading.current_thread().name}")
    time.sleep(2)
    print(f"\tcoffee is ready!")

def make_pastry_sync():
    print(f"\tMaking Pastry...., Thread Name = {threading.current_thread().name}")
    time.sleep(3)
    print(f"\tPastry is ready!")

def order_sync():
    make_coffee_sync()
    make_pastry_sync()

async def make_coffee_async():
    print(f"\tMaking coffee..., Thread Name = {threading.current_thread().name}")
    await asyncio.sleep(2)
    print(f"\tCoffee is ready!")

async def make_pastry_async():
    print(f"\tMaking pastry..., Thread Name = {threading.current_thread().name}")
    await asyncio.sleep(3)
    print(f"\tPastry is reaady!")

async def order_async():
    tasks = [
        asyncio.create_task(make_coffee_async()),
        asyncio.create_task(make_pastry_async())
    ]
    await asyncio.gather(*tasks)


print(f"[red]Synchronous Approach[/red]")
start_time = time.time()

print(f"[blue] Main thread entring order_sync[/blue]")
order_sync()
print(f"[yellow] Main thread exiting order_sync[/yellow]")

print(f"[purple] Total time = {time.time()-start_time}")

print(f"[red]Asynchronous Approach[/red]")
start_time = time.time()

print(f"[blue] Main thread entring order_async[/blue]")
asyncio.run(order_async())
print(f"[blue] Main thread exiting order_async[/blue]")

print(f"[purple] Total time = {time.time()-start_time}")