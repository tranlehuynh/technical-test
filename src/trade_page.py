import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TradePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def search_and_select(self, value):
        search_box = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='symbol-input-search']")))
        search_box.send_keys(value)

        time.sleep(5)  # Wait for the list of items to appear

        # if symbol_inputs_after_search
        items = self.wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[data-testid='symbol-input-search-items']")))
        print(len(items))

        for item in items:
            print(item.text)
            if value in item.text:
                item.click()
                print(f"Clicked on item: {item.text}")
                symbol_overview = self.wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='symbol-overview-id']")))
                return symbol_overview

        return None

    def get_current_price(self):
        trace_price = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="trade-live-buy-price"]')

        print(trace_price.text)

        if int(float(trace_price.text.replace(",", ""))):
            print(int(float(trace_price.text.replace(",", ""))))
            return int(float(trace_price.text.replace(",", "")))

        return None

    def market_buy_price(self, unit_value, stop_loss_price_value, take_profit_price_value):
        time.sleep(2)
        # Buy order
        buy = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-button-order-buy']")))
        buy.click()

        order_type = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-dropdown-order-type']")))
        order_type.click()

        market = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-dropdown-order-type-market']")))
        market.click()

        unit = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-input-volume']")))
        unit.send_keys(unit_value)

        stop_loss_price = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-input-stoploss-price']")))
        stop_loss_price.send_keys(stop_loss_price_value)

        take_profit = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-input-takeprofit-price']")))
        take_profit.send_keys(take_profit_price_value)

        buy_order = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-button-order']")))
        buy_order.click()

        # Confirm order
        confirm_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-confirmation-button-confirm']")))
        confirm_button.click()

        notification_title = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='notification-title']")))
        return notification_title.text
    
    def market_sell_price(self, unit_value, stop_loss_price_value, take_profit_price_value):
        time.sleep(2)
        # Buy order
        sell = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-button-order-sell']")))
        sell.click()

        order_type = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-dropdown-order-type']")))
        order_type.click()

        market = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-dropdown-order-type-market']")))
        market.click()

        unit = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-input-volume']")))
        unit.send_keys(unit_value)

        stop_loss_price = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-input-stoploss-price']")))
        stop_loss_price.send_keys(stop_loss_price_value)

        take_profit = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-input-takeprofit-price']")))
        take_profit.send_keys(take_profit_price_value)

        buy_order = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-button-order']")))
        buy_order.click()

        # Confirm order
        confirm_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-confirmation-button-confirm']")))
        confirm_button.click()

        notification_title = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='notification-title']")))
        return notification_title.text
    
    def validate_order_history(self, unit_value, stop_loss_price_value, take_profit_price_value, order_type_value):
        order_history = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='tab-asset-order-type-history']")))
        order_history.click()

        time.sleep(3)

        rows = self.driver.find_elements(
            By.CSS_SELECTOR,
            "table[data-testId='asset-history-position-table'] tbody[data-testId='asset-history-position-list'] tr"
        )

        for row in rows:
            profit = row.find_element(By.CSS_SELECTOR, "td[data-testId='asset-history-column-take-profit']").text
            stop_loss = row.find_element(By.CSS_SELECTOR, "td[data-testId='asset-history-column-stop-loss']").text
            unit = row.find_element(By.CSS_SELECTOR, "td[data-testId='asset-history-column-units']").text
            order_type = row.find_element(By.CSS_SELECTOR,
                                          "td[data-testId='asset-history-column-order-type'] span").text

            if unit == unit_value and order_type == order_type_value and int(float(profit.replace(",", ""))) == int(
                    take_profit_price_value) and int(float(stop_loss.replace(",", ""))) == int(stop_loss_price_value):
                return True

        return False

    def get_order_history(self):
        order_history = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='tab-asset-order-type-history']")))
        order_history.click()

        time.sleep(3)

        rows = self.driver.find_elements(
            By.CSS_SELECTOR,
            "table[data-testId='asset-history-position-table'] tbody[data-testId='asset-history-position-list'] tr"
        )

        for row in rows:
            profit = row.find_element(By.CSS_SELECTOR, "td[data-testId='asset-history-column-take-profit']").text
            stop_loss = row.find_element(By.CSS_SELECTOR, "td[data-testId='asset-history-column-stop-loss']").text
            unit = row.find_element(By.CSS_SELECTOR, "td[data-testId='asset-history-column-units']").text
            order_type = row.find_element(By.CSS_SELECTOR,
                                          "td[data-testId='asset-history-column-order-type'] span").text

            return profit, stop_loss, unit, order_type

        return False

    def edit_order_price(self, stop_loss_price_value, take_profit_price_value):
        edit = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='asset-open-button-edit']")))
        edit.click()

        stop_loss_price = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='edit-input-stoploss-price']")))
        stop_loss_price.click()
        stop_loss_price.send_keys(Keys.CONTROL + "a")  # Select all text
        stop_loss_price.send_keys(Keys.BACKSPACE)  # Delete existing text
        stop_loss_price.send_keys(stop_loss_price_value)  # Enter new value
        time.sleep(3)

        take_profit = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='edit-input-takeprofit-price']")))
        take_profit.click()
        take_profit.send_keys(Keys.CONTROL + "a")  # Select all text
        take_profit.send_keys(Keys.BACKSPACE)  # Delete existing text
        take_profit.send_keys(take_profit_price_value)  # Enter new value
        time.sleep(3)

        update_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='edit-button-order']")))
        update_button.click()

        confirm_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='edit-confirmation-button-confirm']")))
        confirm_button.click()
        notification_title = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='notification-title']")))
        return notification_title.text

    def validate_open(self, unit_value, stop_loss_price_value, take_profit_price_value, order_type):
        open_position = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='tab-asset-order-type-open-positions']")))
        open_position.click()

        time.sleep(3)
        rows = self.driver.find_elements(
            By.CSS_SELECTOR,
            "table[data-testId='asset-open-table'] tbody[data-testId='asset-open-list'] tr"
        )

        for row in rows:
            profit = row.find_element(By.CSS_SELECTOR, "td[data-testId='asset-open-column-take-profit']").text
            stop_loss = row.find_element(By.CSS_SELECTOR, "td[data-testId='asset-open-column-stop-loss']").text
            unit = row.find_element(By.CSS_SELECTOR, "td[data-testId='asset-open-column-units']").text
            order_type = row.find_element(By.CSS_SELECTOR, "td[data-testId='asset-open-column-order-type'] span").text

            if unit == unit_value and order_type == order_type and int(float(profit.replace(",", ""))) == int(
                    take_profit_price_value) and int(float(stop_loss.replace(",", ""))) == int(stop_loss_price_value):
                return True

        return False

    def get_open_position(self):
        open_position = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='tab-asset-order-type-open-positions']")))
        open_position.click()

        time.sleep(3)
        rows = self.driver.find_elements(
            By.CSS_SELECTOR,
            "table[data-testId='asset-open-table'] tbody[data-testId='asset-open-list'] tr"
        )

        for row in rows:
            profit = row.find_element(By.CSS_SELECTOR, "td[data-testId='asset-open-column-take-profit']").text
            stop_loss = row.find_element(By.CSS_SELECTOR, "td[data-testId='asset-open-column-stop-loss']").text
            unit = row.find_element(By.CSS_SELECTOR, "td[data-testId='asset-open-column-units']").text
            order_type = row.find_element(By.CSS_SELECTOR, "td[data-testId='asset-open-column-order-type'] span").text

            return profit, stop_loss, unit, order_type

        return None

    def validate_order_notification(self):
        time.sleep(5)
        notification_title = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='notification-selector']")))
        notification_title.click()

        orders = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='tab-notification-type-order']")))
        orders.click()

        results = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "[data-testid='notification-list-result'] > div:first-child")))
        results.click()

        # Get orders details label
        orders_details_label = self.wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[data-testid='notification-order-details-label']")))

        orders_details_value = self.wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[data-testid='notification-order-details-value']")))

        labels = []
        values = []
        for i in orders_details_label:
            labels.append(i.text)
        for i in orders_details_value:
            values.append(i.text)

        my_dict = dict(zip(labels, values))
        close_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='notification-order-details-modal-close']")))
        close_button.click()

        return my_dict

    def close_order(self):
        open_position = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='tab-asset-order-type-open-positions']")))
        open_position.click()

        time.sleep(3)

        closed_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='asset-open-button-close']")))
        closed_button.click()

        close_button_submit = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='close-order-button-submit']")))
        close_button_submit.click()
        notification_title = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='notification-title']")))
        return notification_title.text
