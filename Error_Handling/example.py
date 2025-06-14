import random

def generate_random_number(num_samples:int)->(list[tuple[int,int]]):

    try:
        if not isinstance(num_samples,int) or num_samples<=0:
            raise ValueError("Numbers must be integer and +ve")
        data = [(random.randint(1,100),random.randint(1,100)) for _ in range(num_samples)]
        return data
    except ValueError:
        print("data did not generate due to value error")
        return []
    except Exception as e:
        print("Exception error: ",e)
        return []
def calculate_ratio(data:list[tuple[int,int]])->list[tuple]:
    ratios = []
    try:
        for pairs in data:
            num1,num2 = pairs
            if not isinstance(num1,int) or not isinstance(num2,int):
                raise ValueError("Numbers must be integers")
            ratio = num1/num2
            ratios.append(ratio)
        return ratios
    except ZeroDivisionError:
        print("number can't be zero")
        return []
    except TypeError:
        print("please enter numbers")
        return []
    except Exception as e:
        print("Exception:",e)
        return []
def processing(num:int)->list[float]:
    data = generate_random_number(num)
    if not data:
        return[]
    ratio = calculate_ratio(data)
    return ratio

try:
    num = generate_random_number(0)
    result = calculate_ratio(num)

    if result:
        print("Operation succesfull, final list is: ",result)
    else:
        print("Calculation failed due to an error")
except Exception as e:
    print("error",e)
    