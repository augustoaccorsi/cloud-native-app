from flask import Flask

header_text = '''<html>\n<head> <title>Arquitetura de Software - Cloud Native App</title> </head>\n<body>'''
description = '''<p>Essa aplicação é uma demostração de uma Cloud Native Application</p>\n'''
group = '</body>Alunos: José Augusto Accorsi, Renato Dielle, Willian Keji e Dione Adam</html>'
professor = '</body>Professor: Kleinner Silva Farias de Oliveira</html>'

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return header_text + description + group, 200

@app.route("/professor", methods=['GET'])
def prof():
    return header_text + description + professor, 200

if __name__ == '__main__':
    app.run(debug=True)