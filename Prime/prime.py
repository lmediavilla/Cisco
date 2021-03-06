#/usr/bin/python3
import json
import sys
import requests

LOGINUSER = 'xxxx'
LOGINPASSWORD = 'xxxx'
PRIMEIP = 'a.b.c.d'

def user(username):
    requests.packages.urllib3.disable_warnings()
    url = 'https://'+PRIMEIP+'/webacs/api/v2/data/ClientDetails.json?userName=contains("'+username+'")'
    response = requests.get(url, auth=(LOGINUSER, LOGINPASSWORD), verify=False)
    if response.status_code != 200:
        print("Error: "+str(response.status_code))
        input()
        sys.exit()
    output = response.json()
    response.close()
    object = output['queryResponse']
    try:
        entityId = object['entityId']
    except Exception:
        print('User not found')
        sys.exit()
    for entity in entityId:
        url = entity["@url"]
        json = '.json'
        url = url + json;
        response= requests.get(url,auth=(LOGINUSER,LOGINPASSWORD), verify=False)
        clientRaw = response.json()
        response.close
        client = clientRaw['queryResponse']['entity']
        print('-----------------------------------------------')
        try:
            print('User: '+client[0]['clientDetailsDTO']['userName'])
        except Exception:
            pass
        try:        
            print('Status: '+client[0]['clientDetailsDTO']['status'])
        except Exception:
            pass        
        try:
            print('IP: '+client[0]['clientDetailsDTO']['ipAddress']['address']) 
        except Exception:
            pass
        try:
            print('Mac: '+client[0]['clientDetailsDTO']['macAddress'])
        except Exception:
            pass
        try:
            print('WirelessController: '+client[0]['clientDetailsDTO']['deviceName'])
        except Exception:
            pass
        try:
            print('Ap: '+client[0]['clientDetailsDTO']['apName'])
        except Exception:
            pass
        try:
            print('Location: '+client[0]['clientDetailsDTO']['location'])
        except Exception:
            pass
        try:
            print('SSID: '+client[0]['clientDetailsDTO']['ssid'])
        except Exception:
            pass
        try:
            print('Vlan: '+client[0]['clientDetailsDTO']['vlan'])
        except Exception:
            pass
        try:
            print('Vendor: '+client[0]['clientDetailsDTO']['vendor'])
        except Exception:
            pass
        try:
            print('ccxVersion: '+client[0]['clientDetailsDTO']['ccxVersion'])
        except Exception:
            pass
def mac( macaddress ):
    "This prints a passed string into this function"
    requests.packages.urllib3.disable_warnings()
    url = 'https://'+PRIMEIP+'/webacs/api/v2/data/ClientDetails.json?macAddress=contains("'+macaddress+'")'
    response = requests.get(url,auth=(LOGINUSER,LOGINPASSWORD), verify=False)
    if response.status_code != 200:
        print("Error: "+str(response.status_code))
        input()
        sys.exit()
    output = response.json()
    response.close()
    object = output['queryResponse']
    output = response.json()
    response.close()
    object = output['queryResponse']
    try:
        entityId = object['entityId']
    except Exception:
        print('Device not found')
        sys.exit()
    for entity in entityId:
        url = entity["@url"]
        json = '.json'
        url = url + json;
        response= requests.get(url,auth=(LOGINUSER,LOGINPASSWORD), verify=False)
        clientRaw = response.json()
        response.close
        client = clientRaw['queryResponse']['entity']
        print('-----------------------------------------------')
        try:
            print('Mac: '+client[0]['clientDetailsDTO']['macAddress'])
        except Exception:
            pass        
        try:
            print('Switch: '+client[0]['clientDetailsDTO']['deviceName'])
        except Exception:
            pass        
        try:
            print('SwitchIp: '+client[0]['clientDetailsDTO']['deviceIpAddress']['address'])
        except Exception:
            pass        
        try:
            print('Port: '+client[0]['clientDetailsDTO']['clientInterface'])
        except Exception:
            pass        
        try:
            print('Vlan: '+client[0]['clientDetailsDTO']['vlan'])
        except Exception:
            pass        
        try:
            print('Vlan Name: '+client[0]['clientDetailsDTO']['vlanName'])
        except Exception:
            pass        
        try:
            print('Port Description: '+client[0]['clientDetailsDTO']['ifDescr'])
        except Exception:
            pass
        try:    
            print('Port Speed: '+client[0]['clientDetailsDTO']['speed'])
        except Exception:
            pass
if len(sys.argv) < 3:
    raise ValueError('prime.py -user/-mac followerd by user or mac, the mac in dot notation')
if sys.argv[1] == "-user":
    user(sys.argv[2])
elif sys.argv[1] == '-mac':
    mac(sys.argv[2])
else:
    raise ValueError('prime.py -user/-mac followerd by user or mac, the mac in dot notation')
