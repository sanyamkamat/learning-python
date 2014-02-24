import bottle

@bottle.route('/')
def home_page():
	mythings = ['apple', 'orange', 'banana', 'peach']
#	return bottle.template('hello_world_tpl', username="Sanyam", things = mythings)
	return bottle.template('hello_world_tpl', {'username':'Sam', 'things':mythings})
	
	
bottle.debug(True)
bottle.run(host='localhost',port=8080)
