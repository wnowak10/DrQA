# adapted from Head First Python, 2nd edition, by Paul Barry - chapter 10
# this is how a session variable allows you to pass values between pages 

from flask import Flask, session, request,  jsonify
from scripts.pipeline.interactive import process
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/drqa', methods=['GET']) #GET requests will be blocked
def drqa():
    # Send query with get request
#     req_data = request.get_json()
    respondent_id = request.args.get(id, default = 7606, type = int)
    query = request.args.get('query', default = "Why do you love Molly?", type = str)    
# Call drqa/scripts/pipeline/interactive which calls drqa/pipeline/drqa.py
	doc_url = "https://molly.com/q?q=how%20should%20we%20decide%20which%20features%20to%20build?&id="+respondent_id
    output = process(query, dox = doc_url)
#    output = process(req_data['query'], dox = "https://molly.com/q?q=how%20should%20we%20decide%20which%20features%20to%20build?&id=7606")
    return jsonify(output)

if __name__ == '__main__':
#    app.run(debug=True)
    # Port 5000 opening in AWS
    app.run(host='0.0.0.0', port=5000)

# curl -H "Content-Type: application/json" -X POST -d '{"query" : "How much did you sell Twitch for?", "dox" : "https://molly.com/q?q=how%20should%20we%20decide%20which%20features%20to%20build?&id=7606"}' http://127.0.0.1:5000/json-example
# curl -H "Content-Type: application/json" -X GET -d '{"query" : "How much did you sell Twitch for?"}' http://127.0.0.1:5000/drqa
