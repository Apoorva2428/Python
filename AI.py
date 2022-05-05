#Medicine Prescription
user=input("Hello there! For what you want medicine ?")

def process():
    u=user.strip()
    l=u.lower()
    r=l.replace(' ',"")
    return u
process_input=process()

tags=['headache', 'fever', 'cough']
headache=['M1', 'M2', 'M3', 'M4', 'M5']
fever=['M6', 'M7', 'M8']
cough=['M6', 'M8', 'M9']
if process_input in tags:
    print('Yes wait we are here with good items')
    if process_input=='headache':
        print("Hey here are some medicine {}",format(process_input),headache)
    elif process_input=='fever':
        print("Hey here are some medicine {}",format(process_input),fever)
    elif process_input=='cough':
        print("Hey here are some medicine for cough {}",format(process_input),cough)
else:
    print("Sorry no record.")
    print("Try including these tags in your sentence: ", end="")
    print(list(tags))
