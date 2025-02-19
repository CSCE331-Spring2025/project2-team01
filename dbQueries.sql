/*
DEMO QUERIES:

top 5 toppings
top 10 most popular items
profit and loss
top 10 highest spending customers
3 least performing employee
*/

-- FINISHED QUERIES GO HERE 

/* 
Special Query #1: "Weekly Sales History"

pseudocode: select count of orders grouped by week
about: given a specific week, how many orders were placed?
example: "week 1 has 98765 orders"

this query groups orders by the week start and not week number since that is not something we are tracking (doesn't make sense really irl)
weekStart  | orderCount
-------------+------------
2025-01-01  | 98765
2025-01-08  | 87654
*/
SELECT 
    DATE_TRUNC('week', orderDate) AS weekStart,
    COUNT(*) AS orderCount
FROM Orders
GROUP BY weekStart
ORDER BY weekStart;

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
FROM Orders
GROUP BY EXTRACT(HOUR FROM orderDate)
ORDER BY orderHour;

/* 
Special Query #3: "Peak Sales Day"

pseudocode: select top 10 sums of order total grouped by day in descending order by order total
about: given a specific day, what was the sum of the top 10 order totals?
example: "30 August has $12345 of top sales"
*/
-- TODO FIXXXX
SELECT 
    TO_CHAR(orderDate::DATE, 'DD Mon') AS orderDay,
    SUM(totalprice) AS totalOrderSum
FROM Orders
GROUP BY orderDate::DATE
ORDER BY totalOrderSum DESC
LIMIT 10;

/* 
Special Query #4: "Menu Item Inventory"

pseudocode: select count of inventory items from inventory and menu grouped by menu item
about: given a specific menu item, how many items from the inventory does that menu item use?
example: "classic milk tea uses 12 items"
*/
SELECT 
    ItemIngredients.drinkFlavorId AS menuItemId,
    COUNT(ItemIngredients.inventoryId) AS inventoryItemCount
FROM ItemIngredients
GROUP BY ItemIngredients.drinkFlavorId
ORDER BY inventoryItemCount DESC;

/*
Functional Query
Show which employee had the most sales in dollars in december
*/ -- Empty table?

SELECT 
    E.name AS employeename,
    SUM(O.totalPrice) AS totalsales
FROM orders O
JOIN employee E ON O.employeeId = E.ID
WHERE EXTRACT(MONTH FROM O.orderdate) = 12  -- Filters for December
GROUP BY E.name
ORDER BY totalsales DESC
LIMIT 1;  -- Gets the top employee



/* 
Functional Query
select the top 10 most popular items and their relative revenue in descending order
look at orderItem table, select item with itemID, use subTotal to quantify revenue
*/
SELECT
    OrderItem.itemId,
    Item.name,
    Item.subFlavor,
    COUNT(*) as orderCount,
    SUM(OrderItems.subTotal) as totalRevenue
FROM OrderItem
JOIN item ON orderItem.itemId = item.ID
GROUP BY orderItem.itemId, item.name, item.subFlavor
ORDER BY totalRevenue DESC
LIMIT 10;

/* 
Functional Query
make a query to be used for general P/L
*/
WITH WeeklyOrders AS (
    SELECT 
        DATE_TRUNC('week', orderDate) AS weekStart,
        SUM(totalPrice) AS revenue
    FROM Orders
    GROUP BY weekStart
),
InventoryExpense AS (
    SELECT 
        SUM(cost * stockQuantity) AS totalInventoryExpense
    FROM Inventory
),
EmployeeExpense AS (
    SELECT 
        SUM(payGrade * hours) AS totalEmployeeExpense
    FROM Employee
)
SELECT 
    WeeklyOrders.weekStart,
    WeeklyOrders.revenue,
    InventoryExpense.totalInventoryExpense,
    EmployeeExpense.totalEmployeeExpense,
    (WeeklyOrders.revenue - InventoryExpense.totalInventoryExpense - EmployeeExpense.totalEmployeeExpense) AS netProfit
FROM WeeklyOrders
CROSS JOIN InventoryExpense
CROSS JOIN EmployeeExpense
ORDER BY WeeklyOrders.weekStart;


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

/* 
Functional Query : "Peak Sales Hour"
pseudo code: select the peak sales hour
About: Determines the peak sales hour.
Example Output: "12pm is the peak sales hour with 12345 orders"
*/
SELECT 
    EXTRACT(HOUR FROM orderdate) AS sales_hour, 
    COUNT(*) AS total_orders
FROM orders
GROUP BY sales_hour
ORDER BY total_orders DESC
LIMIT 1;



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

--Query to get all items containing allergens
SELECT DISTINCT i.name
FROM Item i
JOIN ItemIngredients ii ON i.ID = ii.drinkFlavorID
JOIN Inventory inv ON ii.inventoryId = inv.ID
WHERE inv.isAllergen = TRUE;

--Query to get top 3 used ingredients in the last month of sales
SELECT i.name AS ingredient_name, SUM(ii.quantity + ti.quantity) AS total_quantity
FROM Inventory i
LEFT JOIN ItemIngredients ii ON i.ID = ii.inventoryId
LEFT JOIN ToppingIngredients ti ON i.ID = ti.inventoryId
LEFT JOIN OrderItem oi ON ii.drinkFlavorID = oi.itemId
LEFT JOIN OrderItemToppings oit ON ti.toppingId = oit.toppingId
LEFT JOIN Orders o ON oi.orderId = o.ID OR oit.orderItemId = oi.ID
WHERE o.dateTime >= DATE_SUB(NOW(), INTERVAL 1 MONTH)
GROUP BY i.name
ORDER BY total_quantity DESC
LIMIT 3;


--Query to get 3 least performing employees, their hours, and their respective managers
SELECT e1.name AS EmployeeName, e1.hours, e2.name AS ManagerName
FROM Employee e1
LEFT JOIN Employee e2 ON e2.isManager = TRUE
ORDER BY e1.hours ASC
LIMIT 3;
