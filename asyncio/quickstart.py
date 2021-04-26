import asyncio,time

async def main():
        printf(f'{time.ctime()} Hello!')
        await asyncio.sleep(1.0)
        printf(f'{time.ctime()} Goodbye!')

asyncio.run(main())