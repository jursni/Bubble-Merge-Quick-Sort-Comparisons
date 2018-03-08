# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 23:22:53 2017

@author: justin
This program compares the average amount of time it takes bubbleSort, recursive mergeSort, and recursive quickSort to sort through the same sequences of various sizes.
WARNING - in order to run, this program raises the recursion limit set by python in order to reach sufficient recursion depth. Therefore, this program may not run on ALL computers and may take a long time (15+minutes to run).
"""

import random
import numpy
import time 
import sys
sys.setrecursionlimit(80000)

def swap(mylist, i, j): #a function for swapping items in a list, used in quickSort and bubbleSort
    mylist[i], mylist[j] = mylist[j], mylist[i]
    
def bubbleSort(list_of_integers): #performs bubbleSort
    unsorted = True #assume list is unsorted
    while unsorted==True: #while the sequence is unsorted...
        unsorted = False #set the sequence as sorted in case we find that it is in fact sorted
        i = 0 #counter
        for i in range(0,len(list_of_integers)-1): #here is where we show whether the sequence is actually sorted or not. for each element of the list...
            if list_of_integers[i]>list_of_integers[i+1]: #if the element is larger than the element following it...
                swap(list_of_integers,i,i+1) #swap the element and the element following it
                unsorted = True #because a swap had to occur, we assume that the list is not yet fully sorted and we force the function to check again to see if there are further swaps
            i+=1
    else: #returns the sorted list if sorted
        return list_of_integers
        
def partition(list_of_integers,first,last): # calculates the pivot point for each given sequence
    pivot=first #set current pivot as the first point
    for i in range(first,last): #we run i through all elements except the last
        if list_of_integers[last]>list_of_integers[i]: #if the value in the last point is greater than our current point
            swap(list_of_integers,i,pivot) #swap our current pivot with the our current point
            pivot+=1 #increase our pivot by 1
    swap(list_of_integers,pivot,last) #swap our pivot point and our last point
    return pivot #return our pivot point
    
def quickSort(list_of_integers,first,last): #performs quickSort recursively
    if last>first: #as long as base case isn't fulfilled...
        pivot = partition(list_of_integers,first,last) #determine current pivot value using partition function
        quickSort(list_of_integers,first,pivot-1) #repeat the process on a subsequence
        quickSort(list_of_integers,pivot+1,last) #repeat the process on the other subsequnce
    return list_of_integers #returns once base case is fulfilled (last <= first)
    
    
def merge(leftHalf,rightHalf): #a function for merging two lists together (meant for the use with two sorted lists to be merged into one large sorted list) for mergeSort
    merged_list=[] #creates an empty list to hold the compiled list
    i=0 #counter
    j=0 #counter
    while len(leftHalf)+len(rightHalf)>len(merged_list): #as long as the the merged list isnt complete...
        if leftHalf[i] < rightHalf[j]: #if the current element of left half is lesser than right half,
            merged_list.append(leftHalf[i]) #the next element of the compiled list to be filled in must be the current element of the left half
            i+=1
        else: #otherwise, add the current element of the right half
            merged_list.append(rightHalf[j])
            j+=1
        if i==len(leftHalf): #if we've added all of leftHalf already....
            merged_list.extend(rightHalf[j:]) #put the rest of rightHalf on the merged list
        if  j==len(rightHalf): #if we've added all of rightHalf already....
            merged_list.extend(leftHalf[i:]) #put the rest of leftHalf on the merged list
    return merged_list
            

def mergeSort(list_of_integers):  #performs mergeSort recurisively    
    if len(list_of_integers)<2: #base case
        return list_of_integers
        
    mid=len(list_of_integers)/2 #set the midpoint as halfway through the list
    leftHalf=mergeSort(list_of_integers[:mid]) #repeat the process on the left half of the current list
    rightHalf=mergeSort(list_of_integers[mid:]) #repeat the process on the right half of current list
    newList=merge(leftHalf, rightHalf) #new sorted list is the merging of the right and left halves using merge function
    return newList #returns sorted list
        
    
def compareSort(): #main function that compares the three sort functions with various sequence sizes
    counter_1000 = 0 #counter to ensure that we are averaging 10 trials
    quicksort1000_runtimes = [] #list to hold the 10 runtimes for quicksort for 1000 integer sequence
    mergesort1000_runtimes = [] #same idea^
    bubblesort1000_runtimes = [] #same idea^
    quicksort_integer_list =[] #list to hold the 1000 integer sequence that will be used for quicksort during each trial
    mergesort_integer_list=[] #same idea^
    bubblesort_integer_list=[] #same idea^
    while counter_1000 < 10: #while we have under 10 trials...
        list_of_integers = [] #list to hold the integer sequence
        
        integer_filler_counter=0 #counter to ensure we are filling the list with 1000 integers
        while integer_filler_counter<1000: #while the list/sequence contains under 1000 integers...
            list_of_integers.append(random.randint(1,100000)) #fill the integer list with a random number between 1 and 100000 
            integer_filler_counter+=1 #add 1 to counter (1 integer has been added to list)
            
        quicksort_integer_list=numpy.copy(list_of_integers) #make a copy of the integer list/sequence
        mergesort_integer_list=numpy.copy(list_of_integers)  #make a copy of the integer list/sequence
        bubblesort_integer_list=numpy.copy(list_of_integers)  #make a copy of the integer list/sequence
        
        before_quicksort=time.clock()     #time before quicksorting   
        quickSort(quicksort_integer_list,0,len(quicksort_integer_list)-1) #quicksort
        after_quicksort=time.clock() #time after quicksorting
        quicksort1000_runtimes=numpy.append(quicksort1000_runtimes,after_quicksort-before_quicksort) #append runtime list with the time taken for a run of quicksort

        before_mergesort=time.clock()    #same idea^     
        mergeSort(mergesort_integer_list) 
        after_mergesort=time.clock()  
        mergesort1000_runtimes=numpy.append(mergesort1000_runtimes,after_mergesort-before_mergesort)       

        before_bubblesort=time.clock()  #same idea^
        bubbleSort(bubblesort_integer_list) 
        after_bubblesort=time.clock()  
        bubblesort1000_runtimes=numpy.append(bubblesort1000_runtimes,after_bubblesort-before_bubblesort) 
        
        counter_1000 +=1 #add 1 to counter (1 trial has been run with each of the sorts)
        
    counter_2000 = 0 #same idea^
    quicksort2000_runtimes = []
    mergesort2000_runtimes = []
    bubblesort2000_runtimes = []
    quicksort_integer_list =[]    
    mergesort_integer_list=[]    
    bubblesort_integer_list=[]
    while counter_2000 < 10:
        list_of_integers = []
        
        integer_filler_counter=0
        while integer_filler_counter<2000:
            list_of_integers.append(random.randint(1,100000)) 
            integer_filler_counter+=1
            
        quicksort_integer_list=numpy.copy(list_of_integers)
        mergesort_integer_list=numpy.copy(list_of_integers)
        bubblesort_integer_list=numpy.copy(list_of_integers)
        
        before_quicksort=time.clock()        
        quickSort(quicksort_integer_list,0,len(quicksort_integer_list)-1)
        after_quicksort=time.clock() 
        quicksort2000_runtimes=numpy.append(quicksort2000_runtimes,after_quicksort-before_quicksort)

        before_mergesort=time.clock()         
        mergeSort(mergesort_integer_list)
        after_mergesort=time.clock() 
        mergesort2000_runtimes=numpy.append(mergesort2000_runtimes,after_mergesort-before_mergesort)      

        before_bubblesort=time.clock() 
        bubbleSort(bubblesort_integer_list)
        after_bubblesort=time.clock() 
        bubblesort2000_runtimes=numpy.append(bubblesort2000_runtimes,after_bubblesort-before_bubblesort)
        
        counter_2000 +=1


    counter_4000 = 0 #same idea^
    quicksort4000_runtimes = []
    mergesort4000_runtimes = []
    bubblesort4000_runtimes = []
    quicksort_integer_list =[]    
    mergesort_integer_list=[]    
    bubblesort_integer_list=[]
    while counter_4000 < 10:
        list_of_integers = []
        
        integer_filler_counter=0
        while integer_filler_counter<4000:
            list_of_integers.append(random.randint(1,100000)) 
            integer_filler_counter+=1
            
        quicksort_integer_list=numpy.copy(list_of_integers)
        mergesort_integer_list=numpy.copy(list_of_integers)
        bubblesort_integer_list=numpy.copy(list_of_integers)
        
        before_quicksort=time.clock()        
        quickSort(quicksort_integer_list,0,len(quicksort_integer_list)-1)
        after_quicksort=time.clock() 
        quicksort4000_runtimes=numpy.append(quicksort4000_runtimes,after_quicksort-before_quicksort)

        before_mergesort=time.clock()         
        mergeSort(mergesort_integer_list)
        after_mergesort=time.clock() 
        mergesort4000_runtimes=numpy.append(mergesort4000_runtimes,after_mergesort-before_mergesort)      

        before_bubblesort=time.clock() 
        bubbleSort(bubblesort_integer_list)
        after_bubblesort=time.clock() 
        bubblesort4000_runtimes=numpy.append(bubblesort4000_runtimes,after_bubblesort-before_bubblesort)
        
        counter_4000 +=1


    counter_8000 = 0 #same idea^
    quicksort8000_runtimes = []
    mergesort8000_runtimes = []
    bubblesort8000_runtimes = []
    quicksort_integer_list =[]    
    mergesort_integer_list=[]    
    bubblesort_integer_list=[]
    while counter_8000 < 10:
        list_of_integers = []
        
        integer_filler_counter=0
        while integer_filler_counter<8000:
            list_of_integers.append(random.randint(1,100000)) 
            integer_filler_counter+=1
            
        quicksort_integer_list=numpy.copy(list_of_integers)
        mergesort_integer_list=numpy.copy(list_of_integers)
        bubblesort_integer_list=numpy.copy(list_of_integers)
        
        before_quicksort=time.clock()        
        quickSort(quicksort_integer_list,0,len(quicksort_integer_list)-1)
        after_quicksort=time.clock() 
        quicksort8000_runtimes=numpy.append(quicksort8000_runtimes,after_quicksort-before_quicksort)

        before_mergesort=time.clock()         
        mergeSort(mergesort_integer_list)
        after_mergesort=time.clock() 
        mergesort8000_runtimes=numpy.append(mergesort8000_runtimes,after_mergesort-before_mergesort)      

        before_bubblesort=time.clock() 
        bubbleSort(bubblesort_integer_list)
        after_bubblesort=time.clock() 
        bubblesort8000_runtimes=numpy.append(bubblesort8000_runtimes,after_bubblesort-before_bubblesort)
        
        counter_8000 +=1
    
    #average the runtimes over 10 trials and print out the average runtimes of each sort with each given sequence size
    print "sorting 1000 integers:"
    print "quickSort:", (sum(quicksort1000_runtimes))/10, "s"
    print "mergeSort:", (sum(mergesort1000_runtimes))/10, "s"
    print "bubbleSort:", (sum(bubblesort1000_runtimes))/10, "s"
    print "\n"
    print "sorting 2000 integers:"
    print "quickSort:", (sum(quicksort2000_runtimes))/10, "s"
    print "mergeSort:", (sum(mergesort2000_runtimes))/10, "s"
    print "bubbleSort:", (sum(bubblesort2000_runtimes))/10, "s"
    print "\n"
    print "sorting 4000 integers:"
    print "quickSort:", (sum(quicksort4000_runtimes))/10, "s"
    print "mergeSort:", (sum(mergesort4000_runtimes))/10, "s"
    print "bubbleSort:", (sum(bubblesort4000_runtimes))/10, "s"
    print "\n"
    print "sorting 8000 integers:"
    print "quickSort:", (sum(quicksort8000_runtimes))/10, "s"
    print "mergeSort:", (sum(mergesort8000_runtimes))/10, "s"
    print "bubbleSort:", (sum(bubblesort8000_runtimes))/10, "s"
    
compareSort()