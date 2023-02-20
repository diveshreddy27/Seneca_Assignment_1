def the_decimal(num):
    num_str = str(num)
    spl = num_str.split(".")
    if(spl[1] == "0"):
        print("Integer")

number = float(23.3)

the_decimal(number)