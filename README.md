# 🛒 eBay Price Tracker

A Python-based price tracker that scrapes product listings from eBay and helps users monitor product prices, conditions, shipping costs, and seller ratings. Supports PostgreSQL integration and CSV exports. Ideal for anyone wanting to keep tabs on deals or drops in prices.

---

## 🚀 Features

- ✅ Scrape product details from eBay:
  - Title
  - Price
  - Link
  - Condition
  - Shipping Cost
  - Seller Rating
- ✅ Save scraped data to `products.csv`
- ✅ Clean and preprocess data using `pandas`
- ✅ Store data in a **PostgreSQL** database
- ✅ Full end-to-end flow from scraping → cleaning → inserting into DB
- ✅ CLI-based input for product search
- ✅ Future-ready database model (`models.py`) and query templates

---

## 📦 Requirements

- Python 3.x
- [`selenium`](https://pypi.org/project/selenium/)
- [`pandas`](https://pypi.org/project/pandas/)
- [`psycopg2`](https://pypi.org/project/psycopg2/)
- [`python-dotenv`](https://pypi.org/project/python-dotenv/)

---

## 🛠️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/Saad-Masroor/ebay-price-tracker.git
cd ebay-price-tracker
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Set up environment variables
Create a .env file in the root directory with your PostgreSQL credentials:

```bash
DB_NAME=ebay_db
DB_USER=ebay_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

## 🧪 Usage
```bash
python main.py
```

You'll be prompted to enter a product name (e.g., Laptop). The scraper will then:

Open eBay in a headless browser

Scrape product listings

Save raw data to data/products.csv

Clean data and save to data/cleaned_ebay_data.csv

Insert cleaned data into your PostgreSQL database

## 🧭 Roadmap
 PostgreSQL DB integration

 Price history tracking over time

 Telegram/email alerts for price drops

 Flask dashboard to visualize trends

 Scheduler for daily/weekly product checks

 Export price insights as charts or reports

## 🧑‍💻 Author
Saad Bin Masroor
Python Developer | Automation Enthusiast
🔗 LinkedIn - https://www.linkedin.com/in/saad-masroor-481015227/
📧 saad.masroor8@gmail.com

## 📝 License
This project is licensed under the MIT License. See the LICENSE file for details.
