operator = 0
list_ = []  #list_ is a list to store names(data type : string)
#   here  I used operator to add multiple names to the list_ one by one according to the user 
while(operator == 0):
    name = input("\nEnter a name : ")
    list_.append(name)
    operator = int(input("\nEnter 0 to add another name or else enter 1  : "))
    if(operator!=0):
        break
    
sorted_names_list = []

for x in list_ :
    i = 0
    x = x.title()
    while(i<len(sorted_names_list)):
        if(x < sorted_names_list[i]):
            break
        else:
            i = i + 1
    sorted_names_list.insert( i , x )
    
print("Names in Ascending order : ",sorted_names_list)
