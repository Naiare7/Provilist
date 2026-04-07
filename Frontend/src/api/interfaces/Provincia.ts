export interface Provincia {
  id: number
  nombre: string
  pais: string
  codigo: string
  tiene_municipio: boolean
}

/** Payload para crear/actualizar una provincia (sin id) */
export interface ProvinciaPayload {
  nombre: string
  pais: string
  codigo: string
  tiene_municipio: boolean
}
