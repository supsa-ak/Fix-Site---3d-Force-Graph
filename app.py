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
	f = open('datasets/nodes.json')
	data = json.load(f)
	list1 = data['nodes']
	list2 = []
	for i in range(len(list1)):
		list2.append(list1[i]['id'])
	return render_template('index.html', list2=json.dumps(list2))

@app.route('/createnewnode', methods=['GET','POST'])
def createnewnode():
	f = open('datasets/nodes.json')
	data = json.load(f)
	if request.method == "POST":
		node_id = request.form["nodeid"]
		node_desc = request.form["nodedesc"]
		node_grp = request.form["nodegrp"]
		node_conn = request.form.getlist("nodeconn2")
		node_no = len(node_conn)
		
		print('Thsi is something', node_conn)
		
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
						
					]
				}
			temp.append(y)

			temp = data["nodes"]
			temp_no = len(temp) - 1
			semp = data["nodes"][temp_no]["links"]
			for i in range(node_no):
				z = {"target": node_conn[i]}
				semp.append(z)
				
			temp2  = data["links"]
			no2 = len(temp2)
			for i in range(node_no):
				k = {
						"source": node_id,
						"target": node_conn[i],
						"value": 1
					}
				temp2.append(k)

			for i in range(node_no):
				for j in temp:
					if j["id"] == node_conn[i]:
						p = {"target": node_id}
						j["links"].append(p)
						break

		write_json(data)
	# print(data)
	return redirect(url_for('index'))	


@app.route('/updatenode', methods=['GET','POST'])
def updatenode():

	
	return redirect(url_for('index'))	

@app.route('/datasets/<path:path>')
def send_js(path):
    return send_from_directory('datasets', path)


if __name__ == "__main__":
	app.run(debug=True)