from flask import Flask, request
import yaml, json
import os
import uuid

app = Flask(__name__)

def json_to_yaml(tmp_json_file):
	"""
	Converts contents of json file to yaml, returns yaml
	"""
	f = open(tmp_json_file, 'r')
	json_obj = json.load(f)
	output = yaml.safe_dump(json_obj)
	return output

def convert_json_file(file):
	"""
	Convert one json file to yaml string
	"""
	tmp_json_file = str(uuid.uuid4())+".json" 
	file.save(tmp_json_file)
	responce = json_to_yaml(tmp_json_file)
	os.remove(tmp_json_file)
	return responce

@app.route('/convert', methods=['POST'])
def post():
	"""
	Got multiple json files and responce with yaml string
	"""
	responce = ''
	files = request.files.getlist('myfiles[]')
	for file in files:
		responce += convert_json_file(file)
	return responce

@app.route('/')
def main():
	"""
	Hello function
	"""
	return "Json to yaml converter!"

if __name__ == '__main__':
	app.run(debug=False, host='0.0.0.0', port=80)