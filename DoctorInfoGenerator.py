import names
import random
import json

# DATA HERE
specializations = ['Internal Medicine','Cardiology','Respiratory','Orthopedic']
price_range = []
clinic_location = []
clinic_address = []
med_school = []
sex = ['Male', 'Female']
# FOR BIRTHYEAR AND MED START YEAR, randomize birth year from 1950 to 1995 and add 21 years to it for med start year

doctor_list = []

# GENERATE doctor_size NUMBER OF DOCTORS
doctor_size = 100

for x in range(doctor_size):
  doctor = {}
  doctor["sex"] = sex[random.randint(0,len(sex)-1)]
  print(doctor["sex"])
  if doctor["sex"] == 'Male':
    doctor["name"] = names.get_full_name(gender='male')
  else:
    doctor["name"] = names.get_full_name(gender='female')
  doctor["specialization"] = specializations[random.randint(0,len(specializations)-1)]

  doctor_list.append(doctor)

# EXPORT LIST AS A JSON FILE
# print(doctor_list)

with open("sample.json", "w") as outfile:
  json.dump(doctor_list, outfile)