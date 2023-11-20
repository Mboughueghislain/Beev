--a. Nombre total de voitures par modèle par pays--
SELECT make, model, country, COUNT(*) as total_cars
FROM public.consumer
GROUP BY make, model, country;

--b. Savoir quel pays a le plus grand nombre de chaque modèle.
WITH RankedModels AS (
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


savoir si un modèle est vendu aux États-Unis mais pas en France.

--savoir combien coûte en moyenne chaque voiture dans chaque pays selon le type de moteur.

--évaluations moyennes des voitures électriques par rapport aux voitures thermiques.
SELECT AVG(review Score) AS Score_Moyen
FROM consumer
GROUP BY client




