export interface Municipio {
  id: number
  nombre: string
  provincia_id: number
  codigo_postal: number
  poblacion: number
  area_km2: number | null
  latitud: number | null
  longitud: number | null
  created_at: string
  updated_at: string
  nombre_provincia?: string  // Campo extra que añade to_dict()
}

export interface MunicipioPayload {
  nombre: string
  provincia_id: number
  codigo_postal: number
  poblacion: number
  area_km2: number | null
  latitud: number | null
  longitud: number | null
}
