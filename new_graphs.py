#!python3

from sqlalchemy import *
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import datetime
import random

    



def failure_mode_graph_generator(name_search, fail_search_string, connection, plot_title):
    
    pie_fail_labels = []
    pie_fail_values = []
    fail_dict = {}

    name_query = connection.execute(name_search)

    for row in name_query:
        if row [0] not in pie_fail_labels:
            pie_fail_labels.append(row[0])

        else:
            continue

    for mode in pie_fail_labels:
        fail_dict[mode] = 0

    fail_query = connection.execute(fail_search_string)

    for row in fail_query:
        fail_dict[row[2]]+=1

    for label in pie_fail_labels:
        pie_fail_values.append(fail_dict[label])

    the_grid = GridSpec(2,2)
    explode =[]
    for wedge in range(len(pie_fail_labels)):
        explode.append(.1)

    
    #plt.subplot(the_grid[0,0], aspect=1)
    fig1, ax1 = plt.subplots()
    font = {'family':'garamond',
            'color': 'black',
            'weight': 'bold',
            'size': 20,}
    ax1.pie(pie_fail_values, explode = explode, labels = pie_fail_labels, startangle=90,
            autopct ='%1.1f%%', pctdistance = .85)
    plt.title(plot_title, loc = "center", fontdict = font, y=1.10)
    ax1.axis('equal')
    plt.tight_layout()

    #File Saving
    current_date = datetime.date.today()
    number = random.randint(1,1000)
    save_string = plot_title+" "+str(current_date)+str(number)
    plt.savefig(save_string, dpi = 800, bbox_inches = 'tight')