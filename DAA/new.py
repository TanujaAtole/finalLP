# Fractional Knapsack using Greedy Method

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight

def fractional_knapsack(items, capacity):
    # Sort items by value/weight ratio in descending order
    items.sort(key=lambda x: x.ratio, reverse=True)
    total_value = 0.0
    taken_items = []

    for item in items:
        if capacity <= 0:
            break
        if item.weight <= capacity:
            # take the whole item
            capacity -= item.weight
            total_value += item.value
            taken_items.append((item.weight, item.value, 1.0))  # 100%
        else:
            # take a fraction of the item
            fraction = capacity / item.weight
            total_value += item.value * fraction
            taken_items.append((capacity, item.value * fraction, fraction))
            capacity = 0

    return total_value, taken_items
# -------------------- MAIN --------------------
if __name__ == "__main__":
    n = int(input("Enter number of items: "))
    items = []
    for i in range(n):
        value = float(input(f"Enter value of item {i+1}: "))
        weight = float(input(f"Enter weight of item {i+1}: "))
        items.append(Item(value, weight))

    capacity = float(input("Enter capacity of knapsack: "))

    max_value, taken_items = fractional_knapsack(items, capacity)

    print("\nItem Taken (Weight | Value | Fraction):")
    for wt, val, frac in taken_items:
        print(f"  Weight taken: {wt:.2f} | Value gained: {val:.2f} | Fraction: {frac*100:.1f}%")

    print("\nMaximum value in Knapsack =", round(max_value, 2))
