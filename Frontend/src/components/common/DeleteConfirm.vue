<script setup lang="ts">
defineProps<{
  show: boolean;
  message: string;
  loading?: boolean;
}>();

const emit = defineEmits(['confirm', 'cancel']);
</script>

<template>
  <Teleport to="body">
    <Transition name="modal">
      <div v-if="show" class="modal-mask" @click.self="emit('cancel')">
        <div class="modal-container glass-panel delete-alert">
          <div class="alert-icon">
            <svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path>
              <line x1="12" y1="9" x2="12" y2="13"></line>
              <line x1="12" y1="17" x2="12.01" y2="17"></line>
            </svg>
          </div>
          
          <h2 class="alert-title">¿Estás seguro?</h2>
          <p class="alert-message">{{ message }}</p>
          
          <div class="alert-actions">
            <button class="btn btn-cancel" @click="emit('cancel')" :disabled="loading">Cancelar</button>
            <button class="btn btn-delete" @click="emit('confirm')" :disabled="loading">
              <span v-if="loading">Eliminando...</span>
              <span v-else>Sí, Eliminar</span>
            </button>
          </div>
        </div>
      </div>
    </Transition>
  </Teleport>
</template>

<style scoped>
.modal-mask {
  position: fixed;
  z-index: 9999;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.4);
  display: flex;
  align-items: center;
  justify-content: center;
  backdrop-filter: blur(6px);
  transition: opacity 0.3s ease;
}

.modal-container {
  width: 90%;
  max-width: 400px;
  padding: 40px;
  text-align: center;
  background-color: rgba(255, 255, 255, 0.95);
  border-radius: 24px;
  box-shadow: 0 30px 60px rgba(220, 38, 38, 0.15);
  transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.alert-icon {
  color: #EF4444;
  margin-bottom: 24px;
  display: flex;
  justify-content: center;
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0% { transform: scale(1); }
  50% { transform: scale(1.1); }
  100% { transform: scale(1); }
}

.alert-title {
  font-size: 24px;
  font-weight: 800;
  color: #0F172A;
  margin-bottom: 12px;
}

.alert-message {
  font-size: 16px;
  color: #64748B;
  margin-bottom: 32px;
  line-height: 1.6;
}

.alert-actions {
  display: flex;
  gap: 16px;
}

.btn {
  flex: 1;
  padding: 14px;
  border-radius: 12px;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.2s;
  border: none;
}

.btn-cancel {
  background-color: #F1F5F9;
  color: #64748B;
}

.btn-cancel:hover {
  background-color: #E2E8F0;
}

.btn-delete {
  background-color: #EF4444;
  color: white;
  box-shadow: 0 8px 20px rgba(239, 68, 68, 0.2);
}

.btn-delete:hover:not(:disabled) {
  background-color: #DC2626;
  transform: translateY(-2px);
  box-shadow: 0 10px 24px rgba(239, 68, 68, 0.3);
}

.btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

/* Modal animation */
.modal-enter-from { opacity: 0; }
.modal-leave-to { opacity: 0; }
.modal-enter-from .modal-container { transform: scale(0.8); }
.modal-leave-to .modal-container { transform: scale(0.95); opacity: 0; }
</style>
