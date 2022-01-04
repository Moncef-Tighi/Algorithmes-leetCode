def num_grid(lst):
  lst2=[['0', '0', '0', '0', '0'],['0', '0', '0', '0', '0'],['0', '0', '0', '0', '0'],['0', '0', '0', '0', '0'],['0', '0', '0', '0', '0']]
  x=0

  def int_add_str(lis):
    lis=int(lis)
    lis=lis+1
    lis=str(lis)
    return lis

  while (x<5):
    y=0
    while (y<5):
      if lst[x][y]=="#":
        lst2[x][y]="#"
        if (x-1>=0) and (y-1>=0): 
          if lst[x-1][y-1]!="#":    
            lst2[x-1][y-1]= int_add_str(lst2[x-1][y-1])
        if (x-1>=0):
          if lst[x-1][y]!="#": 
            lst2[x-1][y]=int_add_str(lst2[x-1][y])
        if (x-1>=0) and (y+1<5):  
          if lst[x-1][y+1]!="#": 
            lst2[x-1][y+1]=int_add_str(lst2[x-1][y+1])
        if (y-1>=0):  
          if lst[x][y-1]!="#": 
            lst2[x][y-1]=int_add_str(lst2[x][y-1])
        if (y+1<5):  
          if lst[x][y+1]!="#": 
            lst2[x][y+1]=int_add_str(lst2[x][y+1])
        if (x+1<5) and (y-1>=0):
          if lst[x+1][y-1]!="#": 
            lst2[x+1][y-1]=int_add_str(lst2[x+1][y-1])
        if (x+1<5):
          if lst[x+1][y]!="#": 
            lst2[x+1][y]=int_add_str(lst2[x+1][y])
        if (x+1<5) and (y+1<5):
          if lst[x+1][y+1]!="#": 
            lst2[x+1][y+1]=int_add_str(lst2[x+1][y+1])
      y=y+1
    x=x+1
  return lst2

test=[
['-', '-', '#', '-', '-'],
['-', '-', '#', '#', '-'],
['#', '-', '-', '#', '-'],
['#', '#', '-', '#', '-'],
['#', '-', '-', '-', '-']
]

test2=num_grid(test)

print(test2)
x=input()
print(x)

