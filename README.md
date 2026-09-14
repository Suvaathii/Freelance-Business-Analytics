# 📊 Freelance Business Analytics

A practical Business Analytics portfolio project demonstrating how raw
retail transaction data can be transformed into an interactive **Power
BI business intelligence dashboard** using Python, Pandas, Power Query,
DAX, and data visualization.

------------------------------------------------------------------------

## 🚀 Project 1 --- Retail Sales Analytics Dashboard

An interactive Power BI dashboard designed to help a retail business
understand:

-   Revenue performance
-   Cost and profitability
-   Product performance
-   Customer segments
-   Payment methods
-   Monthly sales trends
-   Executive-level business insights

### 📸 Dashboard Preview

![Business Sales Dashboard](screenshots/business_sales_dashboard.png)

------------------------------------------------------------------------

## 🎯 Business Problem

Retail businesses often have transaction data but lack a simple way to
answer important questions such as:

-   How much revenue are we generating?
-   How profitable is the business?
-   Which products generate the most revenue?
-   Which category performs best?
-   Which customer segment contributes the most?
-   Which payment methods contribute the most revenue?
-   Which months perform better?
-   How does performance change when different filters are applied?

This project converts raw transaction data into an interactive dashboard
that answers these questions.

------------------------------------------------------------------------

## 💡 Solution

A complete analytics workflow was developed:

**Raw Transaction Data**\
↓\
**Python Data Preparation**\
↓\
**CSV Dataset**\
↓\
**Power Query Transformation**\
↓\
**Data Modeling**\
↓\
**DAX Measures & Calculations**\
↓\
**Interactive Power BI Dashboard**\
↓\
**Business Insights**

------------------------------------------------------------------------

## 📈 Key Metrics

  KPI                     Value
  ------------------ ----------
  💰 Revenue           ₹771.19K
  💸 Cost              ₹472.86K
  📈 Profit            ₹298.33K
  📊 Profit Margin       38.68%
  🧾 Orders                  2K
  📦 Quantity Sold          11K

> **Note:** The dataset used in this project is synthetic and created
> for portfolio demonstration purposes. The metrics above represent the
> generated dataset, not a real client's business performance.

------------------------------------------------------------------------

## 📊 Dashboard Features

### 1. Monthly Revenue Trend

Tracks revenue performance across January--August 2026 and identifies
the highest-revenue month.

### 2. Revenue & Profit by Category

Compares revenue and profitability across different product categories.

### 3. Top 10 Products by Revenue

Identifies the products contributing the most revenue.

### 4. Revenue by Customer Type

Analyzes revenue contribution across customer segments.

### 5. Revenue by Payment Method

Shows the distribution of revenue across payment methods.

### 6. Interactive Filters

The dashboard includes dynamic filtering by:

-   Category
-   Customer Type
-   Payment Method
-   Date Range

### 7. Dynamic Executive Insights

DAX measures automatically identify:

-   Peak Revenue Month
-   Top Revenue Category
-   Top Revenue Product
-   Top Customer Segment
-   Top Payment Method

------------------------------------------------------------------------

## 🔎 Key Insights

Based on the complete generated dataset:

-   **March 2026** recorded the highest monthly revenue.
-   **Office** was the highest-revenue category.
-   **Calculator** was the highest-revenue product.
-   **Individual** customers contributed the highest revenue among
    customer types.
-   **Cash** was the largest revenue-contributing payment method.

These findings demonstrate how an interactive dashboard can turn
transaction-level data into concise business insights.

------------------------------------------------------------------------

## 💼 Business Recommendations

Based on the analysis, a business could:

1.  Investigate the factors behind peak monthly performance.
2.  Prioritize high-performing categories and products.
3.  Monitor product-level revenue trends to support inventory decisions.
4.  Segment customers based on purchasing behavior.
5.  Track payment-method usage when planning payment infrastructure.
6.  Use the dashboard regularly to monitor changes in business
    performance.

> These are analytical recommendations based on the synthetic dataset
> and are not claims of actual business impact.

------------------------------------------------------------------------

## 🖼️ Dashboard Screenshots

### Main Dashboard

