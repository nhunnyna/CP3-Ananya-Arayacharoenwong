usernameInput = input("Username :")
passwordInput = input("Password :")
if usernameInput == "Hello Aloha" and passwordInput == "8698":
    print("Hello Welcome to Bakeyna Shop")
    print("----- Menu Bakeyna Shop -----")
    print("1. Chocolate Cake x1 = 55 THB")
    print("2. Iced Chocolate x1 = 45 THB")
    print("3. Vanilla Frappe x1 = 60 THB")
    print("4. Coffee         x1 = 30 THB")

    print("-----------------------------")
    q_Choc = int(input("Quantity of Menu Number1:"))
    q_IcedChoc = int(input("Quantity of Menu Number2:"))
    q_VaFrap = int(input("Quantity of Menu Number3:"))
    q_Coffee = int(input("Quantity of Menu Number4:"))

    p_Choc = 55
    p_IcedChoc = 45
    p_VaFrap = 60
    p_Coffee = 30

    total_1 = q_Choc * p_Choc
    total_2 = q_IcedChoc * p_IcedChoc
    total_3 = q_VaFrap * p_VaFrap
    total_4 = q_Coffee * p_Coffee
    print("-----------------------------")
    print("Total Price of Menu Number1:",total_1,"THB")
    print("Total Price of Menu Number2:",total_2,"THB")
    print("Total Price of Menu Number3:",total_3,"THB")
    print("Total Price of Menu Number4:",total_4,"THB")
    print("Total:",total_1 + total_2 + total_3 + total_4,"THB")
    print("-----------------------------")
    print("----Thank you comes again----")
else:
    print("Wrong Username and Password")
