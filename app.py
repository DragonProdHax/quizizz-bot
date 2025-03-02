import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from Quizizz import quizizzBot

app = Flask(__name__)

# Enable CORS for a specific domain (replace with your actual domain)
CORS(app, resources={r"/api/*": {"origins": "https://pxi-fusion.com"}})  

@app.route('/api/bot', methods=['POST'])
def create_bots():
    try:
        # Get data from the request body
        data = request.json

        # Extract game_pin, num_bots, and bot_names from the request, provide default values
        game_pin = data.get('game_pin')
        num_bots = data.get('num_bots', 3)  # Default to 3 bots if not specified
        bot_names = data.get('bot_names', [f'Bot{i+1}' for i in range(num_bots)])

        # Check if the game_pin was provided
        if not game_pin:
            return jsonify({'error': 'Missing game_pin'}), 400

        # Initialize the Quizizz bot with the given game pin
        quizz = quizizzBot(join_code=game_pin)

        # Start the bots using the mutiDummy method
        quizz.mutiDummy(num_processes=num_bots, NameList=bot_names, makeAutoExam=True)

        # Return a success response
        return jsonify({
            'message': 'Bots started successfully!',
            'game_pin': game_pin,
            'bot_names': bot_names
        })

    except KeyError as e:
        # Specific error for missing keys in the input
        return jsonify({'error': f'Missing key: {str(e)}'}), 400

    except Exception as e:
        # Generic error handling for other exceptions
        return jsonify({'error': f'Something went wrong: {str(e)}'}), 500

if __name__ == '__main__':
    # Get port from environment variable or default to 10000 (Render assigns the port)
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
