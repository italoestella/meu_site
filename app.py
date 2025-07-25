import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    print(f"Rodando na porta: {port}")
    app.run(host="0.0.0.0", port=port, debug=True)

