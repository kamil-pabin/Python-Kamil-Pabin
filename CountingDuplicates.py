from collections import Counter

def duplicate_count(text):
    num=0
    for x in Counter((text.lower())).values():
        if x > 1 : num+=1 
    return num



print(duplicate_count("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZReturnsTwentySix"))
print(duplicate_count("abcdea"))