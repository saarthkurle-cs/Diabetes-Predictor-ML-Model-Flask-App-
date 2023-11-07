from flask import *
import pickle

with open("diab.model", "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route("/")
def home():
	if request.args.get("fs") and request.args.get("fu"):
		fs = float(request.args.get("fs"))
		fu = request.args.get("fu")
		if fu == "no":
			d = [[fs, 1, 0]]
		else:
			d = [[fs, 0, 1]]
		ans = model.predict(d)
		res = ans[0]
		if res == "NO":
			msg = "You dont have diabetes but still take care"
		else:
			msg = "You might have diabetes. Please consult a doctor"
		return render_template("home.html", msg=msg)
	else:
		return render_template("home.html")

if __name__ == "__main__":
	app.run(debug=True, use_reloader=True)
