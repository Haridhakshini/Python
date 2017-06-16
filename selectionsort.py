#Program for Selection Sort

#Array Input

array_num = list()
num = raw_input("Enter how many elements in the array:")
print "Enter elements in the array: "
for i in range(int(num)):
    n = raw_input("num :")
    array_num.append(int(n))
    
#Selection Sort function

def selectionsort(array_num):
   for slot in range(len(array_num)-1,0,-1):
       locationofmax=0
       for location in range(1,fillslot+1):
           if array_num[location]>array_num[locationofmax]:
               locationofmax = location
       temp = array_num[slot]
       array_num[slot] = array_num[locationofmax]
       array_num[locationofmax] = temp
selectionsort(array_num)
print(array_num)

