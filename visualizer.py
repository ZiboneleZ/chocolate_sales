import matplotlib.pyplot as plt
import seaborn as sns
from chocolate_analyzer import data_cleaner

df = data_cleaner()
print(df.head())

#Sales by country
def revenue_by_country(df):
    plt.figure(figsize=(12.5, 6.5))
    country_sales = df.groupby('Country')['Amount'].sum().sort_values(ascending=False).reset_index()
    sns.barplot(country_sales, x='Country', y='Amount', hue='Amount', legend=False, palette='viridis')
    plt.title('Revenue By Country', fontsize=15)
    #plt.show()
    plt.savefig('outputs/revenue.png')

#Top 10 Sales People
def sales_performance(df):
    plt.figure(figsize=(12.5, 6.5))
    sales_perf = df.groupby('Sales Person')['Amount'].sum().sort_values(ascending=False).head(10).reset_index()
    sns.barplot(sales_perf, x='Amount', y='Sales Person', hue='Sales Person', palette='magma')
    plt.title('Top 10 Sales People', fontsize=15)
    plt.savefig('outputs/top_sales_people.png')

#Top 10 Sold Products
def product_sales(df):
    plt.figure(figsize=(12.5, 6.5))
    products = df.groupby('Product')['Amount'].sum().sort_values(ascending=False).head(10).reset_index()
    sns.barplot(products, x='Amount', y='Product', hue='Amount', palette=('flare'))
    plt.title('Top 10 Products Sold', fontsize=15)
    plt.savefig('outputs/top_10_products.png')

#Monthly Growth Trend
def sales_trend_monthly(df):
    plt.figure(figsize=(12.5, 6.5))
    monthly_trend = df.groupby(df['Date'].dt.to_period('M'))['Amount'].sum()
    monthly_trend.index = monthly_trend.index.to_timestamp()
    plt.plot(monthly_trend.index, monthly_trend.values, marker='o', color='blue', linewidth=2)
    plt.title('Monthly Sales Trend Growth (2022 - 2024)')
    plt.ylabel('Revenue ($)')
    plt.grid(True, alpha=0.3)
    plt.savefig('outputs/monthly_sales_growth.png')

revenue_by_country(df)
sales_performance(df)
product_sales(df)
sales_trend_monthly(df)
