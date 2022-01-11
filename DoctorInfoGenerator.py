import names
import random
import json

# DATA HERE
specializations = ["Internal Medicine", "Cardiology", "Gastroenterology"]
price_range = ["100-500","501-1000", "1001-2000", "2000+"]
clinic_location = [
  ["Philippine General Hospital", "Manila Doctors Hospital", "Manila Medical Center"], 
  ["St. Luke's Medical Center"],
  ["Zamboanga Peninsula Medical Center", "West Metro Medical Center"],
  ["Southern Philippines Medical Center", "Davao Doctors Hospital"]
  ]
clinic_address = ["Manila City", "Quezon City", "Zamboanga City", "Davao City"]
med_school = ["UP","UERM", "UST", "ADMU", "St.Luke's", "FEU", "ADZU", "Davao Doctor's College"]
sex = ['Male', 'Female']
# FOR BIRTHYEAR AND MED START YEAR, randomize birth year from 1950 to 1995 and add 26 years to it for med start year

doctor_list = []

# GENERATE doctor_size NUMBER OF DOCTORS
doctor_size = 100

for x in range(doctor_size):
  doctor = {}
  doctor["sex"] = sex[random.randint(0,len(sex)-1)]
  # print(doctor["sex"])
  if doctor["sex"] == 'Male':
    doctor["name"] = names.get_full_name(gender='male')
  else:
    doctor["name"] = names.get_full_name(gender='female')
  doctor["specialization"] = specializations[random.randint(0,len(specializations)-1)]
  doctor["price_range"] = price_range[random.randint(0,len(price_range)-1)]

  clinic_address_rand = random.randint(0,len(clinic_address)-1)
  doctor["clinic_address"] = clinic_address[clinic_address_rand]
  doctor["clinic_location"] = clinic_location[clinic_address_rand][random.randint(0,len(clinic_location[clinic_address_rand])-1)]
  doctor["med_school"] = med_school[random.randint(0,len(med_school)-1)]
  doctor["birthyear"] = random.randrange(1950,1995,1)
  doctor["startyear"] = doctor["birthyear"] + 26 + random.randrange(0,3,1)

  doctor_list.append(doctor)

# EXPORT LIST AS A JSON FILE
# print(doctor_list)

with open("json/doctors.json", "w") as outfile:
  json.dump(doctor_list, outfile)