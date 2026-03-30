from .seeds_provincias import seeds_provincias
from .seeds_municipios import seeds_municipios


def run_seeds():
    seeds_provincias()
    seeds_municipios()    