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
SELECT 
    TOCHAR(orderDate, 'DD Mon') AS orderDay,
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
        SUM(payGrade * 'hours') AS totalEmployeeExpense
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
ORDER BY WeeklyOrders.week_start;

