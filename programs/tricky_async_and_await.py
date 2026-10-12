import asyncio
async def work():
    print("started")
    return 7

async def main():
    pending = work()
    print("created")
    print(await pending)

if __name__ == "__main__":
    asyncio.run(main())
