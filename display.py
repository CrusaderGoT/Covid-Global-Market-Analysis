from plot_class import DataPlot

'''Here is where you can display plot
of effect of covid on trade
the data here comprise of trade of
different products from 2015-2021
for convienece the countries will be listed.\n
countries('Australia', 'China', 'East Asia (excluding China)',
 'European Union (27)', 'Japan', 'Total (excluding China)', 
'United Kingdom', 'United States')
'''

# to plot first create an instance of Dataplot
#dp = DataPlot()
# print(dp.countries) #to show available countries
# there are a couple of funtions that allows us to display
# first is to get the values to plot
#vl = dp.get_values('australia', 'imports', 2020)
# print(dp.get_prodM(vl)) # to get plottable products
# now we plot
#dp.plot_data(vl, 'All', '$')
# we can provide details for the plot via a dict
# this dict accepts keys('title', 'xlabel', 'ylabel', 'style', 'label', 'a', 'color')
# style and a are int(0-27) and float(0-1) that determine plot stlye and line transperency
"""details = {'title': 'All imports in Australia 2020',
      'ylabel': 'value of export ($)', 'xlabel': 'dates of exports', 'a': 0.5,
      'style': 0, 'label':'All', 'color': 'red'}
dp.plot_data(vl, 'All', '$', kwargs=details)
"""
# for stacking multiple plots
dp = DataPlot()
d = dp.get_values('china', 'exports', 2020)
d2 = dp.get_values('Australia', 'exports', 2020)


dt = {'title': 'Comparison of Meat products in China and USA in 2020',
      'ylabel': 'value of export ($)', 'xlabel': 'dates of exports',
      'style': 8, 'labels':['Meat and edible offal(China)', 'Meat and edible offal(USA)']}
dp.splot([d, d2], ['All', 'All'], '$', kwargs=dt)
