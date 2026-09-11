import pandas as pd

# Utility function to clean each DataFrame
def clean_df(df, date_cols=[], drop_na_cols=[], verbose_name=""):
    print(f"\n--- Cleaning {verbose_name} ---")
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    df.drop_duplicates(inplace=True)
    for col in date_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')
    drop_na_cols = [col for col in drop_na_cols if col in df.columns]
    if drop_na_cols:
        df.dropna(subset=drop_na_cols, inplace=True)
    print(df.info())
    return df

# 1. Begin Inventory
begin = pd.read_csv("begin_inventory.csv")
begin = clean_df(begin, date_cols=["startdate"], drop_na_cols=["onhand", "price"], verbose_name="Begin Inventory")
begin.to_csv("cleaned_begin_inventory.csv", index=False)

# 2. End Inventory
end = pd.read_csv("end_inventory.csv")
end = clean_df(end, date_cols=["enddate"], drop_na_cols=["onhand", "price"], verbose_name="End Inventory")
end.to_csv("cleaned_end_inventory.csv", index=False)

# 3. Purchase Prices
prices = pd.read_csv("purchase_prices.csv")
prices = clean_df(prices, drop_na_cols=["purchaseprice"], verbose_name="Purchase Prices")
prices.to_csv("cleaned_purchase_prices.csv", index=False)

# 4. Purchases
purchases = pd.read_csv("purchases.csv")
purchases = clean_df(purchases, date_cols=["invoicedate"], drop_na_cols=["quantity", "purchaseprice"], verbose_name="Purchases")
purchases.to_csv("cleaned_purchases.csv", index=False)

# 5. Sales
sales = pd.read_csv("sales.csv")
sales = clean_df(sales, date_cols=["salesdate"], drop_na_cols=["salesquantity", "salesprice", "salesdollars"], verbose_name="Sales")
sales.to_csv("cleaned_sales.csv", index=False)

# 6. Vendor Invoice
invoice = pd.read_csv("vendor_invoice.csv")
invoice = clean_df(invoice, date_cols=["invoicedate"], drop_na_cols=["vendornumber", "dollars"], verbose_name="Vendor Invoice")
invoice.to_csv("cleaned_vendor_invoice.csv", index=False)

print("\n✅ All datasets cleaned and saved!")
