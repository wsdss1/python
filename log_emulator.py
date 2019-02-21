'''
log emulator for  system
'''

import datetime, time, random, logging

def randomt():
    for i in range(0,10):
        time.sleep(3)
        dtnow = datetime.datetime.now()
        rnd = random.randint(0,100)
        f = open('\\10.200.12.55\c$\Distr\ftp\PARMA\', 'a')
        f.write(f"{dtnow} test_data {rnd}\n")
        logging.info(f"print mess{dtnow}{rnd}")
        f.close()

if __name__ == "__main__":
    randomt()
