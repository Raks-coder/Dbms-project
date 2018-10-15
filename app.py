from flask import Flask,url_for,render_template,request
import redis;

app=Flask(__name__)

wsgi_app=app.wsgi_app
#connect to redis data store
r=redis.StrictRedis(host='localhost',port=6379,db=0,decode_responses=True);
#r=redis.StrictRedis();
#r=redis.StrictRedis(host='localhost',6379,0);
@app.route('/')
def hello():
	Register="<a href='"+url_for('createUser')+"''>Register as a buyer or Seller</a>";
	Login="<a href='"+url_for('login')+"''>Login</a>";
	
	return """<html>
		<head>
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
		<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="#">Property-Price-Predictor</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="/createUser">Register</a>
      </li>
      <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="/" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          Dropdown
        </a>
        <div class="dropdown-menu" aria-labelledby="navbarDropdown">
          <a class="dropdown-item" href="/">Register</a>
          <a class="dropdown-item" href="/">Login</a>
          <div class="dropdown-divider"></div>
          <a class="dropdown-item" href="/">Something else here</a>
        </div>
      </li>
    </ul>
    <form class="form-inline my-2 my-lg-0">
      <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
      <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
    </form>
  </div>
</nav>

</div>
	<body>
<div class=" container ">
			<div class="jumbotron">
				<h1>Welcome To Property Price Predictor</h1>
			</div>
		</head>
	
		<div class="container"><h4>"""+Register+"""</h4></div>
		<div class="container"><h4>"""+Login+"""</h4></div>
</div>
<div class="card container" style="width: 18rem;">
  <div class="card-body">
    <h4 class="card-title">This is a Website for Buying and Selling property</h4>
    <h5 class="card-subtitle mb-2 text-muted">Property is the real game!</h5>
    <p class="card-text">This website is built by the efforts of the backend and frontend team of <strong>Rakshit and Agrim</strong> and the database team of <strong>Simran and Rohit</strong></p>
    <a href="/" class="card-link">Wanna know more?</a>

  </div>		
		</body>
			</html>"""
			
@app.route('/createUser',methods=['GET','POST'])
def createUser():
	if request.method=='GET':
		return render_template('createUser.html');
	elif request.method=='POST':
		firstname=request.form['firstname'];
		lastname=request.form['lastname'];
		city=request.form['city'];
		gender=request.form['gender'];
		usertype=request.form['usertype'];
		contact=request.form['contact'];
		aadhar=request.form['aadhar'];
		email=request.form['email'];
		password=request.form['password'];
		r.hset(aadhar,'aadhar',aadhar)
		r.hset(aadhar,'firstname',firstname)
		r.hset(aadhar,'lastname',lastname)
		r.hset(aadhar,'city',city)
		r.hset(aadhar,'gender',gender)
		r.hset(aadhar,'usertype',usertype)
		r.hset(aadhar,'contact',contact)
		r.hset(aadhar,'aadhar',aadhar)
		r.hset(aadhar,'email',email)
		r.hset(aadhar,'password',password)
		return render_template('createdUser.html',firstname=firstname,lastname=lastname,city=city,gender=gender,usertype=usertype,contact=contact,aadhar=aadhar,email=email,password=password);	
	

	else:
		return "<h2>Invalid input</h2>"




@app.route('/login',methods=['GET','POST'])
def login():
	if request.method=='GET':
		return render_template('login.html');
	elif request.method=='POST':
		aadhar=request.form['aadhar']
		email=request.form['email']
		password=request.form['password']
		yo=r.hget(aadhar,'password')
		if (password==yo):
			return render_template('loggedin.html');
		else:
			return "<h1>It seems your password is incorrect or aadhar is not registered</h1>"	
	else:
		return "<h2>Invalid input</h2>"


@app.route('/new/',methods=['GET','POST'])
def new():
	if request.method=='GET':
		return render_template('property.html')
	elif request.method=='POST':
		aadhar=request.form['aadhar'];
		pincode=request.form['pincode'];
		city=request.form['city'];
		street=request.form['street'];
		state=request.form['state'];
		sp=request.form['sp'];
		housetype=request.form['housetype'];
		registerydate=request.form['registerydate'];
		furni=request.form['furni'];
		r.hset(aadhar,'pincode',pincode)
		r.hset(aadhar,'street',street)
		r.hset(aadhar,'state',state)
		r.hset(aadhar,'sp',sp)
		r.hset(aadhar,'housetype',housetype)
		r.hset(aadhar,'registerydate',registerydate)
		r.hset(aadhar,'furni',furni)
		return render_template('pr.html')
	else:
		"<h2>Invalid input</h2>"

@app.route('/old',methods=['GET','POST'])
def old():
	if request.method=='GET':
		return render_template('enter.html')
	if request.method=='POST':
		aadhar=request.form['aadhar']
		r.hset(aadhar,'aadhar',aadhar)
		pincode=r.hget(aadhar,'pincode')
		firstname=r.hget(aadhar,'firstname')
		city=r.hget(aadhar,'city')
		street=r.hget(aadhar,'street')
		sp=r.hget(aadhar,'sp')
		registerydate=r.hget(aadhar,'registerydate')
		furni=r.hget(aadhar,'furni')
		password=request.form['password']
		if(password==r.hget(aadhar,'password')):
			return render_template('view.html',pincode=pincode,firstname=firstname,city=city,street=street,sp=sp,registerydate=registerydate,furni=furni)		
		else:
			return "<h1>You have entered wrong password</h1>"
@app.route('/home')
def home():
	return render_template('loggedin.html')

@app.route('/logout')
def logout():
	return render_template('logout.html')

