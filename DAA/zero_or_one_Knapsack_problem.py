def knapsack_dp(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


if __name__ == "__main__":
    n = int(input("Enter number of items: "))
    values = []
    weights = []

    for i in range(n):
        v = int(input(f"Enter value of item {i+1}: "))
        w = int(input(f"Enter weight of item {i+1}: "))
        values.append(v)
        weights.append(w)

    capacity = int(input("Enter capacity of knapsack: "))

    max_value = knapsack_dp(values, weights, capacity)
    print(f"Maximum value in the knapsack: {max_value}")




    '''
    Enter number of items: 4
Enter value of item 1: 1
Enter weight of item 1: 2
Enter value of item 2: 2
Enter weight of item 1: 2
Enter value of item 2: 2
Enter value of item 2: 2
Enter weight of item 2: 3
Enter value of item 3: 5
Enter weight of item 3: 4
Enter value of item 4: 6
Enter weight of item 4: 5
Enter capacity of knapsack: 8   



    # 0-1 Knapsack using Branch and Bound
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight

# Node structure for branch and bound tree
class Node:
    def __init__(self, level, profit, weight, bound):
        self.level = level      # Level in decision tree
        self.profit = profit    # Current profit
        self.weight = weight    # Current weight
        self.bound = bound      # Upper bound on profit

# Function to calculate upper bound
def bound(u, n, W, items):
    if u.weight >= W:
        return 0

    profit_bound = u.profit
    j = u.level + 1
    totweight = u.weight

    # Add items fractionally for upper bound
    while j < n and totweight + items[j].weight <= W:
        totweight += items[j].weight
        profit_bound += items[j].value
        j += 1

    # Add fraction of next item (if available)
    if j < n:
        profit_bound += (W - totweight) * items[j].ratio

    return profit_bound

# Branch and Bound Knapsack
def knapsack_branch_bound(W, items, n):
    # Sort items by value/weight ratio (descending)
    items.sort(key=lambda x: x.ratio, reverse=True)

    queue = []
    u = Node(-1, 0, 0, 0)
    v = Node(0, 0, 0, 0)
    max_profit = 0

    # Start from root node
    u.bound = bound(u, n, W, items)
    queue.append(u)

    # Process the queue
    while queue:
        u = queue.pop(0)

        # If it's the last node, continue
        if u.level == n - 1:
            continue

        # Take next level item
        v.level = u.level + 1

        # Include the next item
        v.weight = u.weight + items[v.level].weight
        v.profit = u.profit + items[v.level].value

        # If within capacity and profit better, update
        if v.weight <= W and v.profit > max_profit:
            max_profit = v.profit

        # Calculate bound for this node
        v.bound = bound(v, n, W, items)

        # If promising, add to queue
        if v.bound > max_profit:
            queue.append(Node(v.level, v.profit, v.weight, v.bound))

        # Exclude the next item
        v.weight = u.weight
        v.profit = u.profit
        v.bound = bound(v, n, W, items)

        if v.bound > max_profit:
            queue.append(Node(v.level, v.profit, v.weight, v.bound))

    return max_profit


# MAIN PROGRAM
if __name__ == "__main__":
    print("=== 0-1 Knapsack Problem using Branch and Bound ===")

    # Input number of items
    n = int(input("Enter number of items: "))
    items = []

    for i in range(n):
        val = int(input(f"Enter value of item {i+1}: "))
        wt = int(input(f"Enter weight of item {i+1}: "))
        items.append(Item(val, wt))

    W = int(input("Enter maximum capacity of knapsack: "))

    # Solve using Branch and Bound
    max_profit = knapsack_branch_bound(W, items, n)
    print("\nMaximum value that can be obtained:", max_profit)

    
    '''
