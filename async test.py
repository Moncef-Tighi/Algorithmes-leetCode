import asyncio


async def test():
    task = asyncio.create_task(test2())
    await asyncio.sleep(2)
    # Tu attends jusqu'à ce que la task au dessus soit finie.
    print("A")


async def test2():
    print("B")
    await asyncio.sleep(1)

asyncio.run(test())
print("C")
print("D")
