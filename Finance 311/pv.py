#present value calc
def pv(numYears,yearArray, rate):

    if numYears is not len(yearArray):
            raise ValueError("Array length does not equal number of years")
    else:
            pv = 0
            for i in range(1,numYears+1):
                    temp_pv = yearArray[i-1]/(1+rate)**i
                    pv += temp_pv
                    print("Discounted cash flow: {}  for year {}".format(temp_pv, i))
            return pv

def discountRate(futureValue, presentValue, time):
    rate = float((futureValue*1.000/presentValue)**(1/time*1.00000))
    return rate - 1.0

def perpetuity(payment, rate):
    return payment/rate

def single_pv(year, payment, rate):
    pv = 0
    pv = payment/(1+rate)**year
    print("Discounted cash flow: {}  for year {}".format(payment, year))
    return pv
