<!doctype html>
<html>
<head>
<title>Hello World!!!</title>
</head>
<body>
<p>Welcome {{username}}</p>
<p>List of fruits I like</p>
<ul>
%for thing in things:
<li>{{thing}}</li>
%end
</ul>
<form action="/favorite_fruit" method="POST">
What is your favourite fruit?
<input type="text" name="fruit" size="40" value=""><br/>
<input type="submit" value="Submit">
</form>
</body>
</html>
