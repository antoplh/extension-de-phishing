# importar dependencias
from varsRF import armarVecRF
from varsCNN import armarVecCNN
from keras.models import load_model
import pickle
import numpy as np
import xgboost
#!pip install sklearn
#!pip install keras
#!pip install tensorflow --user
#!pip install pandas
#!pip install english-words

def minmax_norm(vector):
    mi=min(vector)
    ma=max(vector)
    print(mi,ma)
    for i in range(len(vector)):
        vector[i]=(vector[i]-mi)/(ma-mi)
    return vector
def Prediccion(url):
    # obtener variables
    cnn_vars = minmax_norm(armarVecCNN(url))
    rf_vars = armarVecRF(url)

    # cargar modelos
    cnn_model = load_model("cnn_11.h5")
    rf_model = pickle.load(open("random_forest_11.sav", 'rb'))

    # predecir para cnn
    cnn_vars = np.array(cnn_vars).reshape(96,1)
    cnn_vars = np.array([cnn_vars,])
    CNNproba = [cnn_model.predict(cnn_vars)[0][1],cnn_model.predict(cnn_vars)[0][0]]
    print("CNN RESULT")
    print(CNNproba)

    # predecir para random forest
    RFproba = rf_model.predict_proba([rf_vars])
    print("RF RESULT")
    print(RFproba)
    # predecir para XGBOOST
    #XGBproba = xgb_model.predict_proba([rf_vars])
    print("XGB RESULT")
    #print(XGBproba)

    # predecir para modelo hibrido
    pesos = [0.11094813,0.40562288]#,0.483429]
    yhats = [RFproba, CNNproba]#, XGBproba]
    summed = np.tensordot(yhats, pesos, axes=((0),(0)))
    result = np.argmax(summed, axis=1)
    print(result)
    probabilidad_ph = round(summed[0][1]*100,2)
    print(probabilidad_ph)

    if result[0] == 1:
        return "phishing"#,probabilidad_ph
    else:
        return "legitima"#,probabilidad_ph
url = "https://www.google.com/search?q=visual+studio+code+shortcut+for+run&rlz=1C1CHBF_esPE917PE917&oq=visual+studio+code+shortcut+for+run&aqs=chrome..69i57j0i19i22i30l6.11953j0j7&sourceid=chrome&ie=UTF-8"
print(url)
# obtener variables
cnn_vars = minmax_norm(armarVecCNN(url))
rf_vars = armarVecRF(url)

# cargar modelos
cnn_model = load_model("cnn_11.h5")
rf_model = pickle.load(open("random_forest_11.sav", 'rb'))

# predecir para cnn
cnn_vars = np.array(cnn_vars).reshape(96,1)
cnn_vars = np.array([cnn_vars,])
CNNproba = [cnn_model.predict(cnn_vars)[0][1],cnn_model.predict(cnn_vars)[0][0]]
print("CNN RESULT")
print(CNNproba)

# predecir para random forest
RFproba = rf_model.predict_proba([rf_vars])
print("RF RESULT")
print(RFproba)
# predecir para XGBOOST
#XGBproba = xgb_model.predict_proba([rf_vars])
print("XGB RESULT")
#print(XGBproba)

# predecir para modelo hibrido
pesos = [0.11094813,0.40562288]#,0.483429]
yhats = [RFproba, CNNproba]#, XGBproba]
summed = np.tensordot(yhats, pesos, axes=((0),(0)))
result = np.argmax(summed, axis=1)
print(result)
probabilidad_ph = round(summed[0][1]*100,2)
print(probabilidad_ph)

if result[0] == 1:
    print("phishing")#,probabilidad_ph
else:
    print("legitima")#,probabilidad_ph