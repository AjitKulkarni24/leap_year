def is_leap(year):
   leap = False
   if(year % 4) == 0:
       if(year % 100) == 0:
           if(year % 400) == 0:
               print(True)

   else :
        return leap

year = int(input('enter year:  '))
print(is_leap(year))
