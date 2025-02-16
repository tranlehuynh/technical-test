import time
from enum import Enum

import pytest
from selenium import webdriver
from src.login_page import LoginPage
from src.trade_page import TradePage
from config.settings import USERNAME, PASSWORD


class SearchValues(Enum):
    SEARCH = "BTCUSD.std"


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://aqxtrader.aquariux.com/web/login")
    yield driver
    # input("Press Enter to close the browser...")
    driver.quit()


@pytest.fixture(scope="module")
def data():
    return SearchValues


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
def test_market_sell_price(trade_page, data, shared_data):
    time.sleep(3)
    # Get the current price
    current_price = trade_page.get_current_price()
    print(current_price)
    shared_data["current_price"] = current_price
    assert current_price is not None, "No current price found!"

    # Set the unit, stop loss, and take profit prices
    shared_data["unit"] = "0.01"
    shared_data["stop_loss_price"] = current_price * 2
    shared_data["take_profit_price"] = current_price * 0.5

    # Buy at market price
    time.sleep(2.5)
    noti_title = trade_page.market_sell_price(shared_data["unit"], shared_data["stop_loss_price"],
                                              shared_data["take_profit_price"])
    assert noti_title == "Market Order Submitted", "Market order failed or popup not showed!"

    # Validate the order
    is_validate = trade_page.validate_open(shared_data["unit"], shared_data["stop_loss_price"],
                                           shared_data["take_profit_price"], "SELL")
    assert is_validate == True, "Order validation failed!"

@pytest.mark.dependency(depends=["test_market_sell_price"])
def test_validate_notification_with_open_buy(trade_page, data, shared_data):
    profit, stop_loss_value, unit, order_type = trade_page.get_open_position()
    my_dict = trade_page.validate_order_notification()
    assert my_dict["Units"] == unit, "Unit validation failed!"
    assert my_dict["Stop Loss"] == stop_loss_value, "Stop loss price validation failed!"
    assert my_dict["Take Profit"] == profit, "Take profit price validation failed!"

@pytest.mark.dependency(depends=["test_validate_notification_with_open_buy"])
def test_market_edit_buy_price(trade_page, data, shared_data):
    shared_data["unit_edit"] = shared_data["unit"]
    shared_data["stop_loss_price_edit"] = shared_data["stop_loss_price"] * 1.1
    shared_data["take_profit_price_edit"] = shared_data["take_profit_price"] - shared_data["take_profit_price"] * 0.1

    # Edit the order
    time.sleep(2.5)
    noti_title = trade_page.edit_order_price(shared_data["stop_loss_price_edit"], shared_data["take_profit_price_edit"])
    assert noti_title == "Market Order Updated", "Market order failed or popup not showed!"

    # Validate the order
    is_validate = trade_page.validate_open(shared_data["unit_edit"], shared_data["stop_loss_price_edit"],
                                           shared_data["take_profit_price_edit"], "SELL")
    assert is_validate == True, "Order validation failed!"


@pytest.mark.dependency(depends=["test_market_edit_buy_price"])
def test_close_order(trade_page, data):
    time.sleep(2.5)
    notification_title = trade_page.close_order()
    assert notification_title == "Close Order", "Close order failed or popup not showed!"

@pytest.mark.dependency(depends=["test_close_order"])
def test_validate_order_history(trade_page, shared_data):
    is_validate = trade_page.validate_order_history(shared_data["unit_edit"], shared_data["stop_loss_price_edit"],
                                                    shared_data["take_profit_price_edit"], "SELL")
    assert is_validate == True, "Close order validation failed!"


@pytest.mark.dependency(depends=["test_validate_order_history"])
def test_validate_notification_with_order_history(trade_page, shared_data):
    profit, stop_loss_value, unit, order_type = trade_page.get_order_history()
    my_dict = trade_page.validate_order_notification()

    assert my_dict["Units"] == unit, "Unit validation failed!"
    assert my_dict["Stop Loss"] == stop_loss_value, "Stop loss price validation failed!"
    assert my_dict["Take Profit"] == profit, "Take profit price validation failed!"
