try:
    num,num2=eval(input("Enter two number in cooma"))
    result= num/num2
    print("The ans is ",result)
except ZeroDivisionError:
 print("Bro See the Zero Rule")

except SyntaxError:
 print("Bro See the Comma it is mising")

except:
  print("Wrong ans")
else:
  print("No exectipion")
finally:
  print("Are you Albert Intestine")

