def vowels(name):
    vowels="aeiouAIEOU"
    count=0
    for i in name:
        if i in vowels:
            count+=1
    return count