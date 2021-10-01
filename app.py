from flask import Flask,request, jsonify
import pdfkit 
import base64
import os
import json
from waitress import serve

app = Flask(__name__)

@app.route('/pdf',methods=['POST' ])
def pdf_convertor():
    data = request.get_json()
    htmlstr = data.get('html', None)
    path_kit = r'/usr/local/bin/wkhtmltopdf'
    config = pdfkit.configuration(wkhtmltopdf=path_kit)
    pdfkit.from_string(htmlstr, 'sample.pdf',configuration=config) 
    data = open("sample.pdf", "rb").read()
    encoded = base64.b64encode(data)
    encoded = str(encoded)
    encoded= encoded[2:]
    encoded= encoded[:-1]
    if os.path.exists("sample.pdf"):
            os.remove("sample.pdf")
    return jsonify({'data':str(encoded)})

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)
    #app.run(host='0.0.0.0', port=5000,debug=True)