# Customer Segmentation using Python & K-Means Clustering

## Overview
This project analyzes customer data and groups them into distinct segments based on their purchasing behavior. It utilizes **unsupervised learning** techniques, specifically **K-Means Clustering**, to identify customer clusters. The project also includes data preprocessing, feature scaling, and visualization using **Matplotlib, Seaborn, and Plotly**.

## Features
- **Data Preprocessing:** Cleans and standardizes customer data.
- **Feature Scaling:** Uses `StandardScaler` for normalization.
- **K-Means Clustering:** Groups customers into segments based on purchasing behavior.
- **Elbow Method:** Determines the optimal number of clusters.
- **PCA for Dimensionality Reduction:** Reduces high-dimensional data for better visualization.
- **Interactive Visualization:** Uses **Plotly** to display customer segments.

## Technologies Used
- Python
- Pandas
- Matplotlib
- Seaborn
- Plotly
- Scikit-learn (K-Means, PCA)

## Installation & Usage
### Prerequisites
Ensure you have Python installed along with the required libraries. Install dependencies using:
```bash
pip install pandas matplotlib seaborn plotly scikit-learn
```

### Run the Project
1. Clone this repository:
   ```bash
   git clone https://github.com/thismayank1/Customer-Segmentation-Python-K--Means-Clustering-
   ```
2. Navigate to the project directory:
   ```bash
   cd Customer-Segmentation-Python-K--Means-Clustering-
   ```
3. Place your dataset (`E-commerce.csv`) in the same directory.
4. Run the script:
   ```bash
   python customer_segmentation.py
   ```

## Results
- The model assigns each customer to a cluster.
- The results are saved in `customer_segments.csv`.
- Interactive visualizations help understand customer behavior.
  ![Screenshot 2025-04-03 123332](https://github.com/user-attachments/assets/7e48a44d-8882-498f-8870-58f3f17a41b0)
  ![Screenshot 2025-04-03 123224](https://github.com/user-attachments/assets/43c6bf74-7013-49ee-906d-f827ff4fe148)



## Contributing
Feel free to fork this repository and submit pull requests if you want to improve the project!

## License
This project is licensed under the MIT License.

