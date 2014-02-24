# Iterating through Array

fruit = ['apple','orange','grape']	# init the array

new_fruit = []

for item in fruit:					# iterate
	print item
	
	new_fruit.append(item)

print new_fruit

sum = 0
numbers = [1,2,3,5,8]
for i in numbers:
  sum = sum + i
print i

# prints: 8

# Iterating through Dictionary

person = {'name': 'Sanyam', 'fav_color': 'blue','hair':'brown'}

for key in person: #Iterate
	print "key is " + key + " & the value is " + person[key]
	
people = {'name':'Bob', 'hometown': "Palo Alto", 'favorite_color': 'red'}
for item in people:
	if (item == 'favorite_color'):
		print  people[item]

# prints: red
