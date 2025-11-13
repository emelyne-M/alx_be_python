# weather_advice.py

# Prompt user (exact text)
answer = input("What's the weather like today? (sunny/rainy/cold):").lower()

# Provide clothing recommendations
if answer == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif answer == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif answer == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
