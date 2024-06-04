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
from diagrams.aws.devtools import Codebuild, Codecommit, Codepipeline
from diagrams.aws.ml import Sagemaker
from diagrams.aws.storage import S3
from diagrams.onprem.client import Client
from diagrams.aws.management import Cloudwatch

# os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz-10.0.1-win64/bin'
os.environ["PATH"] += os.pathsep + 'C:/Users/nxf88571/Documents/Graphviz-10.0.1-win64/bin'

path = 'src/sagemaker_mlops_template/'
filename = 'dev_experience'
filepath = path + filename
graph_attr = {
    'pad': '0.2',
}

with Diagram(
    # name='Developer Experience',
    name='',
    filename=filepath,
    show=False,
    graph_attr=graph_attr,
    curvestyle='curved',
):

    user = Client('Developer')
    # input = S3('Input Data')
    codecommit = Codecommit('CodeCommit')

    with Cluster('ML Pipeline'):
        input = S3('Input Data')
        sm = Sagemaker('SageMaker Pipeline')
        output = S3('Results')

    with Cluster('CI/CD'):
        codepipeline = Codepipeline('CodePipeline')
        pull_code = Codecommit('CodeCommit')
        codebuild = Codebuild('CodeBuild')
        (codepipeline >> Edge() << pull_code)
        codepipeline >> codebuild

    # sm = Sagemaker('SageMaker Pipeline')
    sm_logs = Sagemaker('SM Logs')
    # output = S3('Results')

    user >> codecommit >> codepipeline
    user >> input >> sm >> output
    codebuild >> sm
    codebuild >> Cloudwatch('Logs')
    sm >> sm_logs