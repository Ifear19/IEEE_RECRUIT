#Q6 DICTIONARIES

import json
cutoffs=[("Pilani","CS",327),("Pilani","Chemical",247),("Pilani","M.Sc. Bio",236,),
("Pilani","M.Sc. Eco",271),

("Goa","CS",301),("Goa","Chemical",239),("Goa","M.Sc. Bio",234),("Goa","M.Sc. Eco",263),

("Hyderabad","CS",298),("Hyderabad","Chemical",238),("Hyderabad","M.Sc. Bio",234),
("Hyderabad","M.Sc. Eco",261)]

college_dict={}
for college,branch,marks in cutoffs:
    if college not in college_dict:
        college_dict[college]={}
    college_dict[college][branch]=marks

print(json.dumps(college_dict,indent=3))