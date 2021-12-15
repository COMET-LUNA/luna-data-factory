import config
import ApimedicClient
import json
from itertools import chain

apimedic = ApimedicClient.DiagnosisClient(config.username, config.password, config.priaid_authservice_url, config.language, config.priaid_healthservice_url)

body_locations = apimedic.loadBodyLocations()
with open('json/body_locations.json', 'w') as outfile:
  json.dump(body_locations, outfile)


# TODO: Add body locations to each symptom object.
# Algo:
# 1. Get all the IDs of body locations
# 2. Get all body symptoms per ID of body location and combine in one dictionary
# 3. Filter the body parts in body symptoms result to ids that exist IDs
# 4. Remove dupes
# 5. Add symptoms from dictionary to each body locations
#    - If symptoms has 2 or more locations, add to general symptoms

# 1
body_ids = []

for x in body_locations:
  body_ids.append(x["ID"])

print("Body IDs done!")

# 2
body_symptoms_location = []

for x in body_ids:
  body_symptoms_location.append(apimedic.loadSublocationSymptoms(x, ApimedicClient.SelectorStatus.Man))

flattened_body_symptoms_location = list(chain.from_iterable(body_symptoms_location))

print("Body Symptom Locations done!")

# 3
filtered_body_symptoms_location = []
for x in flattened_body_symptoms_location:
  current_bsl = x
  filtered_healthlocationids = []
  
  for y in body_ids:
    for z in x["HealthSymptomLocationIDs"]:
      if y == z:
        filtered_healthlocationids.append(y)

  current_bsl["HealthSymptomLocationIDs"] = filtered_healthlocationids

  filtered_body_symptoms_location.append(current_bsl)

# print(filtered_body_symptoms_location[0]["HealthSymptomLocationIDs"])

# 4
unique_filtered_bsl = []

for x in filtered_body_symptoms_location:
  if x not in unique_filtered_bsl:
    unique_filtered_bsl.append(x)

with open('json/body_symptoms.json', 'w') as outfile:
  json.dump(unique_filtered_bsl, outfile)

# symptoms = apimedic.loadSymptoms()

# with open('json/symptoms.json', 'w') as outfile:
#   json.dump(symptoms, outfile)

print("Formatting and polishing done!")

# 5

for body_part in body_locations:
  symptom_list = []
  for symptom in unique_filtered_bsl:
    if body_part['ID'] in symptom['HealthSymptomLocationIDs']:
      symptom_list.append(symptom)
  body_part['symptoms'] = symptom_list

# 5. For General Symptoms (if exists in 2 or more locations)
general_symptom_list = []

for x in unique_filtered_bsl:
  if len(x['HealthSymptomLocationIDs']) >= 2:
    general_symptom_list.append(x)
body_locations.append(general_symptom_list)

with open('json/body_locations_symptoms.json', 'w') as outfile:
  json.dump(body_locations, outfile)

print('Final body location with symptoms done!')