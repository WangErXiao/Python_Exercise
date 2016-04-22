#!/usr/bin/env python

import json

host1ip=['192.168.1.1','192.168.1.2']
host2ip=['192.168.1.3']
group1 ='test1'
group2 ='test2'
hostdata={group1:{"hosts":host1ip},group2:{"hosts":host2ip}}

print json.dumps(hostdata,indent=4)
