<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { obtenerCapitales, crearCapital, actualizarCapital, eliminarCapital } from '@/api/services/capitalService'
import type { Capital, CapitalPayload } from '@/api/interfaces'
import BaseModal from './common/BaseModal.vue'
import DeleteConfirm from './common/DeleteConfirm.vue'
import CapitalForm from './forms/CapitalForm.vue'

const items = ref<Capital[]>([])
const loading = ref(true)

// Modal states
const showModal = ref(false)
const showDeleteConfirm = ref(false)
const selectedItem = ref<Capital | null>(null)
const actionLoading = ref(false)

const fetchData = async () => {
  try {
    loading.value = true
    items.value = await obtenerCapitales()
  } catch (error) {
    console.error('Error fetching capitales:', error)
  } finally {
    loading.value = false
  }
}

onMounted(fetchData)

const handleAdd = () => {
  selectedItem.value = null
  showModal.value = true
}

const handleEdit = (item: Capital) => {
  selectedItem.value = item
  showModal.value = true
}

const confirmDelete = (item: Capital) => {
  selectedItem.value = item
  showDeleteConfirm.value = true
}

const onSubmit = async (payload: CapitalPayload) => {
  try {
    actionLoading.value = true
    if (selectedItem.value) {
      await actualizarCapital(selectedItem.value.id, payload)
    } else {
      await crearCapital(payload)
    }
    showModal.value = false
    fetchData()
  } catch (error) {
    alert('Error al guardar la capital')
  } finally {
    actionLoading.value = false
  }
}

const onDelete = async () => {
  if (!selectedItem.value) return
  try {
    actionLoading.value = true
    await eliminarCapital(selectedItem.value.id)
    showDeleteConfirm.value = false
    fetchData()
  } catch (error) {
    alert('Error al eliminar la capital')
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
            <th style="width: 40%">CAPITAL</th>
            <th style="width: 20%">PROVINCIA</th>
            <th style="width: 20%">LAT/LON</th>
            <th style="width: 20%; text-align: center;">ACCIONES</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="cap in items" :key="cap.id">
            <td class="col-name">
              <div class="name-wrapper">
                <span class="prov-name-text">{{ cap.nombre }}</span>
              </div>
            </td>
            <td class="col-prov">
              <span class="prov-badge">{{ cap.nombre_provincia || cap.codigo_provincia }}</span>
            </td>
            <td class="col-coords text-secondary">
               {{ cap.latitud?.toFixed(4) || '--' }}, {{ cap.longitud?.toFixed(4) || '--' }}
            </td>
            <td class="col-actions">
              <div class="action-buttons">
                <button class="icon-btn edit-btn" @click="handleEdit(cap)" title="Editar">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M12 20h9"></path>
                    <path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"></path>
                  </svg>
                </button>
                <button class="icon-btn delete-btn" @click="confirmDelete(cap)" title="Eliminar">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                    <polyline points="3 6 5 6 21 6"></polyline>
                    <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path>
                  </svg>
                </button>
              </div>
            </td>
          </tr>
          <tr v-if="items.length === 0">
            <td colspan="4" class="empty-state">No se encontraron capitales.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Modals -->
    <BaseModal 
      :show="showModal" 
      :title="selectedItem ? 'Editar Capital' : 'Añadir Capital'" 
      @close="showModal = false"
    >
      <CapitalForm 
        :initial-data="selectedItem" 
        :loading="actionLoading"
        @submit="onSubmit"
        @cancel="showModal = false"
      />
    </BaseModal>

    <DeleteConfirm 
      :show="showDeleteConfirm" 
      message="¿Seguro que quieres eliminar esta capital? Esta acción es irreversible."
      :loading="actionLoading"
      @confirm="onDelete"
      @cancel="showDeleteConfirm = false"
    />
  </div>
</template>

<style scoped>
.table-wrapper { overflow: hidden; border-radius: 20px; border: 1px solid rgba(226, 232, 240, 0.3); box-shadow: 0 10px 40px rgba(0, 0, 0, 0.03); width: 100%; transition: all 0.3s ease; }
.prov-table { width: 100%; border-collapse: collapse; }
.prov-table th { padding: 24px 32px; font-size: 11px; font-weight: 800; color: #94A3B8; letter-spacing: 1px; text-align: left; border-bottom: 1px solid rgba(226, 232, 240, 0.5); background: rgba(255, 255, 255, 0.2); }
.prov-table td { padding: 16px 32px; background-color: rgba(255, 255, 255, 0.7); border-bottom: 1px solid rgba(226, 232, 240, 0.4); }
.name-wrapper { display: flex; align-items: center; gap: 16px; }
.prov-name-text { font-weight: 800; color: #0F172A; font-size: 16px; }
.prov-badge { background-color: #E2F8FA; color: #008196; font-size: 12px; font-weight: 700; padding: 6px 16px; border-radius: 10px; }
.text-secondary { color: #475569; font-size: 14px; }
.action-buttons { display: flex; justify-content: center; gap: 16px; }
.icon-btn { background: none; border: none; cursor: pointer; padding: 8px; display: flex; align-items: center; justify-content: center; transition: all 0.2s ease; }
.edit-btn { color: #008196; }
.delete-btn { color: #CD1E1E; }
.icon-btn:hover { transform: scale(1.1); }
.loading-state, .empty-state { padding: 60px; text-align: center; color: #64748B; font-style: italic; }
</style>
