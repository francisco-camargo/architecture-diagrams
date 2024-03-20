import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz-10.0.1-win64/bin'

from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

with Diagram('Web Service', filename='src/diagrams_example/test',show=False, outformat=['dot','png']):
    ELB('lb') >> EC2('web') >> RDS('userdb')