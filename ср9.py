def century():
    b = x//100+1
    print(str(b) + " век.")

def yearV():
    print("Високосный год.")
    century()
def yearNV():
    print("Невисокосный год.")
    century()


def check2():
    a = x % 400
    
    if int(a) == 0:
        yearV()
        
    else:
        yearNV()
        

def check1():
    a = x % 100
    if int(a)==0:
       def check2():
           a = x % 400
          
           if int(a) == 0:
               yearV()
           else:
               yearNV()
       check2(a)
    else:
        def check3():
            a = x % 4
            
            if int(a) == 0:
                yearV()
            else:
                yearNV()
        check3()
        
    
    


a = 0
b = 0
while True:
    try:
        x = int(input("Введите год: "))
        if int(x)>0:
            break
        else:
            print("Ошибка.")
            continue
    except ValueError:
        continue
check1()
