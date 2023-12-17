from sortedcontainers import SortedDict

class FoodRatings:
    def __init__(self, foods, cuisines, ratings):
        self.food_to_cuisine = {}       # Maps food to its cuisine
        self.food_ratings = {}          # Maps food to its rating
        self.cuisine_ratings = {}       # Maps cuisine to SortedDict of foods by rating

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            # Initialize mappings
            self.food_to_cuisine[food] = cuisine
            self.food_ratings[food] = rating
            
            # Initialize SortedDict for each cuisine if not already initialized
            if cuisine not in self.cuisine_ratings:
                self.cuisine_ratings[cuisine] = SortedDict()
            
            # Insert food into the SortedDict of the corresponding cuisine
            # The key is a tuple (-rating, food) to sort first by rating (in reverse) and then lexicographically
            self.cuisine_ratings[cuisine][(-rating, food)] = food

    def changeRating(self, food, newRating):
        # Get the cuisine of the food
        cuisine = self.food_to_cuisine[food]
        
        # Remove the old rating from the SortedDict
        oldRating = self.food_ratings[food]
        del self.cuisine_ratings[cuisine][(-oldRating, food)]

        # Update the rating of the food
        self.food_ratings[food] = newRating

        # Add the new rating to the SortedDict
        self.cuisine_ratings[cuisine][(-newRating, food)] = food

    def highestRated(self, cuisine):
        # Return the first food item in the SortedDict of the given cuisine
        # This will be the food with the highest rating (and lexicographically smallest in case of a tie)
        return next(iter(self.cuisine_ratings[cuisine].values()))


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)