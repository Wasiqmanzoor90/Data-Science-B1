class calculator:
  
  def __init__(self):
    print("im from Calculator")

    self.__add(12,12)
  def __add(self,a,b):
    print(a+b)

  def sub(self,a,b):
    print(a-b)
    
    
cal=calculator()

cal.sub(12,23)
