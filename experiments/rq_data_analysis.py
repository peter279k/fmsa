import os
import numpy as np
import scienceplots
import clickhouse_connect
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


print('RQ1 and RQ2 experimental data analysis is started.')

dpi = 300
fontdict={'size': 14}
figsize = (3, 3)
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
status_code200 = []
status_code500 = []

for record in rq1_exp_data.result_rows:
    timestamp = record[0]
    timestamps += float(timestamp.timestamp()),
    if record[-1][0] == '2':
        status_code200 += 1,
        status_code500 += 0,
    else:
        status_code200 += 0,
        status_code500 += 1,


print('Processing and Drawing the RQ1 data.')

xlabel = 'Time'
ylabel = 'Count'
with plt.style.context(['science', 'ieee', 'no-latex']):
    fig, ax = plt.subplots()
    ax.plot(timestamps, status_code200, color='blue', ls='-', marker='.')
    ax.plot(timestamps, status_code500, color='orange', ls='-', marker='.')
    ax.autoscale()
    ax.set_xlabel(xlabel, fontdict=fontdict)
    ax.set_ylabel(ylabel, fontdict=fontdict)
    fig.savefig(f'{plot_dir}/fig_avg_cpu_usage.svg', dpi=dpi)
    plt.close()


rq2_table_name = 'rq2_log_table'
rq2_exp_sql = f'''
SELECT * FROM {rq2_table_name} ORDER BY timestamp
'''

rq2_exp_data = client.query(rq2_exp_sql)
for record in rq2_exp_data.result_rows:
    print(record)


print('RQ1 and RQ2 experimental data analysis is finished.')
