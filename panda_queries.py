# a. Nombre total de voitures par modèle par pays
total_cars_by_model_country = consumer_df.groupby(['make', 'model', 'country']).size().reset_index(name='total_cars')
 
# b. Pays ayant le plus grand nombre de chaque modèle
model_counts = consumer_df.groupby(['country', 'model']).size().reset_index(name='model_count')
model_counts['rank'] = model_counts.groupby('country')['model_count'].rank(method='dense', ascending=False)
top_models_by_country = model_counts[model_counts['rank'] == 1]
 
# c. Modèles vendus aux États-Unis mais pas en France
usa_models = consumer_df[consumer_df['country'] == 'USA']['model']
france_models = consumer_df[consumer_df['country'] == 'France']['model']
models_in_usa_not_france = usa_models[~usa_models.isin(france_models)].drop_duplicates()
 
# d. Coût moyen de chaque voiture dans chaque pays selon le type de moteur
merged_df = consumer_df.merge(car_df, on=['make', 'model'])
average_cost = merged_df.groupby(['country', 'make', 'model', 'year', 'review_score', 'sales_volume'])['price'].mean().reset_index(name='average_car_cost')
 
# e. Evaluation moyenne des voitures électriques par rapport aux voitures thermiques
# (Assuming 'electric' and 'thermal' are distinguished by a column in 'car_df', e.g., 'engine_type')
# and 'review_score' is a column in 'car_df'
avg_review_score = merged_df.groupby(['make', 'model', 'year', 'engine_type'])['review_score'].mean().reset_index(name='score_moyen')