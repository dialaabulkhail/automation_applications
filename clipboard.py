import sys
import clipboard
import json 


"""
Multiple clipboard:
To be able to store multiple things on your clipboard and load them again

you can use these commands: save, load, list
* Run the file in the terminal
"""

"""
to run this :
>python clipboard.py save | load | list

To get this work you need to do the following:
if you copied something, and then used the save command with a key, then you load this key and paste in the terminal, you will see that what you copied is stored there in that key
but if you chose to load another key, you will not be able to paste what you copied in another key 

so each time you copy something and whant to store it in the json file, you need to use the save command and load it with the same key 

the list command is just to show the data in the terminal as keys and values
"""


                              ### Clipboard module basics####
#paste: is going to paste the data from clipboard to the "data" variable
# data = clipboard.paste()
# print(data)


# copy: to save data to the user's clipboard
# clipboard.copy("abc")
# after copying anything, you can "ctrl+v" paste it in the terminal to see it's copied.


# to access the commands, argv: gives all the command line arguments that are passed along side when you run this file
# to make any "command" after the name of the file in the terminal get passed too
# print(sys.argv)


# when running this:
#  python clipboard.py test hello world
# a list will be provided with every word I passed
# ['automation.py', 'test', 'hello', 'world']

# to access elements from the list
# print(sys.argv[1:])
# ['test', 'hello', 'world']



                                ### To activate the program ###
# store the file path in a variable
#this file doesn't exist so I must handle this in the load function
saved_data = "clipboard.json"

# here you should create a json file to allow us to store key,value pairs
def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

# we want the data in a doctoinary form
# save_data("clipboard.json", {"key":"value"})

# to load the json file
def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        #if the file doesn't exist 
        return {}


# to limit the user from accessing more than one command:
# one for the name of the file and the second is the command
if len(sys.argv) == 2:
    command = sys.argv[1]
    
    #here we store all the keys and values of the json dictionary in this variable "data"
    data = load_data(saved_data)
    # print(command)
    # will print: test if I passed only test

    # check is the passed command is equal to the three commands we defined 
    if command == "save":
        #when i want to save something, I want to propmt a message to enter a key to use in dictionary with the item
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(saved_data, data)
        print("Data is saved.")

    elif command == "load":
        key = input("Enter the key you want to load: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data is copied to clipboard")
        else:
            print("The key doesn't exist.")

    elif command == "list":
        print(data)

    else:
        print("Unkown command")

else:
    print("please pass one command only")