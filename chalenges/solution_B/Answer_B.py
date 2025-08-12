# Given list of services with their ratings
services = [
    { "name": "Tutoring", "rating": 4.6 },
    { "name": "Food Delivery", "rating": 4.9 },
    { "name": "Tech Support", "rating": 4.3 },
    { "name": "Child Care", "rating": 4.8 }
]

# Sort services by rating in descending order and take the top 3
top_three_services = sorted(
    services,
    key=lambda service: service["rating"],
    reverse=True
)[:3]

# Output the result
print(top_three_services)