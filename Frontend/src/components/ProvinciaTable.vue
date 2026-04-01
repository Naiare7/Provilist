<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { obtenerProvincias, crearProvincia, actualizarProvincia, eliminarProvincia } from '@/api/services/provinciaService'
import type { Provincia, ProvinciaPayload } from '@/api/interfaces'
import BaseModal from './common/BaseModal.vue'
import DeleteConfirm from './common/DeleteConfirm.vue'
import ProvinciaForm from './forms/ProvinciaForm.vue'

const items = ref<Provincia[]>([])
const loading = ref(true)

// Modal states
const showModal = ref(false)
const showDeleteConfirm = ref(false)
const selectedItem = ref<Provincia | null>(null)
const actionLoading = ref(false)

const fetchData = async () => {
  try {
    loading.value = true
    items.value = await obtenerProvincias()
  } catch (error) {
    console.error('Error fetching provincias:', error)
  } finally {
    loading.value = false
  }
}

onMounted(fetchData)

const handleAdd = () => {
  selectedItem.value = null
  showModal.value = true
}

const handleEdit = (item: Provincia) => {
  selectedItem.value = item
  showModal.value = true
}

const confirmDelete = (item: Provincia) => {
  selectedItem.value = item
  showDeleteConfirm.value = true
}

const onSubmit = async (payload: ProvinciaPayload) => {
  try {
    actionLoading.value = true
    if (selectedItem.value) {
      await actualizarProvincia(selectedItem.value.id, payload)
    } else {
      await crearProvincia(payload)
    }
    showModal.value = false
    fetchData()
  } catch (error) {
    alert('Error al guardar la provincia')
  } finally {
    actionLoading.value = false
  }
}

const onDelete = async () => {
  if (!selectedItem.value) return
  try {
    actionLoading.value = true
    await eliminarProvincia(selectedItem.value.id)
    showDeleteConfirm.value = false
    fetchData()
  } catch (error) {
    alert('Error al eliminar la provincia')
  } finally {
    actionLoading.value = false
  }
}

defineExpose({ handleAdd })
</script>

<template>
  <div class="glass-panel table-wrapper">
    <div v-if="loading" class="loading-state">Cargando datos...</div>
    <div v-else>
      <table class="prov-table">
        <thead>
          <tr>
            <th style="width: 40%">NOMBRE</th>
            <th style="width: 20%">CÓDIGO</th>
            <th style="width: 20%">¿MUNICIPIO?</th>
            <th style="width: 20%; text-align: center;">ACCIONES</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="prov in items" :key="prov.id">
            <td class="col-name">
              <div class="name-wrapper">
                <span class="prov-name-text">{{ prov.nombre }}</span>
              </div>
            </td>
            <td class="col-capital text-secondary">{{ prov.codigo }}</td>
            <td class="col-poblacion text-secondary">
              <span :class="['status-chip', prov.tiene_municipio ? 'chip-success' : 'chip-info']">
                {{ prov.tiene_municipio ? 'Sí' : 'No' }}
              </span>
            </td>
            <td class="col-actions">
              <div class="action-buttons">
                <button class="icon-btn edit-btn" @click="handleEdit(prov)" title="Editar">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M12 20h9"></path>
                    <path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"></path>
                  </svg>
                </button>
                <button class="icon-btn delete-btn" @click="confirmDelete(prov)" title="Eliminar">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                    <polyline points="3 6 5 6 21 6"></polyline>
                    <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path>
                  </svg>
                </button>
              </div>
            </td>
          </tr>
          <tr v-if="items.length === 0">
            <td colspan="4" class="empty-state">No se encontraron provincias.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Modals -->
    <BaseModal 
      :show="showModal" 
      :title="selectedItem ? 'Editar Provincia' : 'Añadir Provincia'" 
      @close="showModal = false"
    >
      <ProvinciaForm 
        :initial-data="selectedItem" 
        :loading="actionLoading"
        @submit="onSubmit"
        @cancel="showModal = false"
      />
    </BaseModal>

    <DeleteConfirm 
      :show="showDeleteConfirm" 
      message="Al eliminar una provincia, se perderán las relaciones asociadas. ¿Deseas continuar?"
      :loading="actionLoading"
      @confirm="onDelete"
      @cancel="showDeleteConfirm = false"
    />
  </div>
</template>

<style scoped>
.table-wrapper { overflow: hidden; padding: 0; border-radius: 20px; border: 1px solid rgba(226, 232, 240, 0.3); box-shadow: 0 10px 40px rgba(0, 0, 0, 0.03); width: 100%; transition: all 0.3s ease; }
.prov-table { width: 100%; border-collapse: collapse; }
.prov-table th { padding: 24px 32px; font-size: 11px; font-weight: 800; color: #475569; letter-spacing: 1px; text-align: left; border-bottom: 1px solid rgba(226, 232, 240, 0.5); background: rgba(255, 255, 255, 0.2); }
.prov-table td { padding: 16px 32px; background-color: rgba(255, 255, 255, 0.7); border-bottom: 1px solid rgba(226, 232, 240, 0.4); }
.prov-table tr:hover td { background-color: rgba(255, 255, 255, 0.9); }
.name-wrapper { display: flex; align-items: center; gap: 16px; }
.prov-name-text { font-weight: 800; color: #0F172A; font-size: 16px; }
.text-secondary { color: #475569; font-size: 14px; }
.status-chip { font-size: 12px; font-weight: 700; padding: 4px 12px; border-radius: 8px; }
.chip-success { background-color: rgba(16, 185, 129, 0.1); color: #10B981; }
.chip-info { background-color: rgba(59, 130, 246, 0.1); color: #3B82F6; }
.action-buttons { display: flex; justify-content: center; gap: 12px; }
.icon-btn { background: none; border: none; cursor: pointer; padding: 8px; display: flex; align-items: center; justify-content: center; transition: all 0.2s ease; border-radius: 8px; }
.edit-btn { color: #00ABC5; }
.delete-btn { color: #EF4444; }
.icon-btn:hover { background-color: rgba(241, 245, 249, 0.8); transform: scale(1.1); }
.loading-state, .empty-state { padding: 60px; text-align: center; color: #64748B; font-style: italic; }
</style>
