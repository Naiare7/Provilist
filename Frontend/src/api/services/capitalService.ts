import apiClient from '../client'
import type { Capital, CapitalPayload } from '../interfaces'

export async function obtenerCapitales(): Promise<Capital[]> {
  const { data } = await apiClient.get<Capital[]>('/capitales')
  return data
}

export async function obtenerCapital(id: number): Promise<Capital> {
  const { data } = await apiClient.get<Capital>(`/capitales/${id}`)
  return data
}

export async function crearCapital(payload: CapitalPayload): Promise<Capital> {
  const { data } = await apiClient.post<Capital>('/capitales', payload)
  return data
}

export async function actualizarCapital(id: number, payload: Partial<CapitalPayload>): Promise<Capital> {
  const { data } = await apiClient.put<Capital>(`/capitales/${id}`, payload)
  return data
}

export async function eliminarCapital(id: number): Promise<{ mensaje: string }> {
  const { data } = await apiClient.delete<{ mensaje: string }>(`/capitales/${id}`)
  return data
}
