fruit_basket1={"apple","orange","orange","banana","grapes","orange"}

fruit_basket2={"banana","mango","grapes","peach","banana","banana"}

print("fruit_basket1:",fruit_basket1,"\nfruit_basket2:",fruit_basket2,"\n")

fruit_basket1.add("orange")
print("new fruit_basket1:",fruit_basket1,"\n")
fruit_basket12=fruit_basket1.intersection(fruit_basket2)
print(fruit_basket12)

import array as arr
fruit_basket3=arr.array("i",[21,21,27,60,79,75])
print("this is basket 3 :",fruit_basket3)

fruit_basket3.insert(1,28)
fruit_basket3.append(78)
print("again the fruit_basket3:",fruit_basket3)

cfruit_basket3=fruit_basket3.count(21)

print("this is how many times 21 comes up in fruit_basket3",cfruit_basket3)

fruit_basket3.reverse()
print(fruit_basket3)

print("="*30)
print("fruit basket recipt\n")
print("fruit_basket1:",fruit_basket1)
print("fruit_basket2:",fruit_basket2)
print("shared fruits:",fruit_basket12)
print("FRUIT_COUNT:",cfruit_basket3)
print("="*30)