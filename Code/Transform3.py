
# Functions for the transformation of each feature


def race_digitalized(trans_list):  # transformation for race
    index = 0
    race = trans_list[index]
    if race == "?":
        trans_list[index] = ''
        trans_list.insert(index + 1, '')
        trans_list.insert(index + 2, '')
    elif race == "Caucasian":
        trans_list[index] = '1'
        trans_list.insert(index + 1, '-1')
        trans_list.insert(index + 2, '-1')
    elif race == "AfricanAmerican":
        trans_list[index] = '-1'
        trans_list.insert(index + 1, '1')
        trans_list.insert(index + 2, '-1')
    elif race == "Hispanic" or race == "Asian" or race == "Other":
        trans_list[index] = '-1'
        trans_list.insert(index + 1, '-1')
        trans_list.insert(index + 2, '1')


def gender_digitalized(gender):  # transformation for gender
    if gender == "Male":
        return '-1'
    elif gender == "Female":
        return '1'
    elif gender == "?" or gender == "Unknown/Invalid":
        return ''


def discharge_digitialized(trans_list):  # transformation for discharge disposition
    index = 3
    discharge = trans_list[index]
    discharge = int(discharge)
    if discharge == 1:  # Discharged to home
        trans_list[index] = '1'
    else:  # Otherwise
        trans_list[index] = '-1'


def admsource_digitalized(trans_list):  # transformation for admission source
    index = 4
    admsorce = trans_list[index]
    admsorce = int(admsorce)
    if admsorce == 7:  # From emergency room
        trans_list[index] = '1'
        trans_list.insert(index + 1, '-1')
        trans_list.insert(index + 2, '-1')
    elif admsorce == 1 or admsorce == 2:  # Admitted because of physician/clinic referral
        trans_list[index] = '-1'
        trans_list.insert(index + 1, '1')
        trans_list.insert(index + 2, '-1')
    else:  # Otherwise
        trans_list[index] = '-1'
        trans_list.insert(index + 1, '-1')
        trans_list.insert(index + 2, '1')


def age_digitalized(trans_list):   # transformation for age
    index = 2
    age = trans_list[index]
    if age == "?":
        trans_list[index] = ''
        trans_list.insert(index + 1, '')
        trans_list.insert(index + 2, '')
    elif age == "[0-10)" or age == "[10-20)" or age == "[20-30)":
        trans_list[index] = '1'
        trans_list.insert(index + 1, '-1')
        trans_list.insert(index + 2, '-1')
    elif age == "[30-40)" or age == "[40-50)" or age == "[50-60)":
        trans_list[index] = '-1'
        trans_list.insert(index + 1, '1')
        trans_list.insert(index + 2, '-1')
    elif age == "[60-70)" or age == "[70-80)" or age == "[80-90)" or age == "[90-100)":
        trans_list[index] = '-1'
        trans_list.insert(index + 1, '-1')
        trans_list.insert(index + 2, '1')


def specialty_digitalized(trans_list):  # transformation for doctor specialty
    index = 6
    spec = trans_list[index]
    if spec == "Cardiology":
        trans_list[index] = '1'
        trans_list.insert(index + 1, '-1')
        trans_list.insert(index + 2, '-1')
        trans_list.insert(index + 3, '-1')
        trans_list.insert(index + 4, '-1')
        trans_list.insert(index + 5, '-1')
    elif spec == "Family/GeneralPractice":
        trans_list[index] = '-1'
        trans_list.insert(index + 1, '1')
        trans_list.insert(index + 2, '-1')
        trans_list.insert(index + 3, '-1')
        trans_list.insert(index + 4, '-1')
        trans_list.insert(index + 5, '-1')
    elif spec == "InternalMedicine":
        trans_list[index] = '-1'
        trans_list.insert(index + 1, '-1')
        trans_list.insert(index + 2, '1')
        trans_list.insert(index + 3, '-1')
        trans_list.insert(index + 4, '-1')
        trans_list.insert(index + 5, '-1')
    elif spec == "?":
        trans_list[index] = '-1'
        trans_list.insert(index + 1, '-1')
        trans_list.insert(index + 2, '-1')
        trans_list.insert(index + 3, '1')
        trans_list.insert(index + 4, '-1')
        trans_list.insert(index + 5, '-1')
    elif "Surgery" in spec:
        trans_list[index] = '-1'
        trans_list.insert(index + 1, '-1')
        trans_list.insert(index + 2, '-1')
        trans_list.insert(index + 3, '-1')
        trans_list.insert(index + 4, '1')
        trans_list.insert(index + 5, '-1')
    else:
        trans_list[index] = '-1'
        trans_list.insert(index + 1, '-1')
        trans_list.insert(index + 2, '-1')
        trans_list.insert(index + 3, '-1')
        trans_list.insert(index + 4, '-1')
        trans_list.insert(index + 5, '1')


