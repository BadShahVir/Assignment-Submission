Num = int(input("Type a Number = "))
print(Num)
if Num > 1:
   for n in range(2, Num):
      if (Num % n) == 0:
         print(Num, "is not prime")
         break
      
   else:
      print(Num, "is a prime number")