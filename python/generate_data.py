import pandas as pd
import random
from datetime import datetime, timedelta

# -----------------------------
# 1. BASIC SETTINGS
# -----------------------------

NUM_TRANSACTIONS = 2000

start_date = datetime(2026, 1, 1)
end_date = datetime(2026, 8, 31)

# -----------------------------
# 2. PRODUCT CATALOG
# -----------------------------

products = {
    "Ball Pen": ("Writing", 5, 10),
    "Gel Pen": ("Writing", 10, 20),
    "Pencil": ("Writing", 4, 8),
    "Eraser": ("School", 3, 7),
    "Notebook": ("Paper", 35, 60),
    "A4 Sheets": ("Paper", 180, 250),
    "File": ("Office", 18, 35),
    "Marker": ("Writing", 20, 35),
    "Stapler": ("Office", 45, 75),
    "Calculator": ("Office", 180, 300),
    "Drawing Book": ("School", 30, 50),
    "Color Pencils": ("School", 45, 80),
    "Glue": ("School", 15, 25),
    "Scissors": ("Office", 25, 45),
    "Highlighter": ("Writing", 20, 35)
}

# -----------------------------
# 3. OTHER BUSINESS VARIABLES
# -----------------------------

customer_types = [
    "Student",
    "Individual",
    "Business"
]

payment_methods = [
    "Cash",
    "UPI",
    "Card"
]

# -----------------------------
# 4. GENERATE TRANSACTIONS
# -----------------------------

data = []

date_range = (end_date - start_date).days

for i in range(1, NUM_TRANSACTIONS + 1):

    order_id = f"ORD{i:04d}"

    date = start_date + timedelta(
        days=random.randint(0, date_range)
    )

    product = random.choice(list(products.keys()))

    category, unit_cost, unit_price = products[product]

    quantity = random.randint(1, 10)

    customer_type = random.choice(customer_types)

    payment_method = random.choice(payment_methods)

    revenue = quantity * unit_price

    cost = quantity * unit_cost

    profit = revenue - cost

    profit_margin = (profit / revenue) * 100

    data.append([
        order_id,
        date,
        product,
        category,
        quantity,
        unit_cost,
        unit_price,
        revenue,
        cost,
        profit,
        profit_margin,
        customer_type,
        payment_method
    ])

# -----------------------------
# 5. CREATE DATAFRAME
# -----------------------------

columns = [
    "Order_ID",
    "Date",
    "Product",
    "Category",
    "Quantity",
    "Unit_Cost",
    "Unit_Price",
    "Revenue",
    "Cost",
    "Profit",
    "Profit_Margin",
    "Customer_Type",
    "Payment_Method"
]

df = pd.DataFrame(data, columns=columns)

# -----------------------------
# 6. SORT BY DATE
# -----------------------------

df = df.sort_values("Date")

# -----------------------------
# 7. SAVE CSV
# -----------------------------

output_path = "data/sales_data.csv"

df.to_csv(output_path, index=False)

# -----------------------------
# 8. DISPLAY RESULTS
# -----------------------------

print("====================================")
print("BUSINESS DATASET CREATED")
print("====================================")

print(f"Transactions : {len(df):,}")
print(f"Date Range   : {df['Date'].min().date()} to {df['Date'].max().date()}")
print(f"Revenue      : ₹{df['Revenue'].sum():,.2f}")
print(f"Cost         : ₹{df['Cost'].sum():,.2f}")
print(f"Profit       : ₹{df['Profit'].sum():,.2f}")

print("\nFirst 5 records:")
print(df.head())

print("\nDataset saved to:")
print(output_path)