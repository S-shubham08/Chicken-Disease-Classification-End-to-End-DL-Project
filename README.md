# Chicken-Disease-Classification-End-to-End-DL-Project

## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml


## Application Demo Page
![image](https://github.com/S-shubham08/Chicken-Disease-Classification-End-to-End-DL-Project/assets/127888794/3bf92b5e-451a-4705-bdf3-4f085a7f9a89)

## Project Description
This project aims to classify chicken faecal images into healthy or coccidiosis-affected categories using deep learning techniques. Coccidiosis is a common and harmful intestinal disease in poultry, and early detection is crucial for effective intervention. The project includes data preprocessing, model architecture design, model training, and a Flask web application for real-time disease classification.

## Project Structure
- /artifacts: Contains the dataset and data preprocessing and trained machine learning model.
- /src/components: Include all the components like data_ingestion, evaluation, prepare_base_model, prepare_callback, and training.
- /src/pipeline: Predice pipeline steps added
- app.py: Includes the Flask web application and API.
- utils.py: Include all the common functions used in a project.
- requirements.txt: List of dependencies required to run the project.

## Install the required packages:
```
pip install -r requirements.txt
```

## Usage
1. Run the Flask application:
```
python app/app.py
```
2. Open your web browser and go to http://localhost:5000 to access the web application.
3. Upload a chicken faecal image to the web application, and it will predict whether the chicken is healthy or affected by coccidiosis.
