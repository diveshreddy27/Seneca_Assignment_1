def test(a,b):
    try:
        #default type of input() method is string so we need to check weather int is a integer or string

        if(x.isnumeric()):
            a=int(a)
        if(y.isnumeric()):
            b=int(b)

        summ = a + b
        print(f"added two inputs {a} and {b} , then we got : ",summ)
    except BaseException :
        print("You cant add int to a string")
                
x=input("enter 1st item : ")   
y=input("enter 2nd item : ")

test(x,y)