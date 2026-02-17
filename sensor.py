# Input
sensor_readings = [3, 4, 7, 8, 10, 12, 5]
valid_readings = []

for i in range(len(sensor_readings)):
    
    # Check if reading is even
    if sensor_readings[i] % 2 == 0:
        valid_readings.append((i, sensor_readings[i]))


print("Valid Sensor Readings (Hour, Value):")
print(valid_readings)