import config
import ApimedicClient
import json

apimedic = ApimedicClient.DiagnosisClient(config.username, config.password, config.priaid_authservice_url, config.language, config.priaid_healthservice_url)

with open('json/body_locations.json', 'w') as outfile:
  json.dump(apimedic.loadBodyLocations(), outfile)


# TODO: Add body locations to each symptom object.
symptoms = apimedic.loadSymptoms()

with open('json/symptoms.json', 'w') as outfile:
  json.dump(symptoms, outfile)