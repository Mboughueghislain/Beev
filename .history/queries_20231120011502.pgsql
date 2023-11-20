a. Nombre total de voitures par modèle par pays
SELECT Model, Country, COUNT(*) as total_cars
FROM consumer
GROUP BY  Model, Country;

