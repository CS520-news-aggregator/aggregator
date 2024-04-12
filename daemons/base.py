import asyncio


class BaseDaemon:
    """A daemon that executes a task every x seconds"""

    def __init__(self, task: callable, delay: int) -> None:
        self._task = task
        self._delay = delay

    async def _execute_task(self) -> None:
        await self._task()

    async def start_daemon(self) -> None:
        while True:
            delay: int = self._delay
            await asyncio.sleep(delay)
            await self._task()
