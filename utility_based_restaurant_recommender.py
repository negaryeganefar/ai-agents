import math


def utility_function(restaurant, user):
    food_score = restaurant['food_quality']
    price_score = 10 - restaurant['price']
    distance = math.sqrt((restaurant['x'] - user['x']) ** 2 + (restaurant['y'] - user['y']) ** 2)
    location_score = 10 / (1 + distance)
    return (user['food_weight'] * food_score +
            user['price_weight'] * price_score +
            user['location_weight'] * location_score)


restaurants = [
    {'name': 'Restaurant A', 'food_quality': 8, 'price': 6, 'x': 0, 'y': 0},
    {'name': 'Restaurant B', 'food_quality': 9, 'price': 9, 'x': 0, 'y': 1},
    {'name': 'Restaurant C', 'food_quality': 5, 'price': 2, 'x': 1, 'y': 1},
    {'name': 'Restaurant D', 'food_quality': 7, 'price': 4, 'x': 1, 'y': 0},
]

user_x = float(input("Enter your location x: "))
user_y = float(input("Enter your location y: "))
food_weight = float(input("Food quality importance (0-10): "))
price_weight = float(input("Price importance (0-10): "))
location_weight = float(input("Location importance (0-10): "))

user = {'x': user_x, 'y': user_y,
        'food_weight': food_weight,
        'price_weight': price_weight,
        'location_weight': location_weight}

scores = []
for r in restaurants:
    scores.append((utility_function(r, user), r['name']))
scores.sort(reverse=True)

print("Recommendations (best first):")
for score, name in scores:
    print(f"{name}: utility = {score:.2f}")

print("Best choice:", scores[0][1])
