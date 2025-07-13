print("### ID CARD GENERATOR ###")
print("")

def id2():    
    c=int(input("ENTER AGE:"))
    c1=int(input("ENTER PHONE NUMBER:"))
    if (c1<1000000000)or(c1>9999999999):
        print("")
        print("PLEASE ENTER VALID PHONE NUMBER!!")
        print("")
        print("PLEASE REOPEN THE APPLICATION!!")
        print("")
        import time

        for i in range(500):
            print("### CODE BY T.HARIN PRANAV ###")
            time.sleep(3600)
        return
    c2=input ("ENTER MAIL ID:")
    print("")
    print("### THANKS FOR YOUR INFORMATION,HERE IS YOUR ID ###")
    print("")
    print("PLEASE WAIT FOR A MOVEMENT!")
    print("")
    import time
    time.sleep(5)
    print("YOUR ID CARD:")
    print("")
    print("------------------------------")
    print("NAME:",a)
    print("DOB:",b2,"/",b1,"/",b)
    print("AGE:",c)
    print("MAIL:",c2)
    print("PHONE:",c1)
    print("------------------------------")
    print("")
    import time
    
    for i in range(500):
        print("### CODE BY T.HARIN PRANAV ###")
        time.sleep(3600)
def id():
    global a
    a=input("ENTER NAME:")
    print("")
    print("ENTER DATE OF BIRTH [IN NUMBER]:")
    global b2,b1,b
    b2=int(input("ENTER DAY:"))
    b1=int(input("ENTER MONTH:"))
    b=int(input("ENTER YEAR:"))
    if (b2<1)or(b2>31) or (b1<1)or(b1>12) or (b<1000)or b>(2090):
         print("")
         print("PLEASE ENTER VALID DATE!!")
         print("")
         print("PLEASE REOPEN THE APPLICATION!!")
         print("")
         import time
         for i in range(500):
             print("### CODE BT T.HARIN PRANAV ###")
             time.sleep(3600)
         return
    else:
        print("")
        id2()
   
id()
