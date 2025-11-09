class Item: 
    def __init__(self, value, weight): 
        self.value = value 
        self.weight = weight 
 
def fractional_knapsack(capacity, items): 
    # Sort items by value/weight ratio in descending order 
    items.sort(key=lambda x: x.value / x.weight, reverse=True) 
 
    total_value = 0.0 
    current_weight = 0 
 
    for item in items: 
        if current_weight + item.weight <= capacity: 
            # Take whole item 
            current_weight += item.weight 
            total_value += item.value 
        else: 
            # Take fraction of the item 
            remaining_capacity = capacity - current_weight 
            fraction = remaining_capacity / item.weight 
            total_value += item.value * fraction 
            break 
 
    return total_value 
 
 
if __name__ == "__main__": 
    n = int(input("Enter number of items: ")) 
    items = [] 
 
    for i in range(n): 
        value = int(input(f"Enter Profit of item {i+1}: ")) 
        weight = int(input(f"Enter weight of item {i+1}: ")) 
        items.append(Item(value, weight)) 
 
    capacity = int(input("Enter capacity of knapsack: ")) 
 
    max_value = fractional_knapsack(capacity, items) 
    print(f"Maximum value in the knapsack: {max_value:.2f}") 


    '''
    Enter number of items: 6
Enter Profit of item 1: 18
Enter weight of item 1: 7
Enter Profit of item 2: 5
Enter weight of item 2: 2
Enter Profit of item 3: 9
Enter weight of item 3: 3
Enter Profit of item 4: 10
Enter weight of item 4: 5
Enter Profit of item 5: 12
Enter weight of item 5: 3
Enter Profit of item 6: 7
Enter weight of item 6: 2
Enter capacity of knapsack: 13
Maximum value in the knapsack: 40.86
    
    
    '''