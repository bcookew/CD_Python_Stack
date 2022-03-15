from pickle import FALSE


string1 = 'SELECT SUM(amount), clients.id FROM billing JOIN clients ON billing.clients_id = clients.id GROUP BY clients.id;'
string2 = 'SELECT sum(amount), clients.id FROM billing JOIN clients ON billing.clients_id = clients.id GROUB BY clients.id;'

def checkEqual(str1,str2):
    isEqual = True
    numMismatch = 0
    if len(str1) != len(str2):
        print(False)
        return
    elif len(str1) == len(str2):
        for i in range(len(str1)):
            if(str1[i] != str2[i]):
                isEqual, numMismatch = False, numMismatch + 1
                print(f"Equal?: {False}\nMismatch: {numMismatch}\nstr1 char {str1[i]}\nstr2 char {str2[i]}\n")
    else:
        print('They are in fact the same.')
        
checkEqual(string1, string2)