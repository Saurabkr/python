inp = input("Enter any value: ")

if(inp != 'quit'):
    raise ValueError("Wrong string Entered")
else:
    print("Good Job")
   
#we can also make our own custon error

# class CustomError(Exception):
#   # code ...
#   pass

# try:
#   # code ...

# except CustomError:
#   # code...   