from sortNumbers import sort_numbers

list_length = int(input("Enter list length: "))
list_numbers = sort_numbers(list_length)
ascend=sorted(list_numbers)
descend=sorted(list_numbers,reverse=True)

print(f"your list is: {list_numbers}")
print(f"your sorted list is: {ascend}")
print(f"your reverse sorted list is: {descend}")
