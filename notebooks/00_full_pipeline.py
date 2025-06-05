# 00_full_pipeline.ipynb

# Sequential execution of all team notebooks

# ✅ Step 1: EDA
%run ./01_eda.ipynb

# ✅ Step 2: Preprocessing
%run ./02_preprocessing.ipynb

# ✅ Step 3: Baseline Models
%run ./03_baseline_models.ipynb

# ✅ Step 4: Advanced Models (XGBoost + LightGBM)
%run ./04_advanced_models.ipynb

# ✅ Step 5: Ensembling
%run ./05_ensemble_final.ipynb

# ✅ Step 6: Submission
%run ./06_submission.ipynb

# (Optional)
# %run ./07_model_viewer.ipynb

print("\n✅ Full pipeline executed successfully.")
