from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat")
def chat():
    return "<h2>AI Chatbot coming soon 🤖</h2>"

@app.route("/trend")
def trend():
    return "<h2>Market Trend Analyzer 📊</h2>"

@app.route("/idea")
def idea():
    return "<h2>AI Product Idea Generator 💡</h2>"

if __name__ == "__main__":
    app.run(debug=True)