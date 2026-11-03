student_data={"id1":{"name":"sara","class":"v","subject_integration":"english,math,science"},"id2":{"name":"David","class":"v","subject_integration":"english,math,science"},"id3":{"name":"Anas","class":"v","subject_integration":"english,math,science"},"id4":{"name":"surja","class":"v","subject_integration":"english,math,science"},}

result={}
seen_key=[]

for student_id,details in student_data.items():
    unique_key=(details["name"], details["class"],details["subject_integration"])
    if unique_key not in seen_key:
        seen_key.append(unique_key)
        result[student_id]=details
for k, v in result.items():
    print(k,":",v)