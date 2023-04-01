import pickle
import pandas as pd
import Feature_extraction_new as feature



def predict_phishing(url):
    with open("model_svm_rbf.pkl", "rb") as f:
        model_svm_rbf = pickle.load(f)

    y_for_test = feature.get_data_set(url)
    val = y_for_test.fillna(0)
    pred = model_svm_rbf.predict(val)
    return pred


pred = predict_phishing("https://www.google.com")
print(pred[0])
