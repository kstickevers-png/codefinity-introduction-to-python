# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}
total_sales_list = []

for product, values in products.items():
    price_str, quantity_str = values

    price = float(price_str)
    quantity_sold = int(quantity_str)
    total = price * quantity_sold
    total_sales_list.append(total)
    print(f"Total sales for {product}: ${total}")

total_sum = sum(total_sales_list)
print(f"Total sum of all sales: ${total_sum}")


min_sales = min(total_sales_list)
max_sales = max(total_sales_list)
print(f"Minimum sales: ${min_sales}")
print(f"Maximum sales: ${max_sales}")
total_sales = zip(products, total_sales_list)

