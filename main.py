"""
See the user guide for the set-up of the main.py functionalities
"""
from os import system, name
import os.path
from os import path

# _ = system('cls')  # clear screen
""""
Action request through argparse. 
"""
import argparse
from datetime import date

def main(command_line=None):                                        # filename with ADIF in CSV format
    parser = argparse.ArgumentParser('ADIF report')
    subparsers = parser.add_subparsers(dest='command')

    report = subparsers.add_parser('report', help='creates a QSO-report on provided CSV file')

    # purchase = subparsers.add_parser('purchase', help='start process of purchasing item')
    #
    # sell = subparsers.add_parser('sell', help='information on sold items')
    # sell.add_argument('-id', '--id', help='identification number of sold item', required=True)
    # sell.add_argument('-soldprice', '--soldprice', help='price for sold item', required=True)
    # sell.add_argument('-solddate', '--solddate', help='date of sold item. Default = today', required=False)
    #
    # expire = subparsers.add_parser('expire', help='simulate expire dates and periods')
    # expire.add_argument('-simdate', '--simdate', help='start date of simulation. Default = today', required=False)
    # expire.add_argument('-numdays', '--numdays', help='number of simulated days', required=True)

    args = parser.parse_args(command_line)

    if args.command == "report":
        import report_ADIF

    # elif args.command == "purchase":
    #     import purchase_input
    #
    # elif args.command == "sell":
    #     id = str(args.id)
    #     sold_price = str(args.soldprice)
    #     sold_date = str(args.solddate)
    #     sell2(id, sold_date, sold_price)
    #
    # elif args.command == "expire":
    #     sim_date = str(args.simdate)
    #     num_of_days = int(args.numdays)
    #     get_expiry_report_simulated(sim_date, num_of_days)

    else:
        print ("\n Your input is required, based on information from the HELP file.\n"
               " Further optional commands are report (and maybe future commands)."
               "\n\n Type 'python main.py -h' for additional information.\n")

if __name__ == '__main__':
    main()