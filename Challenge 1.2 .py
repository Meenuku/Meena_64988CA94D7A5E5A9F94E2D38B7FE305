#Leapyear

"""
year%4 ==0&
year %100!=0/
year %400==0

"""
def isleapyear(year):
  if (year%4==0 and year%100!=0)or
    return True
  else:
     return False

year=2012

if isleapyear (year):
  print("{} is a leapyear.".format(year))
else:
  print("{} is not a leapyear. ".format(year) )