from .seeds_provincias import seed_provincias
from .seeds_municipios import seed_municipios
from .seeds_capitales import seed_capitales

    
def run_seeds():
    seed_provincias()
    seed_municipios()    
    seed_capitales()