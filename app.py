from flask import Flask, escape, request, render_template, jsonify, send_from_directory, url_for, redirect
import urllib.request
import json 


app = Flask(__name__)

def write_json(data, filename="datasets/nodes.json"):
	with open(filename, "w") as f:
		json.dump(data, f, indent=4)

@app.route('/')
def index():
	print("_______INDEX___________")

	return render_template('index.html')

@app.route('/updatejson', methods=['GET','POST'])
def updatejson():
	f = open('datasets/nodes.json')
	data = json.load(f)
	if request.method == "POST":
		node_id = request.form["nodeid"]
		node_desc = request.form["nodedesc"]
		node_grp = request.form["nodegrp"]
		node_conn = request.form["nodeconn"]
		# print(node_id)
		
		with open ("datasets/nodes.json") as json_file:
			data = json.load(json_file)
			temp = data["nodes"]
			no = len(temp)
			# print('this is no', no)
			y = {
					"id": node_id,
					"group": node_grp,
					"description": node_desc, 
					"val": 20, 
					"links":[
						{"target": node_conn}
					]
				}
			temp.append(y)

			temp2  = data["links"]
			no2 = len(temp2)
			k = {
					"source": node_id,
					"target": node_conn,
					"value": 1
				}
			temp2.append(k)

		write_json(data)
	# print(data)
	return redirect(url_for('index'))	


@app.route('/datasets/<path:path>')
def send_js(path):
    return send_from_directory('datasets', path)


if __name__ == "__main__":
	app.run(debug=True)