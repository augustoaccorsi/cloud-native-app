from flask import Flask,  render_template

header_text = '''<html>\n<head> <title>Arquitetura de Software - Cloud Native App</title> </head>\n<body>'''
description = '''<p>Essa aplicação é uma demostração de uma Cloud Native Application</p>\n'''
group = '</body>Alunos: José Augusto Accorsi, Renato Dielle, Willian Keji e Dione Adam</html>'
professor = '</body>Professor: Kleinner Silva Farias de Oliveira</html>'

app = Flask(__name__)

@app.route("/app/home", methods=['GET'])
def home():
    return header_text + description + group, 200

@app.route("/app/professor", methods=['GET'])
def prof():
    return header_text + description + professor, 200

@app.route("/app/teste", methods=['GET'])
def hello():
    return "Hello World ", 200

if __name__ == '__main__':
    app.run(debug=True)