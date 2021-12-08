from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model_file = open('model1.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')


@app.route('/')
def index():
    return render_template('index.html', predict_case=0)


@app.route('/predict', methods=['POST'])
def predict():

    kddati2, tkp, peserta = [x for x in request.form.values()]

    data = []

    data.append(int(tkp))
    if tkp == 'Inap':
        data.extend([0, 1])
    else:
        data.extend([1, 0])

    prediction = model.predict([data])
    output = round(prediction[0], 2)

    return render_template('index.html', predict_case=output, kddati2=kddati2, tkp=tkp, peserta=peserta)


if __name__ == '__main__':
    app.run(debug=True)
