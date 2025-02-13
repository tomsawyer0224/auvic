import os
import click
from multiprocessing import Pool

def execute(command):
    os.system(command)
@click.command()
@click.option("-s", "--source_dir", type=click.STRING)
@click.option("-t", "--target_dir", type=click.STRING)
def convert(source_dir, target_dir):
    os.makedirs(target_dir, exist_ok=True)
    files = os.listdir(source_dir)
    cmds = []
    for file in files:
        source = os.path.join(source_dir, file)
        target = os.path.join(target_dir, file)
        cmd = f"ffmpeg -i {source} -acodec mp3 -vcodec copy {target}"
        cmds.append(cmd)
    with Pool() as p:
        p.map(execute, cmds)

if __name__=="__main__":
    convert()