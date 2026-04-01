<script setup lang="ts">
import { ref, onMounted } from 'vue';
import type { MunicipioPayload, Municipio } from '@/api/interfaces';

const props = defineProps<{
  initialData?: Municipio | null;
  loading?: boolean;
}>();

const emit = defineEmits(['submit', 'cancel']);

const formData = ref<MunicipioPayload>({
  nombre: '',
  provincia_id: 1, // Por defecto Álava (ID 1)
  codigo_postal: 1000,
  poblacion: 0,
  area_km2: null,
  latitud: null,
  longitud: null
});

onMounted(() => {
  if (props.initialData) {
    formData.value = {
      nombre: props.initialData.nombre,
      provincia_id: props.initialData.provincia_id,
      codigo_postal: props.initialData.codigo_postal,
      poblacion: props.initialData.poblacion,
      area_km2: props.initialData.area_km2,
      latitud: props.initialData.latitud,
      longitud: props.initialData.longitud
    };
  }
});

const handleSubmit = () => {
  emit('submit', { ...formData.value });
};
</script>

<template>
  <form @submit.prevent="handleSubmit" class="form-container">
    <div class="form-group">
      <label for="nombre">Nombre del Municipio</label>
      <input 
        id="nombre" 
        v-model="formData.nombre" 
        type="text" 
        placeholder="Ej. Barakaldo" 
        required 
        :disabled="loading"
      />
    </div>

    <div class="form-row">
      <div class="form-group flex-1">
        <label for="provincia_id">ID de Provincia</label>
        <input 
          id="provincia_id" 
          v-model.number="formData.provincia_id" 
          type="number" 
          required 
          :disabled="loading"
        />
      </div>
      <div class="form-group flex-1">
        <label for="codigo_postal">Código Postal</label>
        <input 
          id="codigo_postal" 
          v-model.number="formData.codigo_postal" 
          type="number" 
          required 
          :disabled="loading"
        />
      </div>
    </div>

    <div class="form-row">
      <div class="form-group flex-1">
        <label for="poblacion">Población</label>
        <input 
          id="poblacion" 
          v-model.number="formData.poblacion" 
          type="number" 
          required 
          :disabled="loading"
          min="0"
        />
      </div>
      <div class="form-group flex-1">
        <label for="area_km2">Área (km²)</label>
        <input 
          id="area_km2" 
          v-model.number="formData.area_km2" 
          type="number" 
          step="0.01" 
          :disabled="loading"
          min="0"
        />
      </div>
    </div>

    <div class="form-row">
      <div class="form-group flex-1">
        <label for="latitud">Latitud</label>
        <input 
          id="latitud" 
          v-model.number="formData.latitud" 
          type="number" 
          step="0.000001" 
          :disabled="loading"
        />
      </div>
      <div class="form-group flex-1">
        <label for="longitud">Longitud</label>
        <input 
          id="longitud" 
          v-model.number="formData.longitud" 
          type="number" 
          step="0.000001" 
          :disabled="loading"
        />
      </div>
    </div>

    <div class="form-actions">
      <button type="button" class="btn btn-secondary" @click="emit('cancel')" :disabled="loading">
        Cancelar
      </button>
      <button type="submit" class="btn btn-primary" :disabled="loading">
        <span v-if="loading">Guardando...</span>
        <span v-else>{{ initialData ? 'Actualizar' : 'Crear' }} Municipio</span>
      </button>
    </div>
  </form>
</template>

<style scoped>
.form-container { display: flex; flex-direction: column; gap: 16px; }
.form-group { display: flex; flex-direction: column; gap: 6px; }
.form-row { display: flex; gap: 12px; }
.flex-1 { flex: 1; }
.form-group label { font-size: 13px; font-weight: 700; color: #475569; }
input { padding: 10px 14px; border-radius: 10px; border: 1px solid #E2E8F0; background-color: #F8FAFC; width: 100%; transition: all 0.2s; font-size: 14px; }
input:focus { outline: none; border-color: #00ABC5; box-shadow: 0 0 0 4px rgba(0, 171, 197, 0.1); }
.form-actions { display: flex; justify-content: flex-end; gap: 12px; margin-top: 16px; }
.btn { padding: 10px 20px; border-radius: 10px; font-weight: 700; cursor: pointer; transition: all 0.2s; border: none; font-size: 14px; }
.btn-secondary { background-color: #F1F5F9; color: #475569; }
.btn-primary { background-color: #00ABC5; color: white; box-shadow: 0 6px 14px rgba(0, 171, 197, 0.15); }
.btn:disabled { opacity: 0.6; cursor: not-allowed; }
</style>
