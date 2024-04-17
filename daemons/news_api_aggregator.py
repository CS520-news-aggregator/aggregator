from daemons.base import BaseDaemon
from routers.observer import update_subscribers
from daemons.utils import add_data_to_db
from scrapers.news_api import call_everything
from datetime import datetime, timedelta
from scrapers.constants import LIST_TOPICS

PAGE_SIZE = 10


def get_dt_week() -> tuple[str, str]:
    today = datetime.now()
    last_week = today - timedelta(days=7)
    return last_week.strftime("%Y-%m-%d"), today.strftime("%Y-%m-%d")


class NewsAPIAggDaemon(BaseDaemon):
    def __init__(self, delay: int) -> None:
        self.page_number = 1
        super().__init__(self.task, delay)

    async def task(self) -> None:
        print("NewsAPI Aggregator Daemon task started with page", self.page_number)

        start_dt, end_dt = get_dt_week()
        list_posts = call_everything(
            keywords=LIST_TOPICS,
            fromDate=start_dt,
            to=end_dt,
            pageSize=PAGE_SIZE,
            page=self.page_number,
        )

        for post in list_posts:
            if (post_id := add_data_to_db(post)) != -1:
                update_subscribers(post_id)
            else:
                print("Error adding post to DB", str(post))

        self.page_number += 1
        print("NewsAPI Aggregator Daemon task finished")
