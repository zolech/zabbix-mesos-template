#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import json
import argparse


def get_metric(host, port, metric):
        response = urllib2.urlopen(
            'http://' + host + ':' + port + '/metrics/snapshot')
        data = json.load(response)
        # print json.dumps(data, indent=4, sort_keys=True)
        print data[metric]


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(
        description='Mesos metrics')
    arg_parser.add_argument(
        '-H', '--host', help="Specify host or ip address", required=True)
    arg_parser.add_argument(
        '-p', '--port', help="Specify mesos api port", required=True)
    arg_parser.add_argument(
        '-m', '--metric', help="Specify metric's name", required=True)

    arguments = arg_parser.parse_args()

    get_metric(arguments.host, arguments.port, arguments.metric)
