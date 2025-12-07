from SILPackemaker.PacemakerDevice import PacemakerDevice
import pandas as pd

'''
TODO : Main simulation code steppin and implement data visualization and data reading
'''

def main():
    #initialize pacemaker
    pacemaker = PacemakerDevice()

    #read ecg_signal from MIT-BIH Arrhythmia Database
    ecg_signal = pd.read_csv('MIT-BIH Arrhythmia Database/100.csv')
    ecg_signal = ecg_signal['signal'].values

    ecg_signal_len = len(ecg_signal)

    for i in range(ecg_signal_len):
        new_pace = pacemaker.step(ecg_signal[i])
        print(new_pace)

if __name__ == "__main__":
    main()
