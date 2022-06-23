import requests
import json
conurl = 'http://opmv:8083/connectors'
myobj = {'somekey': 'somevalue'}
headers = {
    'Accept': 'application/json'
}
#'Content-Type', 'application/json'

connectors_res = requests.get(conurl, headers=headers)
connectors = json.loads(connectors_res.text)
allcons = {}
for c in connectors:
    conf_res = requests.get(conurl+"/{}/config".format(c))
    allcons[c] = conf_res.text.replace('","','",'+"\n"+'"')

for key in allcons:
    cfile1 = open('./connect_configs/{}.json'.format(key), 'w')
    cfile1.write(allcons[key])

#connectors_res = requests.post(url, json={
#
#})
