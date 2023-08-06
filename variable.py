# your.python
x=20
def my_func():
  y=23
 # print(x)//ham chahe to global variable ko bhi change kar sakte hai function k ander
  global x
  x=10
  print(y)
my_func()  
print(x)
