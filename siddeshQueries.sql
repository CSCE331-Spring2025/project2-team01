/*
Functional Query : "Most Popular Topping"
pseudo code: select the most frequently used topping across all orders
About: Determines the most frequently used topping across all orders.
Example Output: "Pearl is the most popular topping with 54321 orders"
*/

/* 
Functional Query : "Daily Sales Report"
pseudo code: select the total sales for each day
About: Determines the total sales for each day.
Example Output: "On 30 August, the total sales were $12345"
*/
SELECT 
    orderdate AS sales_day, 
    COUNT(*) AS total_orders, 
    SUM(totalprice) AS total_revenue
FROM orders
GROUP BY sales_day
ORDER BY sales_day;