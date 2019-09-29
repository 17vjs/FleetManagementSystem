# import pandas and matplotlib 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
def multiAnalysis():
    percentl = [ ]
    percentp = [ ]   

    Cars = 'Car A', 'Car B', 'Car C', 'Car D', 'Car E'
    profits = [163,49,343,236,211]
    loss = [113,329,98,101,119]
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
    plt.subplot(121)
    plt.title('Profit %')
    plt.pie(profits, labels=Cars, colors=colors,autopct='%1.1f%%', shadow=True, startangle=90)

    plt.subplot(122)
    plt.title('Loss %')
    plt.pie(loss, labels=Cars, colors=colors,autopct='%1.1f%%', shadow=True, startangle=90)
    plt.suptitle("PROFIT % AND LOSS % ", bbox={'facecolor':'0.8', 'pad':5})
    plt.show()

    data = [[10000, 0, 3400, 1230, 3500], 
            [18000,5000, 4000, 1100,4500], 
            [26000,3000, 3700, 1350,1900], 
            [30000,4500, 0, 1390, 1890], 
            [15000,10000,600, 1107, 1800], 
            [8000,8000, 5000, 0, 800], 
            [16500,2000, 1200, 1330,6600], 
            [48000,6100, 0, 1400,2000], 
            [32000,8350, 800, 2000,7500], 
            [21000,15000, 0, 5400, 4000] ] 
    
    df = pd.DataFrame(data, columns = ['Insurance_Amt','Loans_Amt','Maintenance_Amt','Permit_Amt','Tax_Amt'] ) 

    df.plot.bar() 

    plt.show() 


labels = ['Vehicle 1','Vehicle 2','Vehicle 3','Vehicle 4','Vehicle 5']
Income_of_all_trips = [40000, 34000, 30000, 35000, 27000]
Expenditure_of_the_year = [25000, 32000, 34000, 20000, 25000]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, Income_of_all_trips, width, label='Yearly Income')
rects2 = ax.bar(x + width/2, Expenditure_of_the_year, width, label='Yearly Expenditure')

ax.set_ylabel('Amount in Rs')
ax.set_title('LIABILITY OR ASSET', bbox={'facecolor':'0.8', 'pad':5})
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)
fig.tight_layout()
plt.show()


Maintenance = 'Tyre', 'Oiling', 'Welding', 'Engine', 'Misc'
amount = [800,400,350,450,200]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
plt.pie(amount, labels=Maintenance, colors=colors,autopct='%1.1f%%', shadow=True, startangle=90)
plt.title("MAINTENANCE", bbox={'facecolor':'0.8', 'pad':5})
plt.show()







