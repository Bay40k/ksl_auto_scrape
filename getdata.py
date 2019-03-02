import requests
from config import config_options

def retrieveData():
	params = {
	  "api_key": config_options["parsehub_api_key"],
	  "format": "json"
	}
	r = requests.get('https://www.parsehub.com/api/v2/projects/{}/last_ready_run/data'.format(config_options["parsehub_project_id"]), params=params)
	data = r.json()

	emailString = "Date: {}\n".format(data["date"])

	for car in data["car"]:
		emailString += ("\n{} {} {}\n".format(car["year"], car["make"], car["model"]))
		emailString += ("Price: {}\n".format(car["price"]))

		mileage = car["mileage"]
		if len(mileage) == 3:
			mileage += "000"

		emailString += ("Milege: {}\n".format(mileage))
		emailString += ("URL: https://www.ksl.com{}\n".format(car["URL"]))
		emailString += ("Up for: {}\n".format(car["upFor"]))
		emailString += ("Description: \n{}\n".format(car["description"].encode('utf-8')))
		emailString += ("\n============================================\n")

	return [emailString, data["date"]]
