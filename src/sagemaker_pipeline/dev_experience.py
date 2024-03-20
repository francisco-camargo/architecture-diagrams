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
from diagrams.onprem.vcs import Git

os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz-10.0.1-win64/bin'

path = 'src/sagemaker_pipeline/'
filename = 'dev_experience'
filepath = path + filename
graph_attr = {
    'pad': '0.2',
}

with Diagram(
    name='Developer Experience',
    filename=filepath,
    show=False,
    graph_attr=graph_attr,
    curvestyle='curved',
):

    user = Client('Developer')
    input = S3('Input Data')
    git = Git('Author Code')
    codecommit = Codecommit('CodeCommit')

    with Cluster('CodePipeline'):
        codepipeline = Codepipeline('CodePipeline')
        pull_code = Codecommit('CodeCommit')
        codebuild = Codebuild('CodeBuild')
        (codepipeline >> Edge() << pull_code)
        codepipeline >> codebuild

    sm = Sagemaker('SageMaker Pipeline')
    output = S3('Results')

    user >> git >> codecommit >> codepipeline
    user >> input >> sm >> output
    codebuild >> sm
