import time
import asyncio


async def coro(seq) -> list:
    """'IO' wait time is proportional to the max element."""
    await asyncio.sleep(max(seq))
    return list(reversed(seq))


async def main():
    t = asyncio.create_task(coro([3, 2, 1]))
    t2 = asyncio.create_task(coro([10, 5, 0]))  # Python 3.7+
    print('Start:', time.strftime('%X'))
    a = await asyncio.gather(t, t2)
    print('End:', time.strftime('%X'))  # Should be 10 seconds
    print(f'Both tasks done: {all((t.done(), t2.done()))}')
    return a

t = asyncio.run(main())

"""There’s a subtlety to this pattern: if you don’t await t within main(),
 it may finish before main() itself signals that it is complete.
  Because asyncio.run(main()) calls loop.run_until_complete(main()),
   the event loop is only concerned (without await t present) that main() is done,
    not that the tasks that get created within main() are done. Without await t, 
    the loop’s other tasks will be cancelled, possibly before they are completed.
     If you need to get a list of currently pending tasks, you can use asyncio.Task.all_tasks().

"""