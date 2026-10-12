import asyncio
import httpx
async def main():
    async with httpx.AsyncClient(base_url="http://127.0.0.1:8765", timeout=5) as client:
        response = await client.get("/health")
        assert response.status_code == 200
        assert response.json()["status"] == "ok"
        print("Async health check passed")

if __name__ == "__main__":
    asyncio.run(main())
