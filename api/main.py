from flask import Flask, send_file, abort, request
import os

app = Flask(__name__)

PDF_FILE_PATH = os.path.abspath("pdfs/matematica_paginas_1_a_26.pdf")

print("Caminho absoluto do PDF:", PDF_FILE_PATH)

@app.route("/pdf")
def serve_pdf():
    try:
        return send_file(
            PDF_FILE_PATH,
            mimetype='application/pdf',
            as_attachment=False,
            download_name='matematica.pdf',
            conditional=True
        )
    except Exception as e:
        print("Erro ao servir PDF:", e)
        return abort(500)

if __name__ == "__main__":
    app.run(debug=True)