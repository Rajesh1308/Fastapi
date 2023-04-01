from fastapi import FastAPI, Path
import pickle
import Feature_extraction_new as feature


app = FastAPI()

with open("model_svm_rbf.pkl", "rb") as f:
    model_svm_rbf = pickle.load(f)

@app.get("/")
def home():
    a = 5
    return {"Data" : "Testing", "value" : a}


@app.get("/url-detect")
def get_item(url: str):

    y_for_test = feature.get_data_set(url)
    val = y_for_test.fillna(0)
    pred = model_svm_rbf.predict(val)
    print(pred)
    if pred[0] == 1:
        res = "Legitimate website"
    else:
        res = "Phished"

    return res