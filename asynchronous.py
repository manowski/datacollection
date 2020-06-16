import aiohttp
import asyncio

from utils import get_proxies


page_url = 'https://www.tiktok.com/'
headers = {
            'Referer': page_url,
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0'
        }


async def fetch(session, url):
    proxies = get_proxies()
    proxy_list = list(proxies)

    retry = 15
    while retry >= 0:
        print("Request #{}".format(retry))
        try:
            first_proxy = proxy_list[0]
            proxys = "http://{}".format(first_proxy)
            print(proxys)
            async with session.get(url, headers=headers, proxy=proxys) as response:
                if response.status == 200:
                    data = await response.json()
                    json = data
                return json
        except:
            # Most free proxies will often get connection errors.
            print("Skipping. Connnection error")
            proxy_list.pop(0)
            retry -= 1
            pass


async def fetch_all(urls, loop):
    semaphore = asyncio.Semaphore(200)
    async with semaphore:
        async with aiohttp.ClientSession(loop=loop) as session:
            results = await asyncio.gather(*[fetch(session, url) for url in urls], return_exceptions=True)
            return results
