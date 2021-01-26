import aiohttp
import aiofiles
import asyncio
import time
import os


#定義協程(coroutine)
async def main(links):

    async with aiohttp.ClientSession() as session:
        tasks = [
            asyncio.create_task(fetch(data['url'], data['episodeId'], session)) for data in links
        ]  # 建立任務清單
        await asyncio.gather(*tasks)  # 打包任務清單及執行


#定義協程(coroutine)
async def fetch(link, id, session):
    async with session.get(link) as response:  #非同步發送請求
        if response.status == 200:
            f = await aiofiles.open('/tmp/file.mp3', mode='wb')
            await f.write(await resp.read())
            await f.close()
        try:
            # s3 upload
            print("{} upload success")
        except Exception as e:
            print("{} upload error")

        os.remove('tmp/file.mp3')



start_time = time.time()  #開始執行時間
loop = asyncio.get_event_loop()  #建立事件迴圈(Event Loop)

#  episodes = ...

loop.run_until_complete(main(episodes))  #執行協程(coroutine)
print("花費:" + str(time.time() - start_time) + "秒")