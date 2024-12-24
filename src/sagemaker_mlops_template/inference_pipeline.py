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
from diagrams.aws.integration import Eventbridge

# os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz-10.0.1-win64/bin'
os.environ["PATH"] += os.pathsep + 'C:/Users/nxf88571/Documents/Graphviz-10.0.1-win64/bin'

path = 'src/sagemaker_mlops_template/'
filename = 'inference_experience'
filepath = path + filename
graph_attr = {
    'pad': '0.2',
}

with Diagram(
    name='Single Account Inference Pipeline',
    filename=filepath,
    show=False,
    graph_attr=graph_attr,
    curvestyle='curved',
):

    user = Client('End-User')
    eventbridge = Eventbridge('Detect New Data')

    with Cluster('CI/CD'):
        codepipeline = Codepipeline('CodePipeline')
        inference_codebuild = Codebuild('Inference CodeBuild')
        codepipeline >> inference_codebuild
    eventbridge >> codepipeline
    cloudwatch_logs = Cloudwatch('Logs')

    with Cluster('Inference Pipeline'):
        inference_data = S3('Inference Data')
        inference_sagemaker = Sagemaker('Inference Pipeline')
        inference_logs = Sagemaker('Inference Logs')
        user >> inference_data
        inference_codebuild >> Edge() << inference_sagemaker
        inference_sagemaker >> inference_logs
    inference_codebuild >> cloudwatch_logs
    inference_data << eventbridge # TODO: direction is bugged here...

    with Cluster('ML Artifacts'):
        model_registry = Sagemaker('Model Registry')
        pre_artifact = S3('Feature Engineering\nModel Artifact')
        model_artifact = S3('ML Model Artifact')
        model_registry >> Edge(style='invis') >> pre_artifact
        pre_artifact >> Edge(style='invis') >> model_artifact

    model_artifact >> Edge(style='bold', color='orange') >> inference_sagemaker

    inference_results = S3('Inference Results')
    inference_sagemaker >> inference_results
    inference_data >> inference_sagemaker
