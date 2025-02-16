import time
from enum import Enum

import pytest
from selenium import webdriver
from src.login_page import LoginPage
from src.trade_page import TradePage
from config.settings import USERNAME, PASSWORD


class SearchValues(Enum):
    SEARCH = "BTCUSD.std"
    ORDER_TYPE = "BUY LIMIT"
    EXPIRY_GTC = "Good Till Cancelled"
    EXPIRY_GTD = "Good Till Day"
    URL = "https://aqxtrader.aquariux.com/web/login"


@pytest.fixture(scope="module")
def data():
    return SearchValues


@pytest.fixture(scope="module")
def driver(data):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(data.URL.value)
    yield driver
    # input("Press Enter to close the browser...")
    driver.quit()


@pytest.fixture(scope="module")
def shared_data():
    return {}


@pytest.fixture(scope="module")
def login_page(driver):
    login_page = LoginPage(driver)
    return login_page


@pytest.fixture(scope="module")
def trade_page(driver):
    trade_page = TradePage(driver)
    return trade_page


@pytest.mark.dependency()
def test_login(driver, login_page):
    login_page.login(USERNAME, PASSWORD)

    # Verify successful login
    assert "web" in driver.current_url, "Login failed!"


@pytest.mark.dependency(depends=["test_login"])
def test_search(trade_page, data):
    item = trade_page.search_and_select(data.SEARCH.value)

    assert item is not None, "No search results found!"


@pytest.mark.dependency(depends=["test_search"])
def test_limit_buy_price(trade_page, data, shared_data):
    time.sleep(3)
    # Get the current price
    current_price = trade_page.get_current_price()
    print(current_price)
    shared_data["current_price"] = current_price
    assert current_price is not None, "No current price found!"

    # Set the unit, stop loss, and take profit prices
    shared_data["unit"] = "0.01"
    shared_data["stop_loss_price"] = current_price * 0.5
    shared_data["take_profit_price"] = current_price * 2
    shared_data["trace_input_price_value"] = current_price * 0.7

    # Buy at market price
    time.sleep(2.5)
    noti_title = trade_page.limit_buy_price(shared_data["unit"], shared_data["stop_loss_price"],
                                            shared_data["take_profit_price"],
                                            shared_data["trace_input_price_value"])
    assert noti_title == "Limit Order Submitted", "Market order failed or popup not showed!"

    # Validate the order
    is_validate = trade_page.validate_pending_order(shared_data["unit"], shared_data["stop_loss_price"],
                                                    shared_data["take_profit_price"], data.ORDER_TYPE.value,
                                                    data.EXPIRY_GTC.value)
    assert is_validate == True, "Order validation failed!"

@pytest.mark.dependency(depends=["test_limit_buy_price"])
def test_build_delete(trade_page, data, shared_data):
    time.sleep(2.5)
    noti_title = trade_page.bulk_closed_delete()
    assert noti_title == "Bulk deletion of pending orders", "Close order validation failed!"
