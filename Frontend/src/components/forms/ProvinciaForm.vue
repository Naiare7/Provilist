<script setup lang="ts">
import { ref, onMounted } from 'vue';
import type { ProvinciaPayload, Provincia } from '@/api/interfaces';

const props = defineProps<{
  initialData?: Provincia | null;
  loading?: boolean;
}>();

const emit = defineEmits(['submit', 'cancel']);

const formData = ref<ProvinciaPayload>({
  nombre: '',
  pais: 'España',
  codigo: '',
  tiene_municipio: false
});

onMounted(() => {
  if (props.initialData) {
    formData.value = {
      nombre: props.initialData.nombre,
      pais: props.initialData.pais,
      codigo: props.initialData.codigo,
      tiene_municipio: props.initialData.tiene_municipio
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
      <label for="nombre">Nombre de la Provincia</label>
      <input 
        id="nombre" 
        v-model="formData.nombre" 
        type="text" 
        placeholder="Ej. Álava" 
        required 
        :disabled="loading"
      />
    </div>

    <div class="form-group">
      <label for="codigo">Código (2 caracteres)</label>
      <input 
        id="codigo" 
        v-model="formData.codigo" 
        type="text" 
        maxlength="2" 
        placeholder="Ej. VI" 
        required 
        :disabled="loading"
        style="text-transform: uppercase;"
      />
    </div>

    <div class="form-group">
      <label for="pais">País</label>
      <input 
        id="pais" 
        v-model="formData.pais" 
        type="text" 
        required 
        :disabled="loading"
      />
    </div>

    <div class="form-group checkbox-group">
      <div class="checkbox-wrapper">
        <input 
          id="tiene_municipio" 
          v-model="formData.tiene_municipio" 
          type="checkbox" 
          :disabled="loading"
        />
        <label for="tiene_municipio">¿Tiene municipios registrados?</label>
      </div>
    </div>

    <div class="form-actions">
      <button type="button" class="btn btn-secondary" @click="emit('cancel')" :disabled="loading">
        Cancelar
      </button>
      <button type="submit" class="btn btn-primary" :disabled="loading">
        <span v-if="loading">Guardando...</span>
        <span v-else>{{ initialData ? 'Actualizar' : 'Crear' }} Provincia</span>
      </button>
    </div>
  </form>
</template>

<style scoped>
.form-container {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.form-group label {
  font-size: 14px;
  font-weight: 700;
  color: #475569;
}

input[type="text"], input[type="number"] {
  padding: 12px 16px;
  border-radius: 12px;
  border: 1px solid #E2E8F0;
  background-color: #F8FAFC;
  font-size: 16px;
  color: #0F172A;
  transition: all 0.2s;
  width: 100%;
}

input:focus {
  outline: none;
  border-color: #00ABC5;
  box-shadow: 0 0 0 4px rgba(0, 171, 197, 0.1);
}

.checkbox-group {
  padding: 8px 0;
}

.checkbox-wrapper {
  display: flex;
  align-items: center;
  gap: 12px;
}

input[type="checkbox"] {
  width: 20px;
  height: 20px;
  cursor: pointer;
  accent-color: #00ABC5;
}

.form-actions {
  display: flex;
  justify-content: flex-end;
  gap: 12px;
  margin-top: 20px;
}

.btn {
  padding: 12px 24px;
  border-radius: 12px;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.2s;
  border: none;
}

.btn-secondary {
  background-color: #F1F5F9;
  color: #475569;
}

.btn-primary {
  background-color: #00ABC5;
  color: white;
  box-shadow: 0 8px 20px rgba(0, 171, 197, 0.2);
}

.btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}
</style>
