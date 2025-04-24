import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from product_list import cr_products

def init_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def scrape_search_query(query, max_pages=5):
    driver = init_driver()
    all_products = []

    print(f"\nScraping: {query}")

    for page in range(1, max_pages + 1):
        print(f"Page {page}")
        url = f"https://www.amazon.com/s?k={query.replace(' ', '+')}&page={page}"
        driver.get(url)
        time.sleep(3)

        soup = BeautifulSoup(driver.page_source, "lxml")
        page_products = 0

        for item in soup.select("div.s-main-slot > div[data-component-type='s-search-result']"):
            try:
                title = item.h2.text.strip()
                price = item.select_one(".a-price .a-offscreen")
                price = price.text.strip() if price else "N/A (price not mentioned)"
                reviews = item.select_one(".a-size-base.s-underline-text")
                reviews = reviews.text.strip() if reviews else "N/A (no review)"
                image_url = item.select_one("img.s-image")["src"]

                all_products.append(cr_products(title, price, reviews, image_url))
                page_products += 1
            except Exception as err:
                print(f"Product error: {err}")

        print(f"Page {page} products: {page_products}")
        print(f"Total so far: {len(all_products)}")

    driver.quit()
    return all_products