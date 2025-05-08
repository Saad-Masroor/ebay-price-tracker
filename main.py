import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from data_cleaning import load_data, clean_data, save_data
from database.insert_db import insert_data
def setup_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    service = Service("chromedriver.exe")
    return webdriver.Chrome(service=service, options=options)

def scrape_ebay(product_name):
    search_url = f"https://www.ebay.com/sch/i.html?_nkw={product_name.replace(' ', '+')}"
    driver = setup_driver()
    driver.get(search_url)
    time.sleep(5)  # Wait for page to load

    items = driver.find_elements(By.CSS_SELECTOR, ".s-item")
    scraped_data = []

    for item in items:
        try:
            title = item.find_element(By.CSS_SELECTOR, ".s-item__title").text
            price = item.find_element(By.CSS_SELECTOR, ".s-item__price").text
            link = item.find_element(By.CSS_SELECTOR, ".s-item__link").get_attribute("href")

            # Try extracting condition
            try:
                condition = item.find_element(By.CSS_SELECTOR, ".s-item__details.clearfix .SECONDARY_INFO").text
            except:
                condition = "N/A"

            # Try extracting shipping info
            try:
                shipping = item.find_element(By.CSS_SELECTOR, ".s-item__shipping, .s-item__freeXDays").text
            except:
                shipping = "N/A"

            # Try extracting seller info
            try:
                seller_info = item.find_element(By.CSS_SELECTOR, ".s-item__details.clearfix .s-item__seller-info-text").text
            except:
                seller_info = "N/A"

            scraped_data.append({
                "title": title,
                "price": price,
                "link": link,
                "condition": condition,
                "shipping": shipping,
                "seller_info": seller_info
            })

        except Exception as e:
            print(f"[!] Error scraping item: {e}")
            continue

    driver.quit()
    return scraped_data

def save_to_csv(data, filename="data/products.csv"):
    if not data:
        print("[!] No data to save.")
        return

    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "price", "link", "condition", "shipping", "seller_info"])
        writer.writeheader()
        writer.writerows(data)

    print(f"[+] Saved {len(data)} products to {filename}")

def main():
    product = input("Enter product to search on eBay: ")
    products = scrape_ebay(product)
    save_to_csv(products)

    # Load data
    df = load_data('data/products.csv')

    # Clean data
    df = clean_data(df)

    # Save cleaned data
    save_data(df, 'data/cleaned_ebay_data.csv')
    print("Data cleaned and saved successfully!")

    insert_data("data/cleaned_ebay_data.csv")
    print("Data inserted into PostgreSQL!")

if __name__ == "__main__":
    main()
