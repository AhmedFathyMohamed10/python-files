async def loops(iterable):
    async for i in iterable:
        print(i)

loops([1,2,3,4,5,6])