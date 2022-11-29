# import numpy as np
# import pandas as pd
# # import seaborn as sns
# import sklearn
# from sklearn.preprocessing import LabelEncoder
# from sklearn.preprocessing import OneHotEncoder
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
import sklearn
import streamlit as st
import pandas as pd 
import numpy as np 
import warnings
from sklearn.metrics import make_scorer, accuracy_score,precision_score
warnings.filterwarnings('ignore', category=UserWarning, append=True)

# data
df = pd.read_csv("https://raw.githubusercontent.com/08-Ahlaqul-Karimah/machine-Learning/main/mushrooms.csv")
df.head()

# normalisasi
# data yang dipakai 2000 data
# pemisahan class dan fitur
df=df[:2000]
from sklearn.preprocessing import OrdinalEncoder
x = df.drop(df[['class']],axis=1)
enc = OrdinalEncoder()
a = enc.fit_transform(x)
x=pd.DataFrame(a, columns=x.columns)

# class
y = df.loc[:, "class"]
y = df['class'].values

# Split Data
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=1)

st.set_page_config(page_title="Ima")
@st.cache()
def progress():
    with st.spinner("Bentar ya....."):
        time.sleep(1)
        
st.title("UAS PENDAT")

dataframe, preporcessing, modeling, implementation = st.tabs(
    ["Jamur Data", "Prepocessing", "Modeling", "Implementation"])

with dataframe:
    st.write('Data Jamur')
    dataset,data= st.tabs(['Dataset',"data"])
    with dataset:
        st.dataframe(df)

        
with preporcessing:
    st.write('Ordinal Encoder')
    st.dataframe(x)

with modeling:
    # pisahkan fitur dan label
    knn,naivebayes,decisiontree= st.tabs(
        ["K-Nearest Neighbor","naivebayes","decisiontree"])
    with knn:
      from sklearn.neighbors import KNeighborsClassifier
      knn = KNeighborsClassifier(n_neighbors=3)
      knn.fit(x_train,y_train)
      y_pred_knn = knn.predict(x_test) 
      accuracy_knn=round(accuracy_score(y_test,y_pred_knn)* 100, 2)
      acc_knn = round(knn.score(x_train, y_train) * 100, 2)
      label_knn = pd.DataFrame(
      data={'Label Test': y_test, 'Label Predict': y_pred_knn}).reset_index()
      st.success(f'Tingkat akurasi = {acc_knn}')
      st.dataframe(label_knn)

    with naivebayes:
        #Metrics
        from sklearn.metrics import make_scorer, accuracy_score,precision_score
        from sklearn.metrics import classification_report
        from sklearn.metrics import confusion_matrix
        from sklearn.metrics import accuracy_score ,precision_score,recall_score,f1_score

        #Model Select
        from sklearn.model_selection import KFold,train_test_split,cross_val_score
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.model_selection import train_test_split
        from sklearn.linear_model import  LogisticRegression
        from sklearn.ensemble import RandomForestClassifier
        from sklearn import linear_model
        from sklearn.linear_model import SGDClassifier
        from sklearn.tree import DecisionTreeClassifier
        from sklearn.neighbors import KNeighborsClassifier
        from sklearn.svm import SVC, LinearSVC
        from sklearn.naive_bayes import GaussianNB
        from sklearn.preprocessing import LabelEncoder
        le = LabelEncoder()
        y = le.fit_transform(y)
        gaussian = GaussianNB()
        gaussian.fit(x_train, y_train)
        y_pred = gaussian.predict(x_test) 
        accuracy_nb=round(accuracy_score(y_test,y_pred)* 100, 2)
        acc_gaussian = round(gaussian.score(x_train, y_train) * 100, 2)

        cm = confusion_matrix(y_test, y_pred)
        accuracy = accuracy_score(y_test,y_pred)
        precision =precision_score(y_test, y_pred,average='micro')
        recall =  recall_score(y_test, y_pred,average='micro')
        f1 = f1_score(y_test,y_pred,average='micro')
        print('Confusion matrix for Naive Bayes\n',cm)
        print('accuracy_Naive Bayes: %.3f' %accuracy)
        print('precision_Naive Bayes: %.3f' %precision)
        print('recall_Naive Bayes: %.3f' %recall)
        print('f1-score_Naive Bayes : %.3f' %f1)
        st.success(accuracy)
        label_nb = pd.DataFrame(
        data={'Label Test': y_test, 'Label Predict': y_pred})
        label_nb
        
        
    with decisiontree:
        from sklearn.tree import DecisionTreeClassifier
        d3 = DecisionTreeClassifier()
        d3.fit(x_train, y_train)
        y_predic = d3.predict(x_test)
        data_predic = pd.concat([pd.DataFrame(y_test).reset_index(drop=True), pd.DataFrame(y_predic, columns=["Predict"]).reset_index(drop=True)], axis=1)        
        from sklearn.metrics import accuracy_score
        a=f'acuraty = {"{:,.2f}".format(accuracy_score(y_test, y_predic)*100)}%'
        st.success(a)
        data_predic
        
