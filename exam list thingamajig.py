lst=[]
Mlist=[13,50,70,90,60]
print("these are the mark of the student:",Mlist)
smark=[21,32,59,47,64]*2
print("the sample mark multiplide by 2  is ",smark)
nmlist=len(Mlist)
print("m list length is ",nmlist)
print("these are the first and last marks of the og list",Mlist[0],"and ",Mlist[-1])

WMlist=Mlist[0:3]
wMlist=Mlist[::-1]
print("this is the range of the list",Mlist)
total=0
for M in Mlist:
    total+=M

average=total/len(Mlist)
print("sum:",total)
print("average:",average)\

Mlist.sort()
print("smallest number",Mlist[0])
print("largest number",Mlist[-1],"\n")

print("="*10)
print("this is the recipt of the hw")
print("this is the original list:",Mlist)
print("this is its total:",total)
print("this is its average:",average)
print("this is the first item in the list:",Mlist[0])
print("this is the last item in the list:",Mlist[-1])
print("="*10)