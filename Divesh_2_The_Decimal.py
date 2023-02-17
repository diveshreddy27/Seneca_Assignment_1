def the_decimal(n):
    n = str(n)  #converting the number into string to split the number into two parts
    n_split = n.split(".")
    
    decimal_part=int(n_split[1])
    
    print(f"decimal part of {n} is {decimal_part} from {n_split}")
    
    if(decimal_part==0):
        return "Integer"
    else:
        return decimal_part
    
num = float(input("Enter the number : "))

print(the_decimal(num))
print(the_decimal(num))