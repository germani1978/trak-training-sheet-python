from datetime import datetime
import requests
import claves 


GENDER = "male"
WEIGHT_KG = "90"
HEIGHT = "160.5"
AGE = "44"

GENDER = "MALE"
WEIGHT_KG = "60"
HEIGHT = "160.5"  # entered random height in cm
AGE = "50"


exercise_input = "ran 3 miles and jump 20 min"

sheet_inputs = {}

header = {"x-app-id": claves.APP_ID, "x-app-key": claves.API_KEY}

parameters = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT,
    "age": AGE,
}

response = requests.post(url=claves.exercise_endpoint, json=parameters, headers=header)
response.raise_for_status()
result = response.json()



today_date = datetime.now().strftime("%d%m%y")
now_time = datetime.now().strftime("%x")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    sheet_response = requests.post(claves.sheet_endpoint, json=sheet_inputs, auth=(claves.USER,claves.PASSWORD))





