from flask import Flask,request,render_template
import pickle
import Feature_extraction_new as feature

app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/url-detect")
def url_detect():
     url = request.args.get("url")
     with open("model_svm_rbf.pkl", "rb") as f:
        model_svm_rbf = pickle.load(f)

     y_for_test = feature.get_data_set(url)
     val = y_for_test.fillna(0)
     pred = model_svm_rbf.predict(val)
     print(pred)
     if pred[0] == 1:
         res = "Legitimate website"
     else:
         res = "Phished"

     return res

if __name__ == "__main__":
    app.run()