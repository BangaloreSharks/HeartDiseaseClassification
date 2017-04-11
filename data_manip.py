import pickle

def manip(lines):
    # getting data
    data = [line.split(',') for line in lines]

    # removing null
    processed_data = []
    for line in data:
        flag = 0
        for point in line:
            if point == '?':
                flag = 1
        if flag == 0:
            processed_data.append(line)

    # converting float
    for i in range(len(processed_data)):
        for j in range(len(processed_data[i])):
            processed_data[i][j] = float(processed_data[i][j])
    return processed_data


file = open('data/processed.cleveland.data','r')
lines = file.readlines()
processed_data = manip(lines)
pickle.dump(processed_data,open('data/processed_data/cleveland.pickle','w'))
