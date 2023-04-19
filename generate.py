import random
import json
from datetime import datetime, timedelta

number_data = 20

simulation_data_template = {
    "SimulationId": "sim0",
    "SimulationName": "Test Simulation Created by Jhao-Ting Chen",
    "StartTime": "2023-03-17T00:52:14",
    "EndTime": "2023-03-18T00:52:14",
    "CarId": "Tesla",
    "TrackId": "easy1",
    "gps": [],
    "Speed": {
        "value": [],
        "time": []
    },
    "CarStatus": {
        "value": [],
        "time": []
    },
    "Accel": {
        "value": [],
        "time": []
    },
    "Direction": {
        "value": [],
        "time": []
    },
    "ServoAngle": {
        "value": [],
        "time": []
    },
    "EngineTemperature": {
        "value": [],
        "time": []
    },
    "RPM": {
        "value": [],
        "time": []
    },
    "Position": {
        "value": [],
        "time": []
    },
    "Yaw": {
        "value": [],
        "time": []
    },
    "Pitch": {
        "value": [],
        "time": []
    },
    "Roll": {
        "value": [],
        "time": []
    },
}


# "$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47"
def generate_gps(num_positions):
    # print("called")
    gps_data = []
    randomNum = random.randint(0, 30)
    for i in range(num_positions):
        gps = "$GPGGA,"
        gps += str(123500 + i + randomNum)
        gps += ","
        gps += str(4807 + i * 0.02 + randomNum)
        gps += ",N,"
        gps += str(11131 + i * 0.01 + randomNum)
        gps += ",E,1,08,0.9,545.4,M,46.9,M,,*46"
        gps_data.append(gps)
    # print(gps_data)
    return gps_data


def generate_xyz(num_positions):
    positions = []
    X = round(random.uniform(0, 1), 2)
    Y = round(random.uniform(0, 1), 2)
    Z = round(random.uniform(0, 1), 2)
    for i in range(num_positions):
        position = {
            "X": round ( X + i*0.01 + round(random.uniform(-0.05, 0.05), 2), 2),
            "Y": round ( Y + i*0.01 + round(random.uniform(-0.05, 0.05), 2), 2),
            "Z": round ( Z + i*0.01 + round(random.uniform(-0.05, 0.05), 2), 2),
        }
        positions.append(position)
    return positions


def generate_num(num_positions, a, b):
    positions = []
    num = random.randint(a, b)
    nums = []
    nums.append(num)
    for i in range(num_positions):
        num = num + random.randint(-2, 2)
        nums.append(num)
    return nums


def generate_status(num_positions):
    if num_positions <= 0: 
      return []
    count = random.randint(2, 5)
    count = min(count, num_positions)
    num = random.randint(0, 1)
    value = []
    for _ in range(count):
      value.append(num)
    return value + generate_status(num_positions - count)



def generate_simulation_data(num_simulations=10):
    simulations = []

    for i in range(num_simulations):
        simulation = simulation_data_template.copy()
        simulation["SimulationId"] = f"sim{i}"
        start_time = datetime.strptime(
            simulation["StartTime"], "%Y-%m-%dT%H:%M:%S")
        end_time = datetime.strptime(
            simulation["EndTime"], "%Y-%m-%dT%H:%M:%S")
        
        results = generate_gps(number_data)
        simulation["gps"] = results

        for j in range(number_data):
            time = start_time + \
                timedelta(seconds=random.randint(
                    0, int((end_time - start_time).total_seconds())))
            time_str = time.strftime("%Y-%m-%dT%H:%M:%S")

            simulation["Speed"]["value"] = generate_num(number_data, 0, 100)
            simulation["Speed"]["time"].append(time_str)

            simulation["CarStatus"]["value"] = generate_status(number_data)
            simulation["CarStatus"]["time"].append(time_str)

            simulation["Accel"]["value"] = generate_num(number_data, -10, 10)
            simulation["Accel"]["time"].append(time_str)

            simulation["Direction"]["value"] = generate_num(number_data, -10, 10)
            simulation["Direction"]["time"].append(time_str)

            simulation["ServoAngle"]["value"] = generate_num(number_data, -10, 10)
            simulation["ServoAngle"]["time"].append(time_str)

            simulation["EngineTemperature"]["value"] = generate_num(number_data, -15, 15)
            simulation["EngineTemperature"]["time"].append(time_str)

            simulation["RPM"]["value"] = generate_num(number_data, -10, 10)
            simulation["RPM"]["time"].append(time_str)

            simulation["Position"]["value"] = generate_xyz(number_data)
            simulation["Position"]["time"].append(time_str)

            simulation["Yaw"]["value"] = generate_xyz(number_data)
            # simulation["Yaw"]["value"].append(random.randint(-10, 10))
            simulation["Yaw"]["time"].append(time_str)

            simulation["Pitch"]["value"] = generate_xyz(number_data)
            # simulation["Pitch"]["value"].append(random.randint(-10, 10))
            simulation["Pitch"]["time"].append(time_str)

            simulation["Roll"]["value"] = generate_xyz(number_data)
            # simulation["Roll"]["value"].append(random.randint(-10, 10))
            simulation["Roll"]["time"].append(time_str)

        simulations.append(simulation)

    return simulations


num_simulations_test = 5


for index in range(num_simulations_test):
    simulation_data = generate_simulation_data(1)
    # Save the data into a JSON file
    with open("./" + str(index), "w") as outfile:
        json.dump(simulation_data, outfile, indent=2)
        