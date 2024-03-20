'''
Examples from
    https://diagrams.mingrammer.com/docs/getting-started/examples
'''

import os

from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz-10.0.1-win64/bin'

filename = 'src/diagrams_example/example1'
with Diagram('Web Service', filename=filename, show=False, outformat=['png']):
    ELB('lb') >> EC2('web') >> RDS('userdb')
