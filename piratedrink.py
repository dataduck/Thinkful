import random

"""This script will create a drink based on questions from the user"""

questions = {
	"strong": "Do ye like yer drinks strong?", 
	"salty": "Do ye like yer drinks a lot of saltyness?", 
	"bitter": "Do ye like your drinks bitter like", 
	"sweet": "Do ye like your drinks ye sweet?", 
	"fruity": "Do ye love fruitiness in ya'll drinkin?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

def find_preferences(): 
	preferences = {}
	for type, question in questions.items():
		print question
		preferences[type] = raw_input().lower() in ['y', 'yes']
		print ""
	return preferences

def make_drink(preferences):
	drink = []
	for ingredient_type, liked in preferences.iteritems():
		if not liked: 
			continue 

		drink.append(random.choice(ingredients[ingredient_type]))
	return drink 

def main():
	preferences = find_preferences()
	drink = make_drink(preferences)
	print "Here it comes!"
	print "It's all the stuff you love! Here's what I put in it:"
	for ingredient in drink: 
		print "A {}".format(ingredient)

if __name__ == "__main__": 
	main()


	
