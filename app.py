from flask import Flask, render_template, request, jsonify
import your_ml_model_module

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        audio_file = request.files['audio']
        # Your code to preprocess the audio file and feed it to the model
        result = your_ml_model_module.predict(audio_file)
        return jsonify(result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)