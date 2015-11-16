bill_total=input('Please enter the bill amount :')
tax_percentage=input('please enter the percentage of tax :')
tip_percentage=input('Please enter the tip percentage :')
tax=((float(tax_percentage)/100)*float(bill_total))
print('The Tax to be paid is : {0:.2f}'.format(tax))
tip=(float(tip_percentage)/100)*float(bill_total)
print('The tip to be paid is : {0:.2f}'.format(tip))
Total=float(bill_total)+tax+tip
print('The Total bill to be paid is : {0:.2f}'.format(Total))

