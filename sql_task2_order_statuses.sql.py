-- Задание 2: все трекеры и вычисленный статус
-- finished = 2, cancelled = -1, inDelivery = 1, иначе 0
SELECT
  "track",
   CASE
      WHEN "finished" = true THEN 2
       WHEN "cancelled" = true THEN - 1
        WHEN "inDelivery" = true THEN 1
        ELSE 0
    END AS status
FROM "Orders"
ORDER BY "track"
