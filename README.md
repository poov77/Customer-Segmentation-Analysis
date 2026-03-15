Customer Segmentation Analysis Using RFM and K-Means
Project Overview

This project analyzes customer purchasing behavior from an e-commerce dataset to identify meaningful customer segments. By applying RFM analysis (Recency, Frequency, Monetary) and K-Means clustering, customers are grouped based on their buying patterns.

The goal of this project is to help businesses understand customer value and design targeted marketing strategies such as loyalty programs, retention campaigns, and personalized promotions.

Business Problem

Businesses often treat all customers the same, but customer behavior varies significantly. Identifying different customer segments helps companies:

Improve marketing efficiency

Increase customer retention

Identify high-value customers

Detect customers at risk of churn

Customer segmentation enables businesses to make data-driven decisions about marketing and customer relationship management.

Dataset

Dataset used: Olist Brazilian E-commerce Dataset

This dataset contains real e-commerce transactions from a Brazilian marketplace.

Dataset Statistics
Metric	Count
Orders	~100,000
Customers	~96,000
Order Items	~112,000
Key Tables Used

olist_orders_dataset.csv

olist_customers_dataset.csv

olist_order_items_dataset.csv

olist_order_payments_dataset.csv

Dataset Source:
https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

Project Workflow
1. Data Collection

The dataset consists of multiple relational tables representing different aspects of e-commerce transactions such as orders, customers, products, and payments.

2. Data Merging

Multiple datasets were merged using common keys:

order_id

customer_id

This created a unified dataset containing customer transactions.

Example merge process:

customers → orders → order_items → payments
3. Data Cleaning

Data preprocessing included:

Removing missing values

Converting timestamp fields to datetime

Handling duplicate records

Ensuring valid transaction values

Data cleaning ensures accurate analysis and reliable clustering results.

Feature Engineering (RFM Analysis)

Customer behavior was summarized using RFM metrics.

Metric	Description
Recency	Days since last purchase
Frequency	Number of purchases made
Monetary	Total amount spent

Example RFM table:

Customer	Recency	Frequency	Monetary
C001	5	10	1200
C002	120	2	80

RFM analysis helps quantify customer engagement and value.

Customer Segmentation Using K-Means

After generating RFM features, customers were segmented using K-Means clustering.

Steps performed:

Standardized RFM values using StandardScaler

Determined optimal number of clusters using the Elbow Method

Applied K-Means clustering to segment customers

Final model grouped customers into 4 segments.

Customer Segments Identified
Segment	Description
VIP Customers	High frequency and high spending customers
Loyal Customers	Frequent buyers with moderate spending
At-Risk Customers	Customers who have not purchased recently
New Customers	Recently acquired customers

These segments help businesses tailor marketing strategies.

Dashboard Development

An interactive dashboard was developed using Python and Streamlit.

Dashboard Features:

Customer segment distribution

Recency vs Monetary scatter plot

Cluster summary statistics

Dataset preview

The dashboard allows users to explore customer segments interactively.

Technologies Used
Category	Tools
Programming	Python
Data Processing	Pandas
Machine Learning	Scikit-learn
Visualization	Plotly
Dashboard	Streamlit
Development	Jupyter Notebook
Project Structure
customer-segmentation
│
├── Dashboard.py
├── customer_segments.csv
├── notebooks
│   └── analysis.ipynb
├── images
│   └── dashboard screenshots
└── README.md
Key Insights

Some insights discovered during analysis:

A small percentage of customers contribute to a large share of revenue

Many customers show low recency, indicating potential churn

High-frequency customers generate significantly higher lifetime value

These insights can guide targeted marketing campaigns and customer retention strategies.

How to Run the Project
Clone the repository
git clone https://github.com/your-username/customer-segmentation.git
Install dependencies
pip install pandas scikit-learn streamlit plotly
Run the dashboard
streamlit run Dashboard.py

The dashboard will open at:

http://localhost:8501
Future Improvements

Potential enhancements for this project include:

Adding customer lifetime value (CLV) analysis

Implementing advanced clustering algorithms

Deploying the dashboard online

Integrating real-time data sources

Author

Poovarasan K
B.Tech Artificial Intelligence and Data Science

LinkedIn: https://www.linkedin.com/in/poovarasan007/

GitHub: https://github.com/poov77
