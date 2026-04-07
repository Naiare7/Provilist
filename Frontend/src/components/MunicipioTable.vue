<script setup lang="ts">
import { ref, onMounted, watch } from 'vue'
import { obtenerMunicipios, crearMunicipio, actualizarMunicipio, eliminarMunicipio } from '@/api/services/municipioService'
import type { Municipio, MunicipioPayload } from '@/api/interfaces'
import BaseModal from './common/BaseModal.vue'
import DeleteConfirm from './common/DeleteConfirm.vue'
import MunicipioForm from './forms/MunicipioForm.vue'

const items = ref<Municipio[]>([])
const loading = ref(true)
const total = ref(0)
const pages = ref(0)
const currentPage = ref(1)
const perPage = ref(10)

// Modal states
const showModal = ref(false)
const showDeleteConfirm = ref(false)
const selectedItem = ref<Municipio | null>(null)
const actionLoading = ref(false)

const fetchData = async () => {
  try {
    loading.value = true
    const response = await obtenerMunicipios(currentPage.value, perPage.value)
    if ('items' in response) {
      items.value = response.items
      total.value = response.total
      pages.value = response.pages
    } else {
      items.value = response
      total.value = response.length
    }
  } catch (error) {
    console.error('Error fetching municipios:', error)
  } finally {
    loading.value = false
  }
}

onMounted(fetchData)
watch(currentPage, fetchData)

const handleAdd = () => {
  selectedItem.value = null
  showModal.value = true
}

const handleEdit = (item: Municipio) => {
  selectedItem.value = item
  showModal.value = true
}

const confirmDelete = (item: Municipio) => {
  selectedItem.value = item
  showDeleteConfirm.value = true
}

const onSubmit = async (payload: MunicipioPayload) => {
  try {
    actionLoading.value = true
    if (selectedItem.value) {
      await actualizarMunicipio(selectedItem.value.id, payload)
    } else {
      await crearMunicipio(payload)
    }
    showModal.value = false
    fetchData()
  } catch (error) {
    alert('Error al guardar el municipio')
  } finally {
    actionLoading.value = false
  }
}

const onDelete = async () => {
  if (!selectedItem.value) return
  try {
    actionLoading.value = true
    await eliminarMunicipio(selectedItem.value.id)
    showDeleteConfirm.value = false
    fetchData()
  } catch (error) {
    alert('Error al eliminar el municipio')
  } finally {
    actionLoading.value = false
  }
}

const formatNumber = (num: number | undefined) => {
  return num ? num.toLocaleString('de-DE') : '0'
}

// Expose add method for parent view
defineExpose({ handleAdd })
</script>

