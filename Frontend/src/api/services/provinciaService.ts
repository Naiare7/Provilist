import apiClient from '../client'
import type { Provincia, ProvinciaPayload } from '../interfaces'

export async function obtenerProvincias(): Promise<Provincia[]> {
  const { data } = await apiClient.get<Provincia[]>('/provincias')
  return data
}

export async function obtenerProvincia(id: number): Promise<Provincia> {
  const { data } = await apiClient.get<Provincia>(`/provincias/${id}`)
  return data
}

export async function crearProvincia(payload: ProvinciaPayload): Promise<Provincia> {
  const { data } = await apiClient.post<Provincia>('/provincias', payload)
  return data
}

export async function actualizarProvincia(id: number, payload: Partial<ProvinciaPayload>): Promise<Provincia> {
  const { data } = await apiClient.put<Provincia>(`/provincias/${id}`, payload)
  return data
}

export async function eliminarProvincia(id: number): Promise<{ mensaje: string }> {
  const { data } = await apiClient.delete<{ mensaje: string }>(`/provincias/${id}`)
  return data
}
