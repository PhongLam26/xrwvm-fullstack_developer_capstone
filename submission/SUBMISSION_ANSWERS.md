# Submission answers — 27 questions

All 27 answer slots now have real evidence. IBM Code Engine is running in the Skills Network lab. Data survives page reloads; durability across container replacement is not established. Prior grading attempt: 29/50. The updated submission has not been graded.


## Q1

https://github.com/PhongLam26/xrwvm-fullstack_developer_capstone/blob/main/README.md

## Q2



```text
PS> .venv\Scripts\python.exe -u server/manage.py runserver 127.0.0.1:8010 --noreload
Performing system checks...

System check identified no issues (0 silenced).
October 30, 2026 - 22:04:40
Django version 5.2.18, using settings 'djangoproj.settings'
Starting development server at http://127.0.0.1:8010/
Quit the server with CTRL-BREAK.

WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.
For more information on production servers see: https://docs.djangoproject.com/en/5.2/howto/deployment/

```

## Q3

https://github.com/PhongLam26/xrwvm-fullstack_developer_capstone/blob/main/server/frontend/static/About.html

## Q4

https://github.com/PhongLam26/xrwvm-fullstack_developer_capstone/blob/main/server/frontend/static/Contact.html

## Q5


```text
$ curl.exe -s -X POST -b $cookieJar -c $cookieJar -H "Referer: https://cars-web.2gkdcb8j96ze.us-south.codeengine.appdomain.cloud/" -H "X-CSRFToken: $csrf" -H "Content-Type: application/json" --data-raw "{\"userName\": \"capstone_cloud\", \"password\": \"<REDACTED_VALID_TEST_PASSWORD>\"}" https://cars-web.2gkdcb8j96ze.us-south.codeengine.appdomain.cloud/djangoapp/login
{"status": "Authenticated", "userName": "capstone_cloud", "firstName": "Demo", "lastName": "Driver"}
Password and session values redacted.

```

## Q6


```text
$ curl.exe -s -X GET -b $cookieJar -c $cookieJar -H "Referer: https://cars-web.2gkdcb8j96ze.us-south.codeengine.appdomain.cloud/" -H "X-CSRFToken: $csrf" -H "Content-Type: application/json" https://cars-web.2gkdcb8j96ze.us-south.codeengine.appdomain.cloud/djangoapp/logout
{"userName": "", "status": 200, "message": "Logged out."}
Password and session values redacted.

```

## Q7

https://github.com/PhongLam26/xrwvm-fullstack_developer_capstone/blob/main/server/frontend/src/components/Register/Register.jsx

## Q8

$ curl.exe --silent --show-error --fail-with-body http://127.0.0.1:3030/fetchReviews/dealer/8
[{"_id":"6ae4ad0b52a1f6200cf50cc3","id":51,"name":"Capstone Demo Reviewer","dealership":8,"review":"Friendly team and a smooth, helpful buying experience.","purchase":true,"purchase_date":"2024-06-15","car_make":"Toyota","car_model":"Camry","car_year":2022,"sentiment":"positive","__v":0}]
Exit code: 0

## Q9

