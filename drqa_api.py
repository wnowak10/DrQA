# adapted from Head First Python, 2nd edition, by Paul Barry - chapter 10
# this is how a session variable allows you to pass values between pages 

from flask import Flask, session, request,  jsonify
from scripts.pipeline.interactive import process
from flask_cors import CORS
from urllib.parse import quote
from flask.ext.reqarg import request_args


# adapted from Head First Python, 2nd edition, by Paul Barry - chapter 10
# this is how a session variable allows you to pass values between pages 

from flask import Flask, session, request,  jsonify
# from scripts.pipeline.interactive import process
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/drqa', methods=['GET']) #GET requests will be blocked
def drqa():
	respondent_id = request.args.get('id', default = 7606, type = int)
	query = request.args.get('query', default = "Why do you love Molly?", type = str)  
	print(str(respondent_id))  
	urll = "http://molly.com/q?q="+query+"&id="+str(respondent_id)
	print(urll)
	print(type(urll))
	print(type('hi'))
	output = process(query, urll)
	return jsonify(output)

if __name__ == '__main__':
#    app.run(debug=True)
    # Port 5000 opening in AWS
    app.run(host='0.0.0.0', port=5000)



# app = Flask(__name__)
# CORS(app)


# @app.route('/drqa', methods=['GET']) #GET requests will be blocked
# # @request_args
# # def drqa(did, query):
# def drqa():
# 	respondent_id = request.args.get('id') #, default = 7606, type = int)
# 	query = request.args.get('query') #, default = "Why do you love Molly?", type = str)  
# 	print(str(respondent_id))  
# 	url = "molly.com/q?q="+query+"&id="+str(respondent_id)
# 	print(url)
# 	return jsonify(url)

# if __name__ == '__main__':
# #    app.run(debug=True)
#     # Port 5000 opening in AWS
#     app.run(host='0.0.0.0', port=5000)

	# print(did)
	# print(query)
	# summary  = request.args.get('summary', None)
	# change  = request.args.get('change', None)
	# print(summary)
	# # did = request.args['did']
	# did = request.args.get('id' , type = int, default = 7606)

	# print(str(did))
	# print(did)
	# respondent_id = request.form['id'] #.get('id' , type = int) # default = 7606,


	# print(str(resp_id) + 'why?')
	# query = request.args['query']
	# .get('query', default = "How should we decide which features to build?", type = str)  

	# query = request.form.get('query', default = "How should we decide which features to build?", type = str)  
	# query, resp_id = request.args.get('query','resp_id')
	# print(query)  
	# print(resp_id)
	# Call drqa/scripts/pipeline/interactive which calls drqa/pipeline/drqa.py
	# idd = str(id)
	# url = "https://molly.com/q?q="+quote(query,safe = '')+"&id="+str(did)
	# print(request.args)
	# bar = request.args.get('qid')
	# all_args = request.args.get('qid', type = str)

	# output = process(query, dox = doc_url)
	# print(doc_url)
	# return did 
	# return jsonify(1)

# if __name__ == '__main__':
# #    app.run(debug=True)
#     # Port 5000 opening in AWS
#     app.run(host='0.0.0.0', port=5000)


# curl http://34.238.125.26:5000/drqa?query=what is your name??query=7606
# curl http://0.0.0.0:5000/drqa?query=who%20are%20we%20you%20which%20features%20to%20build?query=7606