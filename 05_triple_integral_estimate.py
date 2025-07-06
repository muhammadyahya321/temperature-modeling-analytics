from scipy.integrate import tplquad
from 02_temperature_modeling import temperature_model

t_lower, t_upper = 5, 10
h_lower, h_upper = 40, 60
a_lower, a_upper = 10, 500

def integrand(a, h, t):
    return temperature_model(t, h, a)

result, error = tplquad(integrand, t_lower, t_upper,
                        lambda t: h_lower, lambda t: h_upper,
                        lambda t,h: a_lower, lambda t,h: a_upper)

print(f"Triple integral (temperature load): {result:.2f}°C")
print(f"Estimated error: {error:.2e}")