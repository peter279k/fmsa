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


host = os.getenv('IP_ADDRESS', '172.17.0.1')
username = 'fmsa_exp'
password = 'fmsa_exp'

client = clickhouse_connect.get_client(host=host, username=username, password=password)

rq4_table_name = 'rq4_log_table'
rq4_exp_sql = f'''
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
    fig.savefig(f'{plot_dir}/fig_rq4_result.png', dpi=dpi)
    plt.close()


rq5_normal_table_name = 'rq5_log_table'
rq5_circuit_table_name = 'rq5_log_table_circuit'
rq5_broken_table_name = 'rq5_log_table_broken'

rq5_normal_exp_sql = f'''
SELECT * FROM {rq5_normal_table_name} ORDER BY timestamp LIMIT 120
'''
rq5_circuit_exp_sql = f'''
SELECT * FROM {rq5_circuit_table_name} ORDER BY timestamp LIMIT 120
'''
rq5_broken_exp_sql = f'''
SELECT * FROM {rq5_broken_table_name} ORDER BY timestamp LIMIT 120
'''

rq5_normal_exp_data = client.query(rq5_normal_exp_sql)
rq5_circuit_exp_data = client.query(rq5_circuit_exp_sql)
rq5_broken_exp_data = client.query(rq5_broken_exp_sql)

timestamps = []

normal_state_blue = []
normal_state_light_blue = []
normal_counter200 = 1
normal_counter500 = 1

circuit_state_yellow = []
circuit_state_light_yellow = []
circuit_counter200 = 1
circuit_counter500 = 1

broken_state_red = []
broken_state_light_red = []
broken_counter200 = 1 
broken_counter500 = 1

second = 0

for record in rq5_normal_exp_data.result_rows:
    timestamps += second,
    second += 1
    if record[2] == '200':
        normal_state_blue += normal_counter200,
        normal_state_light_blue += 0,
        normal_counter200 += 1
    else:
        normal_state_light_blue += normal_counter500,
        normal_state_blue += 0,
        normal_counter500 += 1

for record in rq5_circuit_exp_data.result_rows:
    if record[2] == '200':
        circuit_state_yellow += circuit_counter200,
        circuit_state_light_yellow += 0,
        circuit_counter200 += 1
    else:
        circuit_state_light_yellow += circuit_counter500,
        circuit_state_yellow += 0,
        circuit_counter500 += 1

for record in rq5_broken_exp_data.result_rows:
    if record[2] == '200':
        broken_state_red += broken_counter200,
        broken_state_light_red += 0,
        broken_counter200 += 1
    else:
        broken_state_light_red += broken_counter500,
        broken_state_red += 0,
        broken_counter500 += 1


print('Processing and Drawing the RQ5 data.')

xlabel = 'Timeline (s)'
ylabel = 'Cumulative Count'

with plt.style.context(['science', 'ieee', 'no-latex']):
    fig, ax = plt.subplots()

    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))

    ax.set_xlim(0, 120)

    ax.plot(timestamps, normal_state_blue, label='200-normal', color='darkblue', ls='-')
    ax.plot(timestamps, normal_state_light_blue, label='503-normal', color='royalblue', ls='-')

    ax.plot(timestamps, circuit_state_yellow, label='200-circuit', color='orange', ls='-')
    ax.plot(timestamps, circuit_state_light_yellow, label='503-circuit', color='darkorange', ls='-')

    ax.legend(title='HTTP Status Code')

    ax.set_xlabel(xlabel, fontdict=fontdict)
    ax.set_ylabel(ylabel, fontdict=fontdict)

    fig.savefig(f'{plot_dir}/fig_rq5_normal_circuit_result.svg', dpi=dpi)
    fig.savefig(f'{plot_dir}/fig_rq5_normal_circuit_result.png', dpi=dpi)
    plt.close()

with plt.style.context(['science', 'ieee', 'no-latex']):
    fig, ax = plt.subplots()

    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))

    ax.set_xlim(0, 120)

    ax.plot(timestamps, broken_state_red, label='200', color='darkred', ls='-')
    ax.plot(timestamps, broken_state_light_red, label='503', color='red', ls='-')

    ax.legend(title='HTTP Status Code')

    ax.set_xlabel(xlabel, fontdict=fontdict)
    ax.set_ylabel(ylabel, fontdict=fontdict)

    fig.savefig(f'{plot_dir}/fig_rq5_broken_result.svg', dpi=dpi)
    fig.savefig(f'{plot_dir}/fig_rq5_broken_result.png', dpi=dpi)
    plt.close()


print('RQ4 and RQ5 experimental data analysis is finished.')
