side1= int(input ("enter first side of triangle "))
side2= int(input ("enter second side of triangle "))
side3= int(input ("enter third side of triangle "))
if side1+side2>side3 and side1+side3>side2 and side2+side3>side1:
   perimeter = sum ([side1,side2,side3])
   print (perimeter)
   s= perimeter/2
   area = (s*(s-side1)*(s-side2)*(s-side3))**0.5
   print (area)
else:
  print ("triangle is not valid")
