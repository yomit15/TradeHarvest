from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def get_data_from_db(query):
    conn = sqlite3.connect("backend/database/crop_state_market.db")
    cursor = conn.cursor()
    cursor.execute(query)
    data = [row[0] for row in cursor.fetchall()]  # Fetch the first column of all rows
    conn.close()
    return data if data else []

@app.route('/api/get-dropdown-data', methods=['GET'])
def get_dropdown_data():
    commodities = get_data_from_db("SELECT DISTINCT commodity_name FROM commodities")
    states = get_data_from_db("SELECT DISTINCT state_name FROM states")
    markets = get_data_from_db("SELECT DISTINCT market_name FROM markets")

    return jsonify({
        "commodities": commodities,
        "states": states,
        "markets": markets
    })

if __name__ == '__main__':
    app.run(debug=True)
