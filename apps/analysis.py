from sklearn.preprocessing import StandardScaler
import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn import preprocessing
def app():
    def explore(data):
        df_types = pd.DataFrame(data.dtypes, columns=['Data Type'])
        return df_types.astype(str)

    def viewState(data):
        states=df.State.unique()
        return states.astype(str)

    def describeData(data):
        describe=df.describe()
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.title("Question 3")
    with st.sidebar:
        st.info("Please Select Which Analysis To View")
        selectionRadio = st.radio(
            "Choose Analysis",
            ("Description of Dataset", "Cluster Analysis","Classification","Recommendation And Conclusion"),index=0
        )
        if selectionRadio=="Classification":
            classificationChoice=st.selectbox(
                "Please Select Which Classification to View",
                ("SVC","Random Forest")
            )

    df = pd.read_csv('Bank_CreditScoring.csv')
    if(selectionRadio=="Description of Dataset"):
        st.subheader(selectionRadio)
        st.write("Information of the original dataset")
        info=explore(df)
        st.write(info)
        st.write("We replace the state information for some rows that have inconsistent value")
        state=viewState(df)
        st.write(state)
        replacement_mapping_dict = {
            "Johor B": "Johor",
            "P.Pinang": "Penang",
            "Pulau Penang": "Penang",
            "K.L": "Kuala Lumpur",
            "N.Sembilan": "Negeri Sembilan",
            "N.S": "Negeri Sembilan",
            "SWK": "Sarawak",
            "Trengganu": "Terengganu"
        }
        df["State"].replace(replacement_mapping_dict, inplace=True)
        state=viewState(df)
        st.write("After Replacement")
        st.write(state)
        st.write("The following is the description of the dataset")
        st.write(df.describe())
        st.write("We will be using decision as our class for classification. Before going into classification let's check how may unique value are in the decision")
        decisionunique=df.Decision.value_counts()
        st.write(decisionunique)
        st.write("We then encode the categorical columns before sending it for clustering and classification")
        category_col =['Employment_Type', 'More_Than_One_Products', 'Property_Type', 'State','Decision']  
        labelEncoder = preprocessing.LabelEncoder() 
        
        mapping_dict ={} 
        for col in category_col: 
            df[col] = labelEncoder.fit_transform(df[col]) 
        
            le_name_mapping = dict(zip(labelEncoder.classes_, 
                                labelEncoder.transform(labelEncoder.classes_))) 
        
            mapping_dict[col]= le_name_mapping 
        st.write("Encoded columns and its value")
        st.write(mapping_dict)
        corr = df.corr()
        st.write("Below is the pearson's correlation for all the columns")
        fig=sns.set(rc={'figure.figsize':(40,9)})
        sns.heatmap(corr,linewidths=.5, annot=True, cmap="YlGnBu",mask=np.triu(np.ones_like(corr, dtype=bool)))\
            .set_title("Pearson Correlations Heatmap")

        st.pyplot(fig)

    elif(selectionRadio=='Cluster Analysis'):
        st.subheader('Cluster Analysis : K-Means Cluster Analysis')
        st.write("Step 1: Find the optimal number of clusters for k-means")
        st.write('There are 2 ways to find optimal number of clusers:')
        st.write('a) Elbow Method')  
        st.write('b) Silhouette Coefficients')
        st.write('Elbow Method:')
        sse=pd.read_csv('elbow.csv', squeeze=True,header=None, skiprows=1)
        sse = sse.drop(sse.columns[0], axis=1)
        sse = sse.values.tolist()
        fig1 = plt.figure(figsize = (10, 5))
        plt.plot(range(2,12), sse, marker='o')
        plt.xlabel('Number of clusters')
        plt.ylabel('Distortion')
        plt.title('Elbow Method For Optimal K')
        st.pyplot(fig1)
        st.write('Based on the Elbow Method the optimal value for k is 4')
        st.write('Silhouette Coefficients:')
        fig2 = plt.figure(figsize = (10, 5))
        silhouette_coefficients=pd.read_csv('silhouette.csv')
        plt.plot(range(2,12), sse, marker='o')
        plt.xlabel("Number of Clusters")
        plt.ylabel("Silhouette Coefficient")
        plt.title('Silhouette Coefficients For Optimal K')
        st.pyplot(fig2)
        st.write("We explore Elbow Method and Silhouette Coefficients to find the optimal number of clusters for KMeans Clustering. However, we decide to use number of clusters from elbow method (k=4) because the Silhouette Coefficients are low. By right, +1 means clusters are clearly distinguished, 0 means clusters are neutral in nature and can not be distinguished properly, and -1 means the clusters are assigned in the wrong way. Based on the graph, The highest Silhouette Coefficient is found to be approximately 0.425 only when number of clusters is 2. The value 0.425 is quite low and it means that the clusters are somewhat not distinguishable.")
        st.write("Exploring through all possible graphs for K-Means Clusers, we used Total Sum of Loan vs Loan Amount to illustrate the 4 distinct groups")
        df_clustered =pd.read_csv('cluster.csv')
        fig3, ax = plt.subplots(figsize=(10, 10))
        sns.scatterplot(data=df_clustered, x="Total_Sum_of_Loan", y="Loan_Amount", hue = "Cluster", ax=ax)
        ax.set_title("Total Sum of Loan vs Loan Amount")
        st.pyplot(fig3)
        st.write("As shown in the Figure above, there are 4 clusters represented by the label 0,1,2 and 3. They can be described as \"low loan amount applied for, low total sum lof loan payable\", \"low loan amount applied for, high total sum lof loan payable\", \"high loan amount applied for, low total sum lof loan payable\" and \"high loan amount applied for, high total sum lof loan payable\".")
    elif(selectionRadio=='Classification' and classificationChoice=='SVC'):
        st.subheader("Classification Type : SVC")
        st.write("Step 1: We prepare the dataset into 2 parts Train and Test")
        st.write("Step 2: We test the accuracy of default parameters")
        st.write("The Accuracy is 0.7531914893617021")
        st.write("Step 3: We find the best hyperparameters using gridsearch")
        svcParam = {'kernel': 'sigmoid', 'C': 0.1}
        st.write("The best hyperparamaters found are :")
        st.write(svcParam)
        st.write("Tuned hyperparameters Accuracy Score is 0.7553191489361702")
        st.write("There is a slight improvement from default hyperparameters so we use the tuned hyperparameters")
        st.write("Step 4: Check the confusion matrix")
        ypred = genfromtxt('ypred1.csv', delimiter=',')
        y_test=pd.read_csv('y_test1.csv', squeeze=True,header=None)
        cf_matrix = confusion_matrix(y_test, ypred)
        st.write(cf_matrix)
        fig1 = plt.figure(figsize = (10, 5))
        ax = sns.heatmap( cf_matrix , linewidth = 0.5 , cmap = 'coolwarm')
        plt.title( "2-D Heat Map" )
        plt.show()
        st.pyplot(fig1)
        st.write("The data is imbalanced so we use different evaluation metrics")
        df=[["Accuracy Score",0.7553191489361702],["ROC Score",0.5470177587262708],["Precision Score",0.7553191489361702],["F1 Score",0.8606060606060607]]
        st.table(df)
        
    elif(selectionRadio=='Classification' and classificationChoice=='Random Forest'):
        st.write("Classification Type : Random Forest")
        st.write("Step 1: We prepare the dataset into 2 parts Train and Test")
        st.write("Step 2: We test the accuracy of default parameters")
        st.write("The Accuracy is 0.7489361702127659")
        st.write("Step 3: We find the best hyperparameters using Random Search as there is too many possible combinations we narrow it down to 100")
        randomForestParam = {'n_estimators': 1200,
                            'min_samples_split': 10,
                            'min_samples_leaf': 4,
                            'max_features': 'sqrt',
                            'max_depth': 60,
                            'criterion': 'gini',
                            'bootstrap': True}
        st.write("The best hyperparamaters found are :")
        st.write(randomForestParam)
        st.write("Tuned hyperparameters Accuracy Score is 0.7553191489361702")
        st.write("Step 4:Run again Random Search with smaller domain and random 100 hyperparameters combination")
        randomForestParam2 = {'n_estimators': 1000,
                            'min_samples_split': 5,
                            'min_samples_leaf': 2,
                            'max_features': 'auto',
                            'max_depth': 50,
                            'criterion': 'gini',
                            'bootstrap': True}
        st.write("The best hyperparamaters found are :")
        st.write(randomForestParam2)
        st.write("Tuned hyperparameters Accuracy Score is 0.7531914893617021")
        st.write("Step 4: Check the confusion matrix")
        ypred = genfromtxt('ypred2.csv', delimiter=',')
        y_test=pd.read_csv('y_test2.csv', squeeze=True,header=None)
        cf_matrix = confusion_matrix(y_test, ypred)
        st.write(cf_matrix)
        fig1 = plt.figure(figsize = (10, 5))
        ax = sns.heatmap( cf_matrix , linewidth = 0.5 , cmap = 'coolwarm')
        plt.title( "2-D Heat Map" )
        plt.show()
        st.pyplot(fig1)
        st.write("The data is imbalanced so we use different evaluation metrics")
        df=[["Accuracy Score",0.7531914893617021],["ROC Score",0.5471647274954072],["Precision Score",0.7547974413646056],["F1 Score",0.8592233009708737]]
        st.table(df)

    elif(selectionRadio=='Recommendation And Conclusion'):
        st.subheader(selectionRadio)
        st.write('As requested for this project, the metric used is accuracy which might not be suitable because of data imbalanced. The target variable "Decision" has two values "Accept" and "Reject", where number of occurences of "Accept" is significantly more than "Reject". As such, metrics such as F1 or AUC should be considered instead. Besides, k-fold cross-validation should be used because every subset of data will have its turn of being chosen as test set. The mean score of the metric will give us a more accurate out-of-sample accuracy.')
        st.write('The accuracy in both RF and SVM models have negligible increment prolly due to the models chosen are not suitable for our problem. It is suggested that more classifier models are tested. Again, accuracy alone is insufficient to confirm one model is better than the other.')
        st.write('As a conclusion, RF and SVM both has accuracy of approximately 0.75 which can be considered as good models. However, if we evaluate the models using F1-score instead, we get 0.86 instead where the models are excellent.')