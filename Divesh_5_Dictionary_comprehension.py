lst = range(100,160+1,10)
dict_comp = {x : x/100 for x in lst}
print("\nDictionary where each number in the range is key and each item divided by 100 is its value :",dict_comp)