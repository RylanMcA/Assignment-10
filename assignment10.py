from flask import Flask, render_template, request
from random import randint, seed
app = Flask(__name__)

@app.route("/assignment10.html", methods=["GET","POST"])
def assignment10html():
	if request.method == "GET":
		return render_template("assignment10.html")

@app.route("/number.html", methods=["GET","POST"])
def random():
	if request.method == "GET":
		firstName = request.args.get("firstN")
		lastName = request.args.get("lastN")
		number = rand=randint(1,5)
		return render_template("random.html",first=firstName,last=lastName,rand=number)
	else:
		if(request.form["user"] == request.form["randNum"]):
			return render_template("right.html")
		else:
			userNumber = request.form["user"]
			number = request.form["randNum"]
			return render_template("wrong.html", uN=userNumber, rand=number)

if __name__ == "__main__":
	app.run(debug=True)
