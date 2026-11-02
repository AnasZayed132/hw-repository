def total_bill(bill_amount,tip_perc):
    total=bill_amount*(1+0.01 *tip_perc)
    total=round(total,2)
    print("please pay$",total)
    return total

total_bill(150,20)

def seating_arangement(guests):
    '''this  function is for finding the amount of people with seats ready.'''
    if guests==0 or guests==1:
       return 1
    else:
        return guests* seating_arangement(guests-1)

print(seating_arangement.__doc__)

print("seating arangements for number 1 :",seating_arangement(1))
print("seating arangements for number 2 :",seating_arangement(2))
print("seating arangements for number 3 :",seating_arangement(3))
print("seating arangements for number 5 :",seating_arangement(5))