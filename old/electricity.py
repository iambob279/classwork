previous_meter_reading = 0
current_meter_reading = 0
calorific_value = 39.3

current_meter_reading = int(input("What is your current meter reading? = "))
previous_meter_reading = int(input("What was your previous meter reading? = "))

def energycosts(previous_meter_reading, current_meter_reading, calorific_value):
    unit = current_meter_reading - previous_meter_reading
    kw = unit * 1.022 * (calorific_value / 3.6)
    cost = kw * 0.0284
    cost = round(cost, 2)
    print(f"£{cost}")

energycosts(previous_meter_reading, current_meter_reading, calorific_value)

