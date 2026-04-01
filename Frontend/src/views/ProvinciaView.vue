<script setup lang="ts">
import { ref } from 'vue'
import ProvinciaTable from '@/components/ProvinciaTable.vue'

const tableRef = ref<InstanceType<typeof ProvinciaTable> | null>(null)

const emit = defineEmits<{
  (e: 'navigate', view: string): void
}>()

const onAdd = () => {
  tableRef.value?.handleAdd()
}
</script>

<template>
  <div class="view-container">
    <!-- Hero Header Section -->
    <div class="hero-header">
      <div class="header-left">
        <span class="region-chip">REGIÓN NORTE</span>
        <h2 class="title-main">Provincias del <span class="title-accent">País Vasco</span></h2>
        <p class="subtitle-main">
          Gestiona los territorios históricos de Euskal Herria desde un panel centralizado.
        </p>
      </div>
      <div class="header-right">
        <button class="btn-add-teal" @click="onAdd">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
            <line x1="12" y1="5" x2="12" y2="19"></line>
            <line x1="5" y1="12" x2="19" y2="12"></line>
          </svg>
          Añadir Provincia
        </button>
      </div>
    </div>

    <!-- Table Section -->
    <ProvinciaTable ref="tableRef" />
  </div>
</template>

<style scoped>
.view-container {
  width: 100%;
  max-width: 1100px;
  margin: 0 auto;
  padding: 60px 20px;
}

.hero-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 48px;
}

.header-left {
  flex: 1;
}

.region-chip {
  font-size: 11px;
  font-weight: 700;
  color: #00ABC5;
  letter-spacing: 0.8px;
  margin-bottom: 8px;
  display: block;
}

.title-main {
  font-size: 44px;
  font-weight: 900;
  color: #0F172A;
  margin-bottom: 12px;
  letter-spacing: -1.2px;
}

.title-accent {
  color: #008196;
}

.subtitle-main {
  font-size: 16px;
  color: #64748B;
  max-width: 500px;
  line-height: 1.5;
  font-weight: 400;
}

.btn-add-teal {
  background-color: #00ABC5;
  color: white;
  border: none;
  padding: 14px 28px;
  border-radius: 16px;
  font-weight: 700;
  font-size: 14px;
  display: flex;
  align-items: center;
  gap: 12px;
  cursor: pointer;
  box-shadow: 0 10px 20px rgba(0, 171, 197, 0.2);
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
}

.btn-add-teal:hover {
  transform: translateY(-2px);
  background-color: #0096AD;
  box-shadow: 0 12px 24px rgba(0, 171, 197, 0.3);
}

@media (max-width: 768px) {
  .hero-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 24px;
  }
}
</style>
