import numpy  as np
from sklearn.metrics.pairwise import cosine_similarity
from .models import FoodPlace

def recommend_food_ml(destination, top_n=3):
    """
    Recommend top food places using ML 
    """
    food_places = FoodPlace.objects.filter(destination=destination)
    if not food_places.exists():
        return[]
    

    #step 1: Build feature matrix 
    cuisines = list(set(fp.cuisine for fp in food_places))
    cuisine_to_index ={cuisine: idx for idx, cuisine in enumerate(cuisine)}

    X = []
    for fp in food_places:
        #one-hot encode cuisine +rating
        features =[0] * len(cuisines)
        features[cuisine_to_index[fp.cuisine]] = 1
        features.append(fp.rating) # add rating as numeric feature
        X.append(features)

        X= np.array(X)

        # Step 2: Compute similarity 
        similarity = cosine_similarity(X)

        # Step 3: Pick top places( Highest average similarity +rating)
        avg_scores = similarity.mean(axis=1)
        scored_places = sorted(
            zip(food_places, avg_scores),
            key=lambda x: (x[1], x[0].rating), #Prioritize similarity & rating
            reverse=True
        )

        return [fp for fp, score in scored_places[:top_n]]
    