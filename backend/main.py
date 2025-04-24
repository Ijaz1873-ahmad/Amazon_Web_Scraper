from file_reader import load_search_queries
from amazon_scraper import scrape_search_query
from products_saver import save_products

def main():
    queries = load_search_queries("user_queries.json")
    if not queries:
        print("No queries found.")
        return

    for query in queries:
        products = scrape_search_query(query, max_pages=20)
        save_products(query, products)

if __name__ == "__main__":
    main()
