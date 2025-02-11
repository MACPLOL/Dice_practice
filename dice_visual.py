import plotly.express as px
from die import Die

#Creates two D6 dice

die_1=Die()
die_2=Die()

#Roll it and store results in list
results=[]
for roll_num in range(1000):
    roll_results=die_1.roll()+ die_2.roll()
    results.append(roll_results)

    #Analysis of results
    frequencies=[]
    max_results=die_1.num_sides+ die_2.num_sides
    poss_results=range(2, max_results+1)
    for value in poss_results:
        frequency= results.count(value)
        frequencies.append(frequency)

#Visualization of results
title="Results of Rolling Two D6 1,000 Times"
labels= {'x':'Result', 'y':'Frequency of Result'}
fig=px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

#Extra customization
fig.update_layout(xaxis_dtick=1)
fig.show()