$ curl.exe --silent --show-error --fail-with-body http://127.0.0.1:3030/fetchDealers
[{"_id":"6ae4ad0b52a1f6200cf50c5d","id":1,"city":"El Paso","state":"Texas","address":"3 Nova Court","zip":"88563","lat":"31.6948","long":"-106.3","short_name":"Holdlamis","full_name":"Holdlamis Car Dealership","__v":0},{"_id":"6ae4ad0b52a1f6200cf50c5e","id":2,"city":"Minneapolis","state":"Minnesota","address":"6337 Butternut Crossing","zip":"55402","lat":"44.9762","long":"-93.2759","short_name":"Temp","full_name":"Temp Car Dealership","__v":0},{"_id":"6ae4ad0b52a1f6200cf50c5f","id":3,"city":"Birmingham","state":"Alabama","address":"9477 Twin Pines Center","zip":"35285","lat":"33.5446","long":"-86.9292","short_name":"Sub-Ex","full_name":"Sub-Ex Car Dealership","__v":0},{"_id":"6ae4ad0b52a1f6200cf50c60","id":4,"city":"Dallas","state":"Texas","address":"85800 Hazelcrest Circle","zip":"75241","lat":"32.6722","long":"-96.7774","short_name":"Solarbreeze","full_name":"Solarbreeze Car Dealership","__v":0},{"_id":"6ae4ad0b52a1f6200cf50c61","id":5,"city":"Baltimore","state":"Maryland","address":"93 Golf Course Pass","zip":"21203","lat":"39.2847","long":"-76.6205","short_name":"Regrant","full_name":"Regrant Car Dealership","__v":0},{"_id":"6ae4ad0b52a1f6200cf50c62","id":6,"city":"Wilkes Barre","state":"Pennsylvania","address":"2 Burrows Hill","zip":"18763","lat":"41.2722","long":"-75.8801","short_name":"Stronghold","full_name":"Stronghold Car Dealership","__v":0},{"_id":"6ae4ad0b52a1f6200cf50c63","id":7,"city":"Pueblo","state":"Colorado","address":"9 Cambridge Park","zip":"81010","lat":"38.1286","long":"-104.5523","short_name":"Job","full_name":"Job Car Dealership","__v":0},{"_id":"6ae4ad0b52a1f6200cf50c64","id":8,"city":"Topeka","state":"Kansas","address":"288 Larry Place","zip":"66642","lat":"39.0429","long":"-95.7697","short_name":"Bytecard","full_name":"Bytecard Car Dealership","__v":0},{"_id":"6ae4ad0b52a1f6200cf50c65","id":9,"city":"Dallas","state":"Texas","address":"253 Hanson Junction","zip":"75216","lat":"32.7086","long":"-96.7955","short_name":"Job","full_name":"Job Car Dealership","__v":0},{"_id":"6ae4ad0b52a1f6200cf50c66","id":10,"city":"Washington","state":"District of Columbia","address":"108 Memorial Pass","zip":"20005","lat":"38.9067","long":"-77.0312","short_name":"Alphazap","full_name":"Alphazap Car Dealership","__v":0},{"_id":"6ae4ad0b52a1f6200cf50c67","id":11,"city":"Carol Stream","state":"Illinois","address":"8108 Dryden Court","zip":"60351","lat":"41.9166","long":"-88.1208","short_name":"Rank","full_name":"Rank Car Dealership","__v":0},{"_id":"6ae4ad0b52a1f6200cf50c68","id":12,"city":"Silver Spring","state":"Maryland","address":"168 Pawling Lane","zip":"20918","lat":"39.144","long":"-77.2076","short_name":"Tin","full_name":"Tin Car Dealership","__v":0},{"_id":"6ae4ad0b52a1f6200cf50c69","id":13,"city":"Baltimore","state":"Maryland","address":"452 Fair Oaks Drive","zip":"21275","lat":"39.2847","long":"-76.6205","short_name":"Y-Solowarm","full_name":"Y-Solowarm Car Dealership","__v":0},{"_id":"6ae4ad0b52a1f6200cf50c6a","id":14,"city":"San Francisco","state":"California","address":"2109 Scott Parkway","zip":"94147","lat":"37.7848","long":"-122.7278","short_name":"It","full_name":"It Car Dealership","__v":0},{"_id":"6ae4ad0b52a1f6200cf50c6b","id":15,"city":"San Antonio","state":"Texas","address":"5057 Pankratz Hill","zip":"78225","lat":"29.3875","long":"-98.5245","short_name":"Tempsoft","full_name":"Tempsoft Car Dealership","__v":0},{"_id":"6ae4ad0b52a1f6200cf50c6c","id":16,"city":"El Paso","state":"Texas","address":"0 Rieder Trail","zip":"79994","lat":"31.6948","long":"-106.3","short_name":"Treeflex","full_name":"Treeflex Car Dealership","__v":0},{"_id":"6ae4ad0b52a1f6200cf50c6d","id":17,"city":"San Jose","state":"California","address":"7670 American Ash Drive","zip":"95138","lat":"37.2602","long":"-121.7709","short_name":"Home Ing","full_name":"Home Ing Car Dealership","__v":0},{"_id":"6ae4ad0b52a1f6200cf50c6e","id":18,"city":"Whittier","state":"California","address":"4 Pearson Avenue","zip":"90605","lat":"33.9413","long":"-118.0356","short_name":"Bitchip","full_name":"Bitchip Car Dealership","__v":0},{"_id":"6ae4ad0b52a1f6200cf50c6f","id":19,"city":"Hialeah","state":"Florida","address":"93 Monument Circle","zip":"33013","lat":"25.8594","long":"-80.2725","short_name":"Otcom","full_name":"Otcom Car Dealership","__v":0},{"_id":"6ae4ad0b52a1f6200cf50c70","id":20,"city":"Detroit","state":"Michigan","address":"4580 Waubesa Lane","zip":"48224","lat":"42.4098","long":"-82.9441","short_name":"Subin","full_name":"Subin Car Dealership","__v":0},{"_id":"6ae4ad0b52a1f6200cf50c71","id":21,"city":"San Francisco","state":"California","address":"046 Mockingbird Junction","zip":"94154","lat":"37.7848","long":"-122.7278","short_name":"Andalax","full_name":"Andalax Car Dealership","__v":0},{"_id":"6ae4ad0b52a1f6200cf50c72","id":22,"city":"Fort Lauderdale","state":"Florida","address":"45737 Butternut Lane","zip":"33330","lat":"26.0663","long":"-80.3339","short_name":"Y-Solowarm","full_name":"Y-Solowarm Car Dealership","__v":0},{"_id":"6ae4ad0b52a1f6200cf50c73","id":23,"city":"Des Moines","state":"Iowa","address":"21425 Bartelt Pass","zip":"50936","lat":"41.6727","long":"-93.5722","short_name":"Bitchip","full_name":"Bitchip Car Dealership","__v":0},{"_id":"6ae4ad0b52a1f6200cf50c74","id":24,"city":"Utica","state":"New York","address":"408 Delaware Circle","zip":"13505","lat":"43.0872","long":"-75.2603","short_name":"Aerified","full_name":"Aerified Car Dealership","__v":0},{"_id":"6ae4ad0b52a1f6200cf50c75","id":25,"city":"Washington","state":"District of Columbia","address":"6505 Melrose Junction","zip":"20580","lat":"38.8933","long":"-77.0146","short_name":"Opela","full_name":"Opela Car Dealership","__v":0},{"_id":"6ae4ad0b52a1f6200cf50c76","id":26,"city":"Pittsburgh","state":"Pennsylvania","address":"306 Jenna Parkway","zip":"15279","lat":"40.4344","long":"-80.0248","short_name":"Flowdesk","full_name":"Flowdesk Car Dealership","__v":0},{"_id":"6ae4ad0b52a1f6200cf50c77","id":27,"city":"San Antonio","state":"Texas","address":"95321 Superior Hill","zip":"78245","lat":"29.4189","long":"-98.6895","short_name":"Namfix","full_name":"Namfix Car Dealership","__v":0},{"_id":"6ae4ad0b52a1f6200cf50c78","id":28,"city":"Hialeah","state":"Florida","address":"5458 Maple Way","zip":"33018","lat":"25.9098","long":"-80.3889","short_name":"Fixflex","full_name":"Fixflex Car Dealership","__v":0},{"_id":"6ae4ad0b52a1f6200cf50c79","id":29,"city":"San Francisco","state":"California","address":"9 Harper Circle","zip":"94110","lat":"37.7509","long":"-122.4153","short_name":"Fix San","full_name":"Fix San Car Dealership","__v":0},{"_id":"6ae4ad0b52a1f6200cf50c7a","id":30,"city":"Houston","state":"Texas","address":"5423 Spaight Road","zip":"77218","lat":"29.834","long":"-95.4342","short_name":"Opela","full_name":"Opela Car Dealership","__v":0},{"_id":"6ae4ad0b52a1f6200cf50c7b","id":31,"city":"New York City","state":"New York","address":"5 Northfield Pass","zip":"10131","lat":"40.7808","long":"-73.9772","short_name":"Fintone","full_name":"Fintone Car Dealership","__v":0},{"_id":"6ae4ad0b52a1f6200cf50c7c","id":32,"city":"Wilkes Barre","state":"Pennsylvania","address":"3 Carey Junction","zip":"18768","lat":"41.2722","long":"-75.8801","short_name":"Subin","full_name":"Subin Car Dealership","__v":0},{"_id":"6ae4ad0b52a1f6200cf50c7d","id":33,"city":"Des Moines","state":"Iowa","address":"627 Cottonwood Circle","zip":"50335","lat":"41.6727","long":"-93.5722","short_name":"Tres-Zap","full_name":"Tres-Zap Car Dealership","__v":0},{"_id":"6ae4ad0b52a1f6200cf50c7e","id":34,"city":"Silver Spring","state":"Maryland","address":"8 Green Hill","zip":"20904","lat":"39.0668","long":"-76.9969","short_name":"Gembucket","full_name":"Gembucket Car Dealership","__v":0},{"_id":"6ae4ad0b52a1f6200cf50c7f","id":35,"city":"Seattle","state":"Washington","address":"9 Beilfuss Trail","zip":"98158","lat":"47.4497","long":"-122.3076","short_name":"Treeflex","full_name":"Treeflex Car Dealership","__v":0},{"_id":"6ae4ad0b52a1f6200cf50c80","id":36,"city":"Vienna","state":"Virginia","address":"311 Paget Alley","zip":"22184","lat":"38.8318","long":"-77.2888","short_name":"Latlux","full_name":"Latlux Car Dealership","__v":0},{"_id":"6ae4ad0b52a1f6200cf50c81","id":37,"city":"Detroit","state":"Michigan","address":"152 Moland Lane","zip":"48224","lat":"42.4098","long":"-82.9441","short_name":"Ventosanzap","full_name":"Ventosanzap Car Dealership","__v":0},{"_id":"6ae4ad0b52a1f6200cf50c82","id":38,"city":"Dallas","state":"Texas","address":"821 New Castle Trail","zip":"75226","lat":"32.7887","long":"-96.7676","short_name":"Zamit","full_name":"Zamit Car Dealership","__v":0},{"_id":"6ae4ad0b52a1f6200cf50c83","id":39,"city":"Fresno","state":"California","address":"990 Raven Road","zip":"93740","lat":"36.7464","long":"-119.6397","short_name":"Stronghold","full_name":"Stronghold Car Dealership","__v":0},{"_id":"6ae4ad0b52a1f6200cf50c84","id":40,"city":"Merrifield","state":"Virginia","address":"89375 Main Trail","zip":"22119","lat":"38.8318","long":"-77.2888","short_name":"Greenlam","full_name":"Greenlam Car Dealership","__v":0},{"_id":"6ae4ad0b52a1f6200cf50c85","id":41,"city":"Baltimore","state":"Maryland","address":"9 Sherman Hill","zip":"21275","lat":"39.2847","long":"-76.6205","short_name":"Tres-Zap","full_name":"Tres-Zap Car Dealership","__v":0},{"_id":"6ae4ad0b52a1f6200cf50c86","id":42,"city":"Jersey City","state":"New Jersey","address":"62 Manley Point","zip":"07310","lat":"40.7324","long":"-74.0431","short_name":"Konklab","full_name":"Konklab Car Dealership","__v":0},{"_id":"6ae4ad0b52a1f6200cf50c87","id":43,"city":"Atlanta","state":"Georgia","address":"91 Declaration Avenue","zip":"31119","lat":"33.8913","long":"-84.0746","short_name":"Opela","full_name":"Opela Car Dealership","__v":0},{"_id":"6ae4ad0b52a1f6200cf50c88","id":44,"city":"Roanoke","state":"Virginia","address":"0 Northview Point","zip":"24014","lat":"37.2327","long":"-79.9463","short_name":"Veribet","full_name":"Veribet Car Dealership","__v":0},{"_id":"6ae4ad0b52a1f6200cf50c89","id":45,"city":"Norfolk","state":"Virginia","address":"283 Mockingbird Plaza","zip":"23509","lat":"36.8787","long":"-76.2604","short_name":"Konklux","full_name":"Konklux Car Dealership","__v":0},{"_id":"6ae4ad0b52a1f6200cf50c8a","id":46,"city":"New Orleans","state":"Louisiana","address":"527 Hayes Junction","zip":"70165","lat":"30.033","long":"-89.8826","short_name":"Regrant","full_name":"Regrant Car Dealership","__v":0},{"_id":"6ae4ad0b52a1f6200cf50c8b","id":47,"city":"Stamford","state":"Connecticut","address":"840 Pepper Wood Crossing","zip":"06905","lat":"41.0888","long":"-73.5435","short_name":"Prodder","full_name":"Prodder Car Dealership","__v":0},{"_id":"6ae4ad0b52a1f6200cf50c8c","id":48,"city":"Tucson","state":"Arizona","address":"48610 Morning Street","zip":"85710","lat":"32.2138","long":"-110.824","short_name":"It","full_name":"It Car Dealership","__v":0},{"_id":"6ae4ad0b52a1f6200cf50c8d","id":49,"city":"Athens","state":"Georgia","address":"222 Grasskamp Plaza","zip":"30605","lat":"33.9321","long":"-83.3525","short_name":"Veribet","full_name":"Veribet Car Dealership","__v":0},{"_id":"6ae4ad0b52a1f6200cf50c8e","id":50,"city":"Atlanta","state":"Georgia","address":"76 Clove Trail","zip":"30316","lat":"33.7217","long":"-84.3339","short_name":"Aerified","full_name":"Aerified Car Dealership","__v":0}]
Exit code: 0

