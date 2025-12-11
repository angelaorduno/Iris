# 🌸 Iris Regression & Classification
---

## 🔗 Predictive Analysis: Evaluation of Regression and Classifier Metrics
<a href="./Evaluation-of-Regression-and-Classifier-Metrics.pdf" download>
  <img src="https://img.shields.io/badge/📥_Download_Report-PDF-ff8ad4?style=for-the-badge&logoColor=white&labelColor=b57bff" alt="Download Report Badge"/>
</a>

This project explores the classic Iris dataset using both **regression** and **classification** models, with a custom **pink–purple visualization theme.

---

The work is implemented in a Jupyter notebook and includes:

- 📊 **Data loading & preprocessing**
  - Uses `sklearn.datasets.load_iris()` wrapped into a pandas DataFrame.
  - Adds engineered features such as:
    - `new` feature combining sepal/petal dimensions.
    - `sepal_minus_petal_width` for regression.
    - `sepal_length_class` as a binary target for classification.

- 📈 **Regression modeling**
  - Predicts **petal length** from:
    - Single predictor: `sepal length (cm)`.
    - Two predictors: `petal_length` and `sepal_minus_petal_width`.
  - Evaluates models using custom metrics:
    - ME, MPE, MAE, MSE, RMSE, MAPE.
  - Visuals:
    - Training vs testing split bar chart.
    - 2D regression line vs actual points.
    - 3D regression surface over engineered features.

- 🧠 **Classification modeling**
  - Binary classification with **Logistic Regression**.
  - Target: `sepal_length_class` (0 = short, 1 = long) based on median sepal length.
  - Evaluation:
    - Accuracy score.
    - Classification report.
    - Confusion matrix heatmap using the pink–purple colormap.

- 🎨 **Custom visualization theme**
  - A reusable **pink–purple colormap** defined with:
    - `#FFC0CB`, `#FF69B4`, `#C71585`, `#8B008B`
  - Used consistently across plots (bar charts, regression plots, heatmaps, 3D surfaces).

---

