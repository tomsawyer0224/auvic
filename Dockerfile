FROM continuumio/miniconda3

WORKDIR /app
COPY environment.yml .

RUN conda env create -f environment.yml

SHELL ["conda", "run", "-n", "auvic", "/bin/bash", "-c"]

COPY convert.py .

ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "auvic", "python", "convert.py"]