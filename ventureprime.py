from flask import Flask, render_template

app = Flask(__name__)

##############################
#	Home Page
##############################

@app.route('/')
def homepage():
    return render_template('homepage/index.html')

##############################
#	How VP Works 
##############################

@app.route('/howvpworks/')
def howvpworks():
    return render_template('howvpworks/overview.html')

@app.route('/howvpworks/<user_type>/<page>/')
def howvpworks_pages(user_type, page):
	template="howvpworks/%s/%s.html" % (user_type, page)
	return render_template(template)

##############################
#	User Accounts 
##############################

@app.route('/accounts/login/')
def login():
    return render_template('accounts/login.html')

@app.route('/accounts/home/')
def login_home():
    return render_template('accounts/login_home.html')

@app.route('/accounts/signup/')
def create_account():
    return render_template('accounts/create_account.html')

##############################
#	Venture Interface
##############################

@app.route('/accounts/venture/active_interviews/<page>/')
def active_interviews(page):
	template="venture_interface/active_interviews_%s.html" % (page)
	return render_template(template)

@app.route('/accounts/venture/add_interviews/<page>/')
def add_interviews(page):
	template="venture_interface/add_interviews_%s.html" % (page)
	return render_template(template)

@app.route('/accounts/venture/<page>/')
def venture_interface(page):
	template="venture_interface/%s.html" % (page)
	return render_template(template)

##############################
#	Primer Interface
##############################

@app.route('/accounts/primer/<page>/')
def primer_interface(page):
	template="primer_interface/%s.html" % (page)
	return render_template(template)




if __name__ == "__main__":
    app.run(debug=True)