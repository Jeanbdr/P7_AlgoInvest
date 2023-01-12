"""OPTIMIZATION TIME"""
import csv
import itertools
import time

start = time.time()


def search_csv():
    stocks = []
    with open("Action.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            stock = (
                row[0],
                int(row[1]),
                int(row[2]),
                float(row[1]) * float(row[2]) / 100,
            )
            stocks.append(stock)
    return stocks


stocks = search_csv()


def knapSack(budget, action_cost, action_roi):
    actions_number = len(action_roi)
    table = [[0 for x in range(budget + 1)] for x in range(actions_number + 1)]
    for i in range(actions_number + 1):
        for j in range(budget + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif action_cost[i - 1] <= j:
                table[i][j] = max(
                    action_roi[i - 1] + table[i - 1][j - action_cost[i - 1]],
                    table[i - 1][j],
                )
            else:
                table[i][j] = table[i - 1][j]
    return table[actions_number][budget]


roi = [action[3] for action in stocks]
cost = [action[1] for action in stocks]
budget = 500

print(knapSack(budget=budget, action_cost=cost, action_roi=roi))
end = time.time()
print("This script took :", (end - start) * 10**3, "ms to give you this result.")
