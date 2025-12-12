score=0
questions_answered=0
while True:
    
  print("\n Welcome to the quiz")
  print("1. How much is 10 + 20 ?")
  print("2. What is capital of India ?")
  print("3. How many gms in 1kg ?")
  print("4. How many days in a week ?")
  print("5. Exit ")

  choice=input("Enter your choice from 1 to 5\n ")
  
  if choice=="5":
     print("Thanks for partcipating\n")
     print("Your final score is : ", score , "out of 4")
     
     if questions_answered <4:   
         print("You exited early, quiz not completed.")
     else:
         if score<=2:
             print("You failed this quiz")
         else:
             print("You passed the quiz")
     break

  if choice not in ["1","2","3","4","5"]:
      print("Enter valid number")
      continue
  else:
     if choice=="1":
      ans=input("Enter the answer for first question\n ")
      questions_answered += 1
      if ans=="30":
              score=score + 1
              print("your answer is correct, score: ", score)
      else:
          print("Your answer is wrong, score: ", score)
               

     elif choice=="2":
      ans=input("Enter the answer for second question\n ")
      questions_answered += 1
      if ans=="Delhi" or "delhi":
              score=score + 1
              print("your answer is correct, score: ", score) 
      else:
          print("Your answer is wrong, score: ", score)

          
     elif choice=="3":
      ans=input("Enter the answer for third question\n ")
      questions_answered += 1
      if ans=="1000":
              score=score + 1
              print("your answer is correct, score: ", score) 
      else:
          print("Your answer is wrong, score: ", score)
          

     elif choice=="4":
      ans=input("Enter the answer for fourth question\n ")
      questions_answered += 1
      if ans=="7":
              score=score + 1
              print("your answer is correct, score: ", score) 
      else:
          print("Your answer is wrong, score: ", score)
        

      

