from functools import lru_cache

@lru_cache  # CRITICAL: Without this, model reloads every request!
def get_model():
    print("Loading model...")  # You'll see this only ONCE in logs
    return joblib.load("model.pkl")  # Heavy operation, runs once

@app.post("/predict")
def predict(data: PredictRequest, model = Depends(get_model)):
    # Model already in memory, just run inference
    return {"prediction": model.predict([data.features])[0]}




# Why @lru_cache is essential:

# Without it: get_model() runs every request → 30 sec load time per request
# With it: get_model() runs once → cached forever → instant predictions