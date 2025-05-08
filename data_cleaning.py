import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def clean_price(price_range):
    """Convert price range to actual Price"""

    if isinstance(price_range, str):
        try:
            if 'to' in price_range:
                lower, upper = price_range.split(' to ')
                return (float(lower.replace('$', '').replace(',','').strip()) +
                        float(upper.replace('$', '').replace(',','').strip())) / 2
            
            else:
                return float(price_range.replace('$', '').replace(',','').strip())
        
        except Exception as e:
            return 0
    return 0

def clean_data(df):
    """Cleaning Ebay Data"""

    # Drop Rows with missing title
    df = df.dropna(subset=['title'])

    # Filling missing Price with 0
    df.loc[:, 'price'] = df['price'].fillna(0)

    # Cleaning Price
    df.loc[:, 'price'] = df['price'].apply(clean_price)

    # Cleaning condition (fill missing with 'Unknown')
    df.loc[:, 'condition'] = df['condition'].fillna('Unknown')

    # Cleaning shipping info (fill missing with 'Not Available')
    df.loc[:, 'shipping'] = df['shipping'].fillna('Not Available')

    # Cleaning seller info (fill missing with 'Unknown Seller')
    df.loc[:, 'seller_info'] = df['seller_info'].fillna('Unknown Seller')

    # Drop Duplicates based on links
    df = df.drop_duplicates(subset=['link'])

    return df

def save_data(df, output_file):
    """ Saving clean data to CSV """
    df.to_csv(output_file, index = False)

if __name__ == "__main__":
    df = load_data("ebay_data.csv")

    df = clean_data(df)

    save_data(df, 'cleaned_ebay_data.csv')
