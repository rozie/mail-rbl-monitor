#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import socket
import sys


def reverse_ip(ip):
    octets = ip.split(".")
    octets.reverse()
    return ".".join(octets)


def read_ip_list():
    pass


def load_rbls(rbls_file):
    rbls = set()
    try:
        with open(rbls_file, "r") as fh:
            for line in fh:
                rbls.add(line.strip())
    except Exception as e:
        print("Cannot read RBLs from {}, error was {}".format(rbls_file, e))
    return rbls


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='abcc - Automatic Best Connection Chooser')

    parser.add_argument(
        '-i', '--ip', required=False,
        default=False, help="Single IP to be checked"
    )
    parser.add_argument(
        '-r', '--rbls', required=False, default='rbls.list',
        help="File with RBLs to check. One RBL in each line"
    )
    parser.add_argument(
        '-c', '--count', required=False, action='store_true',
        help="Report count of RBLs for each IP"
    )
    parser.add_argument(
        '-g', '--global_count', required=False, action='store_true',
        help="Report total count of RBLs occurences"
    )
    parser.add_argument(
        '-d', '--detailed', required=False, action='store_true',
        help="Report status of IP on every RBL. 1 means listed."
    )
    options = parser.parse_args()
    return options


def check_ip_on_rbl(ip, rbl):
    query = reverse_ip(ip) + '.' + rbl
    try:
        socket.gethostbyname(query)
        return 1
    except socket.error:
        return 0


def main():
    options = parse_arguments()
    rbls = load_rbls(options.rbls)
    ips = set()
    if options.ip:
        ips.add(options.ip)
    global_count = 0
    for ip in ips:
        count = 0
        for rbl in rbls:
            result = check_ip_on_rbl(ip, rbl)
            count += result
            if options.detailed:
                print("{} {}".format(rbl, result))
        if options.global_count:
            global_count += count
    if options.global_count:
        print(global_count)
    sys.exit(bool(count))


if __name__ == '__main__':
    main()
