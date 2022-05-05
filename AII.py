tags = ['headache','fever','both']
inp = input("Enter your problem: type 'headache' for headache, 'fever'for fever or both-->")
if inp in tags:
    print('Your input has been successfully taken')
    if inp=='headache':
        print("Dispirin,saridon,Tylenol,Imitrex,Nimsaid-P")
    elif inp=='fever':
        print('Aspirin,Nimsaid-P,Ibuprofen')
    elif inp=='both':
        print('Aspirin and Nimsaid-p')
else:
    print('Sorry no record has been received from the administrator')
