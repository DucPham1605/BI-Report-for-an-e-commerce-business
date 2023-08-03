--Cleansing product table
with cte as(
	select p.product_id, p.product_category_name,
	isnull(p.product_name_lenght,0) product_name_length,
	isnull(p.product_description_lenght,0) product_description_length,
	isnull(p.product_photos_qty,0) product_photos_qty,
	isnull(p.product_weight_g,0) product_weight_g,
	isnull(p.product_length_cm,0) product_length_cm,
	isnull(p.product_width_cm,0) product_width_c,
	isnull(pt.product_category_name_english, 'Not determined') product_category_name_english
	from products p
	left join product_category_name_translation pt on p.product_category_name = pt.product_category_name
)
select *
into product_cleansed
from cte


--Enrich Customers table
with cte as (
select o.order_id,o.customer_id, count(ors.review_id) total_reviews
from orders o
left join order_reviews ors on o.order_id = ors.order_id
group by o.order_id,o.customer_id
)


select c.customer_id, c.customer_unique_id, c.customer_zip_code_prefix, c.customer_city, c.customer_state, count(o.order_id) total_order,
case 
	when count(o.order_id) < 2 then 'New customer'
	when count(o.order_id) > 5 then 'Regular customer'
end customer_type,
sum(cte.total_reviews) total_reviews
into customers_enriched
from customers c
left join orders o on c.customer_id = o.customer_id
left join cte cte on c.customer_id = cte.customer_id
group by c.customer_id, c.customer_unique_id, c.customer_zip_code_prefix, c.customer_city, c.customer_state
order by total_reviews desc

--Enrich Orders table
select o.order_id, o.customer_id, o.order_status, o.order_purchase_timestamp, o.order_approved_at, o.order_delivered_carrier_date, o.order_delivered_customer_date, o.order_estimated_delivery_date,
count(order_item_id) total_item,
sum(price) total_price,
sum(oi.freight_value) total_freight_value
into orders_enriched
from orders o
left join order_items oi on o.order_id = oi.order_id
group by o.order_id, o.customer_id, o.order_status, o.order_purchase_timestamp, o.order_approved_at, o.order_delivered_carrier_date, o.order_delivered_customer_date, o.order_estimated_delivery_date
order by total_item desc
