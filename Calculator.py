import math

def calculate_average(data):
    total = sum(data)
    average = total / len(data)
    return average

def calculate_variance(data):
    average = calculate_average(data)
    dev_squ_sum = 0
    for num in data:
        dev_squ_sum += (num - average) ** 2
    variance = dev_squ_sum / len(data)
    return variance

def calculate_std(variance):
    std_dev = math.sqrt(variance)
    return std_dev

def point(number):
    str_number = str(number)
    if '.' in str_number:
        decimal_places = len(str_number.split('.')[1])
        if decimal_places > 3:
            return round(number, 3)
    return number

data = input("데이터를 입력하세요 (숫자들을 쉼표로 구분하여 입력하세요): ")
data = [float(x.strip()) for x in data.split(',')]

average = calculate_average(data)
variance = calculate_variance(data)
std_dev = calculate_std(variance)

average = point(average)
variance = point(variance)
std_dev = point(std_dev)

print("입력한 데이터:", data)
print("평균:", average)
print("분산:", variance)
print("표준편차:", std_dev)