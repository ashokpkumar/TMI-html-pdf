from flask import Flask,request, jsonify
app = Flask(__name__)

@app.route('/',methods=['POST' ])
def hello():
    import pdfkit 
    htmlstr = request.form["html"]
    print(htmlstr)
    pdfkit.from_string(htmlstr, 'sample.pdf') 
    #file = open("sample.pdf", "r")
    #data = file.read()
    #data = base64.encodebytes(data) 
    #pdfkit.from_url('https://www.google.com/','sample.pdf')
    #return jsonify({'data':data})
    return "Done"

if __name__ == '__main__':
    app.run(debug=True)