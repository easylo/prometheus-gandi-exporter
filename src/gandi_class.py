from prometheus_client.core import GaugeMetricFamily

import json, requests, sys, time, os, ast, signal, datetime

import logging, socket, ssl
from xmlrpc import client

class GandiCollector(object):

  def __init__(self, api_key):
        """ initializing attributes"""
        self.apikey = api_key
        self.METRIC_PREFIX = 'gandi_info'
        
  def collect(self):

    metric_description = 'Number of days before the domain expires' 
    labels =  ['domain','fqdn', 'date_registry_creation', 'date_updated', 'date_registry_end']
    gauge = GaugeMetricFamily(self.METRIC_PREFIX, '%s' % metric_description, value=None, labels=labels)

    api = client.ServerProxy('https://rpc.gandi.net/xmlrpc/')

    domains = api.domain.list(self.apikey, {'items_per_page': 500,'sort_by' : 'date_registry_end asc'})

    for domain in domains:

        domain_date_fmt = r'%Y%m%dT%H:%M:%S' #20150227T15:25:14

        fqdn = ''
        date_registry_end = ''
        date_registry_creation = ''

        for key, field in domain.items():

            # print(key, 'is the key for ', field)
            if key == "fqdn" :
                fqdn = field
            elif key == "date_registry_end" :
                date_registry_end = field
            elif key == "date_updated" :
                date_updated = field
            elif key == "date_registry_creation" :
                date_registry_creation = field
            #else :
                #no action

        # todo if fqdn date_registry_end date_registry_creation 

        days_valid = datetime.datetime.strptime(str(date_registry_end),domain_date_fmt) - datetime.datetime.utcnow()    

        gauge.add_metric([ fqdn, fqdn, str(date_registry_creation), str(date_updated), str(date_registry_end)], days_valid.days)

    yield gauge
