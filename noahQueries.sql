/*
Special Query #1: "Weekly Sales History"

    pseudocode: select count of orders grouped by week
    about: given a specific week, how many orders were placed?
    example: "week 1 has 98765 orders"
*/
SELECT 
    TO_CHAR(dateTime, 'IYYY-IW') AS week,  
    COUNT(*) AS total_orders
FROM Orders
GROUP BY week
ORDER BY week;

/*
Functional Query
Show the most popular 5 toppings by sales
*/

SELECT 
    T.type AS topping_name, 
    COUNT(OIT.toppingId) AS total_sales
FROM OrderItemToppings OIT
JOIN Toppings T ON OIT.toppingId = T.ID
GROUP BY OIT.toppingId
ORDER BY total_sales DESC
LIMIT 5;

/*
Functional Query
Show which employee had the most sales in dollars in december
*/

SELECT 
    E.name AS employee_name,
    SUM(O.totalPrice) AS total_sales
FROM Orders O
JOIN Employee E ON O.employeeId = E.ID
WHERE STRFTIME('%m', O.dateTime) = '12'  -- Filters for December
GROUP BY O.employeeId
ORDER BY total_sales DESC
LIMIT 1;  -- Gets the top employee
