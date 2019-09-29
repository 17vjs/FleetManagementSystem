# sum uptax and group by vehicle
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
import numpy as np
def taxExpenditure():
    x = np.arange(4)
    money = [1e3, 2e3, 4.5e3, 3.0e3]

    a= ['CAR A', 'CAR B', 'CAR C', 'CAR D']

    fig, ax = plt.subplots()

    plt.bar(x, money)
    plt.xticks(x,a)
    plt.suptitle("Taxes amount for vehicles ", bbox={'facecolor':'0.8', 'pad':5})
    plt.show()
