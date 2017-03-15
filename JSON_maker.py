from collections import defaultdict
import json

hostel = defaultdict(str)

hostel['roomSize'] = ['6 bed', '4 bed', '3 bed', '2 bed', '1 bed']
hostel['roomType'] = ['AC', 'Non-AC']
hostel['blocks'] = ['A', 'B', 'C', 'D', 'D Annex', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'P', 'Q']

mess = dict()

mess['messTypeV'] = ['Veg', 'Non-Veg']
mess['messTypeRegional'] = ['North', 'South', 'Special']
mess['annualCharge'] = [{'North-Veg':'44000'}, {'North-Non-Veg':'48500'}, {'Special':'53000'}, {'South-Veg':'39000'}, {'South-Non-Veg':'41500'}]

building = defaultdict(str)

building['buildingType'] = ['Educational', 'Administrative']
building['buildingName'] = ['Silver Jublee Tower (SJT)', 'Technology Tower (TT)', 'Main Building (MB)', 'GDN' ]

with open('hostel.json', 'w') as f1:
    json.dump(hostel, f1)

with open('building.json', 'w') as f2:
    json.dump(building, f2)

with open('mess.json', 'w') as f3:
    json.dump(mess, f3)

f1.close()
f2.close()
f3.close()