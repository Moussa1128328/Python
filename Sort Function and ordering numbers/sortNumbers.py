def sort_numbers(numbers):
    l = []
    for i in range(1, numbers+1):
        l.append(int(input(f"Enter number {i}: ")))
    return l