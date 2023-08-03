import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Total orders over years
orders['order_year'] = orders['order_purchase_timestamp'].dt.strftime('%Y')
order_per_year = orders.groupby(['order_year'],as_index= False).agg(total_order=('order_id','count'))

year = order_per_year['order_year']
total_order = order_per_year['total_order']
plt.bar(year,total_order, color = 'red', width = 0.4)
plt.ylabel("Total orders")
plt.xlabel("Year")
plt.title("Total order per year")
plt.show()


#Sales over years
#total sales of orders with year
sales_order = orders.merge(order_items, how='left', on = 'order_id')

sales_order['year'] = sales_order['order_purchase_timestamp'].dt.strftime('%Y')
sales_order2 = sales_order.groupby(['year'],as_index = False).agg(total_sales = ('price','sum'))

total_sales = sales_order2['total_sales']
year = sales_order2['year']
plt.bar(year,total_sales, color = 'red', width = 0.5)
plt.ylabel("Total sales")
plt.xlabel("Year")
plt.title("Total sales per year")
plt.show()

#Revenue over years (Revenue = Number of units sold x Sales price per unit)


#Profit over years (Profit = Selling Price - Cost Price)


# products_dataset
products = pd.read_excel('products_dataset.xlsx')
orders = pd.read_excel('orders_dataset.xlsx')
order_items = pd.read_excel('order_items_dataset.xlsx')

#Replacing NA values
products=products.fillna('Not determined')

