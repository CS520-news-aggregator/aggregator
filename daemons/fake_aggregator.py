from daemons.base import BaseDaemon
from models.data import Post
from routers.observer import update_subscribers
from daemons.utils import add_data_to_db


class FakeAggDaemon(BaseDaemon):
    def __init__(self, delay: int) -> None:
        super().__init__(self.task, delay)

    async def task(self) -> None:
        print("Fake Aggregator Daemon task started")

        # post = Post(
        #     title="fake title",
        #     link="fake link",
        #     media="fake media",
        #     author="fake author",
        #     date="fake date",
        # )

        # if (post_id := add_data_to_db(post)) != -1:
        #     update_subscribers(post_id)

        print("Fake Aggregator Daemon task finished")
