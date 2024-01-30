import csv
from datetime import datetime

fp = 'data\\effects-of-covid-19-on-trade-at-15-december-2021-provisional.csv'
with open(fp, 'r') as f:
    reader = csv.reader(f)
    head_row = next(reader)
    header = dict()
    for index, col_head in enumerate(head_row):
        header[col_head.lower()] = index
    
    data = dict()
    '''a dict containing all the necessary processed information'''
    for row in reader:
        match row:
            case[dir, year, date, _, country, commodity, _, measure, val, cum_val] if dir == 'Exports':
                # exclude countries named All
                if country != 'All':
                    data.setdefault(country, dict())
                    data[country].setdefault(dir, dict())
                    data[country][dir].setdefault(year, dict())
                    data[country][dir][year].setdefault(commodity, dict())
                    #divide into commodities based on measure($ or Tonnes)
                    if commodity == commodity and measure == '$':
                        # add values for $
                        data[country][dir][year][commodity].setdefault(measure, list())
                        data[country][dir][year][commodity][measure].append(int(val))
                        # collect dates
                        data[country][dir][year][commodity].setdefault('$dates', list())
                        data[country][dir][year][commodity]['$dates'].append(datetime.strptime(date, "%d/%m/%Y"))
                    elif commodity == commodity and measure == 'Tonnes':
                        # add values for $
                        data[country][dir][year][commodity].setdefault(measure, list())
                        data[country][dir][year][commodity][measure].append(int(val))
                        # collect dates
                        data[country][dir][year][commodity].setdefault('Tdates', list())
                        data[country][dir][year][commodity]['Tdates'].append(datetime.strptime(date, "%d/%m/%Y"))
                    else:
                        print(f"{commodity} in {measure} wasn't processed")
            case[dir, year, date, _, country, commodity, _, measure, val, cum_val] if dir == 'Imports':
                if country != 'All':
                    data.setdefault(country, dict())
                    data[country].setdefault(dir, dict())
                    data[country][dir].setdefault(year, dict())
                    data[country][dir][year].setdefault(commodity, dict())
                    #divide into commodities based on measure($ or Tonnes)
                    if commodity == commodity and measure == '$':
                        # add values for $
                        data[country][dir][year][commodity].setdefault(measure, list())
                        data[country][dir][year][commodity][measure].append(int(val))
                        # collect dates
                        data[country][dir][year][commodity].setdefault('$dates', list())
                        data[country][dir][year][commodity]['$dates'].append(datetime.strptime(date, "%d/%m/%Y"))
                    elif commodity == commodity and measure == 'Tonnes':
                        # add values for $
                        data[country][dir][year][commodity].setdefault(measure, list())
                        data[country][dir][year][commodity][measure].append(int(val))
                        # collect dates
                        data[country][dir][year][commodity].setdefault('Tdates', list())
                        data[country][dir][year][commodity]['Tdates'].append(datetime.strptime(date, "%d/%m/%Y"))
                    else:
                        print(f"{commodity} in {measure} wasn't processed")
            case[dir, year, date, _, country, commodity, _, measure, val, cum_val] if dir == 'Reimports':
                if country != 'All':
                    data.setdefault(country, dict())
                    data[country].setdefault(dir, dict())
                    data[country][dir].setdefault(year, dict())
                    data[country][dir][year].setdefault(commodity, dict())
                    #divide into commodities based on measure($ or Tonnes)
                    if commodity == commodity and measure == '$':
                        # add values for $
                        data[country][dir][year][commodity].setdefault(measure, list())
                        data[country][dir][year][commodity][measure].append(int(val))
                        # collect dates
                        data[country][dir][year][commodity].setdefault('$dates', list())
                        data[country][dir][year][commodity]['$dates'].append(datetime.strptime(date, "%d/%m/%Y"))
                    elif commodity == commodity and measure == 'Tonnes':
                        # add values for $
                        data[country][dir][year][commodity].setdefault(measure, list())
                        data[country][dir][year][commodity][measure].append(int(val))
                        # collect dates
                        data[country][dir][year][commodity].setdefault('Tdates', list())
                        data[country][dir][year][commodity]['Tdates'].append(datetime.strptime(date, "%d/%m/%Y"))
                    else:
                        print(f"{commodity} in {measure} wasn't processed")
            case _:
                print(f'These cases did not match:\n{row}')

