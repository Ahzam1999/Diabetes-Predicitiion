
# Create your views here.
# diabetes_prediction_app/views.py
from django.shortcuts import render
import joblib

def home_view(request):
    return render(request, 'home.html')


def predict_diabetes(request):
    if request.method == 'POST':
        # Load the trained model
        model = joblib.load('C:\\data science\\diabetes_prediction_project\\diabetes_prediction_app\\models\\reg.pk1')

        # Extract input data from the form
        Pregnancies = int(request.POST['Pregnancies'])
        Glucose = float(request.POST['Glucose'])
        BloodPressure= float(request.POST['BloodPressure'])
        SkinThickness = float(request.POST['SkinThickness'])
        Insulin = float(request.POST['Insulin'])
        BMI = float(request.POST['BMI'])
        DiabetesPedigreeFunction = float(request.POST['DiabetesPedigreeFunction'])
        Age = int(request.POST['Age'])
       


        # Extract more input data as needed
        
        # Make prediction
        input_data = [[Pregnancies, Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]]  # Format input data as required by the model
        prediction = model.predict(input_data)[0]

        print("Prediction value:", prediction)

        if prediction >0.5:
            prediction_text = "Yes"
        
        else:
            prediction_text = "NO"

        # Render the prediction result
        return render(request, 'prediction_result.html', {'prediction': prediction_text})
    else:
        return render(request, 'predict_form.html')
