import gradio as gr
import joblib
import numpy as np

# Load trained model
model = joblib.load("model.pkl")

# Prediction function
def predict(iq, cgpa, marks_10th, marks_12th, communication_skills):
    features = np.array([[iq, cgpa, marks_10th, marks_12th, communication_skills]])
    prediction = model.predict(features)[0]
    return "Placed" if prediction == 1 else "Not Placed"

# Gradio interface
demo = gr.Interface(
    fn=predict,
    inputs=[
        gr.Number(label="IQ"),
        gr.Number(label="CGPA"),
        gr.Number(label="10th Marks (%)"),
        gr.Number(label="12th Marks (%)"),
        gr.Number(label="Communication Skills (0-10)")
    ],
    outputs="text",
    title="🎓 Student Placement Prediction",
    description="Upload student details and get placement prediction."
)

# Launch the app
demo.launch()
