
📌 Project Structure
main.py → contains all functions (YOU must implement them)
test_main.py → contains unit tests (DO NOT change)





🔁 LOOPS & BASIC LOGIC
1. even_odd_tracker(numbers)

Task: Transform a list of integers into a list of "Even" or "Odd" strings.

Example:
even_odd_tracker([1,2,3,4]) → ["Odd", "Even", "Odd", "Even"]


2. temperature_filter(temps)

Task: Filter temperatures to keep only those between 18–25 (inclusive).

Example:
temperature_filter([10,18,22,30]) → [18, 22]


3. calculate_order_total(price, quantity)

Task: Compute order total with rules:

Base fee = 10
Total = base + (price × quantity)
If quantity ≥ 5 → add 20
Minimum total = 50

Example:
calculate_order_total(5, 2) → 50
calculate_order_total(20, 5) → 130


🧩 CONDITIONALS & LOOP CONTROL
4. process_scores(scores)

Task: Loop through scores and stop if any score < 40.
Return appropriate message:

"Stopped early at score X" if a score is < 40
"All scores processed" if all are ≥ 40

Example:
process_scores([60,70,35,80]) → "Stopped early at score 35"
process_scores([45,50,55]) → "All scores processed"



📦 DATA STRUCTURES
5. organize_products(items)

Task: Group products by category. Each item has 'name' and 'category'.
Return dictionary with categories as keys and list of names as values.

Example:

items = [
    {"name": "Milk", "category": "Dairy"},
    {"name": "Cheese", "category": "Dairy"},
    {"name": "Bread", "category": "Bakery"}
]
organize_products(items) → {"Dairy": ["Milk", "Cheese"], "Bakery": ["Bread"]}
⚡ LIST & SEQUENCE ALGORITHMS
6. sequence_growth(nums)

Task: Find the length of the longest strictly increasing consecutive sequence.

Example:

sequence_growth([3,4,5,1,2]) → 3
sequence_growth([1,2,3,4,5]) → 5
sequence_growth([5,4,3,2,1]) → 1



▶️ How to Run Tests
python -m pytest test_main.py -v


🧠 Strategy for Practice
Start with:
Loops (even_odd_tracker, temperature_filter)
Conditional logic (process_scores, calculate_order_total)

Then:
Dictionaries (organize_products)
Sequence analysis (sequence_growth)

Test edge cases carefully:
Empty lists
Single elements
Negative numbers
Multiple sequences

🚀 Final Tip
If a test fails:

Check input vs output carefully
Use print() to debug values
Focus on small steps to fix issues
