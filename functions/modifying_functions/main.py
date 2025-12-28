def apply_discount(price, discount=0.05):
    discounted_price = price * (1 - discount)
    return discounted_price
    
def apply_tax(discounted_price, tax=0.07):
    price_plus_tax = discounted_price * (1 + tax)
    return price_plus_tax

def calculate_total(price, discount=0.05, tax=0.07):
    discounted_price = apply_discount(price,discount)
    final_price = apply_tax(discounted_price,tax)
    return final_price

total_cost = calculate_total(120)

print(f"Total cost with default discount and tax: ${total_cost}")

total_cost = calculate_total(100, discount=0.10, tax=0.08)

print(f"Total cost with custom discount and tax: ${total_cost}")
