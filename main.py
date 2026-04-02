
# ====================================================================
# QUESTION 1: even_odd_tracker
# ====================================================================
def even_odd_tracker(numbers: list) -> list:
    """Convert even/odd numbers to their string representations."""
    ls = []
    for num in numbers:
        if num % 2 == 0:
            ls.append("Even")
        else:
            ls.append("Odd")
    return ls
# print(even_odd_tracker([2,3,4,6]))


# ====================================================================
# QUESTION 2: temperature_filter
# ====================================================================
def temperature_filter(temps: list) -> list:
    """Filter valid temperatures between 18-25 degrees (inclusive)."""
    t = []
    for temp in temps:
        if temp >= 18 and temp <= 25:
            t.append(temp)
    return t
# print(temperature_filter([10,18,22,30]))


# ====================================================================
# QUESTION 3: calculate_order_total
# ====================================================================
def calculate_order_total(price: int, quantity: int) -> int:
    """
    Calculate total order cost with:
    - Base fee = 10
    - If quantity >= 5, add 20
    - Minimum total = 50
    """

    base = 10
    total = base + price * quantity  

    if quantity >= 5:
        total = total + 20 

    if total < 50:
        total = 50  

    return total
# print(calculate_order_total(20, 5))

# ====================================================================
# QUESTION 4: process_scores
# ====================================================================
def process_scores(scores: list) -> str:
    """Loop through scores and stop if any score is below 40."""
    for score in scores:
        if score < 40:
            return f"Stopped early at score {score}"
    return "All scores processed"
# print(process_scores([60,70,35,80]))


# ====================================================================
# QUESTION 5: organize_products
# ====================================================================
def organize_products(items: list) -> dict:
    """Group products by their category."""
    new_dict = {}
    for item in items:
        name = item["name"]
        category = item["category"]
        if category not in new_dict:
            new_dict[category] = []
        new_dict[category].append(name)
    return new_dict
# print(organize_products([
#     {"name": "Milk", "category": "Dairy"},
#     {"name": "Cheese", "category": "Dairy"},
#     {"name": "Bread", "category": "Bakery"}
# ]))

# ====================================================================
# QUESTION 6: sequence_growth
# ====================================================================
def sequence_growth(nums: list) -> int:
    """Find the longest strictly increasing consecutive sequence."""
    if not nums: 
        return 0 
    
    max_len = 1 
    current_len = 1 

    for i in range(1, len(nums)): 
        if nums[i] > nums[i - 1]: 
            current_len += 1 
            max_len = max(max_len, current_len) 
        else: 
            current_len = 1 
    return max_len 
# print(sequence_growth([3, 4, 5, 1, 2]))