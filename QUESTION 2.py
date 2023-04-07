gi=float(input("Your Annual Income is "))
du=int(input("Dependent users in your family are "))
sd=10000
ti=gi-sd-(3000*du)
if ti>0:
    t=ti*0.2
    print("Tax Payable =",t)
else:
    print("Your income is not Taxable")