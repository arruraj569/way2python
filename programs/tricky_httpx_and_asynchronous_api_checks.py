import asyncio
async def work(value):
    await asyncio.sleep(0)
    return value * 2
async def main():
    result = await asyncio.gather(work(3), work(1), work(2))
    print(result)
if __name__ == "__main__":
    asyncio.run(main())
