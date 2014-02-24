print("Hello World!")

print("This" + " is" + " a" + " concatenated" +" message.")

# Lists / Array
fruits = ['apple','mango','orange']
print fruits

# Array slice
a = [0,1,2,3,4,5]
print a[0:3] # prints 0 1 2
print a[:4] # prints 0 1 2 3
print a[2:3] # prints 2
print a[3:] # prints 3 4 5

# Inclusion
if 'apple' in fruits:
	print("Apple is there")

if 'grape' in fruits:
	print("Grape is there")
elif 'pear' in fruits:
	print("Pear is there")
else:
	print("Grape nor Pear is there")

# Dictionaries
things = { 'name': 'Sanyam', 'hobbies': ['reading','playing TT', 'running']}
print things


# Inclusion
# Note: In Dictionary we search for the keys
if 'name' is things:
	print ("name key is present")
