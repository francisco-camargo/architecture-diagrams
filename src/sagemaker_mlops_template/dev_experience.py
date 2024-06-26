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
    codecommit = Codecommit('CodeCommit')
    user >> codecommit

    with Cluster('CI/CD'):
        codepipeline = Codepipeline('CodePipeline')
        pull_code = Codecommit('CodeCommit')
        training_codebuild = Codebuild('Training CodeBuild')
        test_codebuild = Codebuild('Test CodeBuild')
        codepipeline << pull_code
        codepipeline >> test_codebuild
        test_codebuild >> training_codebuild

        inference_codebuild = Codebuild('Inference CodeBuild')
    codecommit >> codepipeline
    cloudwatch_logs = Cloudwatch('Logs')
    training_codebuild >> cloudwatch_logs

    with Cluster('Training Pipeline'):
        training_data = S3('Training Data')
        user >> training_data
        training_sagemaker = Sagemaker('Training Pipeline')
        training_logs = Sagemaker('Training Logs')
        training_sagemaker >> training_logs
    training_data >> training_sagemaker
    training_codebuild >> Edge() << training_sagemaker

    # eventbridge = Eventbridge('Detect New Data')
    # inference_data >> eventbridge
    with Cluster('Inference Pipeline'):
        inference_data = S3('Inference Data')
        inference_sagemaker = Sagemaker('Inference Pipeline')
        inference_logs = Sagemaker('Inference Logs')
        user >> inference_data
        inference_codebuild >> Edge() << inference_sagemaker
        inference_sagemaker >> inference_logs
    training_codebuild >> inference_codebuild
    inference_codebuild >> cloudwatch_logs

    with Cluster('ML Artifacts'):
        model_registry = Sagemaker('Model Registry')
        pre_artifact = S3('Feature Engineering\nModel Artifact')
        model_artifact = S3('ML Model Artifact')
        model_registry >> Edge(style='invis') >> pre_artifact
        pre_artifact >> Edge(style='invis') >> model_artifact

        training_sagemaker >> Edge(style='bold', color='orange') >> model_registry
        # model_registry >> pre_artifact
        # model_registry >> model_artifact
    model_artifact >> Edge(style='bold', color='orange') >> inference_sagemaker

    inference_results = S3('Inference Results')
    inference_sagemaker >> inference_results
    inference_data >> inference_sagemaker
    # eventbridge >> inference_sagemaker
    # pre_artifact >> inference_sagemaker
    # model_artifact >> inference_sagemaker
