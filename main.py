from flask import Flask 
from flask import render_template
#submitted data will be stored in request object
from flask import request 
#__name__ refers to the name of the file
#to let the flask determine paths to template static files etc..
from block import write_block,check_integrity
app=Flask(__name__)


#route decorator
@app.route("/", methods=['POST','GET'])#sets index as handler of all requests to the root url address
#we pass the url address as string
#it means that all requests to the url address will be handled by index
#methods-list of http methods that the index function will handle
def index():
	#check whether the check request was pause request or not
	if request.method=='POST':
		holder = request.form.get('holder')
		amount = request.form.get('amount')
		type = request.form.get('type')
		write_block(holder=holder,amount=amount,type=type)
	return render_template('index.html')#returns index.html template

if __name__=='__main__':
	# flask will automatically restart the development server when the files of the project will be changed
	app.run(debug=True)

#handles requests to root url address, to the local host support number(?)
#such functions are called views
