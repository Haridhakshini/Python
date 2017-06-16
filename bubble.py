#Program for Bubble Sort in Python
# Array Input

array_num = list()
num = raw_input("Enter how many elements in the array:")
print "Enter elements in the array: "
for i in range(int(num)):
    n = raw_input("num :")
    array_num.append(int(n))

def bubble(array_num):
    for passnum in range(len(array_num)-1,0,-1):
        for i in range(passnum):
            if array_num[i]>array_num[i+1]:
                temp = array_num[i]
                array_num[i] = array_num[i+1]
                array_num[i+1] = temp
bubble(array_num)
print(array_num)


