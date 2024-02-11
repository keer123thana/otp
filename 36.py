def rand1(m):
    import random
    for i in range(0,10,1):
        n=m
        temp=random.randint(10**(n-1),10**n-1)
        print(temp)
banks=["HDFC","ICIC"]
bankname=input("enter bank name:").upper()
if banks[0]==bankname:
    print("HDFC OTPs are:")
    rand1(6)
else:
    if bankname in banks:
        print(bankname,"OTPs are:")
        rand1(8)
    else:
        print(bankname,"not registered")
