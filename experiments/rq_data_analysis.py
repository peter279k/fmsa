import os
import numpy as np
import scienceplots
import clickhouse_connect
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


print('RQ1 and RQ2 experimental data analysis is started.')

dpi = 300
fontdict={'size': 14}
plot_dir = './exp_plot'

if os.path.isdir(plot_dir) is False:
    os.mkdir(plot_dir)


host = '172.17.0.1'
username = 'fmsa_exp'
password = 'fmsa_exp'

client = clickhouse_connect.get_client(host=host, username=username, password=password)

rq1_table_name = 'rq1_log_table'
rq1_exp_sql = f'''
SELECT * FROM {rq1_table_name} ORDER BY timestamp
'''
rq2_table_name = 'rq2_log_table'
rq2_exp_sql = f'''
SELECT * FROM {rq1_table_name} ORDER BY timestamp
'''


rq1_exp_data = client.query(rq1_exp_sql)
timestamps = []
second = 0
status_code200 = []
status_code500 = []

for record in rq1_exp_data.result_rows:
    timestamp = record[0]
    timestamps += second,
    if record[-1][0] == '2':
        status_code200 += 1,
        status_code500 += 0,
    else:
        status_code200 += 0,
        status_code500 += 1,

    second += 1


print('Processing and Drawing the RQ1 data.')

xlabel = 'Timeline (s)'
ylabel = 'Count'
with plt.style.context(['science', 'ieee', 'no-latex']):
    fig, ax = plt.subplots()
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))

    ax.set_xlim(0, 60)

    ax.plot(timestamps, status_code200, label='200', color='blue', ls='-', marker='')
    ax.plot(timestamps, status_code500, label='500', color='orange', ls='-', marker='')

    ax.set_xlabel(xlabel, fontdict=fontdict)
    ax.set_ylabel(ylabel, fontdict=fontdict)

    fig.savefig(f'{plot_dir}/fig_rq1_result.svg', dpi=dpi)
    plt.close()


rq2_table_name = 'rq2_log_table'
rq2_exp_sql = f'''
SELECT * FROM {rq2_table_name} ORDER BY timestamp
'''

rq2_exp_data = client.query(rq2_exp_sql)
timestamps = []

closed_state = []
half_open_state = []
open_state = []

for record in rq2_exp_data.result_rows:
    timestamp = record[0]
    timestamps += timestamp.strftime('%f')[0:3],
    message = record[1].lower()
    if 'closed' in record[1].lower():
        closed_state += 1,
        half_open_state += 0,
        open_state += 0,
    elif 'half' in record[1].lower():
        closed_state += 0,
        half_open_state += 1,
        open_state += 0,
    else:
        closed_state += 0,
        half_open_state += 0,
        open_state += 1,

print('Processing and Drawing the RQ2 data.')

xlabel = 'Timeline (ms)'
ylabel = 'Count'
with plt.style.context(['science', 'ieee', 'no-latex']):
    fig, ax = plt.subplots()
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))

    ax.bar(timestamps, closed_state, label='closed', color='green')
    ax.bar(timestamps, half_open_state, label='half open', color='blue')
    ax.bar(timestamps, open_state, label='open', color='orange')

    ax.set_xlabel(xlabel, fontdict=fontdict)
    ax.set_ylabel(ylabel, fontdict=fontdict)

    fig.savefig(f'{plot_dir}/fig_rq2_result.svg', dpi=dpi)
    plt.close()


print('RQ1 and RQ2 experimental data analysis is finished.')
