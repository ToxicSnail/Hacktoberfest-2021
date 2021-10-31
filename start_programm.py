import os

n = input('Какую монету вы хотите видеть?\n')
if n == 'eth':
    os.system('run_eth.py')
elif n == 'hot':
    os.system('run_hot.py')
