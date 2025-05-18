from flask import Flask, request, render_template
from sappo_core.main import generate_response  # Pastikan file ini ada dan benar

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    response = ""
    if request.method == "POST":
        user_input = request.form.get("user_input", "")
        response = generate_response(user_input)
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

