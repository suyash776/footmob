from mobfot import MobFot
import json
client = MobFot()
a = client.get_matches_by_date("20240305")
# b= client.get_player(id=1000)
# client.get
json_formatted_str = json.dumps(a, indent=2)
print(json_formatted_str)