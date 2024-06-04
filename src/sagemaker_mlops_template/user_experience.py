'''
    Architecture diagram of SageMaker Pipeline project with
        Preprocessing
        Hyperparameter optimization
        Evaluation
        Explainability
        Model registration
'''

import os


from diagrams import Cluster, Diagram, Edge
from diagrams.aws.ml import Sagemaker
from diagrams.aws.storage import S3
from diagrams.onprem.client import Client
from diagrams.aws.integration import Eventbridge
from diagrams.aws.devtools import Codepipeline

# os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz-10.0.1-win64/bin'
os.environ["PATH"] += os.pathsep + 'C:/Users/nxf88571/Documents/Graphviz-10.0.1-win64/bin'

path = 'src/sagemaker_mlops_template/'
filename = 'user_experience'
filepath = path + filename
graph_attr = {
    'pad': '0.2',
}

with Diagram(
    name='User Experience',
    filename=filepath,
    show=False,
    graph_attr=graph_attr,
    curvestyle='curved',
):

    user = Client('End-User')
    input = S3('Inference Data')

    with Cluster('Black-box'):
        eventbridge = Eventbridge('Detect New Data')
        ml_pipeline =  Codepipeline('Inference Pipeline')

    output = S3('Inference Results')

    user >> input
    input >> eventbridge
    eventbridge >> ml_pipeline >> output