def diag_digitalized(trans_list):  # transformation for the first diagnose
    index = 7
    diag = trans_list[index]
    if diag == "?":  # if diag is ?, return empty strings
        trans_list[index] = ''
        trans_list.insert(index + 1, '')
        trans_list.insert(index + 2, '')
        trans_list.insert(index + 3, '')
        trans_list.insert(index + 4, '')
        trans_list.insert(index + 5, '')
        trans_list.insert(index + 6, '')
        trans_list.insert(index + 7, '')
        trans_list.insert(index + 8, '')
        return
    elif "V" in diag or "E" in diag:  # if diag is V or E, return the output of group 9
        trans_list[index] = '-1'
        trans_list.insert(index + 1, '-1')
        trans_list.insert(index + 2, '-1')
        trans_list.insert(index + 3, '-1')
        trans_list.insert(index + 4, '-1')
        trans_list.insert(index + 5, '-1')
        trans_list.insert(index + 6, '-1')
        trans_list.insert(index + 7, '-1')
        trans_list.insert(index + 8, '1')
        return

    diag = float(diag)  # follow the grouping of https://www.hindawi.com/journals/bmri/2014/781670/tab2/
    if 390 <= diag <= 459 or diag == 785:
        trans_list[index] = '1'
        trans_list.insert(index + 1, '-1')
        trans_list.insert(index + 2, '-1')
        trans_list.insert(index + 3, '-1')
        trans_list.insert(index + 4, '-1')
        trans_list.insert(index + 5, '-1')
        trans_list.insert(index + 6, '-1')
        trans_list.insert(index + 7, '-1')
        trans_list.insert(index + 8, '-1')
    elif 460 <= diag <= 519 or diag == 786:
        trans_list[index] = '-1'
        trans_list.insert(index + 1, '1')
        trans_list.insert(index + 2, '-1')
        trans_list.insert(index + 3, '-1')
        trans_list.insert(index + 4, '-1')
        trans_list.insert(index + 5, '-1')
        trans_list.insert(index + 6, '-1')
        trans_list.insert(index + 7, '-1')
        trans_list.insert(index + 8, '-1')
    elif 520 <= diag <= 579 or diag == 787:
        trans_list[index] = '-1'
        trans_list.insert(index + 1, '-1')
        trans_list.insert(index + 2, '1')
        trans_list.insert(index + 3, '-1')
        trans_list.insert(index + 4, '-1')
        trans_list.insert(index + 5, '-1')
        trans_list.insert(index + 6, '-1')
        trans_list.insert(index + 7, '-1')
        trans_list.insert(index + 8, '-1')
    elif 250 <= diag < 251:
        trans_list[index] = '-1'
        trans_list.insert(index + 1, '-1')
        trans_list.insert(index + 2, '-1')
        trans_list.insert(index + 3, '1')
        trans_list.insert(index + 4, '-1')
        trans_list.insert(index + 5, '-1')
        trans_list.insert(index + 6, '-1')
        trans_list.insert(index + 7, '-1')
        trans_list.insert(index + 8, '-1')
    elif 800 <= diag <= 999:
        trans_list[index] = '-1'
        trans_list.insert(index + 1, '-1')
        trans_list.insert(index + 2, '-1')
        trans_list.insert(index + 3, '-1')
        trans_list.insert(index + 4, '1')
        trans_list.insert(index + 5, '-1')
        trans_list.insert(index + 6, '-1')
        trans_list.insert(index + 7, '-1')
        trans_list.insert(index + 8, '-1')
    elif 710 <= diag <= 739:
        trans_list[index] = '-1'
        trans_list.insert(index + 1, '-1')
        trans_list.insert(index + 2, '-1')
        trans_list.insert(index + 3, '-1')
        trans_list.insert(index + 4, '-1')
        trans_list.insert(index + 5, '1')
        trans_list.insert(index + 6, '-1')
        trans_list.insert(index + 7, '-1')
        trans_list.insert(index + 8, '-1')
    elif 580 <= diag <= 629 or diag == 788:
        trans_list[index] = '-1'
        trans_list.insert(index + 1, '-1')
        trans_list.insert(index + 2, '-1')
        trans_list.insert(index + 3, '-1')
        trans_list.insert(index + 4, '-1')
        trans_list.insert(index + 5, '-1')
        trans_list.insert(index + 6, '1')
        trans_list.insert(index + 7, '-1')
        trans_list.insert(index + 8, '-1')
    elif 140 <= diag <= 239:
        trans_list[index] = '-1'
        trans_list.insert(index + 1, '-1')
        trans_list.insert(index + 2, '-1')
        trans_list.insert(index + 3, '-1')
        trans_list.insert(index + 4, '-1')
        trans_list.insert(index + 5, '-1')
        trans_list.insert(index + 6, '-1')
        trans_list.insert(index + 7, '1')
        trans_list.insert(index + 8, '-1')
    else:
        trans_list[index] = '-1'
        trans_list.insert(index + 1, '-1')
        trans_list.insert(index + 2, '-1')
        trans_list.insert(index + 3, '-1')
        trans_list.insert(index + 4, '-1')
        trans_list.insert(index + 5, '-1')
        trans_list.insert(index + 6, '-1')
        trans_list.insert(index + 7, '-1')
        trans_list.insert(index + 8, '1')


