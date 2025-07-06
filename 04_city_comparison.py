from 02_temperature_modeling import temperature_model

cities = {
    'City A': (14, 55, 150),
    'City B': (12, 60, 20),
    'City C': (16, 40, 300)
}

for name, (t, h, a) in cities.items():
    temp = temperature_model(t, h, a)
    print(f"{name}: {temp:.2f}°C")