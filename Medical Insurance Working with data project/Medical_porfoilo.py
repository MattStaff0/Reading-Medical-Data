#Matthew Stafford Working with Medical Data 

import csv 
def get_data():
    with open('insurance.csv', 'r') as medical_data:
        csv_reader = csv.reader(medical_data)
        next(csv_reader)
        ages = []
        sex = []
        bmi = []
        children = []
        smoker = []
        region = []
        charges = []

        

        for row in csv_reader:
            
            ages.append(int(row[0]))
            sex.append(row[1])
            bmi.append(float(row[2]))
            children.append(int(row[3]))
            smoker.append(row[4])
            region.append(row[5])
            charges.append(float(row[6]))
        master_list = [ages, sex, bmi, children, smoker, region, charges]
        
    return master_list
master_list = get_data()



#Findning basic statistic measurements within the data

def averages(data):
    #Numerical Averages
    num_titles = ['age', 'bmi', 'amount of children', 'insurance cost']
    num_data = [data[0], data[2], data[3], data[6]]


    for name, info in zip(num_titles,num_data):
            print(f'The average {name} in this dataset is {round(sum(info)/len(info), 2)}.')
    #Categorial Averages 
    cat_data = [data[1], data[4], data[5]]
    males = 0 
    females = 0 
    south_west = 0 
    south_east = 0 
    north_east = 0
    north_west = 0
    smoker_count = 0 
    for sets in cat_data:
        for data in sets:
            if data == 'male':
                males += 1
            if data == 'female':
                females += 1
            if data == 'southwest':
                south_west += 1
            if data == 'southeast':
                south_east += 1
            if data == 'northeast':
                north_east += 1 
            if data == 'northwest':
                north_west += 1
            if data == 'yes':
                smoker_count += 1
    cat_list = ['males', 'females', 'south west', 'south east', 'north east', 'north west', 'smokers']
    new_cat_data = [males, females, south_west, south_east, north_east, north_west, smoker_count]
    for names, infos in zip(cat_list, new_cat_data):
        if names == 'males' or 'females' or 'smokers':
            print(f'The amount {names} in this data set is {infos}.')
        else:
            print(f'There are {infos} people from {names}.')
    
    return 

def insuance_by_variable(list):
    list_names = ['ages', 'sex', 'bmi', 'children', 'smoker', 'region', 'charges']
    age_data = list[0]
    sex_data = list[1]
    smoker_data = list[4]
    #age average insurance 
    low_age_range = [i for i in range(min(age_data), 36)]
    high_age_range = [i for i in range(36, max(age_data))]
    low_count = 0
    high_count = 0 
    
    insurance_cost_low = 0
    insurance_cost_high = 0 
    for i, val in enumerate(age_data):

        if val in low_age_range:
            insurance_cost_low += list[6][i]
            low_count += 1
        elif val in high_age_range:
            insurance_cost_high += list[6][i]
            high_count += 1

        
    avg_age_cost_low = insurance_cost_low / low_count
    avg_age_cost_high = insurance_cost_high / high_count
    

    print(f'The average insurance cost for a young adult, ages 19-35, is: ${round(avg_age_cost_low, 2)} and for an older adult, ages 36 and up, is ${round(avg_age_cost_high, 2)}.')
    #sex average cost
    insurance_cost_m = 0 
    insurance_cost_f = 0
    for i, val in enumerate(sex_data):
        if val == 'male':
            insurance_cost_m += list[6][i]
        else:
            insurance_cost_f += list[6][i]
    m_avg = insurance_cost_m / sex_data.count('male')
    f_avg = insurance_cost_f / sex_data.count('female')
    print(f'The average cost of insurance for a female is ${round(f_avg, 2)} and for a male is ${round(m_avg, 2)}')
    #smoker average cost 
    insurance_cost_smoke_y = 0 
    insurance_cost_smoke_n = 0
    for i, val in enumerate(smoker_data):
        if val == 'yes':
            insurance_cost_smoke_y += list[6][i]
        else:
            insurance_cost_smoke_n += list[6][i]
    smoke_y_avg = insurance_cost_smoke_y/smoker_data.count("yes")
    smoke_n_avg = insurance_cost_smoke_n/smoker_data.count("no")

    print(f'The average insurance cost for a smoker is ${round(insurance_cost_smoke_y/smoker_data.count("yes"), 2)} and for a non-smoker is ${round(insurance_cost_smoke_n/smoker_data.count("no"), 2)}. ')
    avgs_master_list = [f_avg, m_avg, avg_age_cost_low, avg_age_cost_high, smoke_y_avg, smoke_n_avg]
    return avgs_master_list

#anaylsis function 
def differences(list_dif):
    #list of differences and names 
    names_list =['males', 'old(36 and older)', 'smokers']
    differences_list = []
    #sex dif 
    sex_dif = list_dif[1] - list_dif[0]
    differences_list.append(sex_dif)
    #age range dif
    age_dif= list_dif[3] - list_dif[2]
    differences_list.append(age_dif)
    #smoker dif 
    smoke_dif = list_dif[4] - list_dif[5]
    differences_list.append(smoke_dif)
    combined_list = list(zip(differences_list, names_list))
    #print(combined_list)
    for val, name in combined_list:
        print(f'The {name} insurance cost is ${round(val,2)} above its counterpart.')


    
        
    return 
        
        
    

            


        
averages(master_list)
insuance_by_variable(master_list)
differences(insuance_by_variable(master_list))




        
            
    






 
