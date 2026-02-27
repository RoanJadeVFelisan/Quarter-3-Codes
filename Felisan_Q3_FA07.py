savings = [
    [500, 300, 200],
    [150, 250, 100],
    [400, 350, 300]
]

for i in range(len(savings)):
    print("Category", i + 1, "data:", savings[i])
    
    total = sum(savings[i])
    average = total / len(savings[i])
    
    print("Total:", total)
    print("Average:", average)
    print()

max_value = max(max(row) for row in savings)
min_value = min(min(row) for row in savings)

print("Maximum value in dataset:", max_value)
print("Minimum value in dataset:", min_value)
