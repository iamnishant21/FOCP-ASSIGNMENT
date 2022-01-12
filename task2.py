from statistics import mean
miles=[]
kms=[]
count=0
print("Swallow Speed Analysis: Version 1.0")
while True:
    user=input("Enter the Next Reading:")
    count=count+1
    if user=="":
        break
    if user[0].capitalize()!="U" and user[0].capitalize()!="E":
        print("Invalid input")
        continue
    elif user[0].capitalize()=="U":
        speed = float(user[1:])
        miles.append(speed)
    else:
        speed = float(user[1:])
        miles.append(speed*0.621371)
if miles==[]:
    print("No readings entered. Nothing to do.")
else:
    for i in miles:
        kms.append(i/0.621371)
    print("\nResults Summary\n")
    print("{} Readings Analysed.\n".format(count))
    print("Max Speed:{:.2f}MPH,{:.2f}KPH".format(max(miles),max(kms)))
    print("Min Speed:{:.2f}MPH,{:.2f}KPH".format(min(miles),min(kms)))
    print("Avg Speed:{:.2f}MPH,{:.2f}KPH".format(mean(miles),mean(kms)))
