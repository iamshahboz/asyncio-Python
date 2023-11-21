import asyncio


# this line below will handle the whole event loop
# asyncio.run(main())  # Python 3.7+

# # There is more long-winded way of managing the asyncio event loop, with get_event_loop()

# loop = asyncio.get_event_loop()
# try:
#     loop.run_until_complete(main())
# finally:
#     loop.close()


async def main():
    print("Hello...")
    await asyncio.sleep(1)
    print('world')

routine = main()
# print(routine)


asyncio.run(routine)




