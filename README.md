# PCOS-Detection-Model

PCOS Detection model is a supervised learning model trained on a dummy dataset of 200 entries using a custom python script.The Symptom features were defined based on the symptoms defined on Mayo Clinic, Cleveland Clinic and Queensland Health Department's websites.

For preprocessing, Label Encoding was used to convert categorical variables into numerical equivalents. Using Random Forest Algorithm, the model was trained on 80% training data with the rest 20% of data serving as validation set. 

The model acheived 95% accuracy with an F1-Score of 0.9722.

As a bonus challenge, I implemented the model as a react.js web application. With Flask backend using CORS, the webpage takes input from user and predicts wether the user can likely have PCOS based on the predictions of the trained model. 

