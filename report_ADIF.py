import os
import sys
import fileinput
import csv
import math
from os import system, name
from print_tabel import print_tabel
_ = system('cls')                                         # clear screen

QSO_count = 0                           # QSO-counter

# modes
FT8_count = 0
SSB_count = 0
AM_count = 0
FM_count = 0
SSTV_count = 0
BPSK_count = 0
othermode_count = 0

# operators
flag = 0
PA3EFR_count = 0
PD9HIX_count = 0
PE2PVD_count = 0
PD1EHO_count = 0
PD7BDN_count = 0
PB7TT_count = 0
PD3APM_count = 0
PD2SVA_count = 0
PD2GWE_count = 0
PD1RJM_count = 0
PA3TVV_count = 0
otheropr_count = 0

# bands
count_160 = 0
count_80 = 0
count_60 = 0
count_40 = 0
count_30 = 0
count_20 = 0
count_17 = 0
count_15 = 0
count_12 = 0
count_10 = 0
count_6 = 0
count_4 = 0
count_2 = 0
count_70 = 0
count_EL = 0
otherband_count = 0
otherband_type = []
othermode_type = []
otheropr_type = []

full_path = os.path.realpath(__file__)
file_directory = os.path.dirname(full_path)
to_report_file = input ("Name of the ADIF.CSV file for the report (in the same directory): ")
# to_report_file = "ADIF2.csv"                                 # test line
ADIF_file = os.path.join(file_directory, to_report_file)
print_tabel(ADIF_file)                                      # external routine

with fileinput.input(files=ADIF_file, inplace=False, mode='r') as file:
    reader =csv.DictReader(file)
    # print("\t,".join(reader.fieldnames))                  # print back the headers
    for row in reader:
        QSO_count+= 1                                           # QSO-counter
# mode counting
        if row["mode"] == "FT8":
            FT8_count += 1
        elif row["mode"] == "SSB" or row["mode"] == "LSB" or row["mode"] =="USB":
            SSB_count += 1
        elif row["mode"] == "AM":
            AM_count += 1
        elif row["mode"] == "FM":
            FM_count += 1
        elif row["mode"] == "SSTV":
            SSTV_count += 1
        elif row["mode"] == "BPSK" or row["mode"] == "PSK31" or row["mode"] == "QPSK":
            BPSK_count += 1
        else:
            if row["mode"] in othermode_type:
                pass
            else:
                othermode_type = othermode_type + [row["mode"]]
            othermode_count += 1

# operator counting
        row["comment"] = str.upper(row["comment"])
        if "PA3EFR" in row["comment"] or "ERWIN" in row["comment"]:
            PA3EFR_count += 1
            flag = 1
        if "PD9HIX" in row["comment"] or "SANDER" in row["comment"]:
            PD9HIX_count += 1
            flag = 1
        if "PE2PVD" in row["comment"] or "PATRICK" in row["comment"]:
            PE2PVD_count += 1
            flag = 1
        if "PD1EHO" in row["comment"] or "EVELYN" in row["comment"]:
            PD1EHO_count += 1
            flag = 1
        if "PD7BDN" in row["comment"] or "BAS" in row["comment"]:
            PD7BDN_count += 1
            flag = 1
        if "PB7TT" in row["comment"] or "RONALD" in row["comment"]:
            PB7TT_count += 1
            flag = 1
        if "PD3APM" in row["comment"] or "ANNE-PAUL" in row["comment"]:
            PD3APM_count += 1
            flag = 1
        if "PD2SVA" in row["comment"] or "MAARTEN" in row["comment"]:
            PD2SVA_count += 1
            flag = 1
        if "PD2GWE" in row["comment"] or "GUIDO" in row["comment"]:
            PD2GWE_count += 1
            flag = 1
        if "PD1RJM" in row["comment"] or "RAMON" in row["comment"]:
            PD1RJM_count += 1
            flag = 1
        if "PA3TVV" in row["comment"] or "THOMAS" in row["comment"]:
            PA3TVV_count += 1
            flag = 1
        if flag == 0:
            if row["comment"] in otheropr_type:
                pass
            else:
                otheropr_type = otheropr_type + [row["comment"]]
            otheropr_count += 1
        flag = 0

# band counting
        if "160m" in row["band"]:
            count_160 += 1
        elif "80m" in row["band"]:
            count_80 += 1
        elif "60m" in row["band"]:
            count_60 += 1
        elif "40m" in row["band"]:
            count_40 += 1
        elif "30m" in row["band"]:
            count_30 += 1
        elif "20m" in row["band"]:
            count_20 += 1
        elif "17m" in row["band"]:
            count_17 += 1
        elif "15m" in row["band"]:
            count_15 += 1
        elif "12m" in row["band"]:
            count_12 += 1
        elif "10m" in row["band"]:
            count_10 += 1
        elif "6m" == row["band"]:
            count_6 += 1
        elif "4m" == row["band"]:
            count_4 += 1
        elif "2m" == row["band"]:
            count_2 += 1
        elif "70cm" in row["band"]:
            count_70 += 1
        elif row["band"] == "Echolink" or row["band"] == "ECHOLINK":
            count_EL += 1
        else:
            if row["band"] in otherband_type:
                pass
            else:
                otherband_type = otherband_type + [row["band"]]
            otherband_count += 1

print("\t number of QSO's:",QSO_count)

print("\n Modes:")
print("\t FT-8\t\t\t:", FT8_count)
print("\t SSB \t\t\t:", SSB_count)
print("\t AM \t\t\t:", AM_count)
print("\t FM \t\t\t:", FM_count)
print("\t SSTV\t\t\t:", SSTV_count)
print("\t PSK\t\t\t:", BPSK_count)
print("\t Other modes \t\t:", othermode_count, othermode_type)

print("\n Frequency Bands:")
print("\t 160 meters\t\t:", count_160)
print("\t 80 meters\t\t:", count_80)
print("\t 60 meters\t\t:", count_60)
print("\t 40 meters\t\t:", count_40)
print("\t 30 meters\t\t:", count_30)
print("\t 20 meters\t\t:", count_20)
print("\t 17 meters\t\t:", count_17)
print("\t 15 meters\t\t:", count_15)
print("\t 12 meters\t\t:", count_12)
print("\t 10 meters\t\t:", count_10)
print("\t 6 meters\t\t:", count_6)
print("\t 4 meters\t\t:", count_4)
print("\t 2 meters\t\t:", count_2)
print("\t 70 centimeters\t\t:", count_70)
print("\t Echolink\t\t:", count_EL)
print("\t Other Bands\t\t:", otherband_count, otherband_type)

print("\n Modes:")
print("\t PA3EFR, Erwin\t\t:", PA3EFR_count)
print("\t PA3TVV, Thomas\t\t:", PA3TVV_count)
print("\t PB7TT,  Ronald\t\t:", PB7TT_count)
print("\t PD1EHO, Evelyn \t:", PD1EHO_count)
print("\t PD1RJM, Ramon\t\t:", PD1RJM_count)
print("\t PD2GWE, Guido \t\t:", PD2GWE_count)
print("\t PD2SVA, Maarten \t:", PD2SVA_count)
print("\t PD3APM, Anne-Paul \t:", PD3APM_count)
print("\t PD7BDN, Bas\t\t:", PD7BDN_count)
print("\t PD9HIX, Sander \t:", PD9HIX_count)
print("\t PE2PVD, Patrick \t:", PE2PVD_count)
print("\t Other operators \t:", otheropr_count, otheropr_type)
