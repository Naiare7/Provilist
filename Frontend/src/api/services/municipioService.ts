import apiClient from '../client'
import type { Municipio, MunicipioPayload } from '../interfaces'

// Tipo para la respuesta paginada
export interface PaginatedResponse<T> {
  items: T[]
  total: number
  pages: number
  current_page: number
}

export async function obtenerMunicipios(page?: number, perPage?: number): Promise<PaginatedResponse<Municipio> | Municipio[]> {
  const params = page && perPage ? { page, per_page: perPage } : {}
  const { data } = await apiClient.get<PaginatedResponse<Municipio> | Municipio[]>('/municipios', { params })
  return data
}

export async function obtenerMunicipio(id: number): Promise<Municipio> {
  const { data } = await apiClient.get<Municipio>(`/municipios/${id}`)
  return data
}

export async function crearMunicipio(payload: MunicipioPayload): Promise<Municipio> {
  const { data } = await apiClient.post<Municipio>('/municipios', payload)
  return data
}

export async function actualizarMunicipio(id: number, payload: Partial<MunicipioPayload>): Promise<Municipio> {
  const { data } = await apiClient.put<Municipio>(`/municipios/${id}`, payload)
  return data
}

export async function eliminarMunicipio(id: number): Promise<{ mensaje: string }> {
  const { data } = await apiClient.delete<{ mensaje: string }>(`/municipios/${id}`)
  return data
}
