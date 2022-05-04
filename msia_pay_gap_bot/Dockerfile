FROM --platform=linux/amd64 continuumio/anaconda3:2021.11

# aka mkdir and cd to it in the docker container
WORKDIR /bot_dir

# add host directory to docker container's /bot_dir
ADD ./ ./

ENV PYTHONPATH=/bot_dir
ENV USERNAME=wheattortoise
ENV PASSWORD=Shaolin8465123@

# RUN conda env create -f conda_environment.yml
# SHELL ["conda", "run", "-n", "myenv", "/bin/bash", "-c"]
# RUN cat /etc/apt/sources.list

RUN apt update -y
RUN apt install tesseract-ocr -y

RUN pip install -r requirements.txt

# RUN bash scripts/fetch_all_insta.sh
# RUN bash scripts/entrypoint.sh

# RUN python scripts/gen_post_id_csv.py malaysianpaygap/2022/