from price_page import OnlinerHelper


def test_price(browser):
    """
    Checks correspondence of prices for goods in the frame and on the product page
    """
    link = 'https://www.onliner.by/'
    page = OnlinerHelper(browser, link)
    page.go_to_site()
    page.enter_сatalog()
    page.find_in_catalog('iphone')
    frame = page.find_frame()
    page.switch(frame)
    frame_price = page.find_price().text
    page.show_details()
    page.default()
    page_price = page.find_price_in_page()
    assert page_price == frame_price
