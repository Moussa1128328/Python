def detector(name):
    char="i"
    index=0
    for letter in name:
        if letter == char:
            print(f"'i' found at position {index}")
        index+=1

    return "Done"
