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


def generate_xyz(num_positions):
    positions = []
    for _ in range(num_positions):
        position = {
            "X": round(random.uniform(0, 1), 2),
            "Y": round(random.uniform(0, 1), 2),
            "Z": round(random.uniform(0, 1), 2),
        }
        positions.append(position)
    return positions


def generate_simulation_data(num_simulations=10):
    simulations = []

    for i in range(num_simulations):
        simulation = simulation_data_template.copy()
        simulation["SimulationId"] = f"sim{i}"
        start_time = datetime.strptime(
            simulation["StartTime"], "%Y-%m-%dT%H:%M:%S")
        end_time = datetime.strptime(
            simulation["EndTime"], "%Y-%m-%dT%H:%M:%S")

        for j in range(number_data):
            time = start_time + \
                timedelta(seconds=random.randint(
                    0, int((end_time - start_time).total_seconds())))
            time_str = time.strftime("%Y-%m-%dT%H:%M:%S")
            simulation["Speed"]["value"].append(random.randint(0, 100))
            simulation["Speed"]["time"].append(time_str)

            simulation["CarStatus"]["value"].append(random.randint(0, 1))
            simulation["CarStatus"]["time"].append(time_str)

            simulation["Accel"]["value"].append(random.randint(-10, 10))
            simulation["Accel"]["time"].append(time_str)

            simulation["Direction"]["value"].append(random.randint(-10, 10))
            simulation["Direction"]["time"].append(time_str)

            simulation["ServoAngle"]["value"].append(random.randint(-10, 10))
            simulation["ServoAngle"]["time"].append(time_str)

            simulation["EngineTemperature"]["value"].append(
                round(random.uniform(-15, 15), 1))
            simulation["EngineTemperature"]["time"].append(time_str)

            simulation["RPM"]["value"].append(random.randint(-10, 10))
            simulation["RPM"]["time"].append(time_str)

            simulation["Position"]["value"] = generate_xyz(number_data)
            # simulation["Position"]["value"].append(random.randint(-10, 10))
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
