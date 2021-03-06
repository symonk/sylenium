from typing import Optional

from sylenium import Configuration
from sylenium import SyleniumDriver
from sylenium import SyleniumElement
from sylenium import driver_manager


def go(url: str) -> None:
    get_driver().get(url)


def find(locatable) -> SyleniumElement:
    return get_driver().find(locatable)


def terminate_drivers() -> None:
    driver_manager.terminate_all()


def get_driver(config: Optional[Configuration] = None) -> SyleniumDriver:
    """
    Responsible for yielding a thread local driver instance for the thread in question.
    In the event that no driver exists for the thread, a new driver will be configured and registered
    using the optional configuration provided.  default configuration will be used otherwise and the 'global'
    configuration can be configured by calling the configure(config) option of sylenium to modify all
    non explicitly configured browser instances.
    """
    return driver_manager.get_threaded_driver(config)
