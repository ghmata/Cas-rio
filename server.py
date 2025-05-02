from flask import Flask, request, jsonify
import yagmail

app = Flask(__name__)

# Configuração do e-mail
EMAIL = "gabrielhm00@gmail.com"
SENHA = "ztqc mbdg vpph rdwu"
yag = yagmail.SMTP(EMAIL, SENHA)

@app.route('/enviar-email', methods=['POST'])
def enviar_email():
    try:
        # Coleta os dados do formulário enviados pelo site
        dados = request.json
        nome = dados.get('nome')
        telefone = dados.get('telefone')
        acompanhantes_adultos = dados.get('Acp - Adulto', 0)  # Atualizado para refletir o nome da coluna
        acompanhantes_criancas = dados.get('Acp - Criança', 0)  # Atualizado para refletir o nome da coluna
        confirmacao = dados.get('presenca')
        email_usuario = dados.get('email')  # Supondo que o e-mail do usuário seja incluído

        # Monta o corpo do e-mail
        assunto = "Confirmação de Presença"
        corpo = f"""
        Olá {nome},

        Obrigado por confirmar sua presença no nosso evento!
        Detalhes:
        - Telefone: {telefone}
        - Acompanhantes adultos: {acompanhantes_adultos}
        - Acompanhantes crianças: {acompanhantes_criancas}
        - Confirmação: {confirmacao}

        Estamos ansiosos para recebê-lo!

        Gabriel & Isabella
        """

        # Envia o e-mail
        yag.send(
            to=email_usuario,
            subject=assunto,
            contents=corpo
        )

        return jsonify({"status": "success", "message": "E-mail enviado com sucesso!"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)