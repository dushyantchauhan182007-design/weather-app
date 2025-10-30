from flask import Flask, render_template, request, jsonify
import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__, template_folder="../frontend/templates", static_folder="../frontend/static")

# Get API key
API_KEY = os.getenv("API_KEY")



@app.route("/")
def home():
    """Render the main page."""
    return render_template("index.html")



@app.route("/weather", methods=["GET"])
def get_weather():
    """Return weather data as JSON for a given city."""
    city = request.args.get("city")

    if not city:
        return jsonify({"error": "City name is required"}), 400

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        return jsonify({"error": data.get("message", "City not found")}), response.status_code

    result = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"].title(),
        "icon": f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png"
    }

    return jsonify(result)


# ---------- RUN SERVER ----------
if __name__ == "__main__":
    app.run(debug=True)
