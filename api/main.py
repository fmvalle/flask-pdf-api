import os
from flask import Flask, send_file, abort

app = Flask(__name__)

@app.route("/pdf")
def serve_pdf():
    try:
        # Caminho seguro baseado no local do arquivo
        base_dir = os.path.dirname(os.path.abspath(__file__))
        pdf_path = os.path.join(base_dir, '..', 'pdfs', 'matematica_paginas_1_a_26.pdf')

        return send_file(
            pdf_path,
            mimetype='application/pdf',
            as_attachment=False,
            download_name='matematica.pdf'
        )
    except Exception as e:
        print("Erro ao servir PDF:", e)
        return abort(500)
