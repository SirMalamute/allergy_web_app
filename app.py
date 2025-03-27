from flask import Flask, render_template, abort, jsonify
import os
import json

app = Flask(__name__)

# Path to the folder containing JSON files
JSON_FOLDER = "JSON"

# Ensure the folder exists
os.makedirs(JSON_FOLDER, exist_ok=True)

@app.route("/<restaurant_name>")
def restaurant_page(restaurant_name):
    file_path = os.path.join(JSON_FOLDER, f"{restaurant_name}.json")
    if not os.path.exists(file_path):
        abort(404, description="Restaurant not found")

    # Load restaurant data from JSON
    with open(file_path, "r") as file:
        restaurant_data = json.load(file)

    if not isinstance(restaurant_data, dict) or "items" not in restaurant_data:
        abort(400, description="Invalid restaurant data")
        
    print(restaurant_data)  # Log the data being passed to React

    return render_template("restaurant.html", data=restaurant_data)

if __name__ == "__main__":
    app.run(debug=True)