![Main Dashboard](screenshots/business_sales_dashboard.png)

### Filtered Dashboard

Demonstrates how the dashboard responds dynamically to multiple filters.

![Filtered Dashboard](screenshots/dashboard_filtered.png)

### Executive Insights

Dynamic DAX-driven insights highlighting the strongest-performing
dimensions.

![Executive Insights](screenshots/executive_insights.png)

------------------------------------------------------------------------

## 🛠️ Tools & Technologies

  Technology              Purpose
  ----------------------- ------------------------------------------
  🐍 Python               Dataset generation and preparation
  🐼 Pandas               Data manipulation
  🔄 Power Query          Data transformation
  📊 Power BI             Dashboard development
  🧮 DAX                  KPI calculations and dynamic insights
  📈 Data Visualization   Business reporting
  🔧 Git & GitHub         Version control and portfolio management

------------------------------------------------------------------------

## 🧮 Key DAX Measures

The dashboard uses DAX measures for core business KPIs:

``` dax
Total Revenue = SUM(sales_data[Revenue])

Total Cost = SUM(sales_data[Cost])

Total Profit = SUM(sales_data[Profit])

Profit Margin =
DIVIDE([Total Profit], [Total Revenue], 0)

Total Orders =
DISTINCTCOUNT(sales_data[Order_ID])

Total Quantity =
SUM(sales_data[Quantity])
```

Dynamic insight measures were also created to identify the
top-performing month, product, category, customer type, and payment
method based on the current filter context.

------------------------------------------------------------------------

## 📁 Project Structure

``` text
Freelance_Business_Analytics/
│
├── data/
│   └── sales_data.csv
│
├── portfolio/
│   └── Retail_Sales_Analytics_Case_Study.md
│
├── powerbi/
│   └── Business_Sales_Dashboard.pbix
│
├── python/
│   └── generate_data.py
│
├── screenshots/
│   ├── business_sales_dashboard.png
│   ├── dashboard_filtered.png
│   └── executive_insights.png
│
├── .gitignore
└── README.md
```

------------------------------------------------------------------------

## 📋 Project Workflow

### Data Layer

-   Generated 2,000 retail transactions
-   Created realistic sales, cost, product, customer, and payment data
-   Stored the dataset as CSV

### Transformation Layer

-   Loaded the dataset into Power BI
-   Performed data transformation using Power Query
-   Prepared fields for analysis

### Analytics Layer

-   Created DAX measures
-   Calculated revenue, cost, profit, margin, orders, and quantity
-   Created dynamic executive insight measures

### Visualization Layer

-   Designed an interactive Power BI dashboard
-   Added KPI cards
-   Added charts and slicers
-   Implemented dynamic filtering

### Reporting Layer

-   Extracted business insights
-   Created executive-level summary views
-   Documented the project as a portfolio case study

------------------------------------------------------------------------

## 🎓 Skills Demonstrated

-   Business Analytics
-   Data Analysis
-   Data Cleaning
-   Data Transformation
-   Exploratory Data Analysis
-   KPI Development
-   Business Intelligence
-   Power BI
-   Power Query
-   DAX
-   Data Visualization
-   Interactive Dashboard Development
-   Business Insight Generation
-   Python
-   Pandas
-   Git & GitHub

------------------------------------------------------------------------

## 📄 Detailed Case Study

A detailed explanation of the project methodology, dashboard design,
findings, and recommendations is available here:

👉 [Retail Sales Analytics Case
Study](portfolio/Retail_Sales_Analytics_Case_Study.md)

------------------------------------------------------------------------

## 🔮 Future Portfolio Projects

This repository will be expanded with additional analytics projects
involving:

-   📊 Sales Analytics
-   👥 Customer Analytics
-   💰 Financial Analytics
-   📈 Advanced Power BI Reporting
-   🐍 Python Data Analysis
-   🗄️ SQL Analytics
-   ⚙️ Business Process Automation

------------------------------------------------------------------------

## 👨‍💻 Portfolio

This repository is part of a practical Business Analytics portfolio
focused on transforming data into clear, actionable business insights.

**Built with Python + Power BI + DAX + Business Thinking.**