## Q10

$ curl.exe --silent --show-error --fail-with-body http://127.0.0.1:3030/fetchDealer/8
[{"_id":"6ae4ad0b52a1f6200cf50c64","id":8,"city":"Topeka","state":"Kansas","address":"288 Larry Place","zip":"66642","lat":"39.0429","long":"-95.7697","short_name":"Bytecard","full_name":"Bytecard Car Dealership","__v":0}]
Exit code: 0

## Q11

$ curl.exe --silent --show-error --fail-with-body http://127.0.0.1:3030/fetchDealers/Kansas
[{"_id":"6ae4ad0b52a1f6200cf50c64","id":8,"city":"Topeka","state":"Kansas","address":"288 Larry Place","zip":"66642","lat":"39.0429","long":"-95.7697","short_name":"Bytecard","full_name":"Bytecard Car Dealership","__v":0}]
Exit code: 0

## Q12


C:\Users\phong\Downloads\crs\cars-dealership-capstone\submission\evidence\screenshots\admin_login.png

## Q13


C:\Users\phong\Downloads\crs\cars-dealership-capstone\submission\evidence\screenshots\admin_logout.png

## Q14



```text
$ curl.exe --silent --show-error --fail-with-body http://127.0.0.1:8010/djangoapp/get_cars
{"status": 200, "CarModels": [{"id": 13, "CarMake": "Audi", "CarModel": "A3", "type": "Hatchback", "year": 2020}, {"id": 89, "CarMake": "Audi", "CarModel": "A3", "type": "Hatchback", "year": 2022}, {"id": 3, "CarMake": "Audi", "CarModel": "A4", "type": "Sedan", "year": 2021}, {"id": 33, "CarMake": "Audi", "CarModel": "A5", "type": "Convertible", "year": 2020}, {"id": 61, "CarMake": "Audi", "CarModel": "A5", "type": "Convertible", "year": 2021}, {"id": 56, "CarMake": "Audi", "CarModel": "A6", "type": "Sedan", "year": 2022}, {"id": 79, "CarMake": "Audi", "CarModel": "Q3", "type": "SUV", "year": 2020}, {"id": 107, "CarMake": "Audi", "CarModel": "Q3", "type": "SUV", "year": 2022}, {"id": 38, "CarMake": "Audi", "CarModel": "Q3", "type": "SUV", "year": 2023}, {"id": 8, "CarMake": "Audi", "CarModel": "Q5", "type": "SUV", "year": 2020}, {"id": 75, "CarMake": "Audi", "CarModel": "Q5", "type": "SUV", "year": 2022}, {"id": 94, "CarMake": "Audi", "CarModel": "Q7", "type": "SUV", "year": 2021}, {"id": 18, "CarMake": "Audi", "CarModel": "Q7", "type": "SUV", "year": 2023}, {"id": 66, "CarMake": "Audi", "CarModel": "Q8", "type": "SUV", "year": 2020}, {"id": 48, "CarMake": "Audi", "CarModel": "Q8", "type": "SUV", "year": 2021}, {"id": 70, "CarMake": "Audi", "CarModel": "S3", "type": "Sedan", "year": 2023}, {"id": 23, "CarMake": "Audi", "CarModel": "S5", "type": "Coupe", "year": 2022}, {"id": 84, "CarMake": "Audi", "CarModel": "S5", "type": "Coupe", "year": 2023}, {"id": 43, "CarMake": "Audi", "CarModel": "S7", "type": "Sedan", "year": 2022}, {"id": 28, "CarMake": "Audi", "CarModel": "TT", "type": "Convertible", "year": 2021}, {"id": 102, "CarMake": "Audi", "CarModel": "TT", "type": "Convertible", "year": 2023}, {"id": 17, "CarMake": "Kia", "CarModel": "Cadenza", "type": "Sedan", "year": 2020}, {"id": 93, "CarMake": "Kia", "CarModel": "Cadenza", "type": "Sedan", "year": 2022}, {"id": 52, "CarMake": "Kia", "CarModel": "Forte", "type": "Sedan", "year": 2020}, {"id": 47, "CarMake": "Kia", "CarModel": "Forte", "type": "Sedan", "year": 2022}, {"id": 106, "CarMake": "Kia", "CarModel": "Forte", "type": "Sedan", "year": 2023}, {"id": 37, "CarMake": "Kia", "CarModel": "Niro", "type": "SUV", "year": 2020}, {"id": 55, "CarMake": "Kia", "CarModel": "Niro", "type": "SUV", "year": 2023}, {"id": 83, "CarMake": "Kia", "CarModel": "Optima", "type": "Sedan", "year": 2020}, {"id": 22, "CarMake": "Kia", "CarModel": "Optima", "type": "Sedan", "year": 2023}, {"id": 27, "CarMake": "Kia", "CarModel": "Rio", "type": "Hatchback", "year": 2022}, {"id": 74, "CarMake": "Kia", "CarModel": "Rio", "type": "Hatchback", "year": 2023}, {"id": 2, "CarMake": "Kia", "CarModel": "Seltos", "type": "SUV", "year": 2022}, {"id": 101, "CarMake": "Kia", "CarModel": "Soul", "type": "Hatchback", "year": 2020}, {"id": 65, "CarMake": "Kia", "CarModel": "Soul", "type": "Hatchback", "year": 2021}, {"id": 42, "CarMake": "Kia", "CarModel": "Soul", "type": "Hatchback", "year": 2023}, {"id": 12, "CarMake": "Kia", "CarModel": "Sportage", "type": "SUV", "year": 2021}, {"id": 88, "CarMake": "Kia", "CarModel": "Sportage", "type": "SUV", "year": 2023}, {"id": 32, "CarMake": "Kia", "CarModel": "Stinger", "type": "Sedan", "year": 2021}, {"id": 60, "CarMake": "Kia", "CarModel": "Stinger", "type": "Sedan", "year": 2022}, {"id": 69, "CarMake": "Kia", "CarModel": "Telluride", "type": "SUV", "year": 2020}, {"id": 7, "CarMake": "Kia", "CarModel": "Telluride", "type": "SUV", "year": 2021}, {"id": 49, "CarMake": "Mercedes", "CarModel": "A-Class", "type": "Sedan", "year": 2020}, {"id": 108, "CarMake": "Mercedes", "CarModel": "A-Class", "type": "Sedan", "year": 2021}, {"id": 53, "CarMake": "Mercedes", "CarModel": "A-Class", "type": "Sedan", "year": 2022}, {"id": 67, "CarMake": "Mercedes", "CarModel": "AMG GT", "type": "Coupe", "year": 2023}, {"id": 76, "CarMake": "Mercedes", "CarModel": "C-Class", "type": "Sedan", "year": 2021}, {"id": 9, "CarMake": "Mercedes", "CarModel": "C-Class", "type": "Sedan", "year": 2023}, {"id": 29, "CarMake": "Mercedes", "CarModel": "CLA", "type": "Sedan", "year": 2020}, {"id": 103, "CarMake": "Mercedes", "CarModel": "CLA", "type": "Sedan", "year": 2022}, {"id": 90, "CarMake": "Mercedes", "CarModel": "E-Class", "type": "Sedan", "year": 2021}, {"id": 14, "CarMake": "Mercedes", "CarModel": "E-Class", "type": "Sedan", "year": 2023}, {"id": 57, "CarMake": "Mercedes", "CarModel": "GLA", "type": "SUV", "year": 2021}, {"id": 34, "CarMake": "Mercedes", "CarModel": "GLA", "type": "SUV", "year": 2023}, {"id": 44, "CarMake": "Mercedes", "CarModel": "GLB", "type": "SUV", "year": 2021}, {"id": 95, "CarMake": "Mercedes", "CarModel": "GLC", "type": "SUV", "year": 2020}, {"id": 19, "CarMake": "Mercedes", "CarModel": "GLC", "type": "SUV", "year": 2022}, {"id": 80, "CarMake": "Mercedes", "CarModel": "GLC", "type": "SUV", "year": 2023}, {"id": 4, "CarMake": "Mercedes", "CarModel": "GLE", "type": "SUV", "year": 2020}, {"id": 39, "CarMake": "Mercedes", "CarModel": "GLE Coupe", "type": "SUV", "year": 2022}, {"id": 62, "CarMake": "Mercedes", "CarModel": "GLS", "type": "SUV", "year": 2020}, {"id": 98, "CarMake": "Mercedes", "CarModel": "GLS", "type": "SUV", "year": 2023}, {"id": 71, "CarMake": "Mercedes", "CarModel": "M-Class", "type": "SUV", "year": 2022}, {"id": 24, "CarMake": "Mercedes", "CarModel": "S-Class", "type": "Sedan", "year": 2021}, {"id": 85, "CarMake": "Mercedes", "CarModel": "S-Class", "type": "Sedan", "year": 2022}, {"id": 73, "CarMake": "Nissan", "CarModel": "370Z", "type": "Coupe", "year": 2020}, {"id": 26, "CarMake": "Nissan", "CarModel": "370Z", "type": "Coupe", "year": 2023}, {"id": 87, "CarMake": "Nissan", "CarModel": "Altima", "type": "Sedan", "year": 2020}, {"id": 11, "CarMake": "Nissan", "CarModel": "Altima", "type": "Sedan", "year": 2022}, {"id": 36, "CarMake": "Nissan", "CarModel": "Armada", "type": "SUV", "year": 2021}, {"id": 110, "CarMake": "Nissan", "CarModel": "Armada", "type": "SUV", "year": 2022}, {"id": 97, "CarMake": "Nissan", "CarModel": "Cube", "type": "Hatchback", "year": 2022}, {"id": 59, "CarMake": "Nissan", "CarModel": "Cube", "type": "Hatchback", "year": 2023}, {"id": 100, "CarMake": "Nissan", "CarModel": "Juke", "type": "SUV", "year": 2021}, {"id": 64, "CarMake": "Nissan", "CarModel": "Juke", "type": "SUV", "year": 2022}, {"id": 46, "CarMake": "Nissan", "CarModel": "Juke", "type": "SUV", "year": 2023}, {"id": 16, "CarMake": "Nissan", "CarModel": "Maxima", "type": "Sedan", "year": 2021}, {"id": 92, "CarMake": "Nissan", "CarModel": "Maxima", "type": "Sedan", "year": 2023}, {"id": 21, "CarMake": "Nissan", "CarModel": "Murano", "type": "SUV", "year": 2020}, {"id": 82, "CarMake": "Nissan", "CarModel": "Murano", "type": "SUV", "year": 2021}, {"id": 1, "CarMake": "Nissan", "CarModel": "Pathfinder", "type": "SUV", "year": 2023}, {"id": 6, "CarMake": "Nissan", "CarModel": "Rogue", "type": "SUV", "year": 2022}, {"id": 41, "CarMake": "Nissan", "CarModel": "Sentra", "type": "Sedan", "year": 2020}, {"id": 105, "CarMake": "Nissan", "CarModel": "Versa", "type": "Sedan", "year": 2020}, {"id": 51, "CarMake": "Nissan", "CarModel": "Versa", "type": "Sedan", "year": 2021}, {"id": 31, "CarMake": "Nissan", "CarModel": "Versa", "type": "Sedan", "year": 2022}, {"id": 78, "CarMake": "Nissan", "CarModel": "Versa", "type": "Sedan", "year": 2023}, {"id": 45, "CarMake": "Toyota", "CarModel": "4Runner", "type": "SUV", "year": 2020}, {"id": 99, "CarMake": "Toyota", "CarModel": "4Runner", "type": "SUV", "year": 2022}, {"id": 63, "CarMake": "Toyota", "CarModel": "4Runner", "type": "SUV", "year": 2023}, {"id": 40, "CarMake": "Toyota", "CarModel": "Avalon", "type": "Sedan", "year": 2021}, {"id": 68, "CarMake": "Toyota", "CarModel": "Avalon", "type": "Sedan", "year": 2022}, {"id": 5, "CarMake": "Toyota", "CarModel": "Camry", "type": "Sedan", "year": 2023}, {"id": 20, "CarMake": "Toyota", "CarModel": "Corolla", "type": "Sedan", "year": 2021}, {"id": 81, "CarMake": "Toyota", "CarModel": "Corolla", "type": "Sedan", "year": 2022}, {"id": 77, "CarMake": "Toyota", "CarModel": "Highlander", "type": "SUV", "year": 2020}, {"id": 10, "CarMake": "Toyota", "CarModel": "Highlander", "type": "SUV", "year": 2022}, {"id": 72, "CarMake": "Toyota", "CarModel": "Land Cruiser", "type": "SUV", "year": 2021}, {"id": 109, "CarMake": "Toyota", "CarModel": "Prius", "type": "Hatchback", "year": 2020}, {"id": 54, "CarMake": "Toyota", "CarModel": "Prius", "type": "Hatchback", "year": 2021}, {"id": 35, "CarMake": "Toyota", "CarModel": "Prius", "type": "Hatchback", "year": 2022}, {"id": 91, "CarMake": "Toyota", "CarModel": "RAV4", "type": "SUV", "year": 2020}, {"id": 15, "CarMake": "Toyota", "CarModel": "RAV4", "type": "SUV", "year": 2022}, {"id": 25, "CarMake": "Toyota", "CarModel": "Sienna", "type": "Minivan", "year": 2020}, {"id": 86, "CarMake": "Toyota", "CarModel": "Sienna", "type": "Minivan", "year": 2021}, {"id": 104, "CarMake": "Toyota", "CarModel": "Tacoma", "type": "Pickup", "year": 2021}, {"id": 30, "CarMake": "Toyota", "CarModel": "Tacoma", "type": "Pickup", "year": 2023}, {"id": 50, "CarMake": "Toyota", "CarModel": "Tundra", "type": "Pickup", "year": 2023}, {"id": 58, "CarMake": "Toyota", "CarModel": "Yaris", "type": "Hatchback", "year": 2020}, {"id": 96, "CarMake": "Toyota", "CarModel": "Yaris", "type": "Hatchback", "year": 2023}]}
Exit code: 0

```

