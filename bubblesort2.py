#Program for Bubble sort.
import os
import sys

def bubblesort(array):
	for i in range(0,len(array)):
		for j in range(0,len(array)):
			if int(array[i])<int(array[j]):
				temp=array[i]
				array[i]=array[j]
				array[j]=temp
	return array
	
def main():
	list=[]
	for i in range(0,5):
		number=input("Please enter a number:")
		list.append(number)
		sorted=bubblesort(list)
		for k in sorted:print(k)
		
main()

