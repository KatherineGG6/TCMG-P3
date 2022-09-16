#Marketing wants to know two things: 
#How many total requests have been made in the 6 months?
#How many total requests were made in the time period represented by the log?

import requests

downloadUrl = "https://s3.amazonaws.com/tcmg476/http_access_log"

req = requests.get(downloadUrl)
