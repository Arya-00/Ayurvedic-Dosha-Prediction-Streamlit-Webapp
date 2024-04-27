# Ayurvedic-Dosha-Prediction-Webapp
### Trained using Neural Networks
An approach to identify the actual importance of body characteristics such as body size, weight, hair quality, etc. in Ayurvedic Dosha Prediction and determining Body Dosha using these traits.

***Re-train each model, if your (tf.__version__ != 2.16.1) before launching app***

## Model Architecture
![Model Architecture](https://github.com/Arya-00/Ayurvedic-Dosha-Prediction-Streamlit-Webapp/blob/main/Ayurvedic_Dosha_Prediction_Project/Doshas_Model_Architecture.png)

## How to run:
1. Execute app.py.
2. Run command 'streamlit run app.py' on the terminal.

## How to train:
1. Open 'Model Trainer' folder.
2. Execute all notebook files to obtain three Keras zip file.
3. Replace the files in trained_models with new files.

## Requirements:
1. streamlit (v1.33.0)
2. tensorflow
3. sklearn
4. pandas
5. numpy
