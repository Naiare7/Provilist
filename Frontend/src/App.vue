<script setup lang="ts">
import { ref, computed } from 'vue'
import Home from './components/Home.vue'
import ProvinciaTable from './components/ProvinciaTable.vue'
import CapitalTable from './components/CapitalTable.vue'
import MunicipioTable from './components/MunicipioTable.vue'

type View = 'home' | 'provincias' | 'capitales' | 'municipios'
const currentView = ref<View>('home')

const handleNavigate = (view: string) => {
  currentView.value = view as View
}

const currentComponent = computed(() => {
  switch(currentView.value) {
    case 'home': return Home
    case 'provincias': return ProvinciaTable
    case 'capitales': return CapitalTable
    case 'municipios': return MunicipioTable
    default: return Home
  }
})
</script>

<template>
  <h1>Provi List</h1>
  <p>
    La base de datos mas grande con la informacion exacta sobre Euskal Herria.!
  </p>
  <header class="app-header glass-panel glass-header">
    <div class="header-content">
      <div class="brand">
        <h1 class="brand-title" @click="handleNavigate('home')" style="cursor: pointer;">PROVILIST</h1>
        <p class="brand-tagline">Datos del País Vasco</p>
      </div>
      
      <nav v-if="currentView !== 'home'" class="top-nav">
        <button class="nav-btn" @click="handleNavigate('home')">← Volver al Inicio</button>
      </nav>
    </div>
  </header>

  <main class="app-main">
    <transition name="fade" mode="out-in">
      <component :is="currentComponent" @navigate="handleNavigate"></component>
    </transition>
  </main>
</template>

<style scoped>
.app-header {
  position: sticky;
  top: 0;
  z-index: 100;
  border-radius: 0;
  border-top: none;
  border-left: none;
  border-right: none;
}

.header-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 16px 24px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.brand {
  display: flex;
  flex-direction: column;
}

.nav-btn {
  background: transparent;
  border: 1px solid var(--border-color);
  color: var(--text-main);
  padding: 8px 16px;
  border-radius: var(--border-radius-sm);
  cursor: pointer;
  font-weight: 500;
  font-size: 14px;
  transition: all 0.2s;
}

.nav-btn:hover {
  background: rgba(255, 255, 255, 0.5);
  border-color: var(--primary);
  color: var(--primary);
}

.app-main {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
}

/* Page Transitions */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease, transform 0.3s ease;
}

.fade-enter-from {
  opacity: 0;
  transform: translateY(10px);
}
.fade-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}
</style>
