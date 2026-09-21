import asyncio
class Countdown:
    def __init__(self, seconds):
        self.seconds = seconds

    def __await__(self):
        for i in reversed(range(1, self.seconds + 1)):
            print(f"⏲️ {i}...")
            yield from asyncio.sleep(3).__await__()
        return "🚀 Blast off!"

async def main():
    result = await Countdown(5)
    print("Result:", result)

asyncio.run(main())

#Future Example
async def example_future():
    future = asyncio.Future()
    print(f"Initial state: {future.done()}")

    await asyncio.sleep(2)

    future.set_result("Task Completed") 
    print(f"Final state: {future.done()}")
    print(f"Result: {future.result()}")
asyncio.run(example_future())