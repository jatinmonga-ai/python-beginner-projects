expenses = []
categories=["Food", "Travel", "Shopping", "Other" ]
while True:
    
    print("\n Welcome to expense app : ")
    print("1. Add an expense")
    print("2. View an expense")
    print("3. Total expense")
    print("4. Exit")

    choice=input("Choose an option from 1 to 4: \n")

    if choice=="4":
        print("Thanks for using me.")
        break
    else:
        if choice not in ["1","2","3","4"]:
            print("Enter valid number")
            continue
        else:
             if choice=="1":
                add_expense=float(input("Enter the $ expense you wanna add \n "))

                print("\n Choose your category: ")
                for y,z in enumerate(categories,start=1):
                     print(y , ".", z)

                choice2=input("Choose your category \n ")

                if choice2 not in["Food","Travel","Shopping","Other", "food","travel","shopping","other"]:
                    print("Choose appropriate category")
                    continue

                print("You selected : ", choice2)

                expenses.append({
                    "amount" : add_expense,
                    "category" : choice2
                })
                
                
             elif choice=="2":
                  if len(expenses)<=0:
                      print("No expense to view here")
                  else:
                      print(" Here is the list of expenses: \n ")
                      for e in expenses:
                          print("$", e["amount"], "-", e["category"])
                            
             elif choice=="3":
                  if len(expenses)<=0:
                      print("No expesne to calculate")
                  else:
                     total = 0
                     for e in expenses:
                        total= total + e["amount"]
                      
                  print(" Here is the total of expenses: ", "$",total)         
              

