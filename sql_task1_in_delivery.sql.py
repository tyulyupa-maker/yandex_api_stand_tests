-- Задание 1: логины курьеров и количество их заказов "в доставке"
SELECT
c.login AS courier_login,
COUNT(o.id) AS orders_in_delivery
FROM "Couriers" AS c
JOIN "Orders"   AS o ON o."courierId" = c.id
WHERE o."inDelivery" = true
GROUP BY c.login
ORDER BY orders_in_delivery DESC
