<script setup lang="ts">
import { ref, onMounted } from 'vue';
import type { CapitalPayload, Capital } from '@/api/interfaces';

const props = defineProps<{
  initialData?: Capital | null;
  loading?: boolean;
}>();

const emit = defineEmits(['submit', 'cancel']);

const formData = ref<CapitalPayload>({
  nombre: '',
  codigo_provincia: '',
  latitud: null,
  longitud: null
});

onMounted(() => {
  if (props.initialData) {
    formData.value = {
      nombre: props.initialData.nombre,
      codigo_provincia: props.initialData.codigo_provincia,
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
      <label for="nombre">Nombre de la Capital</label>
      <input 
        id="nombre" 
        v-model="formData.nombre" 
        type="text" 
        placeholder="Ej. Bilbao" 
        required 
        :disabled="loading"
      />
    </div>

    <div class="form-group">
      <label for="codigo_provincia">Código de Provincia</label>
      <input 
        id="codigo_provincia" 
        v-model="formData.codigo_provincia" 
        type="text" 
        maxlength="2" 
        placeholder="Ej. BI" 
        required 
        :disabled="loading"
        style="text-transform: uppercase;"
      />
    </div>

    <div class="form-row">
      <div class="form-group flex-1">
        <label for="latitud">Latitud</label>
        <input 
          id="latitud" 
          v-model.number="formData.latitud" 
          type="number" 
          step="0.000001" 
          placeholder="0.000000" 
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
          placeholder="0.000000" 
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
        <span v-else>{{ initialData ? 'Actualizar' : 'Crear' }} Capital</span>
      </button>
    </div>
  </form>
</template>

<style scoped>
.form-container { display: flex; flex-direction: column; gap: 20px; }
.form-group { display: flex; flex-direction: column; gap: 8px; }
.form-row { display: flex; gap: 16px; }
.flex-1 { flex: 1; }
.form-group label { font-size: 14px; font-weight: 700; color: #475569; }
input { padding: 12px 16px; border-radius: 12px; border: 1px solid #E2E8F0; background-color: #F8FAFC; width: 100%; transition: all 0.2s; }
input:focus { outline: none; border-color: #00ABC5; box-shadow: 0 0 0 4px rgba(0, 171, 197, 0.1); }
.form-actions { display: flex; justify-content: flex-end; gap: 12px; margin-top: 20px; }
.btn { padding: 12px 24px; border-radius: 12px; font-weight: 700; cursor: pointer; transition: all 0.2s; border: none; }
.btn-secondary { background-color: #F1F5F9; color: #475569; }
.btn-primary { background-color: #00ABC5; color: white; box-shadow: 0 8px 20px rgba(0, 171, 197, 0.2); }
.btn:disabled { opacity: 0.6; cursor: not-allowed; }
</style>
