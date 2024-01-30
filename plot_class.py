from covid_on_trade_plot import data as main_data
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpathces

class DataPlot:
    '''a class for making use of the data for different functions'''
    def __init__(self, data: dict=main_data) -> None:
        'initializes the class with the data dict'
        self.data = data
        # get the countries, direction, and year
        self.countries = set()
        self.direction = set()
        self.years = set()
        for k, v in self.data.items():
            self.countries.add(k)
            for k2, v2 in v.items():
                self.direction.add(k2)
                for k3 in v2.keys():
                    self.years.add(k3)
        # sort the sets into lists
        self.countries = sorted(self.countries)
        self.years = sorted(self.years)
        self.direction = sorted(self.direction)
        # bool for getting products and measures from values
        self.bool = False
    def get_values(self, country: str, dir: str, year: int) -> dict:
        '''returns a dict of corresponding commodities, measure, and dates.'''
        keys = []
        condition = 0
        if country.title() in self.countries:
            keys.append(country.title())
            condition += 1
        else:
            print(f'{country} not in available list of countries.\n'
                  f'{self.countries}')
            raise KeyError
        if dir.title() in self.direction:
            keys.append(dir.title())
            condition += 1
        else:
            print(f'{dir} not in list of direction.\n'
                  f'{self.direction}.')
            raise KeyError
        if str(year) in self.years:
            keys.append(str(year))
            condition += 1
        else:
            print(f'{year} not in available list of years.\n'
                  f'{self.years}')
            raise KeyError
        # if condition is meet(complete-correct arguments), fetch the values
        if condition == 3:
            try:
                self.values = self.data[keys[0]][keys[1]][keys[2]]
            except KeyError:
                print(f"No {keys[1]} on {keys[0]} for the year {keys[2]} available.")
                raise KeyError
            else:
                self.bool = True
                self.get_prodM(self.values)
                return self.values
        return dict()  
    def get_prodM(self, value: dict):
        'for getting the products available for plot'
        if self.bool:
            self.lst = []
            for k in value.keys():
                self.lst.append((k))
            return self.lst
        else:
            print('Run get_value() first')
            raise ValueError
    def plot_data(self, value, product: str, measure: str='$' or 'Tonnes', **kwargs):
        'for ploting single values'
        vl = value
        # initialize the mode for fetching datetime
        date_time = None
        if measure == '$':
            date_time = '$dates'
        elif measure == 'Tonnes':
            date_time = 'Tdates'
        else:
            print(f'{measure} should either be `$` or `Tonnes`.')
            raise AttributeError
        for k, v in vl.items(): # v = {$:[values], dates[datetime]}
            if k == product and product in self.lst:
                for k2, v2 in v.items():
                    if k2 == measure:
                        self.y_values = v2
                    if k2 == date_time:
                        self.x_values = v2
            elif product not in self.lst and k != product:
                print(f'invalid product "{product}"'
                      '.\nRun get_prodM() '
                      'to see list of products.')  
                raise AttributeError
        y = np.array(self.y_values)
        x = self.x_values
        if kwargs:
            try:
                #style plot
                sl = plt.style.available
                styles = dict()
                for i, n in enumerate(sl):
                    styles[i] = n
                plt.style.use(styles[int(kwargs['kwargs']['style'])])
                # create fig and ax
                fig, ax = plt.subplots(figsize=(12, 6))
                ax.plot(x, y, c=kwargs['kwargs']['color'], label=kwargs['kwargs']['label'], alpha=float(kwargs['kwargs']['a']))
                # format plot
                ax.set(title=kwargs['kwargs']['title'],
                    ylabel=kwargs['kwargs']['ylabel'], xlabel=kwargs['kwargs']['xlabel'])
                fig.autofmt_xdate(ha='left')
                ax.tick_params(axis='both', which='major', labelsize=10)
                plt.legend(fancybox=True, draggable=True, loc='upper center', fontsize='small', labelcolor='linecolor')
            except KeyError:
                print('Rename your key to match or create the key that caused error.')
                raise KeyError
            else:
                plt.show()
        else:
            #style plot
            sl = plt.style.available
            styles = {}
            for i, n in enumerate(sl):
                styles[i] = n
            plt.style.use(styles[5])
            # create fig and ax
            fig, ax = plt.subplots(figsize=(12, 6))
            ax.plot(x, y, c='red')
            fig.autofmt_xdate(ha='left')
            ax.tick_params(axis='both', which='major', labelsize=10)
            plt.show()
    def splot(self, values: list, product: list, measure: str='$' or 'Tonnes', **kwargs):
        'for stackin multiple value, and plot'
        # check if the length of values, and product to check parallel to eachother are same
        if len(values) == len(product):
            pass
        else:
            print('The number of elements in the values and product must be the same')
            raise IndexError
        # initialize the mode for fetching datetime
        date_time = None
        if measure == '$':
            date_time = '$dates'
        elif measure == 'Tonnes':
            date_time = 'Tdates'
        else:
            print(f'{measure} should either be `$` or `Tonnes`.')
            raise ValueError
        # process the value to a dict that contains the product as key
        # and the values to plot as values
        num_values = list()
        dates_values = list()
        for inx, vl in enumerate(values):
            for k, v in vl.items():
                for ind, prd in enumerate(product):
                    if inx == ind and k == prd:
                        for k2, v2 in v.items():
                            if k2 == measure:
                                num_values.append(v2)
                            if k2 == date_time:
                                dates_values.append(v2)
                    elif prd not in self.lst:
                        print(f"{prd} not a valid item.\n"
                              f"This is the list of valid items {self.lst}")
                        raise ValueError
        # plot the num and date values
        fig, ax = plt.subplots()
        for ix, vs in enumerate(num_values):
            for i, dt in enumerate(dates_values):
                for ie, p in enumerate(product):
                    if ix == i and ix == ie:
                        ax.plot(dt, vs, label=f'{p}', linewidth=0.8)
        fig.autofmt_xdate(ha='left')
        if kwargs:
            try:
                #style plot
                sl = plt.style.available
                styles = dict()
                for i, n in enumerate(sl):
                    styles[i] = n
                plt.style.use(styles[kwargs['kwargs']['style']])
                ax.set(title=kwargs['kwargs']['title'],
                    ylabel=kwargs['kwargs']['ylabel'], xlabel=kwargs['kwargs']['xlabel'])
                ax.tick_params(axis='both', which='major', labelsize=10)
                # try to change the label if provided
                patch = list()
                if kwargs['kwargs']['labels']:
                    print(kwargs['kwargs']['labels'])
                    for i in kwargs['kwargs']['labels']:
                        p = mpathces.Patch(label=f'{i}')
                        patch.append(p)
            except KeyError:
                print('Rename your key to match or create the key that caused error.')
                raise KeyError
            else:
                plt.legend(draggable=True, fontsize='small', labelcolor='linecolor')
                plt.show()
        else:
            plt.show()
