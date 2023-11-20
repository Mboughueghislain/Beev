a. Nombre total de voitures par modèle par pays
SELECT model, country, COUNT(*) as total_cars
FROM car_table
GROUP BY model, country;
