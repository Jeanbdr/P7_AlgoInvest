import csv
import time

BUDGET = 500


def search_csv():
    stocks = []
    with open("Action.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == "name" or float(row[1]) <= 0 or float(row[2]) <= 0:
                pass
            else:
                stock = (
                    row[0],
                    int(row[1]),
                    float(row[2]),
                    (float(row[1]) * float(row[2])) / 100,
                )
                stocks.append(stock)
    return stocks


def knapSack():
    budget = BUDGET
    action_cost = [action[1] for action in stocks]
    action_roi = [action[3] for action in stocks]
    actions_number = len(stocks)
    table = [[0 for x in range(budget + 1)] for x in range(actions_number + 1)]
    for i in range(1, actions_number + 1):
        for j in range(1, budget + 1):
            if action_cost[i - 1] <= j:
                table[i][j] = max(
                    # J'achete l'action
                    action_roi[i - 1] + table[i - 1][j - action_cost[i - 1]],
                    # Je n'achete pas l'action
                    table[i - 1][j],
                )
            else:
                table[i][j] = table[i - 1][j]
    combination = []
    while budget >= 0 and actions_number >= 0:
        if (
            table[actions_number][budget]
            == table[actions_number - 1][budget - action_cost[actions_number - 1]]
            + action_roi[actions_number - 1]
        ):
            combination.append(stocks[actions_number - 1])
            budget -= action_cost[actions_number - 1]
        actions_number -= 1
    print(f"\nThe algorithm choose {len(combination)} actions\n\n")
    print(f"Those actions are :\n{combination}\n\n")
    print(f"This combination will generate a profit of {table[-1][-1]}€")


start = time.time()
stocks = search_csv()
knapSack()
end = time.time()
print("\nThis script took :", (end - start) * 10**3, "ms to give you this result.")
