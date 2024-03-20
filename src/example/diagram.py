from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

# with Diagram('Web Service', show=False):
#     ELB('lb') >> EC2('web') >> RDS('userdb')

import graphviz  # doctest: +NO_EXE
dot = graphviz.Digraph(comment='The Round Table')
dot  #doctest: +ELLIPSIS

dot.node('A', 'King Arthur')  # doctest: +NO_EXE
dot.node('B', 'Sir Bedevere the Wise')
dot.node('L', 'Sir Lancelot the Brave')

dot.edges(['AB', 'AL'])
dot.edge('B', 'L', constraint='false')

print(dot.source)

dot.render('doctest-output/round-table.gv', view=True)  # doctest: +SKIP
'doctest-output/round-table.gv.pdf'