# eBay Price Tracker

## Description

A web scraper that extracts product details (e.g., name, price, link) from eBay search results. This project allows users to track price changes, monitor product conditions, shipping costs, and seller ratings. It provides notifications when a product's price drops below a user-defined threshold. 

## Features

- Scrape product name, price, link, condition, shipping cost, and seller ratings from eBay search results.
- Store scraped data in a CSV file.
- Clean and process data using Pandas.
- Track price changes over time and compare past prices.
- Set up notifications to alert users when a product's price drops below a certain threshold.
- (Future) Optional: A Flask dashboard to display tracked prices.

## Requirements

- Python 3.x
- `selenium` for web scraping
- `pandas` for data processing
- `psycopg2` for PostgreSQL database integration
- `smtplib` or `python-telegram-bot` for notifications

## Setup

### 1. Clone the repository:

```bash
git clone https://github.com/yourusername/ebay-price-tracker.git
cd ebay-price-tracker