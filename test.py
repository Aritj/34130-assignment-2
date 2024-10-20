import timeit

# Data structure as
data_list = [
    {"category": "A", "value": 10},
    {"category": "B", "value": 15},
    {"category": "A", "value": 5},
    {"category": "C", "value": 7},
] * 25


# Data structure b

data_dict = {"A": [10, 5] * 25, "B": [15] * 25, "C": [7] * 25}


def approach_a(data: list[dict]) -> dict[str, int]:
    aggregated_data = {}
    for row in data:
        category = row["category"]
        value = row["value"]

        if category in aggregated_data:
            aggregated_data[category] += value
        else:
            aggregated_data[category] = value
    return aggregated_data


# Define the optimized approach (Dictionary of lists)
def approach_b(data: dict[str, list[int]]) -> dict[str, int]:
    return {category: sum(values) for category, values in data.items()}


# Time the original approach
a_time = timeit.timeit("approach_a(data_list)", globals=globals(), number=10000)

# Time the optimized approach
b_time = timeit.timeit("approach_b(data_dict)", globals=globals(), number=10000)

print(f"Approach A: {a_time}")
print(f"Approach B: {b_time}")
