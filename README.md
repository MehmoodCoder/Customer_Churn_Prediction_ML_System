# Customer_Churn_Prediction_ML_System
📊 Enterprise Customer Churn Prediction System 🚀 | End-to-End ML Pipeline 🤖 with FastAPI ⚡, Risk Stratification 🎯 & Explainable AI 🔍


## 📋 Project Overview
The primary objective of this project is to architect an end-to-end Machine Learning classification pipeline that evaluates customer demographics, account tenure, usage patterns, and support history to predict churn risk, stratify customers into risk tiers, and serve inference through a FastAPI service.

---

## 📂 Repository Structure 

**Generated:** 10/17/2026, 7:58:39 PM
**Root Path:** `workspace\Customer_Churn_Prediction_ML_System`

```
├── 📁 Data
│   └── 📄 customer_churn_dataset-training-master.csv
├── 📁 Main
│   ├── 🐍 app.py
│   ├── 📄 best_model.joblib
│   ├── 📄 main.ipynb
│   └── 📄 preprocessor.joblib
├── ⚙️ .gitignore
├── 📕 Proposal.pdf
└── 📝 README.md
```

---

## 📊 Dataset & Download Link
- **Dataset Source:** Kaggle (Customer Churn Dataset - Shahid Azeem).
- **Note on Dataset Size:** Since the full dataset is very large (~440k+ records, exceeding GitHub's file size limits), a representative sample dataset has been included in the repository. You can download and access the full training dataset from the original source or via the dataset link provided during the internship.

## 🚀 How to Run the Project
1. **Run Machine Learning Pipeline:** Open `Main/main.ipynb` in Jupyter Notebook and execute cells to train models and generate `.joblib` files.
2. **Run FastAPI Server:** Navigate to the `Main` folder and start the local server using Uvicorn:
   ```bash
   python -m uvicorn app:app --reload
   ```
---

Test API: Open your browser and go to http://127.0.0.1:8000/docs to test predictions via Swagger UI.

## 👤 Author

**MehmoodCoder**

- 🔗 GitHub: [https://github.com/MehmoodCoder](https://github.com/MehmoodCoder)
- 🌐 Portfolio: [My Portfolio Link](https://mh56-portfolio.vercel.app)

---

## 📄 License

This project is open-source and available under the **MIT License**.

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve the API, add new features, or optimize database queries, please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

### ** 🤷‍♂️ Happy coding without chai ! ☕ **
