#!/usr/bin/env python3

# TODO: Create a legend http://stackoverflow.com/questions/3499056/making-a-legend-key-in-graphviz
# 
# Proposed legend:
#   essential dependency = line w/ arrow
#   non-essential dependency = dotted line w/ arrow

from graphviz import Digraph

# Github subraph
g = Digraph('cluster_github',
            body=['label=Github'],
            graph_attr={'style': 'filled', 'fillcolor': 'white'})
github_nodes = ['github_repo', 'github_webhook']
[g.node(github_node) for github_node in github_nodes]
g.edge('github_webhook', 'github_repo')

# Docker subgraph
d = Digraph('cluster_docker',
           body=['label=Docker'],
           graph_attr={'style': 'filled', 'fillcolor': 'white'})
docker_nodes = ['docker_compose', 'docker_engine']
[d.node(docker_node) for docker_node in docker_nodes]
d.edge('docker_compose', 'docker_engine')

# Makefile subgraph
m = Digraph('cluster_makefile',
            body=['label=Makefile'],
            graph_attr={'style': 'filled', 'fillcolor': 'white'})
makefile_nodes = [
    'make_dev',
    'make_test',
    'make_build',
    'make_check',
    'make_mock',
    'make_echo_image_name',
    'make_clean'
]
[m.node(makefile_node) for makefile_node in makefile_nodes]
m.edges((
    ('make_check', 'make_clean'),
    ('make_check', 'make_mock'),
    ('make_mock', 'make_build')
))

# Jenkins subgraph
j = Digraph('cluster_jenkins',
            body=['label=Jenkins'],
            graph_attr={'style': 'filled', 'fillcolor': 'white'})
jenkins_nodes = [
    'build_now',
    'build_trigger',
    'stage_test',
    'stage_build',
    'stage_check',
    'stage_push',
    'stage_deploy_qa',
    'stage_deploy_staging',
    'stage_gate',
    'stage_deploy_production',
    'section_post_always'
]
[j.node(jenkins_node) for jenkins_node in jenkins_nodes]
j.edge('build_trigger', 'build_now', style='dotted')
j.edges((
    ('stage_test', 'build_trigger'),
    ('stage_build', 'stage_test'),
    ('stage_check', 'stage_build'),
    ('stage_push', 'stage_check'),
    ('stage_deploy_qa', 'stage_push'),
    ('stage_deploy_staging', 'stage_push'),
    ('stage_gate', 'stage_deploy_staging'),
    ('stage_deploy_production', 'stage_gate'),
    ('section_post_always', 'build_trigger')
))

# ECR subgraph
e = Digraph('cluster_ecr',
            body=['label=ECR'],
            graph_attr={'style': 'filled', 'fillcolor': 'white'})
ecr_nodes = ['ecr_repo']
[e.node(ecr_node) for ecr_node in ecr_nodes]

# Kubernetes Manifest subgraph
km = Digraph('cluster_k8s_manifest',
            body=['label="Kubernetes Files"'],
            graph_attr={'style': 'filled', 'fillcolor': 'white'})
k8s_manifest_nodes = [
    'k8s_manifest'
]
[km.node(k8s_manifest_node) for k8s_manifest_node in k8s_manifest_nodes]

# Kubernetes Objects subgraph
ko = Digraph('cluster_k8s_objects',
            body=['label="Kubernetes Objects"'],
            graph_attr={'style': 'filled', 'fillcolor': 'white'})
k8s_objects_nodes = [
    'k8s_configmap',
    'k8s_secret',
    'k8s_pod',
    'k8s_svc',
    'k8s_deployment' 
]
[ko.node(k8s_objects_node) for k8s_objects_node in k8s_objects_nodes]
ko.edges((
    ('k8s_svc', 'k8s_pod'),
    ('k8s_deployment', 'k8s_pod')
))

# Main graph
ci = Digraph(name='ci-pipeline',
            comment='Directed graph of continuous integration pipelline',
            graph_attr={'rankdir': 'RL', 'compound': 'true', 'size': '10'})
ci.node('start', shape='Mdiamond', style='filled', fillcolor='green')
ci.node('endpoints', shape='Mdiamond', style='filled', fillcolor='green')
ci.node('qa', shape='rectangle', style='filled', fillcolor='azure')
ci.node('staging', shape='rectangle', style='filled', fillcolor='azure')
ci.node('production', shape='rectangle', style='filled', fillcolor='azure')

# Add subgraphs to main graph
subgraphs = [g, d, m, j, e, km, ko]
[ci.subgraph(subgraph) for subgraph in subgraphs]

# Add custom styled cross-subgraph node edges
ci.edge('build_trigger', 'github_webhook', style='dotted')
ci.edge('make_dev', 'docker_engine', ltail='cluster_makefile', lhead='cluster_docker')
ci.edge('build_trigger', 'docker_engine', ltail='cluster_jenkins', lhead='cluster_docker')
ci.edge('qa', 'k8s_svc', lhead='cluster_k8s_objects')
ci.edge('staging', 'k8s_svc', lhead='cluster_k8s_objects')
ci.edge('production', 'k8s_svc', lhead='cluster_k8s_objects')

# Add add cross-subgraph node edges
ci.edges((
    ('start', 'build_trigger'),
    ('stage_build', 'make_build'),
    ('stage_test', 'make_test'),
    ('stage_check', 'make_check'),
    ('stage_push', 'make_echo_image_name'),
    ('stage_push', 'ecr_repo'),
    ('section_post_always', 'make_clean'),
    ('stage_deploy_qa', 'k8s_manifest'),
    ('stage_deploy_staging', 'k8s_manifest'),
    ('stage_deploy_production', 'k8s_manifest'),    
    ('qa', 'stage_deploy_qa'),
    ('staging', 'stage_deploy_staging'),
    ('production', 'stage_deploy_production'),
    ('k8s_manifest', 'ecr_repo'),
    ('k8s_pod', 'k8s_secret'),
    ('k8s_pod', 'k8s_configmap'),
    ('endpoints', 'k8s_svc')    
))

# print(ci.source)
ci
