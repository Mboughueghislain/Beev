--a. Nombre total de voitures par modèle par pays--
SELECT make, model, country, COUNT(*) as total_cars
FROM public.consumer
GROUP BY make, model, country;

--b. Pays ayant le plus grand nombre de chaque modèle.
-- # création d'une sous requêtte
WITH Ranking AS (
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



--c Modèles vendus aux États-Unis mais pas en France.
SELECT DISTINCT Model
FROM consumer
WHERE Country = 'USA'
AND Model NOT IN (
    SELECT Model
    FROM consumer
    WHERE Country = 'France'
);

--d Coût emoyenne chaque voiture dans chaque pays selon le type de moteur.
SELECT Country, EngineType, AVG(SalesVolume) AS Moyenne_Cout
FROM consumer
GROUP BY Country, EngineType;

--e Evaluations moyennes des voitures électriques par rapport aux voitures thermiques.
SELECT AVG(review_score) AS score_moyen, car_type
FROM consumer
WHERE car_type IN ('Voiture Électrique', 'Voiture Thermique')
GROUP BY car_type;





