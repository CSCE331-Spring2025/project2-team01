
-- FIND THE TOP 10 HIGHEST SPENDING CUSTOMER ON ORDERS
SELECT 
    customername, 
    COUNT(*) AS total_orders
FROM orders
GROUP BY customername
ORDER BY total_orders DESC
LIMIT 10;

-- Customer Retention and Repeat Orders (Which customers are returning and how frequently do they place orders?
SELECT 
    customername, 
    COUNT(*) AS orderCount, 
    MIN(orderdate) AS firstOrder, 
    MAX(orderdate) AS lastOrder,
    ROUND(AVG(DATE_PART('day', MAX(orderdate) - MIN(orderdate)) / COUNT(*)), 2) AS avgDaysBetweenOrders
FROM orders
GROUP BY customername
HAVING COUNT(*) > 1
ORDER BY orderCount DESC;

-- Sales Trends by Season - How do sales vary by season?
SELECT 
    CASE 
        WHEN EXTRACT(MONTH FROM orderdate) IN (12, 1, 2) THEN 'Winter'
        WHEN EXTRACT(MONTH FROM orderdate) IN (3, 4, 5) THEN 'Spring'
        WHEN EXTRACT(MONTH FROM orderdate) IN (6, 7, 8) THEN 'Summer'
        ELSE 'Fall'
    END AS season,
    COUNT(*) AS totalOrders,
    SUM(totalprice) AS totalSales
FROM orders
GROUP BY season
ORDER BY totalSales DESC;

-- Sales Conversion Rates - What is the conversion rate of orders to fulfilled orders
SELECT 
    DATE_TRUNC('month', orderdate) AS month,
    COUNT(*) AS totalOrders,
    SUM(CASE WHEN isfulfilled THEN 1 ELSE 0 END) AS fulfilledOrders,
    ROUND((SUM(CASE WHEN isfulfilled THEN 1 ELSE 0 END)::FLOAT / COUNT(*)) * 100, 2) AS conversionRate
FROM orders
GROUP BY month
ORDER BY month;

-- Customer Lifetime Value (CLV) What is the estimated lifetime value of each customer?
SELECT 
    customername, 
    COUNT(*) AS totalOrders, 
    SUM(totalprice) AS totalSpent,
    ROUND(SUM(totalprice) / NULLIF(COUNT(*), 0), 2) AS avgOrderValue,
    ROUND((SUM(totalprice) / NULLIF(COUNT(*), 0)) * COUNT(*) * 0.5, 2) AS estimatedCLV  -- Assuming 50% retention rate
FROM orders
GROUP BY customername
ORDER BY estimatedCLV DESC;
