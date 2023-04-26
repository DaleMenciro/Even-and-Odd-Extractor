import tkinter as tk
from tkinter import filedialog, messagebox

def select_input_file():
    """Select the input file"""
    global input_file
    input_file = filedialog.askopenfilename(title="Select Input File", filetypes=(("Text Files", "*.txt"),))

def select_output_dir():
    """Select the output directory"""
    global output_dir
    output_dir = filedialog.askdirectory(title="Select Output Directory")

def extract_numbers():
    try:
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
        messagebox.showinfo("Task Complete", "Even and odd numbers extracted successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the GUI window
root = tk.Tk()
root.title("Extract Even and Odd Numbers")
root.geometry("400x200")

# Create the select input file button
btn_select_input = tk.Button(root, text="Select Input File", command=select_input_file)
btn_select_input.pack(pady=10)

# Create the select output directory button
btn_select_output = tk.Button(root, text="Select Output Directory", command=select_output_dir)
btn_select_output.pack(pady=10)

# Create the extract numbers button
btn_extract_numbers = tk.Button(root, text="Extract Numbers", command=extract_numbers)
btn_extract_numbers.pack(pady=10)

# Start the GUI loop
