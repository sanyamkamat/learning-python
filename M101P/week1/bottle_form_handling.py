import bottle

@bottle.route('/')
def home_page():
	mythings = ['apple', 'orange', 'banana', 'peach']
#	return bottle.template('hello_world_tpl', username="Sanyam", things = mythings)
	return bottle.template('hello_world_tpl', {'username':'Sam', 'things':mythings})
	
@bottle.post('/favorite_fruit')
def fav_fruit():
	fruit = bottle.request.forms.get('fruit')
	if (fruit == None or fruit == ''):
		fruit="No fruit selected!"
		
	return bottle.template('fruit_selected.tpl',{'fruit': fruit})

bottle.debug(True)
bottle.run(host='localhost',port=8080)
