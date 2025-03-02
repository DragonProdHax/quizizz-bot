import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from Quizizz import quizizzBot

app = Flask(__name__)
CORS(app)  # Enable CORS for all origins

@app.route('/api/bot', methods=['POST'])
def create_bots():
    try:
        data = request.json

        game_pin = data.get('game_pin')
        num_bots = data.get('num_bots', 3)
        bot_names = data.get('bot_names', [f'Bot{i+1}' for i in range(num_bots)])

        if not game_pin:
            return jsonify({'error': 'Missing game_pin'}), 400

        quizz = quizizzBot(join_code=game_pin)
        quizz.mutiDummy(num_processes=num_bots, NameList=bot_names, makeAutoExam=True)

        return jsonify({'message': 'Bots started successfully!', 'game_pin': game_pin, 'bot_names': bot_names})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Use Render's assigned port
    app.run(host='0.0.0.0', port=port)
