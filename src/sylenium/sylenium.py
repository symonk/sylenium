from typing import Optional
from typing import Type

from sylenium import session_manager
from sylenium.pages.pageobjects import PageObject


def start(
    url: str, page_class: Optional[Type[PageObject]] = None
) -> Optional[PageObject]:
    driver = session_manager.fetch().get_driver()
    if page_class is None:
        driver.get(url)
    return PageObject()
