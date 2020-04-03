# This program says hello and asks for my name

print('hello world!')

print('What is your name?') #ask for their name
myName = input()

print(myName + ' is a really cool name!' + ' it is nice to meet you ' +myName+'.')
print('As a computer i must tell you that the length of your name is: ')
print(len(myName))

print('what is your age ' + myName +'?') #ask for their age
myAge = input()
print('you will be ' +str(int(myAge) + 1) + ' in a year.')
