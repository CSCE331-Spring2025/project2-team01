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

