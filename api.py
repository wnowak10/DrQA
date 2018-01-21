from flask import Flask, session, request,  jsonify
from scripts.pipeline.interactive import process
from flask_cors import CORS
from urllib.parse import quote

app = Flask(__name__)
CORS(app)

@app.route('/drqa', methods=['GET']) #GET requests will be blocked
def drqa():
    respondent_id = request.args.get('id', default = 7606, type = int)
    query = request.args.get('query', default = "Why do you love Molly?", type = str)  
    urll = "http://molly.com/q?q="+quote(query,safe = '')+"&id="+str(respondent_id)
    output = process(query, urll)
    return jsonify(output)

if __name__ == '__main__':
    # Port 5000 opening in AWS
    app.run(host='0.0.0.0', port=5000)
