import gradio as gr
import pickle
import pandas as pd

# Load the trained model
with open('./movie_rental_model.pkl', 'rb') as f:
    model = pickle.load(f)

def preprocess_input(amount, release_year, rental_rate,
                     length, replacement_cost, NC_17, PG, PG_13, R,
                     return_weekend, rental_weekend, deleted_scenes,
                     behind_the_scenes):
    # Create a DataFrame for the model input
    input_data = pd.DataFrame({
        'amount': [amount],
        'release_year': [release_year],
        'rental_rate': [rental_rate],
        'length': [length],
        'replacement_cost': [replacement_cost],
        'NC-17': [1 if NC_17 == 'Yes' else 0],
        'amount_2': [amount**2] ,
        'length_2': [length**2],
        'rental_rate_2': [rental_rate**2],
        'PG': [1 if PG == 'Yes' else 0],
        'PG-13': [1 if PG_13 == 'Yes' else 0],
        'R': [1 if R == 'Yes' else 0],
        'return_weekend': [1 if return_weekend == 'Yes' else 0],
        'rental_weekend': [1 if rental_weekend == 'Yes' else 0],
        'deleted_scenes': [1 if deleted_scenes == 'Yes' else 0],
        'behind_the_scenes': [1 if behind_the_scenes == 'Yes' else 0],
    })
    return input_data

# Define prediction function
def predict_rent_duration(amount, release_year, rental_rate,
                          length, replacement_cost, NC_17, PG, PG_13, R,
                          return_weekend, rental_weekend, deleted_scenes,
                          behind_the_scenes):
    input_data = preprocess_input(amount, release_year, rental_rate,
                                  length, replacement_cost, NC_17, PG, PG_13, R,
                                  return_weekend, rental_weekend, deleted_scenes,
                                  behind_the_scenes)
    prediction = model.predict(input_data)
    return f"Predicted Movie Duration: {round(prediction[0])} days"

# Create Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# Movie Rental Duration Prediction")

    with gr.Row():
        amount = gr.Number(label='Price of DVD')
        release_year = gr.Number(label='Release Year')
        rental_rate = gr.Number(label='Rental Rate')
        length = gr.Number(label='Length of Movie')
        replacement_cost = gr.Number(label='Replacement Cost')
        NC_17 = gr.Radio(label='NC-17', choices=["Yes", "No"])
        PG = gr.Radio(label='PG', choices=["Yes", "No"])
        PG_13 = gr.Radio(label='PG-13', choices=["Yes", "No"])
        R = gr.Radio(label='R', choices=["Yes", "No"])
        return_weekend = gr.Radio(label='Return Weekend', choices=["Yes", "No"])
        rental_weekend = gr.Radio(label='Rental Weekend', choices=["Yes", "No"])
        deleted_scenes = gr.Radio(label='Deleted Scenes', choices=["Yes", "No"])
        behind_the_scenes = gr.Radio(label='Behind the Scenes', choices=["Yes", "No"])
    predict_button = gr.Button("Predict")

    output = gr.Text(label="Prediction Results")

    predict_button.click(
        fn=predict_rent_duration,
        inputs=[amount, release_year, rental_rate,
                length, replacement_cost, NC_17, PG, PG_13, R,
                return_weekend, rental_weekend, deleted_scenes,
                behind_the_scenes],
        outputs=output
    )

# Run the app
demo.launch(share=True)
