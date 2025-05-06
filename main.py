import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from data_cleaning import load_data, clean_data, save_data

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
    time.sleep(5)  # Increased time for page to load completely

    items = driver.find_elements(By.CSS_SELECTOR, ".s-item")
    scraped_data = []

    for item in items:
        try:
            title = item.find_element(By.CSS_SELECTOR, ".s-item__title").text
            price = item.find_element(By.CSS_SELECTOR, ".s-item__price").text
            link = item.find_element(By.CSS_SELECTOR, ".s-item__link").get_attribute("href")
            scraped_data.append({"title": title, "price": price, "link": link})
        except Exception as e:
            print(f"[!] Error scraping item: {e}")  # You can log the error if needed
            continue  # Skip items that don't have required info

    driver.quit()
    return scraped_data

def save_to_csv(data, filename="data/products.csv"):
    if not data:
        print("[!] No data to save.")
        return

    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "price", "link"])
        writer.writeheader()
        writer.writerows(data)

    print(f"[+] Saved {len(data)} products to {filename}")

def main():
    product = input("Enter product to search on eBay: ")
    products = scrape_ebay(product)
    save_to_csv(products)

    # Load the data from the CSV file (Ensure this matches the filename you're saving)
    df = load_data('data/products.csv')
    
    # Clean the data
    df = clean_data(df)
    
    # Save the cleaned data to a new file
    save_data(df, 'data/cleaned_ebay_data.csv')
    print("Data cleaned and saved successfully!")

if __name__ == "__main__":
    main()
