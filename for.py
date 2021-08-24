exp=[2340,231,3459,3232,1313,445,45,4646]
total=0
for item in exp:
    total =total+item
print(total)
# range
for i in range(1,3):
    print(i*i)
#     month expense
for j in range(len(exp)):
    print("month:", (j+1),"expense:",exp[j])
    total=total+exp[j]
print("total expense :",total)

# keys searching

keys_location="inCar"
locations=["garage","living area","office table","inCar","bedroom"]
for i in locations:
    if i == keys_location:
        print(" keys are found  :",i)
        break
    else:
        print("keys not found:",i)
# continue
for i in range(1,8):
    if i%2==0:
        continue
    print(i*i)