@app.route('/delete',methods=['GET','POST'])
def delete():
	if request.method=='GET':
		return render_template('enter.html')
	elif request.method=='POST':
		aadhar=request.form['aadhar']
		password=request.form['password']
		if(password==r.hget(aadhar,'password')):
			r.hdel(aadhar,'firstname','lastname','city','aadhar','pincode','registerydate','street','sp','street','state','housetype','furni','gender','usertype','contact','email','password')
			return render_template('delete.html')
		else:
			return "<h1>You have entered a wrong password or You haven't registered</h1>"

@app.route('/search',methods=['GET','POST'])
def search():
	if request.method=='GET':
		return render_template('search.html')
	elif request.method=='POST':
		aadhar=request.form['aadhar']
		housetype=request.form['housetype']
		pincode=r.hget(aadhar,'pincode')
		firstname=r.hget(aadhar,'firstname')
		city=r.hget(aadhar,'city')
		street=r.hget(aadhar,'street')
		sp=r.hget(aadhar,'sp')
		registerydate=r.hget(aadhar,'registerydate')
		furni=r.hget(aadhar,'furni')
		return render_template('searched.html',pincode=pincode,firstname=firstname,city=city,street=street,sp=sp,registerydate=registerydate,furni=furni)


@app.route('/update',methods=['GET','POST'])
def update():
	if request.method=='GET':
		return render_template('createUser.html')
	elif request.method=='POST':
			firstname=request.form['firstname'];
			lastname=request.form['lastname'];
			city=request.form['city'];
			gender=request.form['gender'];
			usertype=request.form['usertype'];
			contact=request.form['contact'];
			aadhar=request.form['aadhar'];
			email=request.form['email'];
			password=request.form['password'];
			r.hset(aadhar,'aadhar',aadhar)
			r.hset(aadhar,'firstname',firstname)
			r.hset(aadhar,'lastname',lastname)
			r.hset(aadhar,'city',city)
			r.hset(aadhar,'gender',gender)
			r.hset(aadhar,'usertype',usertype)
			r.hset(aadhar,'contact',contact)
			r.hset(aadhar,'aadhar',aadhar)
			r.hset(aadhar,'email',email)
			r.hset(aadhar,'password',password)
			return render_template('createdUser.html',firstname=firstname,lastname=lastname,city=city,gender=gender,usertype=usertype,contact=contact,aadhar=aadhar,email=email,password=password);	
	else:
		return "<h2>Invalid input</h2>"

@app.route('/predict',methods=['GET','POST'])
def predict():
	if request.method=='GET':
		return render_template('predict.html')
	if request.method=='POST':
		city=request.form['city'];
		housetype=request.form['housetype'];
		furni=request.form['furni'];
		if(city=="MUMBAI" and housetype=="1BHK" and furni=="YES"):
			return "<h1>The price for your house is around 40Lakhs</h1>"
		elif(city=="MUMBAI" and housetype=="2BHK" and furni=="YES"):
			return "<h1>The price for your house is around  60Lakhs</h1>"
		elif(city=="MUMBAI" and housetype=="3BHK" and furni=="YES"):
			return "<h1>The price for your house is around 80Lakhs</h1>"	
		elif(city=="MUMBAI" and housetype=="4BHK" and furni=="YES"):
			return "<h1>The price for your house is around  1 Crore</h1>"		
		elif(city=="MUMBAI" and housetype=="5BHK" and furni=="YES"):
			return "<h1>The price for your house is around 2 Crore</h1>"
		elif(city=="MUMBAI" and housetype=="1BHK" and furni=="NO"):
			return "<h1>The price for your house is around 30Lakhs</h1>"		
		elif(city=="MUMBAI" and housetype=="2BHK" and furni=="NO"):
			return "<h1>The price for your house is around 50Lakhs</h1>"
		elif(city=="MUMBAI" and housetype=="3BHK" and furni=="NO"):
			return "<h1>The price for your house is around 70Lakhs</h1>"
		elif(city=="MUMBAI" and housetype=="4BHK" and furni=="NO"):
			return "<h1>The price for your house is around 90Lakhs</h1>"
		elif(city=="MUMBAI" and housetype=="5BHK" and furni=="NO"):
			return "<h1>The price for your house is around 1 crore 25Lakhs</h1>"
		elif(city=="MUMBAI" and housetype=="1BHK" and furni=="YES"):
			return "<h1>The price for your house is around 50Lakhs</h1>"
		elif(city=="DELHI" and housetype=="2BHK" and furni=="YES"):
			return "<h1>The price for your house is around 80Lakhs</h1>"
		elif(city=="DELHI" and housetype=="3BHK" and furni=="YES"):
			return "<h1>The price for your house is around 1 Crore</h1>"
		elif(city=="DELHI" and housetype=="4BHK" and furni=="YES"):
			return "<h1>The price for your house is around 1.3 Crores </h1>"
		elif(city=="DELHI" and housetype=="5BHK" and furni=="YES"):
			return "<h1>The price for your house is around 2.4 Crores</h1>"
		elif(city=="DELHI" and housetype=="1BHK" and furni=="NO"):
			return "<h1>The price for your house is around  40Lakhs</h1>"									
		elif(city=="DELHI" and housetype=="2BHK" and furni=="NO"):
			return "<h1>The price for your house is around 60Lakhs</h1>"
		elif(city=="DELHI" and housetype=="3BHK" and furni=="NO"):
			return "<h1>The price for your house is around 80Lakhs</h1>"		
		elif(city=="DELHI" and housetype=="4BHK" and furni=="NO"):
			return "<h1>The price for your house is around 1 Crore</h1>"	
		elif(city=="DELHI" and housetype=="5BHK" and furni=="NO"):
			return "<h1>The price for your house is around 1.5 Crores</h1>"	
