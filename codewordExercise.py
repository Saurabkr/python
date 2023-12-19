#saurab -> udi-aurabs-khe
import random
import string

def generate_random_string(length):
	# Get all the ASCII letters in lowercase and uppercase
	letters = string.ascii_letters
	# Randomly choose characters from letters for the given length of the string
	random_string = ''.join(random.choice(letters) for i in range(length))
	return random_string

word = input("Enter your message: ")

def sender(message):
	if(len(message)>=3):
		message = generate_random_string(3) + message[1:] + message[0] + generate_random_string(3)
		# print(message)
		return message
	else:
		message = message[::-1]
		# print(message)	
		return message
		
def reciever(msg):
	if(len(msg)>=3):
		msg = msg[-4] + msg[3:-4]
		print(msg)
	else:
		msg = msg[-4] + msg[3:-4]
		msg = msg[::-1]
		print(msg)	

sender(word)
reply = sender(word)
reciever(reply)    
			  		

   

    		
		
	
