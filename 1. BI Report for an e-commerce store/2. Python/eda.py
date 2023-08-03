import pandas as pd
import numpy as np

# EDA in general

# CUSTOMERS_DATASET

customers_dataset = pd.read_excel('customers_dataset.xlsx')
print(customers_dataset.head())
print(customers_dataset.info())


# ORDER_ITEMS_DATASET
order_items_dataset = pd.read_excel('order_items_dataset.xlsx')
print(order_items_dataset.head())
print(order_items_dataset.info())

# order_payments_dataset
order_payments_dataset = pd.read_excel('order_payments_dataset.xlsx')
print(order_payments_dataset.head())
print(order_payments_dataset.info())

#order_reviews_dataset
order_reviews_dataset = pd.read_excel('order_reviews_dataset.xlsx')
print(order_reviews_dataset.head())
print(order_reviews_dataset.info())

# orders_dataset
orders_dataset = pd.read_excel('orders_dataset.xlsx')
print(orders_dataset.head())
print(orders_dataset.info())		 	

# product_category_name_translation
product_category_name_translation = pd.read_excel('product_category_name_translation.xlsx')
print(product_category_name_translation.head())
print(product_category_name_translation.info())

# products_dataset
products_dataset = pd.read_excel('products_dataset.xlsx')
print(products_dataset.head())
print(products_dataset.info())
