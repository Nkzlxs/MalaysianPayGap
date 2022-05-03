FROM --platform=linux/amd64 continuumio/anaconda3:2021.11

# aka mkdir and cd in the docker container
WORKDIR /bot_dir

# add host directory to docker container's /bot_dir
ADD ./ ./

ENV PYTHONPATH=/bot_dir

# RUN conda env create -f conda_environment.yml
# SHELL ["conda", "run", "-n", "myenv", "/bin/bash", "-c"]

RUN pip install -r requirements.txt

RUN bash scripts/fetch_all_insta.sh

RUN python scripts/gen_post_id_csv.py malaysianpaygap/2022/