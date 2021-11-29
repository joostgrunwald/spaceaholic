# druktevoorspeller
import requests
from amadeus import Client, ResponseError

busyness = False 


url = "https://besttime.app/api/v1/forecasts"


routeurl1 = "https://api.openrouteservice.org/v2/directions/"
routeurl2 = "?api_key="
keyopenroute = '5b3ce3597851110001cf6248f16eb51a05ef4c08ac9f153c82c1c311'

# amadeus = Client(
#     client_id='C41IKhjez4X2jHx2hIuhEXeG701mTlGM',
#     client_secret='cr1AXkPhUnOE92SF'
# )

# safety scores from amadeus
vondelpark = [73, 78, 70, 89, 64, 81, 69]
amstelpark = [74, 80, 70, 89, 63, 78, 76]
flevopark = [74, 78, 70, 89, 62, 79, 76]
gaasperplas = [76, 85, 60, 90, 63, 79, 73]
oosterpark = [73, 78, 70, 90, 62, 77, 75]
sarphatipark = [73, 77, 70, 90, 69, 80, 66]
bijlmerpark = [60, 75, 55, 88, 65, 55, 61]

vondelparkc = [52.3579946, 4.8686484]
amstelparkc = [52.3307494, 4.8931539]
flevoparkc = [52.3620113, 4.9491089]
gaasperplasc = [52.3058653, 4.994065]
oosterparkc = [52.3589699, 4.9209303]
sarphatiparkc = [52.3545723, 4.8964731]
bijlmerparkc = [52.3114185, 4.96367306422919]
# lat = 52.3579946
# long = 4.8686484

#latn = lat + 0.042
#lats =  lat - 0.042
#longe = lat + 0.042
#longw = lat - 0.042
modes = ["driving-car", "cycling-regular", "foot-walking", "wheelchair"]

#TODO: adjust for location
urlroute = routeurl1 + modes[0] + routeurl2 + keyopenroute + "&start=" + str(vondelparkc[1]) + ',' + str(vondelparkc[0]) + "&end=" + str(amstelparkc[1]) + "," + str(amstelparkc[0])
responser = requests.request("GET", urlroute)
responser = str(responser.json())
responser = responser[:responser.find("geometry")]

instructions = []
# try:
#     response = amadeus.safety.safety_rated_locations.get(
#         latitude=lat,
#         longitude=long,
#         radius=20)
#     safetydata = str(response.data)
#     safetysi = safetydata.find("safetyScores")
#     safetyw = safetydata.find("women")
#     safetyscore = safetydata[safetysi:safetyw+11]
#     print(safetydata)
#     print(safetyscore)
# except ResponseError as error:
#     print(error)

if busyness:
    #url = "https://besttime.app/api/v1/keys/pri_4b3f3864c9ae4c8b9442272859e52cde"
    params = {
        'api_key_private': 'pri_4b3f3864c9ae4c8b9442272859e52cde',
        'venue_name': 'Vondelpark',
        'venue_address': 'Amsterdam'
    }

    response = requests.request("POST", url, params=params)

    responses = requests.request("GET", url)
    print(responses.json())

    response2 = response
    response = str(response.json())

    park = response.find("'venue_type': 'PARK'") != -1
    busyin = response.find("busy_hours")
    quietin = response.find("quiet_hours")
    peakin = response.find("peak_hours")

    peoplecome = response.find("most_people_come")
    peopleleave = response.find("most_people_leave")
    hourin = response.find("hour_analysis")

    busyhours = response[busyin:quietin-2]
    quiethours = response[quietin:peakin-2]

    peoplecomed = response[peoplecome:peopleleave-2]
    peopleleaved = response[peopleleave:hourin-2]

    day_rawi = response.find("day_raw")
    subs = response[day_rawi:]
    day_infoi = subs.find("]")

    raw_data = response[day_rawi:day_rawi + day_infoi+1]

    if park:
        print("The venue is a park")

    print("" + busyhours)
    print("" + quiethours)
    print("" + peoplecomed)
    print("" + peopleleaved)
    print("" + raw_data)