## Q15

$ curl.exe --silent --show-error --fail-with-body http://127.0.0.1:5050/analyze/Fantastic%20services
{"scores":{"compound":0.5574,"neg":0.0,"neu":0.217,"pos":0.783},"sentiment":"positive"}

Exit code: 0

## Q16


C:\Users\phong\Downloads\crs\cars-dealership-capstone\submission\evidence\screenshots\get_dealers.png

## Q17


C:\Users\phong\Downloads\crs\cars-dealership-capstone\submission\evidence\screenshots\get_dealers_loggedin.png

## Q18


C:\Users\phong\Downloads\crs\cars-dealership-capstone\submission\evidence\screenshots\dealersbystate.png

## Q19


C:\Users\phong\Downloads\crs\cars-dealership-capstone\submission\evidence\screenshots\dealer_id_reviews.png

## Q20


C:\Users\phong\Downloads\crs\cars-dealership-capstone\submission\evidence\screenshots\dealership_review_submission.png

## Q21


C:\Users\phong\Downloads\crs\cars-dealership-capstone\submission\evidence\screenshots\added_review.png

## Q22





```text

✓ main Capstone CI · 41084078460
Triggered via push about 4 minutes ago

JOBS
✓ Lint Python Files in 8s (ID 124160498679)
  ✓ Set up job
  ✓ Checkout Repository
  ✓ Set up Python
  ✓ Install dependencies
  ✓ Print working directory
  ✓ Run Linter
  ✓ Post Set up Python
  ✓ Post Checkout Repository
  ✓ Complete job
✓ checks in 1m57s (ID 124160498880)
  ✓ Set up job
  ✓ Run actions/checkout@v4
  ✓ Run actions/setup-python@v5
  ✓ Run pip install -r server/requirements.txt
  ✓ Run python manage.py check
  ✓ Run python manage.py test
  ✓ Run actions/setup-node@v4
  ✓ Run npm ci
  ✓ Run npm run build
  ✓ Run npm ci && npm test
  ✓ Run docker compose build
  ✓ Build Django deployment image
  ✓ Build Code Engine database service image
  ✓ Post Run actions/setup-node@v4
  ✓ Post Run actions/setup-python@v5
  ✓ Post Run actions/checkout@v4
  ✓ Complete job
✓ Lint JavaScript Files in 9s (ID 124160499339)
  ✓ Set up job
  ✓ Checkout Repository
  ✓ Install Node.js
  ✓ Install JSHint
  ✓ Run Linter
  ✓ Post Install Node.js
  ✓ Post Checkout Repository
  ✓ Complete job

ANNOTATIONS
! Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4, actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
Lint Python Files: .github#2

- "The ubuntu-latest label will migrate to Ubuntu 26 beginning October 19, 2026. For more information, see https://github.com/actions/runner-images/issues/14748"
Lint Python Files: .github#1

! Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4, actions/setup-node@v4, actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
checks: .github#2

- "The ubuntu-latest label will migrate to Ubuntu 26 beginning October 19, 2026. For more information, see https://github.com/actions/runner-images/issues/14748"
checks: .github#1

! Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4, actions/setup-node@v4. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
Lint JavaScript Files: .github#2

- "The ubuntu-latest label will migrate to Ubuntu 26 beginning October 19, 2026. For more information, see https://github.com/actions/runner-images/issues/14748"
Lint JavaScript Files: .github#1


For more information about a job, try: gh run view --job=<job-id>
View this run on GitHub: https://github.com/PhongLam26/xrwvm-fullstack_developer_capstone/actions/runs/41084078460

```

## Q23



https://cars-web.2gkdcb8j96ze.us-south.codeengine.appdomain.cloud

## Q24



C:\Users\phong\Downloads\crs\cars-dealership-capstone\submission\evidence\screenshots\deployed_landingpage.png

## Q25



C:\Users\phong\Downloads\crs\cars-dealership-capstone\submission\evidence\screenshots\deployed_loggedin.png

## Q26



C:\Users\phong\Downloads\crs\cars-dealership-capstone\submission\evidence\screenshots\deployed_dealer_detail.png

## Q27



C:\Users\phong\Downloads\crs\cars-dealership-capstone\submission\evidence\screenshots\deployed_add_review.png
