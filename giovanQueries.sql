/* 
Special Query #2: "Realistic Sales History"

pseudocode: select count of orders, sum of order total grouped by hour
about: given a specific hour of the day, how many orders were placed and what was the total sum of the orders?
example: e.g., "12pm has 12345 orders totaling $86753"
*/
SELECT 
    EXTRACT(HOUR FROM orderDate) AS orderHour,
    COUNT(*) AS orderCount, 
    SUM(totalprice) AS totalOrderSum
FROM orders
GROUP BY EXTRACT(HOUR FROM orderDate)
ORDER BY orderHour;

/* 
Special Query #3: "Peak Sales Day"

pseudocode: select top 10 sums of order total grouped by day in descending order by order total
about: given a specific day, what was the sum of the top 10 order totals?
example: "30 August has $12345 of top sales"
*/
SELECT 
    TOCHAR(orderDate, 'DD Mon') AS orderDay,
    SUM(totalprice) AS totalOrderSum
FROM orders
GROUP BY orderDate::DATE
ORDER BY totalOrderSum DESC
LIMIT 10;

/* 
Functional Query
select the top 10 most popular items and their relative revenue in descending order
look at orderItem table, select item with itemID, use subTotal to quantify revenue
*/
SELECT
    orderItem.itemId,
    item.name,
    item.subFlavor,
    COUNT(*) as orderCount,
    SUM(orderItems.subTotal) as totalRevenue
FROM orderItem
JOIN item ON orderItem.itemId = item.ID
GROUP BY orderItem.itemId, item.name, item.subFlavor
ORDER BY totalRevenue DESC
LIMIT 10;

/* 
Functional Query
 */
