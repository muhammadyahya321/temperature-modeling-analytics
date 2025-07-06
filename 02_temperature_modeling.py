def temperature_model(t, h, a):
    return (
        31.285 + 0.7046*t - 0.0122*h - 0.0161*a - 0.0228*t**2 - 0.0003*t*h
        + 0.0003*t*a + 0.0200*h**2 - 0.0001*h*a - 0.0007*a**2
    )

# Example usage
print("Predicted Temp at (14, 45, 100):", temperature_model(14, 45, 100))