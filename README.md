# README: Walmart Sales Data Analysis

This project provides an analysis of Walmart sales data using Python libraries like `pandas`, `numpy`, `matplotlib`, and `seaborn`. The notebook offers insights into sales trends, customer behavior, and other key metrics by generating visualizations and performing data analytics. Below is a brief overview of the content, dependencies, and usage of the project.

---

## 1. Overview
The project answers various analytical questions related to Walmart's sales data, such as:
- Identifying the most common product line, payment methods, and customer types.
- Understanding customer purchasing behavior based on gender, time, and location.
- Analyzing revenue by product line, city, and month.
- Visualizing sales trends over time and per weekday.

## 2. Dependencies
To run this project, the following Python libraries are required:
- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`

Install the dependencies using:
```bash
pip install numpy pandas matplotlib seaborn
```

## 3. Data Preparation
- The dataset used in this project is loaded from a CSV file `WalmartSalesData.csv`. Make sure the file path is correct before running the notebook.
- The `Date` and `Time` columns are converted into datetime format, and additional columns such as `weekday` and `hour` are created to support the analysis.

## 4. Analysis Questions and Visualizations

### Product Analysis
1. **Unique Product Lines**: Displays the number of unique product lines.
2. **Most Common Payment Method**: Identifies the most frequent payment method used by customers.
3. **Most Selling Product Line**: Highlights which product line sells the most items.
4. **Total Revenue by Month**: Shows the total revenue generated per month.
5. **Largest COGS (Cost of Goods Sold)**: Identifies which month had the highest COGS.
6. **Product Line with Largest Revenue**: Analyzes which product line generates the most revenue.
7. **City with Largest Revenue**: Determines which city contributes the most to revenue.
8. **Product Line with Largest VAT**: Finds which product line generates the most VAT.
9. **Product Line Performance**: Adds a "Good" or "Bad" label to each product line based on average sales.
10. **Branch Performance**: Compares branches based on average product sales.
11. **Most Common Product Line by Gender**: Identifies the most popular product line for each gender.
12. **Average Rating per Product Line**: Displays the average customer rating for each product line.

### Sales Analysis
1. **Sales by Time of Day per Weekday**: Visualizes the number of sales made at different times of the day for each weekday using a heatmap.
2. **Revenue by Customer Type**: Analyzes which customer type brings the most revenue.
3. **City with Largest VAT**: Shows which city has the highest average VAT.
4. **VAT Paid by Customer Type**: Examines which customer type pays the most VAT.

### Customer Analysis
1. **Unique Customer Types**: Counts the number of unique customer types.
2. **Unique Payment Methods**: Counts the unique payment methods used in transactions.
3. **Most Common Customer Type**: Identifies the most frequent customer type.
4. **Purchasing Behavior by Customer Type**: Compares total purchases made by each customer type.
5. **Most Common Customer Gender**: Determines the gender of the majority of customers.
6. **Gender Distribution per Branch**: Visualizes the distribution of customer gender across different branches.
7. **Customer Ratings by Time**: Shows which time of day customers give the most ratings.
8. **Ratings by Time and Branch**: Analyzes customer ratings across different times of the day and branches.
9. **Best Day for Ratings**: Identifies which day of the week receives the best average ratings.
10. **Ratings per Branch by Day**: Shows the best-rated day per branch.

## 5. Example Visualizations

- **Sales Heatmap**: A heatmap showing the number of sales per hour for each weekday.
- **Revenue Bar Charts**: Multiple bar charts display revenue breakdowns by customer type, product line, and city.
- **Ratings Line Plots**: Line plots showing average customer ratings based on time of day and branch.

## 6. Usage
To run the notebook and view the results:
1. Make sure all dependencies are installed.
2. Place the CSV file in the appropriate directory.
3. Run the cells in the notebook to generate results and visualizations.

---

This project provides comprehensive insights into Walmart sales trends, customer behavior, and product performance, using data visualization and analysis techniques. The insights can help improve decision-making and optimize business operations.