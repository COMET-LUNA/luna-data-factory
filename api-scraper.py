import config
import ApimedicClient
import json

apimedic = ApimedicClient.DiagnosisClient(config.username, config.password, config.priaid_authservice_url, config.language, config.priaid_healthservice_url)

body_locations = apimedic.loadBodyLocations()
with open('json/body_locations.json', 'w') as outfile:
  json.dump(body_locations, outfile)


# TODO: Add body locations to each symptom object.
# Algo:
# 1. Get all the IDs of body locations
# 2. Get all body symptoms per ID of body location and combine in one dictionary
# 3. Filter the body parts in body symptoms result to ids that exist IDs
# 4. Add symptoms from dictionary to each body locations
#    - If symptoms has 2 or more locations, add to general symptoms
body_ids = []

for x in body_locations:
  body_ids.append(x["ID"])

print(body_ids)

symptoms = apimedic.loadSymptoms()

with open('json/symptoms.json', 'w') as outfile:
  json.dump(symptoms, outfile)