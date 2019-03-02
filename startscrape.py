import requests
from config import config_options

params = {
  "api_key": config_options["parsehub_api_key"],
  "start_url": config_options["page_to_scrape"],
  "start_template": "main_template",
  "send_email": "0"
}
r = requests.post("https://www.parsehub.com/api/v2/projects/{}/run".format(config_options["parsehub_project_id"]), data=params)

print(r.text)