def glu_digitalized(trans_list):  # transformation for Glucose serum test result
    index = 15
    glu = trans_list[index]
    if glu == ">200":
        trans_list[index] = '1'
        trans_list.insert(index + 1, '-1')
        trans_list.insert(index + 2, '-1')
        trans_list.insert(index + 3, '-1')
    elif glu == ">300":
        trans_list[index] = '-1'
        trans_list.insert(index + 1, '1')
        trans_list.insert(index + 2, '-1')
        trans_list.insert(index + 3, '-1')
    elif glu == "Norm":
        trans_list[index] = '-1'
        trans_list.insert(index + 1, '-1')
        trans_list.insert(index + 2, '1')
        trans_list.insert(index + 3, '-1')
    elif glu == "None":
        trans_list[index] = '-1'
        trans_list.insert(index + 1, '-1')
        trans_list.insert(index + 2, '-1')
        trans_list.insert(index + 3, '1')


def a1_digitalized(trans_list):   # transformation for A1 test result
    index = 8
    a1 = trans_list[index]
    change = trans_list[index+1]
    if (a1 == ">8" or a1 == ">7") and change == "No":
        trans_list[index] = '1'
        trans_list[index + 1] = '-1'
        trans_list.insert(index + 2, '-1')
        trans_list.insert(index + 3, '-1')
    elif (a1 == ">8" or a1 == ">7") and change == "Ch":
        trans_list[index] = '-1'
        trans_list[index + 1] = '1'
        trans_list.insert(index + 2, '-1')
        trans_list.insert(index + 3, '-1')
    elif a1 == "Norm":
        trans_list[index] = '-1'
        trans_list[index + 1] = '-1'
        trans_list.insert(index + 2, '1')
        trans_list.insert(index + 3, '-1')
    elif a1 == "None":
        trans_list[index] = '-1'
        trans_list[index + 1] = '-1'
        trans_list.insert(index + 2, '-1')
        trans_list.insert(index + 3, '1')


def med_features_digitalized(trans_list, index):   # transformation for 24 features for medications
    medf = trans_list[index]
    if medf == "Up":
        trans_list[index] = '1'
        trans_list.insert(index+1, '-1')
        trans_list.insert(index+2, '-1')
        trans_list.insert(index+3, '-1')
    elif medf == "Down":
        trans_list[index] = '-1'
        trans_list.insert(index + 1, '1')
        trans_list.insert(index + 2, '-1')
        trans_list.insert(index + 3, '-1')
    elif medf == "Steady":
        trans_list[index] = '-1'
        trans_list.insert(index + 1, '-1')
        trans_list.insert(index + 2, '1')
        trans_list.insert(index + 3, '-1')
    elif medf == "No":
        trans_list[index] = '-1'
        trans_list.insert(index + 1, '-1')
        trans_list.insert(index + 2, '-1')
        trans_list.insert(index + 3, '1')


def change_digitalized(change):  # transformation for change of medicine
    if change == "No":
        return '-1'
    elif change == "Ch":
        return '1'
    elif change == "?":
        return ''


def diabetesmed_digitalized(diabe):  # transformation for Diabetes medications
    if diabe == "No":
        return '-1'
    elif diabe == "Yes":
        return '1'
    elif diabe == "?":
        return ''


def readmitted_digitalized(readm):  # transformation for being readmitted within 30 days or not
    if readm == "NO":
        return '-1'
    elif readm == "<30":
        return '1'
    elif readm == ">30":
        return '-1'

    ''' # For original labels classification 
    if readm == "NO":
        return '0'
    elif readm == "<30":
        return '1'
    elif readm == ">30":
        return '2'
    '''


'''
read the database
'''

original_database = []
database = open('diabetic_data3.csv')
database.readline()
while True:
# for test in a smaller scale
# i = 0
# while i < 12:
    one_transaction = database.readline()
    if one_transaction != "" and one_transaction != "\n":
        original_database.append(one_transaction.split(","))  # put the data into list
    else:
        break
    #i += 1
if database:
    database.close()

# print original_database

cleaned_database = original_database[:]

'''
categorize continues attributes
'''
final_database = []

patient_id_list = []  # a list to record every patient id
for trans in cleaned_database:
    if trans[11] in patient_id_list:  # if the patient id has been seen, skip this record
        continue
    else:
        patient_id_list.append(trans[11])  # add new patient id to the list

    if trans[3] == "11" or trans[3] == "19" or trans[3] == "20" or trans[3] == "21" \
            or trans[3] == "13" or trans[3] == "14":
        continue  # remove diseased or hospice patients to prevent bias

    # Digitalized each feature
    trans[10] = readmitted_digitalized(trans[10])
    a1_digitalized(trans)
    diag_digitalized(trans)
    specialty_digitalized(trans)
    admsource_digitalized(trans)
    discharge_digitialized(trans)
    age_digitalized(trans)
    trans[1] = gender_digitalized(trans[1])
    race_digitalized(trans)

    final_database.append(trans)


# print final_database


with open('digitalized3.csv','wb') as file:  # write the result to digitalized3.csv
    for l in final_database:
        for item in l:
            if l.index(item) < len(l) - 1:
                file.write(str(item)+",")
            else:
                file.write(item)

