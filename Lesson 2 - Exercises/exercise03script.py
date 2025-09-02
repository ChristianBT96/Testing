
def printer_cartridges_price_calculator(amount: int) -> float:
    if amount < 5:
        raise ValueError("Amount must be at least 5")
    
    price_per_unit = 10

    if amount >= 100:
        price_per_unit *= 0.8  # Apply 20% discount

    return amount * price_per_unit
    
    

