import joblib
import json
from pathlib import Path
from datetime import datetime

def save_model_artifact(model, metrics, features, base_path="../models", version="v1"):
    """
    Handles the boilerplate of saving models and metadata.
    """
    export_path = Path(base_path) / version
    export_path.mkdir(parents=True, exist_ok=True)
    
    # Save model
    joblib.dump(model, export_path / "model.pkl")
    
    # Save metrics
    for name, df in metrics.items():
        df.to_csv(export_path / f"{name}.csv", index=False)
    
    # Save metadata
    metadata = {
        "version": version,
        "date": datetime.now().isoformat(),
        "model_type": type(model).__name__,
        "features": list(features)
    }
    
    with open(export_path / "metadata.json", "w") as f:
        json.dump(metadata, f, indent=4)
        
    return export_path