'''
Examples from
    https://diagrams.mingrammer.com/docs/getting-started/examples
'''

import os

from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.aggregator import Fluentd
from diagrams.onprem.analytics import Spark
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.monitoring import Grafana, Prometheus
from diagrams.onprem.network import Nginx
from diagrams.onprem.queue import Kafka

os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz-10.0.1-win64/bin'

filename = 'src/diagrams_example/example5'
with Diagram(
    name="Advanced Web Service with On-Premise (colored)",
    filename=filename,
    show=False,
):
    ingress = Nginx("ingress")

    metrics = Prometheus("metric")
    metrics << Edge(color="firebrick", style="dashed") << Grafana("monitoring")

    with Cluster("Service Cluster"):
        grpcsvc = [Server("grpc1"), Server("grpc2"), Server("grpc3")]

    with Cluster("Sessions HA"):
        primary = Redis("session")
        (
            primary - Edge(color="brown", style="dashed") - Redis("replica")
            << Edge(label="collect")
            << metrics
        )
        grpcsvc >> Edge(color="brown") >> primary

    with Cluster("Database HA"):
        primary = PostgreSQL("users")
        (
            primary - Edge(color="brown", style="dotted") - PostgreSQL("replica")
            << Edge(label="collect")
            << metrics
        )
        grpcsvc >> Edge(color="black") >> primary

    aggregator = Fluentd("logging")
    (
        aggregator
        >> Edge(label="parse")
        >> Kafka("stream")
        >> Edge(color="black", style="bold")
        >> Spark("analytics")
    )

    (
        ingress
        >> Edge(color="darkgreen")
        << grpcsvc
        >> Edge(color="darkorange")
        >> aggregator
    )
