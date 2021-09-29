from flask import Flask,request, jsonify
import pdfkit 
import base64
import os
import json
app = Flask(__name__)

# @app.route('/host',methods=['POST' ])
# def hello():
#     htmlstr = request.form["html"]
#     pdfkit.from_string(htmlstr, 'sample.pdf') 
#     file = open("sample.pdf", "r")
#     data = file.read()
#     data = base64.encodebytes(data) 
#     return jsonify({'data':data})


@app.route('/pdf',methods=['POST' ])
def pdf_convertor():
    data = request.get_json()
    htmlstr = data.get('html', None)
    #htmlstr = request.form["html"]
    #json.decoder
    # path_kit = r'/usr/local/bin/wkhtmltopdf'
    # config = pdfkit.configuration(wkhtmltopdf=path_kit)
    # pdfkit.from_string(htmlstr, 'sample.pdf',configuration=config) 

    pdfkit.from_string(htmlstr, 'sample.pdf')
    data = open("sample.pdf", "rb").read()
    encoded = base64.b64encode(data)
    if os.path.exists("sample.pdf"):
            os.remove("sample.pdf")
    return jsonify({'encoded':str(encoded),'data':str(data)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)