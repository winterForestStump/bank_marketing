# deposit prediction classifier on bank marketing dataset

* The data is related with direct marketing campaigns (phone calls) of a Portuguese banking institution. The classification goal is to predict if the client will subscribe a term deposit. Source: https://archive.ics.uci.edu/dataset/222/bank+marketing

* All previous ML experiments and results are in `ml_bank_marketing_experiments.ipynb` notebook. The results were unsufficient

* Experiments with SGDClassifier (with better results) are in `ml_sgdClassifier_bank_marketing_experiments.ipynb`

* The model with the best parameters is saved as `sgd_bank_marketing_pipe.skops` (and running on HF space)

* Application configuration file `app.py` for Gradio

* Dependencies for HuggingFace space are in `requirements .txt`

* Link to HuggingFace Space with the app: https://huggingface.co/spaces/winterForestStump/bank_deposit_prediction
