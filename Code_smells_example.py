#Code Smells Example for long method
def calculate_total_price(items):
    total = 0
    
    for item in items:
        if item.quantity <= 0:
            continue  
            
        discounted_price = item.price * 0.9 if item.price > 100 else item.price * 0.95
        total += discounted_price

    return total
