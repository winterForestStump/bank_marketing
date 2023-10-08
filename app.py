import skops.io as sio
import gradio as gr

#pipe = sio.load("bank_marketing_pipe.skops", trusted=True)
pipe = sio.load('sgd_bank_marketing_pipe.skops', trusted=True)

classes = [
    "Not Subscribe",
    "Subscribe"]


def classifier(age, job, marital, education, default, balance, housing,loan, contact):
    pred = pipe.predict([[age, job, marital, education, default, balance, housing,loan, contact]])[0]
    label = f"Predicted output: **{classes[pred]}**"
    return label


inputs = [
    gr.Slider(10, 90, step=1, label="Age"),
    gr.Dropdown(["admin.","unknown","unemployed","management","housemaid","entrepreneur","student","blue-collar",
                 "self-employed","retired","technician","services"], label="Job", multiselect=False),
    gr.Dropdown(["married","divorced","single"], label="Marital", multiselect=False),
    gr.Dropdown(["unknown","secondary","primary","tertiary"], label="Education", multiselect=False),
    gr.Radio(["yes","no"], label="Default", info='has credit in default?'),
    gr.Slider(-100000, 100000, step=1, label="Balance"),
    gr.Radio(["yes","no"], label="Housing", info='has housing loan?'),
    gr.Radio(["yes","no"], label="Loan", info='has personal loan?'),
    gr.Dropdown(["unknown","telephone","cellular"], label="Contact")
]

outputs = [gr.Label(num_top_classes=2)]

title = "Deposit Subscription Prediction"
description = "Enter the details to identify where or not the customer is subscribed or not subscribed for deposit"

gr.Interface(
    fn=classifier,
    inputs=inputs,
    outputs=outputs,
    title=title,
    description=description,
).launch()
