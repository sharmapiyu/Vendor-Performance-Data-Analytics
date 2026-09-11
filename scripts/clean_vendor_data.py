import pandas as pd

# Load all datasets
begin_inventory = pd.read_csv('begin_inventory.csv')
end_inventory = pd.read_csv('end_inventory.csv')
purchase_prices = pd.read_csv('purchase_prices.csv')
purchases = pd.read_csv('purchases.csv')
sales = pd.read_csv('sales.csv')
vendor_invoice = pd.read_csv('vendor_invoice.csv')

# Preview shapes and basic info
print("Begin Inventory:", begin_inventory.shape)
print("End Inventory:", end_inventory.shape)
print("Purchase Prices:", purchase_prices.shape)
print("Purchases:", purchases.shape)
print("Sales:", sales.shape)
print("Vendor Invoice:", vendor_invoice.shape)

# Optional: See first 5 rows
print(begin_inventory.head())
