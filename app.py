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
		
		# print('Thsi is something', node_conn)
		
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
	f = open('datasets/nodes.json')
	data = json.load(f)
	if request.method == "POST":
		node_index = int(request.form["index-node"])
		node_id = request.form["nodeid"]
		node_desc = request.form["nodedesc"]
		node_grp = request.form["nodegrp"]
		conn_to = request.form.getlist("nodeconn")
		conn_to_node = request.form.getlist("nodeconn2")
		with open ("datasets/nodes.json") as json_file:
			data = json.load(json_file)

			#prev node id 
			prev_id = data['nodes'][node_index]['id']
			# print('this is prev id ', prev_id)
			# editing id desc and grp / new node id
			data['nodes'][node_index]['id'] = node_id
			# if we have to update node_id it has to be updated all over the file
			targets = []

			for i in range (len(data['nodes'][node_index]['links'])):
				targets.append(data['nodes'][node_index]['links'][i]['target'])
			flag = False			
			print("this is target here 1", targets)
			for i in range(len(targets)):
				flag = False
				print('i is ',i)
				for j in range(len(data['nodes'])):
					print('j is ', j)
					if flag:
						break
					if data['nodes'][j]['id'] == targets[i]:
						print('here i target is ',targets[i])
						for m in range(len(data['nodes'][j]['links'])):
							if data['nodes'][j]['links'][m]['target'] == prev_id:
								print('m is ', m, 'and ', data['nodes'][j]['links'][m], 'is target')
								data['nodes'][j]['links'][m]['target'] = node_id
								flag = True
								break
			for i in range(len(targets)):
				for j in range(len(data['links'])):
					if data['links'][j]['source'] == prev_id and data['links'][j]['target'] == targets[i]:
						data['links'][j]['source'] = node_id
					if data['links'][j]['source'] == targets[i] and data['links'][j]['target'] == prev_id:
						data['links'][j]['target'] = node_id


			data['nodes'][node_index]['description'] = node_desc
			data['nodes'][node_index]['group'] = node_grp

			temp3 = list(set(targets) - set(conn_to))
			# print('this si temp3' ,temp3)
			if len(temp3) != 0:
				# deleting link inside node_index  
				for i in range(len(temp3)):
					for j in range(len(data['nodes'][node_index]['links'])):
						if temp3[i] == data['nodes'][node_index]['links'][j]['target']:
							del data['nodes'][node_index]['links'][j]
							break
				# deleting link inside temp3 each node
				for i in range(len(temp3)):
					for j in range(len(data['nodes'])):
						if temp3[i] == data['nodes'][j]['id']:
							for k in range(len(data['nodes'][j]['links'])):
								if data['nodes'][j]['links'][k]['target'] == node_id:
									del data['nodes'][j]['links'][k]
									break
				# deleting link inside nodes.json
				count = 0
				for i in range(len(temp3)):
					# print('this is i ', i)
					for j in range(len(data['links'])):
						# print('this is j', j)
						if temp3[i] == data['links'][j]['source'] and node_id == data['links'][j]['target']:
							del data['links'][j]
							break
							count + 1
				if count != len(temp3):
					for k in range(len(temp3)):
						for l in range(len(data['links'])):
							# print('this is j2', l)
							if node_id == data['links'][l]['source'] and temp3[k] == data['links'][l]['target']:
								del data['links'][l]
								break		
			
			if conn_to_node != 0:
				for i in range(len(conn_to_node)):
					y = {"target": conn_to_node[i]}
					data['nodes'][node_index]['links'].append(y)

					k = {
						"source": node_id,
						"target": conn_to_node[i],
						"value": 1
					}
					data['links'].append(k)
					for j in range(len(data['nodes'])):
						if data['nodes'][j]['id'] == conn_to_node[i]:
							z = {"target": node_id}
							data['nodes'][j]['links'].append(z)
							break

		write_json(data)

	return redirect(url_for('index'))	

@app.route('/deletenode', methods=['GET','POST'])
def deletenode():


	return redirect(url_for('index'))	

@app.route('/datasets/<path:path>')   
def send_js(path):
    return send_from_directory('datasets', path)


if __name__ == "__main__":
	app.run(debug=True)