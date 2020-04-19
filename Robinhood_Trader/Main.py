import sys
import robin_stocks as r

if len(sys.argv) != 3:
    print('Usage: python3 Main.py <username> <password>')
    sys.exit(0)

r.login(sys.argv[1], sys.argv[2])

#print("Account profile: ")
#print(r.load_account_profile())

#FIRST STEP TOP DOWN:

#1. CALCULATE MACD

    #1.1 CALCULATE LONG TERM EMA (26 DAY TERM)

        #1.1A CALCULATE SMA - Calculate simple mean average for 26 days. Need to find historicals for the last 26
# values per day divided by the number of days which is a constant 26.



            # Test of the historicals and current number putting into a list from Robinstocks api
def get_Last_20(inputSymbol):

    historicals_1 = r.get_historicals(inputSymbol, span='month', bounds='regular')
    first_value = []
    indexes = []
    new_list = list(historicals_1)
    for days in new_list:
        first_value.append(days.get('begins_at'))
    for n in range(0,(len(first_value) - 1)):
        string = first_value[n]
        if string[11:20] == '19:00:00Z':
           indexes.append(n)
    list1 = []
    for i in range(0, len(indexes) - 1):
        string2 = indexes[i]
        current_dic = new_list[string2]
        list1.append(float(current_dic.get('close_price')))

    Sum_Last_20 = float(sum(list1))

    total_number = len(list1)
    SMA = Sum_Last_20/total_number
    print(SMA)
    return SMA
    
    #1.1B CALCULATE SMOOTHING FACTOR - Call Function

    #1.1C CALCULATE EMA

    #get brandon help with recurssion

    #1.2 CALCULATE SHORT TERM EMA (12 DAY TERM)

        #1.2A CALCULATE SMA
def get_Last_12(inputSymbol):

    historicals_2 = r.get_historicals(inputSymbol, span='month', bounds='regular')
    first_value = []
    indexes = []
    new_list = list(historicals_2)
    for days in new_list:
        first_value.append(days.get('begins_at'))
    for n in range(0,(len(first_value) - 1)):
        string = first_value[n]
        if string[11:20] == '19:00:00Z':
           indexes.append(n)
    list1 = []
    for i in range(0, len(indexes) - 1):
        string2 = indexes[i]
        current_dic = new_list[string2]
        list1.append(float(current_dic.get('close_price')))

    Sum_Last_12 = float(sum(list1))

    total_number = len(list1)
    SMA = Sum_Last_12/total_number
    print(SMA)
    return SMA


        #1.2B CALCULATE SMOOTHING FACTOR
def smoothing_fac(days):
    smoothing_factor = 2/(days - 1)
    return smoothing_factor

        #1.2C CALCULATE EMA

        # get brandon help for recurssion

    #1.3 CALCULATE DIFFERENCE OF SHORT TERM MINUS LONG TERM

#2. CALCULATE SIGNAL LINE

    #2.1 CALCULATE SMA (9 DAY TERM)

#3. IF MACD CROSSES SIGNAL LINE, DECIDE TO BUY OR SELL.

    #3.1 COMPARISON BETWEEN 1.3 AND 2.1


get_Last_20('MDT')
get_Last_12('MMM')

#https://www.investopedia.com/terms/m/macd.asp


r.logout()

