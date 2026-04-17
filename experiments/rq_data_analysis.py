import os
import numpy as np
import scienceplots
import clickhouse_connect
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


print('RQ4 and RQ5 experimental data analysis is started.')

dpi = 300
fontdict={'size': 14}
plot_dir = './exp_plot'

if os.path.isdir(plot_dir) is False:
    os.mkdir(plot_dir)


host = '172.17.0.1'
username = 'fmsa_exp'
password = 'fmsa_exp'

client = clickhouse_connect.get_client(host=host, username=username, password=password)

rq4_table_name = 'rq4_log_table'
rq4_exp_sql = f'''
SELECT * FROM {rq4_table_name} ORDER BY timestamp
'''
rq5_table_name = 'rq5_log_table'
rq5_exp_sql = f'''
SELECT * FROM {rq4_table_name} ORDER BY timestamp
'''


rq4_exp_data = client.query(rq4_exp_sql)
timestamps = []
second = 0
status_code200 = []
status_code500 = []

counter2 = 1
counter5 = 1
for record in rq4_exp_data.result_rows:
    timestamp = record[0]
    timestamps += second,
    if record[2][0] == '2':
        status_code200 += counter2,
        status_code500 += 0,
        counter2 += 1
    else:
        status_code200 += 0,
        status_code500 += counter5,
        counter5 += 1

    second += 1


print('Processing and Drawing the RQ4 data.')

xlabel = 'Timeline (s)'
ylabel = 'Cumulative Count'
with plt.style.context(['science', 'ieee', 'no-latex']):
    fig, ax = plt.subplots()
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))

    ax.set_xlim(0, 120)

    ax.plot(timestamps, status_code200, label='200', color='blue', ls='-', marker='')
    ax.plot(timestamps, status_code500, label='503', color='orange', ls='-', marker='')

    ax.legend(title='HTTP Status Code')

    ax.set_xlabel(xlabel, fontdict=fontdict)
    ax.set_ylabel(ylabel, fontdict=fontdict)

    fig.savefig(f'{plot_dir}/fig_rq4_result.svg', dpi=dpi)
    plt.close()


rq5_table_name = 'rq5_log_table'
rq5_circuit_table_name = 'rq5_log_table_circuit'
rq5_exp_sql = f'''
SELECT * FROM {rq5_table_name} ORDER BY timestamp LIMIT 120
'''
rq5_exp_circuit_sql = f'''
SELECT * FROM {rq5_circuit_table_name} ORDER BY timestamp LIMIT 120
'''

rq5_exp_data = client.query(rq5_exp_sql)
rq5_cirsuit_exp_data = client.query(rq5_exp_circuit_sql)
timestamps = []

normal_state = []
circuit_state = []
second = 0

for record in rq5_exp_data.result_rows:
    timestamps += second,
    normal_state += int(record[2]),
    second += 1

for record in rq5_cirsuit_exp_data.result_rows:
    circuit_state +=  int(record[2][0:3]),

print('Processing and Drawing the RQ5 data.')

xlabel = 'Timeline (s)'
ylabel = 'HTTP Status Code'
with plt.style.context(['science', 'ieee', 'no-latex']):
    fig, ax = plt.subplots()

    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_yticks([200, 503])

    ax.plot(timestamps, normal_state, label='normal', color='blue', ls='-')
    ax.plot(timestamps, circuit_state, label='open/half-open', color='orange', ls='-')

    ax.set_xlabel(xlabel, fontdict=fontdict)
    ax.set_ylabel(ylabel, fontdict=fontdict)

    fig.savefig(f'{plot_dir}/fig_rq5_result.svg', dpi=dpi)
    plt.close()


print('RQ4 and RQ5 experimental data analysis is finished.')
