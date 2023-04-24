#Write a Python program that reads a text file named numbers.txt that contains 20 integers. 
#The program will create two other text file; the first text file will be named even.txt that 
#will contains all even numbers extracted from the numbers.txt. The second text file will be named 
#odd.txt that will contains all odd numbers extracted from the numbers.txt.

#Open 'number.txt' file for read
with open('numbers.txt') as my_file:
    #read lines and conver it to int
    numbers= [int(line.strip()) for line in my_file.readlines()]

#open 'even.txt' file to write
    #open 'odd.txt' file to write
        #loop each numbers on the list
            #check if even
                #write to 'even.txt' if the number is even
                #write to 'odd.txt' if the number is odd