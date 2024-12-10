from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# Connexion à la base de données SQLite
def get_cycle_data(cycle_id):
    conn = sqlite3.connect('Predictions.db')  
    cursor = conn.cursor()
    query = "SELECT predictions, df_profile_ML FROM table_predication WHERE rowid = ?"
    cursor.execute(query, (cycle_id,))
    result = cursor.fetchone()
    conn.close()
    return result

# API pour récupérer les données du cycle
@app.route('/get_cycle_data', methods=['GET'])
def get_data():
    cycle_id = request.args.get('id', type=int)  # Récupère l'ID du cycle passé dans l'URL
    if cycle_id:
        data = get_cycle_data(cycle_id)
        if data:
            return jsonify({
                'id': cycle_id,
                'predicted_value': data[0],
                'actual_value': data[1]
            })
        else:
            return jsonify({'error': 'Cycle ID not found'}), 404
    else:
        return jsonify({'error': 'Invalid ID'}), 400

if __name__ == '__main__':
    app.run(debug=True)
