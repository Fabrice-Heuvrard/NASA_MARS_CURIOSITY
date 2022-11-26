import requests
import urllib

api_key = #YOUR API KEY

parameters = {"api_key":api_key}

Camera = 'NAVCAM'
#cameras: [ "CHEMCAM", "FHAZ", "MARDI", "RHAZ", "NAVCAM"]}

sol = 3662
#24/11/2022 = 3662

URL_request = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=' + str(sol) + '=&camera='+ Camera + '&api_key=' + str(api_key)

URL_json = requests.get(URL_request,params=parameters).json()

for i in range(len(URL_json['photos'])):
    print(URL_json['photos'][i]['img_src'])
    Nom_du_fichier = 'Sol ' + str(URL_json['photos'][i]['sol'])+ " - ID "+str(URL_json['photos'][i]['id']) + " - "+ str(URL_json['photos'][i]['rover']['name']) + " " + Camera + " " + str(URL_json['photos'][i]['earth_date'])+ ".jpg"
    urllib.request.urlretrieve(URL_json['photos'][i]['img_src'],Nom_du_fichier)

print("....Download successful !")


