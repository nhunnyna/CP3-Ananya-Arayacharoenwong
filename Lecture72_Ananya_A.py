menuList = []
def showBill():
    print("---- My Food ----")
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1])
while True:
    menuName = input("Please Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append([menuName,menuPrice])
showBill()
