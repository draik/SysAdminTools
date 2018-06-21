#! /usr/bin/env python

'''
Check on the health of hard drives, using SMART monitor tools.
This requires the installation of smartmontools on the operating system.
'''

from argparse import ArgumentParser
from email.MIMEText import MIMEText
import json
from os import geteuid
import pySMART
import requests
import smtplib
from sys import argv


# Send email notification
def send_email(SUBJECT, BODY):
    smtp_server = 'localhost'
    sender = 'pysmart@YourHost'
    receiver = 'You@Example.Com'
    msg = MIMEText(BODY)
    msg['Subject'] = SUBJECT

    server = smtplib.SMTP(smtp_server)
    server.sendmail(sender, receiver, msg.as_string())
    server.quit()


# Send Telegram notification
def notify_telegram(HEADER, MESSAGE):
    tg_url = 'https://api.telegram.org/bot'
    tg_token = '123456789:AbCdEfGhIjKlMnOpQrStUvWxYz123456789'
    tg_method = 'sendMessage'
    tg_bot_url = tg_url + tg_token + '/' + tg_method
    tg_chat_id = 987654321

    msg_data = {'chat_id': tg_chat_id,
                'text': "*{}*\n{}".format(HEADER,
                                          MESSAGE),
                'parse_mode': 'Markdown'}

    requests.get(tg_bot_url, params=msg_data)


# Check drive status from self-tests
def check_drive():
    dev_stats = []
    for dev in devlist.devices:
        dev_stats.append("{}: {}".format(dev.name,
                                         dev.assessment))

    return dev_stats


# Information on each drive
def drive_info():
    info = {}
    for dev in devlist.devices:
        drive = dev.name
        info[drive] = {}
        info[drive]['model'] = dev.model
        info[drive]['serial'] = dev.serial
        info[drive]['firmware'] = dev.firmware
        info[drive]['capacity'] = dev.capacity
        info[drive]['check'] = dev.assessment

    return json.dumps(info,
                      indent=4,
                      separators=(',',':'),
                      sort_keys=True)


# Drive menu
def drive_list():
    drive_menu = {}
    opt = 1
    for dev in devlist.devices:
        drive_menu[opt] = dev.name
        opt += 1

    drive_menu['A'] = 'ALL'
    drive_menu['Q'] = 'Quit'

    return drive_menu


# Results from self-tests
def test_results():
    drive_menu = drive_list()

    for k, v in sorted(drive_menu.iteritems()):
        print "{:>3}) {}".format(k, v)

    selection = raw_input("Select drive(s) to check: ")

    try:
        if selection.upper() == 'A':
            for dev in devlist.devices:
                dev.update()
                print dev.name
                dev.all_selftests()
        elif selection.upper() == 'Q':
            exit('Quitting.')
        elif int(selection) in drive_menu:
            drive = '/dev/' + drive_menu[int(selection)]
            dev = pySMART.Device(drive)
            dev.update()
            print dev.name
            dev.all_selftests()
    except ValueError:
        exit('Invalid option')


# Perform a self-test on drives
def test_drive(TYPE):
    drive_menu = drive_list()

    for k, v in sorted(drive_menu.iteritems()):
        print "{:>3}) {}".format(k, v)

    selection = raw_input("Select drive(s) to test: ")

    try:
        if selection.upper() == 'A':
            for dev in devlist.devices:
                print "{}: {}".format(dev.name,
                                      dev.run_selftest(TYPE)[1])
        elif selection.upper() == 'Q':
            exit('Quitting.')
        elif int(selection) in drive_menu:
            drive = '/dev/' + drive_menu[int(selection)]
            dev = pySMART.Device(drive)
            print "{}: {}".format(dev.name,
                                  dev.run_selftest(TYPE)[1])
    except ValueError:
        exit('Invalid option')


# Main function
def main():
    arguments()


# List of arguments
def arg_parser():
    parser = ArgumentParser(conflict_handler='resolve',
                            description='SMART drive health monitor tool',
                            usage="%(prog)s [options]")

    options = parser.add_mutually_exclusive_group()
    options.add_argument('-c',
                         action='store_true',
                         dest='CHECK',
                         help='Check PASS/FAIL self-test status')
    options.add_argument('-i',
                         action='store_true',
                         dest='INFO',
                         help='Info for each drive')
    options.add_argument('-r',
                         action='store_true',
                         dest='RESULTS',
                         help='Results from self-tests')
    options.add_argument('-t',
                         choices=['long', 'short'],
                         dest='TEST',
                         help='Perform drive self-test')
    parser.add_argument('--notify',
                         action='store_true',
                         dest='NOTIFY',
                         help='Send email and Telegram alert')

    if len(argv) == 1:
        exit(parser.print_help())
    else:
        return parser.parse_args()


# Arguments
def arguments():
    args = arg_parser()

    global devlist
    devlist = pySMART.DeviceList()

    if args.CHECK:
        for drive in check_drive():
            print drive
        if args.NOTIFY:
            send_email('Drive Check',
                       '\n'.join(check_drive()))
            notify_telegram('Drive Check',
                            '\n'.join(check_drive()))
    elif args.INFO:
        print drive_info()
        if args.NOTIFY:
            send_email('Drive Info',
                       drive_info())
            drive = json.loads(drive_info())
            for dev in drive:
                info = []
                for k, v in drive[dev].iteritems():
                    info.append("{}: {}".format(k, v))
                notify_telegram('Drive Info',
                                '\n'.join(info))
    elif args.RESULTS:
        test_results()
    elif args.TEST:
        test_drive(args.TEST)


if __name__ == '__main__':
    try:
        # MUST be run as root/sudo
        if geteuid() != 0:
            exit("Needs to be run as root!")
        else:
            main()
    except KeyboardInterrupt:
        exit("Quitting.")

