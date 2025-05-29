import os
from flask import Flask, Response, abort, request

app = Flask(__name__)

VALID_TOKEN = "p0o9i8U&"

@app.route("/pdf")
def serve_pdf():
    auth_header = request.headers.get("Authorization")

    if not auth_header or not auth_header.startswith("Bearer "):
        return abort(401, description="Token de autenticação ausente")

    token = auth_header.split("Bearer ")[1]

    if token != VALID_TOKEN:
        return abort(403, description="Token inválido")

    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        pdf_path = os.path.join(base_dir, '..', 'pdfs', 'matematica_paginas_1_a_26.pdf')
        with open(pdf_path, 'rb') as f:
            content = f.read()
        return Response(
            content,
            mimetype='application/pdf',
            headers={
                'Content-Disposition': 'inline; filename="hidden.pdf"',
                'X-Content-Type-Options': 'nosniff',
                'Cache-Control': 'no-store',
                'Pragma': 'no-cache'
            }
        )
    except Exception as e:
        print("Erro ao servir PDF:", e)
        return abort(500)
