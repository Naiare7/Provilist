export interface Capital {
  id: number
  nombre: string
  codigo_provincia: string
  latitud: number | null
  longitud: number | null
  nombre_provincia?: string  // Campo extra que añade to_dict()
}

export interface CapitalPayload {
  nombre: string
  codigo_provincia: string
  latitud: number | null
  longitud: number | null
}
