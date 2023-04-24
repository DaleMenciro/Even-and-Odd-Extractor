#Open 'number.txt' file for read
with open('numbers.txt') as my_file:
    #read lines and conver it to int
    numbers= [int(line.strip()) for line in my_file.readlines()]

#open 'even.txt' file to write
with open('even.txt', 'w') as file_even:
    #open 'odd.txt' file to write
    with open('odd.txt', 'w') as file_odd:
        #loop each numbers on the list
        for num in numbers:
            #check if even
            if num % 2 == 0:
                #write to 'even.txt' if the number is even
                file_even.write(str(num) + '\n')
            else:
                #write to 'odd.txt' if the number is odd
                file_odd.write(str(num) + '\n')