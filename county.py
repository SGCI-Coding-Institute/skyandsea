import matplotlib.pyplot as plt

# line 1 points
x1 = ['Adams','Alexander','Bond','Boone','Brown','Bureau','Calhoun','Carroll','Cass','Champaign','Chicago','Christian','Clark','Clay','Clinton','Coles','Cook','Crawford','De Witt','DeKalb','Douglas','DuPage','Edgar','Edwards','Effingham','Fayette','Ford','Franklin','Fulton','Gallatin','Greene','Grundy','Hamilto','Hancock','Hardin','Henderson','Henry','Iroquois','Jackson','Jasper','Jefferson','Jersey','Jo Daviess','Johnson','Kane','Kankakee','Kendall','Knox','La Salle','Lake','Lawrence','Lee','Livingston','Logan','McDonough','McHenry','McLean','Macon','Macoupin','Madison','Marion','Marshall','Mason','Massac','Menard','Mercer','Monroe','Montgomery','Morgan','Moultrie','Ogle','Peoria','Perry','Piatt','Pike','Pope','Pulaski','Putnam','Randolph','Richland','Rock Island','Saline','Sangamon','Schuyler','Scott','Shelby','St. Clair','Stark','Stephenson','Tazewell','Union','Vermilion','Wabash','Warren','Washington','Wayne','White','Whiteside','Will','Williamson','Winnebago','Woodford']
y1 = [65691,6060,16630,53577,6556,32993,4802,14312,12260,209983,2705994,32661,15596,13253,37639,50885,2474499,18807,10808,15769,104143,19479,928589,17360,6392,34208,21416,13264,38701,34844,5058,13044,50972,8163,17844,3910,6709,4909,27604,57419,9611,37820,21366,12456,534216,110024,127915,50112,700832,109430,15765,34223,35761,28925,104712,45313,264461,37620,11534,13565,14080,29955,308570,172828,12288,15601,34335,28601,33976,14717,50923,180621,21174,16396,15611,4212,5463,5740,32106,15763,143477,23906,195348,6907,4926,21741,261059,5427,44753,132328,16841,76806,11549,17032,13995,16332,13665,55626,692310,67056,284081,38463]
# plotting the line 1 points
plt.plot(x1, y1, label = "Population")

# line 2 points
x2 = ['Adams','Alexander','Bond','Boone','Brown','Bureau','Calhoun','Carroll','Cass','Champaign','Chicago','Christian','Clark','Clay','Clinton','Coles','Cook','Crawford','De Witt','DeKalb','Douglas','DuPage','Edgar','Edwards','Effingham','Fayette','Ford','Franklin','Fulton','Gallatin','Greene','Grundy','Hamilto','Hancock','Hardin','Henderson','Henry','Iroquois','Jackson','Jasper','Jefferson','Jersey','Jo Daviess','Johnson','Kane','Kankakee','Kendall','Knox','La Salle','Lake','Lawrence','Lee','Livingston','Logan','McDonough','McHenry','McLean','Macon','Macoupin','Madison','Marion','Marshall','Mason','Massac','Menard','Mercer','Monroe','Montgomery','Morgan','Moultrie','Ogle','Peoria','Perry','Piatt','Pike','Pope','Pulaski','Putnam','Randolph','Richland','Rock Island','Saline','Sangamon','Schuyler','Scott','Shelby','St. Clair','Stark','Stephenson','Tazewell','Union','Vermilion','Wabash','Warren','Washington','Wayne','White','Whiteside','Will','Williamson','Winnebago','Woodford']
y2 = [26411,876,5543,22884,2596,13277,1563,5120,5205,99204,1330540,10946,4909,3624,15616,16598,1299202,6416,3044,5869,43317,6580,529608,5401,1649,11476,5045,5218,11382,15059,1618,3800,20728,1949,5402,962,1402,21250,9289,21632,2979,11595,8697,8223,4046,252835,38274,62595,21920,346541,46073,4796,15501,13412,11759,38896,17763,110790,11421,4767,5398,3772,11084,147139,80827,5164,6449,15695,10705,13577,4491,21195,79812,7127,6819,4490,972,1208,2347,11631,5116,53645,7585,94262,2684,1502,6174,104622,2119,17419,58183,6263,23721,3662,6113,5696,4528,4149,22972,328798,23559,116797,16189]
# plotting the line 2 points
plt.plot(x2, y2, label = "Persons Fully Vaccinated")

# naming the x axis
plt.xlabel('Illinois Counties')
# naming the y axis
plt.ylabel('# of persons')
# giving a title to my graph
plt.title('Illinois Vacinated Citizens vs Population')

# show a legend on the plot
plt.legend()

# function to show the plot
plt.show()
