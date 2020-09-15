#!/usr/bin/env python3

# Update your portfolio with current values (if you add a stock, add the investment map as well)
# Update the surplus with whatever additional money you can invest
# Run the script

import sys
import json
import yaml

with open(sys.argv[1]) as file:
    data = yaml.load(file, Loader=yaml.FullLoader)
    portfolio = data.get('portfolio')
    ideal_allocation_percent = data.get('ideal_allocation_percent')
    investment_map = data.get('investment_map')
    surplus = data.get('surplus')

def dump(x):
    print(json.dumps(x, indent=4, sort_keys=True))

current_allocation = {}
for x in ideal_allocation_percent:
    current_allocation[x] = 0

for x in portfolio:
    current_allocation[investment_map[x]] += portfolio[x]

print("Current allocation:")
dump(current_allocation)

total_allocation_percent = 0

for x in ideal_allocation_percent:
    total_allocation_percent += ideal_allocation_percent[x]

assert total_allocation_percent == 100, "You must allocate 100%% (%s)" % total_allocation_percent

total_to_invest = surplus

for x in current_allocation:
    total_to_invest += current_allocation[x]

print("Total to invest: " + str(total_to_invest))
ideal_allocations = {}

for x in ideal_allocation_percent:
    ideal_allocations[x] = ideal_allocation_percent[x] * total_to_invest / 100

print("Ideal allocations:")
dump(ideal_allocations)

differences = {}
positives = negatives = 0

for x in ideal_allocations:
    differences[x] = current_allocation[x] - ideal_allocations[x]

    if differences[x] < 0:
        negatives += abs(differences[x])

subtotal = 0

for x in differences:
    if differences[x] < 0:
        subtotal += ideal_allocation_percent[x]

allocations = {}
for x in differences:
    if differences[x] < 0:
        allocations[x] = round(surplus * (ideal_allocation_percent[x] / subtotal), 2)

print("These are your overall differences:")
dump(differences)
print("This is how you should invest:")
dump(allocations)