from daemons.base import BaseDaemon
from routers.observer import update_subscribers
from daemons.utils import add_data_to_db
from scrapers.news_api import call_top_headline
from datetime import datetime, timedelta

PAGE_SIZE = 100


def get_dt_week() -> tuple[str, str]:
    today = datetime.now()
    last_week = today - timedelta(days=7)
    return last_week.strftime("%Y-%m-%d"), today.strftime("%Y-%m-%d")


class NewsAPIAggDaemon(BaseDaemon):
    def __init__(self, delay: int) -> None:
        self.page_number = 1
        super().__init__(self.task, delay)

    async def task(self) -> None:
        print("NewsAPI Aggregator Daemon task started with page=", self.page_number)

        list_posts = call_top_headline(
            pageSize=PAGE_SIZE,
            page=self.page_number,
        )

        list_post_ids = []

        if not list_posts:
            print("No posts to process. Encountered error with API")
        else:
            for post in list_posts:
                if (post_id := add_data_to_db(post)) != -1:
                    list_post_ids.append(post_id)
                else:
                    print("Error adding post to DB", str(post))
            update_subscribers(list_post_ids)
            self.page_number += 1

        print("NewsAPI Aggregator Daemon task finished")