<template>
  <div class="glass-panel table-wrapper">
    <div v-if="loading" class="loading-state">Cargando datos...</div>
    <div v-else>
      <table class="prov-table">
        <thead>
          <tr>
            <th>MUNICIPIO</th>
            <th>PROVINCIA</th>
            <th class="text-center">C.P.</th>
            <th class="text-right">POBLACIÓN</th>
            <th class="text-right">ÁREA (km²)</th>
            <th class="text-center">COORDENADAS</th>
            <th class="text-center">ACCIONES</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="mun in items" :key="mun.id">
            <td class="col-name">
              <span class="prov-name-text">{{ mun.nombre }}</span>
            </td>
            <td class="col-capital text-secondary">{{ mun.nombre_provincia || mun.provincia_id }}</td>
            <td class="text-center text-secondary">{{ mun.codigo_postal }}</td>
            <td class="text-right text-secondary">{{ formatNumber(mun.poblacion) }}</td>
            <td class="text-right text-secondary">{{ mun.area_km2 || '--' }}</td>
            <td class="text-center">
              <span class="coords-badge">{{ mun.latitud?.toFixed(2) || '--' }}, {{ mun.longitud?.toFixed(2) || '--' }}</span>
            </td>
            <td class="col-actions">
              <div class="action-buttons">
                <button class="icon-btn edit-btn" @click="handleEdit(mun)" title="Editar">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M12 20h9"></path>
                    <path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"></path>
                  </svg>
                </button> 
                <button class="icon-btn delete-btn" @click="confirmDelete(mun)" title="Eliminar">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                    <polyline points="3 6 5 6 21 6"></polyline>
                    <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path>
                  </svg>
                </button>
              </div>
            </td>
          </tr>
          <tr v-if="items.length === 0">
            <td colspan="7" class="empty-state">No se encontraron municipios.</td>
          </tr>
        </tbody>
      </table>

      <!-- Pagination -->
      <div v-if="pages > 1" class="pagination">
        <button 
          class="page-btn" 
          :disabled="currentPage === 1" 
          @click="currentPage--"
        >
          &laquo; Anterior
        </button>
        <span class="page-info">Página {{ currentPage }} de {{ pages }}</span>
        <button 
          class="page-btn" 
          :disabled="currentPage === pages" 
          @click="currentPage++"
        >
          Siguiente &raquo;
        </button>
      </div>
    </div>

    <!-- Modals -->
    <BaseModal 
      :show="showModal" 
      :title="selectedItem ? 'Editar Municipio' : 'Añadir Municipio'" 
      @close="showModal = false"
    >
      <MunicipioForm 
        :initial-data="selectedItem" 
        :loading="actionLoading"
        @submit="onSubmit"
        @cancel="showModal = false"
      />
    </BaseModal>

    <DeleteConfirm 
      :show="showDeleteConfirm" 
      message="Esta acción no se puede deshacer. Se eliminará el municipio permanentemente."
      :loading="actionLoading"
      @confirm="onDelete"
      @cancel="showDeleteConfirm = false"
    />
  </div>
</template>

<style scoped>
.table-wrapper { overflow: hidden; border-radius: 20px; border: 1px solid rgba(226, 232, 240, 0.3); box-shadow: 0 10px 40px rgba(0, 0, 0, 0.03); width: 100%; transition: all 0.3s ease; }
.prov-table { width: 100%; border-collapse: collapse; }
.prov-table th { padding: 24px 20px; font-size: 11px; font-weight: 800; color: #475569; letter-spacing: 1px; text-align: left; border-bottom: 1px solid rgba(226, 232, 240, 0.5); background: rgba(255, 255, 255, 0.2); }
.prov-table td { padding: 16px 20px; background-color: rgba(255, 255, 255, 0.7); border-bottom: 1px solid rgba(226, 232, 240, 0.4); }
.prov-table tr:hover td { background-color: rgba(255, 255, 255, 0.9); }
.prov-name-text { font-weight: 800; color: #0F172A; font-size: 15px; }
.text-secondary { color: #475569; font-size: 14px; }
.coords-badge { background: rgba(148, 163, 184, 0.1); padding: 4px 8px; border-radius: 6px; font-size: 12px; color: #64748B; font-family: monospace; }
.action-buttons { display: flex; justify-content: center; gap: 8px; }
.icon-btn { background: none; border: none; cursor: pointer; padding: 8px; display: flex; align-items: center; justify-content: center; transition: all 0.2s ease; border-radius: 8px; }
.edit-btn { color: #00ABC5; }
.delete-btn { color: #CD1E1E; }
.icon-btn:hover { background-color: rgba(241, 245, 249, 0.8); transform: scale(1.1); }
.text-center { text-align: center; }
.text-right { text-align: right; }
.loading-state, .empty-state { padding: 60px; text-align: center; color: #64748B; font-style: italic; font-size: 16px; }

/* Pagination Styles */
.pagination { display: flex; justify-content: center; align-items: center; gap: 20px; padding: 24px; background: rgba(255, 255, 255, 0.3); border-top: 1px solid rgba(226, 232, 240, 0.5); }
.page-btn { padding: 8px 20px; border-radius: 12px; border: 1px solid #E2E8F0; background: white; color: #0F172A; font-weight: 700; cursor: pointer; transition: all 0.2s; font-size: 14px; }
.page-btn:hover:not(:disabled) { border-color: #00ABC5; color: #00ABC5; background: #E2F8FA; }
.page-btn:disabled { opacity: 0.4; cursor: not-allowed; }
.page-info { font-size: 14px; color: #64748B; font-weight: 600; }
</style>
