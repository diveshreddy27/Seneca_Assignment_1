
lst1 = [19542209, 4887871, 1420491, 626299, 1805832, 39865590]
lst2 = ["New York", "Alabama","Hawaii","Vermont","West Virginia","California"]

f_lst = list()

for z in zip(lst1,lst2):
    f_lst.append(z)
    
print("\nThe merged list of tuples : \n",f_lst)