with implementation:
      df=df[:2000]
      from sklearn.preprocessing import OrdinalEncoder
      x = df.drop(df[['class']],axis=1)
      enc = OrdinalEncoder()
      a = enc.fit_transform(x)
      x=pd.DataFrame(a, columns=x.columns)
          cap-shape=st.text_input('cap-shape')
          cap-surface=st.text_input('cap-surface')
          cap-color=st.text_input('cap-color')
          bruises=st.text_input('bruises')
          odor=st.text_input('odor')
          gill-attachment=st.text_input('gill-attachment')
          gill-spacing=st.text_input('gill-spacing')
          gill-size=st.text_input('gill-size')
          gill-color=st.text_input('gill-color')
#       x_new = ['x','y','y','t','l','f','c','b','g','e','c','s','s','w','w','p','w','o','p','k','s','m'] # hasil=0/e
      x_new = ["x","s","w","t","p","f","c","n","k","e","e","s","s","w","w","p","w","o","p","k","v","g"] # hasil=1/p
      hinput=enc.transform(np.array([x_new]))
      hinput
      from sklearn.neighbors import KNeighborsClassifier
      knn = KNeighborsClassifier(n_neighbors=3)
      knn.fit(x_train,y_train)
      Y_pred = knn.predict(x_test) 
      accuracy_knn=round(accuracy_score(y_test,Y_pred)* 100, 2)
      acc_knn = round(knn.score(x_train, y_train) * 100, 2)
      accuracy_knn
      acc_knn
      y_predict = knn.predict(hinput)
      st.write("Hasil prediksi adalah",y_predict[0])
      # return y_predict[0]









# # KNN
# from sklearn.neighbors import KNeighborsClassifier
# knn = KNeighborsClassifier(n_neighbors=3)
# knn.fit(x_train,y_train)

# # Akurasi
# Y_pred = knn.predict(x_test) 
# accuracy_knn=round(accuracy_score(y_test,Y_pred)* 100, 2)
# acc_knn = round(knn.score(x_train, y_train) * 100, 2)
# accuracy_knn
# acc_knn

# x_new = ['x','y','y','t','l','f','c','b','g','e','c','s','s','w','w','p','w','o','p','k','s','m'] # hasil=0/e
# # x_new = ["x","s","w","t","p","f","c","n","k","e","e","s","s","w","w","p","w","o","p","k","v","g"] # hasil=1/p
# hinput=enc.transform(np.array([x_new]))
# hinput

# def KNN(x_new):
#       from sklearn.neighbors import KNeighborsClassifier
#       knn = KNeighborsClassifier(n_neighbors=3)
#       knn.fit(x_train,y_train)
#       Y_pred = knn.predict(x_test) 
#       accuracy_knn=round(accuracy_score(y_test,Y_pred)* 100, 2)
#       acc_knn = round(knn.score(x_train, y_train) * 100, 2)
#       accuracy_knn
#       acc_knn
#       y_predict = knn.predict(x_new)
#       print(y_predict[0])
#       return y_predict[0]
# KNN(hinput)
