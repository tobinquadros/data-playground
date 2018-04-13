FROM jupyter/minimal-notebook
# See README for image docs here:
# https://github.com/jupyter/docker-stacks/tree/master/minimal-notebook

LABEL component-id="jupyter"

ADD requirements.txt /code/
WORKDIR /code

USER $NB_USER
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD jupyter_notebook_config.py /home/jovyan/.jupyter/
