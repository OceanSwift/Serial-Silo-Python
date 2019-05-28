import os
import random
import string
import sys

# Getting the current work directory (cwd)
thisdir = os.getcwd()

# Variables
quantity = 1000
digits = 8
filename = "serial_silo.txt"

def main():
	if len(sys.argv) > 1:
		if sys.argv[1] == '?':
			print("arg1 = file name")
			print("arg2 = quantity")
			print("arg3 = digits")
			return
		else:			
			filename = sys.argv[1] + ".txt"
	else:
		filename = "serial_silo.txt"			
	if len(sys.argv) > 2:
		quantity = int(sys.argv[2])
	else:
		quantity = 1000
	if len(sys.argv) > 3:
		digits = sys.argv[3]
	else:
		digits = 8
	silo = [None] * quantity
	i = 0
	while i < quantity:
  		x = randomPassword()
  		silo[i] = x
  		i += 1
	f = open(filename,"w+")
	f.write(' '.join(silo))
	f.write('\n')
	f.write('\n')
	f.write('\n'.join(silo))
	f.close
	print (filename + ' created in ' + thisdir)

def randomPassword():
    randomSource = string.ascii_letters + string.digits
    password = random.choice(string.ascii_lowercase)
    for i in range(digits - 1):
        password += random.choice(randomSource)
    passwordList = list(password)
    random.SystemRandom().shuffle(passwordList)
    password = ''.join(passwordList)
    return password

if __name__ == "__main__":
    # execute only if run as a script
    main()

