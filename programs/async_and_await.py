import asyncio
async def label(number):
    await asyncio.sleep(0)
    return f"case-{number}"

async def main():
    results = await asyncio.gather(label(1), label(2))
    print(results)

if __name__ == "__main__":
    asyncio.run(main())
