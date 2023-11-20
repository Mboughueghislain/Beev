--a. Nombre total de voitures par modèle par pays--
SELECT make, model, country, COUNT(*) as total_cars
FROM public.consumer
GROUP BY make, model, country;

--b. Pays ayant le plus grand nombre de chaque modèle.
-- # Etape 1: création d'une sous requêtte :)
WITH Ranking AS 
(
    SELECT
        country,
        model,
        COUNT(*) AS model_count,
        RANK() OVER (PARTITION BY country ORDER BY COUNT(*) DESC) AS rank
    FROM
        consumer
    GROUP BY
        country, model
)
SELECT
    country,
    model,
    model_count
FROM
    RankedModels
WHERE
    rank = 1;



--c. Modèles vendus aux États-Unis mais pas en France.
SELECT DISTINCT Model
FROM consumer
WHERE Country = 'USA'
AND Model NOT IN 
(
    SELECT Model
    FROM consumer
    WHERE Country = 'France'
);

--d. Coût moyen de chaque voiture dans chaque pays selon le type de moteur.
SELECT
    c.Country,
    c.Make,
    c.Model,
    c.Year,
    c.ReviewScore,
    c.SalesVolume,
    AVG(cr.Price) AS AverageCarCost
FROM
    consumer as c
JOIN
    car as cr ON c.Make = cr.Make AND c.Model = cr.Model
GROUP BY
    c.Country,
    c.Make,
    c.Model,
    c.Year,
    c.ReviewScore,
    c.SalesVolume;

--e. Evaluation moyenne des voitures électriques par rapport aux voitures thermiques.
SELECT AVG(review_score) AS score_moyen, car_type
FROM consumer
WHERE car_type IN ('Voiture Électrique', 'Voiture Thermique')
GROUP BY car_type;

SELECT
    c.Country,
    c.Make,
    c.Model,
    c.Year,
    c.ReviewScore,
    c.SalesVolume,
    AVG(cr.Price) AS AverageCarCost
FROM
    consumer c
JOIN
    car cr ON c.car_type = cr.car_type
GROUP BY
    c.Country,
    c.Make,
    c.Model,
    c.Year,
    c.ReviewScore,
    c.SalesVolume;




