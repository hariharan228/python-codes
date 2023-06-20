def calculate_gifts(num_employees, ranks):
    gifts = [1] * num_employees  # Initialize all employees with at least one gift

    # Traverse from left to right
    for i in range(1, num_employees):
        if ranks[i] > ranks[i - 1]:
            gifts[i] = gifts[i - 1] + 1

    # Traverse from right to left
    # for i in range(num_employees - 2, -1, -1):
    #     if ranks[i] > ranks[i + 1]:
    #         gifts[i] = max(gifts[i], gifts[i + 1] + 1)

    return sum(gifts)


# Read the number of test cases
num_test_cases = int(input())

results = []

# Process each test case
for _ in range(num_test_cases):
    num_employees = int(input())
    ranks = list(map(int, input().split()))

    min_gifts = calculate_gifts(num_employees, ranks)
    results.append(min_gifts)

# Print the results
for result in results:
    print(result)
