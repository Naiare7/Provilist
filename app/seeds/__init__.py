from .seeds_provincias import seed_provincias
from .seeds_municipios import seed_municipios


def run_seeds():
    seed_provincias()
    seed_municipios()    