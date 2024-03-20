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

filename = 'src/diagrams_example/example2'
with Diagram("Grouped Workers", filename=filename, show=False, direction="TB"):
    (
        ELB("lb")
        >> [
            EC2("worker1"),
            EC2("worker2"),
            EC2("worker3"),
            EC2("worker4"),
            EC2("worker5"),
        ]
        >> RDS("events")
    )
