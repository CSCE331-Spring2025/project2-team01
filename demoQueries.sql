/* 
Chosen By TA Dineth
(in order)
top 5 toppings
top 10 most popular items
profit and loss
top 10 highest spending customers 
3 least performing employee
*/

/* top 5 toppings */
SELECT 
    Toppings.type AS toppingName, 
    COUNT(OrderItemToppings.toppingId) AS totalSales
FROM OrderItemToppings
JOIN Toppings ON OrderItemToppings.toppingId = Toppings.ID
GROUP BY OrderItemToppings.toppingId, Toppings.type
ORDER BY totalSales DESC
LIMIT 5;

/* top 10 most popular items */
SELECT
    OrderItem.itemId,
    Item.name,
    Item.subFlavor,
    COUNT(*) as orderCount,
    SUM(OrderItem.subTotal) as totalRevenue
FROM OrderItem
JOIN item ON orderItem.itemId = item.ID
GROUP BY orderItem.itemId, item.name, item.subFlavor
ORDER BY totalRevenue DESC
LIMIT 10;

/* profit and loss */
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
ORDER BY WeeklyOrders.weekStart
LIMIT 10; 

/* top 10 highest spending customers */
SELECT 
    customername, 
    COUNT(*) AS total_orders
FROM orders
GROUP BY customername
ORDER BY total_orders
LIMIT 10;

/* 3 least performing employee */
SELECT e.ID, e.name, e.hours, 
       CASE WHEN e.isManager THEN 'Manager' ELSE 'Employee' END AS role, 
       COALESCE(SUM(o.totalPrice), 0) AS total_sales
FROM Employee e
LEFT JOIN Orders o ON e.ID = o.employeeId
GROUP BY e.ID, e.name, e.hours, e.isManager
ORDER BY total_sales ASC
LIMIT 3;