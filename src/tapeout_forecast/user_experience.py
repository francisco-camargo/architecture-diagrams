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

# os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz-10.0.1-win64/bin'
os.environ["PATH"] += os.pathsep + 'C:/Users/nxf88571/Documents/Graphviz-10.0.1-win64/bin'

path = 'src/sagemaker_pipeline/'
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

    with Cluster('ML Pipeline'):
        input = S3('Input Data')
        ml_pipeline = Sagemaker('SageMaker Pipeline')
        output = S3('Results')

    gui = Sagemaker('GUI')

    user >> input >> ml_pipeline >> output
    user >> gui >> ml_pipeline
