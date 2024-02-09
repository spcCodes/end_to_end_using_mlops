# end_to_end_using_mlops
This is a end to end project implementation using mlops


## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py

## How to run?
## STEPS:
```
conda create -n mlproj python=3.8 -y 
conda activate mlproj
pip install -r requirements.txt
```

#for dagshub experiment tracking

MLFLOW_TRACKING_URI=https://dagshub.com/spcCodes/end_to_end_using_mlops.mlflow \
MLFLOW_TRACKING_USERNAME=spcCodes \
MLFLOW_TRACKING_PASSWORD=3f7a9c79d5525e15df189302054536f641f31cfa \
python script.py


```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/spcCodes/end_to_end_using_mlops.mlflow

export MLFLOW_TRACKING_USERNAME=spcCodes 

export MLFLOW_TRACKING_PASSWORD=3f7a9c79d5525e15df189302054536f641f31cfa

