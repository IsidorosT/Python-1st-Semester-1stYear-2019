def mainprogramm():
    Num = UserInput()
    Result(Num)
def UserInput():
    run1 = True
    while run1:
        number = input('Insert an integer between(1-1000000):')
        try:
            number = int(number)
            run1 = False
        except ValueError:
            print('You didnt give an integer!!!!')
            run1 = True
        if number < 1 and number > 1000000 :
            print('The integer you insert is out of range!!!')
            run1 = True
    return number
def Result(num):
    a = []
    i = 1
    while (1<=num):
        if(i^2 > num):
            break
        k=0
        if(num%i==0):
            j=1
            while(j<=i):
                if(i%j==0):
                    k=k+1
                j=j+1
            if(k==2):
                a.append(i)
        i=i+1
    for i in range(len(a)):
        l = 0
        while num%a[i] == 0:
            l = l + 1
            num = num / a[i]
        if l==1:
           print('(',a[i],')',end="")
        else:
            print('(',a[i],'**',l,')',end="")
        
    
mainprogramm()

    
    
