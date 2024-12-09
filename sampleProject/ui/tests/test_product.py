import pytest
from common.utilities.logger import Logger
from sampleProject.ui.pages.product_page import ProductPage


def test_products(login):
    """
    Verify No of products
    """
    driver = login
    product_page = ProductPage(driver,"product_page")
    no_of_products = product_page.find_products()
    Logger.info(f"{no_of_products}")
    assert no_of_products>0, "No Products found"

def test_product_titles(login):
    """
    Verify product titles contains "Sauce"
    """
    driver = login
    product_page = ProductPage(driver,"product_page")
    titles = product_page.find_products_title()
    Logger.info(f"{titles}")
    assert any("Sauce" in title for title in titles)

@pytest.mark.parametrize("option_list",["az","za"])
def test_product_titles(login,option_list):
    """
    Verify products are sorted {option_list}
    """
    driver = login
    product_page = ProductPage(driver,"product_page")
    product_page.sort_products(option_list)
    titles = product_page.find_products_title()
    sorted_bool = False
    if option_list=='az':
       sorted_bool = sorted(titles)
    else:
        sorted_bool = sorted(titles, reverse=True)
    Logger.info(f"{sorted_bool}")
    assert sorted_bool, "Titles are not sorted"