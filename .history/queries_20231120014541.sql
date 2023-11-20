--a. Nombre total de voitures par modèle par pays--
SELECT make, model, country, COUNT(*) as total_cars
FROM public.consumer
GROUP BY make, model, country;

savoir quel pays a le plus grand nombre de chaque modèle.


