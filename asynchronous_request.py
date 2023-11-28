'''
Asynchronous Request

    You may be wondering why Python's requests package is not compatible with asyncio. requests
is built on top of urllib3, which in turn uses Python's http and socket modules.
    By default socket operations are blocking. This means that Python won't like await 
requests.get(url) because .get() is not awaitable. In contrast almost everything in 
aiohttp is an awaitable coroutine such as session.request() and response.text(). It's
great package otherwise, but you are doing yourself a disservice by using requests in 
asynchronous code 




'''