--a. Nombre total de voitures par modèle par pays--
SELECT make, model, country, COUNT(*) as total_cars
FROM public.consumer
GROUP BY make, model, country;

savoir quel pays a le plus grand nombre de chaque modèle.


savoir si un modèle est vendu aux États-Unis mais pas en France.

--savoir combien coûte en moyenne chaque voiture dans chaque pays selon le type de moteur.

--évaluations moyennes des voitures électriques par rapport aux voitures thermiques.
SELECT AVG(review sco) AS Prix_Moyen
FROM consumer
GROUP BY client




SELECT Departement, sum(Salary) AS total 
FROM employee 
GROUP BY Departement;-----------------