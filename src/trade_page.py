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

    def limit_buy_price(self, unit_value, stop_loss_price_value, take_profit_price_value,
                        trace_input_price_value):
        time.sleep(2)
        # Click on buy button
        buy = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-button-order-buy']")))
        buy.click()

        # Select order type dropdown
        order_type = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-dropdown-order-type']")))
        order_type.click()

        # Select order type limit
        limit_order_type = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-dropdown-order-type-limit']")))
        limit_order_type.click()

        # Enter size
        size = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-input-volume']")))
        size.click()
        size.send_keys(unit_value)

        # Enter price
        trace_input_price = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-input-price']")))
        trace_input_price.click()
        trace_input_price.send_keys(trace_input_price_value)

        # Enter stop loss
        stop_loss = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-input-stoploss-price']")))
        stop_loss.click()
        stop_loss.send_keys(stop_loss_price_value)

        # Enter take profit
        take_profit = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-input-takeprofit-price']")))
        take_profit.click()
        take_profit.send_keys(take_profit_price_value)

        # Select expiry
        expiry_dropdown = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-dropdown-expiry']")))
        expiry_dropdown.click()

        good_till_cancelled = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "[data-testid='trade-dropdown-expiry-good-till-cancelled']")))
        good_till_cancelled.click()

        buy_order = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-button-order']")))
        buy_order.click()

        # Confirm order
        confirm_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-confirmation-button-confirm']")))
        confirm_button.click()

        notification_title = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='notification-title']")))
        print(notification_title.text)
        return notification_title.text

    def limit_sell_price(self, unit_value, stop_loss_price_value, take_profit_price_value,
                         trace_input_price_value):
        time.sleep(2)
        # Click on buy button
        buy = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-button-order-sell']")))
        buy.click()

        # Select order type dropdown
        order_type = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-dropdown-order-type']")))
        order_type.click()

        # Select order type limit
        limit_order_type = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-dropdown-order-type-limit']")))
        limit_order_type.click()

        # Enter size
        size = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-input-volume']")))
        size.click()
        size.send_keys(unit_value)

        # Enter price
        trace_input_price = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-input-price']")))
        trace_input_price.click()
        trace_input_price.send_keys(trace_input_price_value)

        # Enter stop loss
        stop_loss = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-input-stoploss-price']")))
        stop_loss.click()
        stop_loss.send_keys(stop_loss_price_value)

        # Enter take profit
        take_profit = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-input-takeprofit-price']")))
        take_profit.click()
        take_profit.send_keys(take_profit_price_value)

        # Select expiry
        expiry_dropdown = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-dropdown-expiry']")))
        expiry_dropdown.click()

        good_till_cancelled = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "[data-testid='trade-dropdown-expiry-good-till-cancelled']")))
        good_till_cancelled.click()

        buy_order = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-button-order']")))
        buy_order.click()

        # Confirm order
        confirm_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-confirmation-button-confirm']")))
        confirm_button.click()

        notification_title = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='notification-title']")))
        print(notification_title.text)
        return notification_title.text
    
    def stop_sell_price(self, unit_value, stop_loss_price_value, take_profit_price_value,
                        trace_input_price_value):
        time.sleep(2)
        # Click on buy button
        sell = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-button-order-sell']")))
        sell.click()

        # Select order type dropdown
        order_type = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-dropdown-order-type']")))
        order_type.click()

        # Select order type limit
        limit_order_type = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-dropdown-order-type-stop']")))
        limit_order_type.click()

        # Enter size
        size = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-input-volume']")))
        size.click()
        size.send_keys(unit_value)

        # Enter price
        trace_input_price = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-input-price']")))
        trace_input_price.click()
        trace_input_price.send_keys(trace_input_price_value)

        # Enter stop loss
        stop_loss = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-input-stoploss-price']")))
        stop_loss.click()
        stop_loss.send_keys(stop_loss_price_value)

        # Enter take profit
        take_profit = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-input-takeprofit-price']")))
        take_profit.click()
        take_profit.send_keys(take_profit_price_value)

        # Select expiry
        expiry_dropdown = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-dropdown-expiry']")))
        expiry_dropdown.click()

        good_till_cancelled = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "[data-testid='trade-dropdown-expiry-good-till-day']")))
        good_till_cancelled.click()

        buy_order = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-button-order']")))
        buy_order.click()

        # Confirm order
        confirm_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-confirmation-button-confirm']")))
        confirm_button.click()

        notification_title = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='notification-title']")))
        print(notification_title.text)
        return notification_title.text
    
    def stop_buy_price(self, unit_value, stop_loss_price_value, take_profit_price_value,
                       trace_input_price_value):
        time.sleep(2)
        # Click on buy button
        buy = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-button-order-buy']")))
        buy.click()

        # Select order type dropdown
        order_type = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-dropdown-order-type']")))
        order_type.click()

        # Select order type limit
        limit_order_type = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-dropdown-order-type-stop']")))
        limit_order_type.click()

        # Enter size
        size = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-input-volume']")))
        size.click()
        size.send_keys(unit_value)

        # Enter price
        trace_input_price = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-input-price']")))
        trace_input_price.click()
        trace_input_price.send_keys(trace_input_price_value)

        # Enter stop loss
        stop_loss = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-input-stoploss-price']")))
        stop_loss.click()
        stop_loss.send_keys(stop_loss_price_value)

        # Enter take profit
        take_profit = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-input-takeprofit-price']")))
        take_profit.click()
        take_profit.send_keys(take_profit_price_value)

        # Select expiry
        expiry_dropdown = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-dropdown-expiry']")))
        expiry_dropdown.click()

        good_till_cancelled = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "[data-testid='trade-dropdown-expiry-good-till-day']")))
        good_till_cancelled.click()

        buy_order = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-button-order']")))
        buy_order.click()

        # Confirm order
        confirm_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='trade-confirmation-button-confirm']")))
        confirm_button.click()

        notification_title = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='notification-title']")))
        print(notification_title.text)
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
    
    def validate_pending_order(self, unit_value, stop_loss_price_value, take_profit_price_value, order_type_value, expiry_value):
        # Click on pending order tab
        pending_order_tab = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='tab-asset-order-type-pending-orders']")))
        pending_order_tab.click()

        time.sleep(3)
        rows = self.driver.find_elements(
            By.CSS_SELECTOR,
            "table[data-testId='asset-pending-table'] tbody[data-testId='asset-pending-list'] tr"
        )

        for row in rows:
            profit = row.find_element(By.CSS_SELECTOR, "td[data-testId='asset-pending-column-take-profit']").text
            stop_loss = row.find_element(By.CSS_SELECTOR, "td[data-testId='asset-pending-column-stop-loss']").text
            unit = row.find_element(By.CSS_SELECTOR, "td[data-testId='asset-pending-column-units']").text
            order_type = row.find_element(By.CSS_SELECTOR,
                                          "td[data-testId='asset-pending-column-order-type'] span").text
            expiry = row.find_element(By.CSS_SELECTOR, "td[data-testId='asset-pending-column-expiry']").text

            if unit == unit_value and order_type == order_type_value and expiry == expiry_value and int(
                    float(profit.replace(',', ''))) == int(take_profit_price_value) and int(
                    float(stop_loss.replace(',', ''))) == int(stop_loss_price_value):
                return True

        return False

    def get_pending_order(self):
        # Click on pending order tab
        pending_order_tab = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='tab-asset-order-type-pending-orders']")))
        pending_order_tab.click()

        time.sleep(3)
        rows = self.driver.find_elements(
            By.CSS_SELECTOR,
            "table[data-testId='asset-pending-table'] tbody[data-testId='asset-pending-list'] tr"
        )

        for row in rows:
            profit = row.find_element(By.CSS_SELECTOR, "td[data-testId='asset-pending-column-take-profit']").text
            stop_loss = row.find_element(By.CSS_SELECTOR, "td[data-testId='asset-pending-column-stop-loss']").text
            unit = row.find_element(By.CSS_SELECTOR, "td[data-testId='asset-pending-column-units']").text
            order_type = row.find_element(By.CSS_SELECTOR,
                                          "td[data-testId='asset-pending-column-order-type'] span").text
            expiry = row.find_element(By.CSS_SELECTOR, "td[data-testId='asset-pending-column-expiry']").text

            return profit, stop_loss, unit, order_type

        return None

    def edit_pending_order(self, price_value, stop_loss_price_value, take_profit_price_value, is_change_expiry: bool):
        edit = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='asset-pending-button-edit']")))
        edit.click()

        price = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='edit-input-price']")))
        price.click()
        price.send_keys(Keys.CONTROL + "a")
        price.send_keys(Keys.BACKSPACE)
        price.send_keys(price_value)

        stop_loss_price = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='edit-input-stoploss-price']")))
        stop_loss_price.click()
        stop_loss_price.send_keys(Keys.CONTROL + "a")
        stop_loss_price.send_keys(Keys.BACKSPACE)
        stop_loss_price.send_keys(stop_loss_price_value)

        take_profit = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='edit-input-takeprofit-price']")))
        take_profit.click()
        take_profit.send_keys(Keys.CONTROL + "a")
        take_profit.send_keys(Keys.BACKSPACE)
        take_profit.send_keys(take_profit_price_value)

        if is_change_expiry:
            expiry_value = self.driver.find_element(
                By.CSS_SELECTOR, "[data-testid='edit-dropdown-expiry'] div div"
            )
            print(expiry_value.text)
            if expiry_value.text == "Good Till Cancelled":
                expiry = self.wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='edit-dropdown-expiry']")))
                expiry.click()

                expiry_gtc = self.wait.until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, "[data-testid='edit-dropdown-expiry-good-till-day']")))
                expiry_gtc.click()

            elif expiry_value.text == "Good Till Day":
                expiry = self.wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='edit-dropdown-expiry']")))

                expiry.click()

                expiry_gtd = self.wait.until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, "[data-testid='edit-dropdown-expiry-good-till-cancelled']")))
                expiry_gtd.click()

        update_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='edit-button-order']")))
        update_button.click()

        confirm_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='edit-confirmation-button-confirm']")))
        confirm_button.click()
        notification_title = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='notification-title']")))
        print(notification_title.text)
        return notification_title.text
    
    def close_pending_order(self):
        # Click on delete button
        delete_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='asset-pending-button-close']")))
        delete_button.click()

        # Confirm delete
        delete_button_confirm = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Delete Order")]')))
        delete_button_confirm.click()

        notification_title = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='notification-title']")))
        return notification_title.text

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
    
    def bulk_closed_open(self):
        bulk_closed_open = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='bulk-close']")))
        bulk_closed_open.click()

        closed_all_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='dropdown-bulk-close-all']")))
        closed_all_button.click()

        confirm_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='bulk-close-modal-button-submit-all']")))
        confirm_button.click()

        notification_title = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='notification-title']")))
        return notification_title.text

    def bulk_closed_delete(self):
        bulk_closed_open = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='bulk-delete']")))
        bulk_closed_open.click()

        confirm_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='bulk-delete-modal-button-submit']")))
        confirm_button.click()

        notification_title = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='notification-title']")))
        return notification_title.text
