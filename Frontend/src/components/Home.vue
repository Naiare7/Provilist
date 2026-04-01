<script setup lang="ts">
const emit = defineEmits<{
  (e: 'navigate', view: string): void
}>()
</script>

<template>
  <div class="home-wrapper">
    <!-- Hero Section -->
    <div class="hero-section">
      <h1 class="hero-title">
        <span class="title-dark">ProviList:</span>
        <span class="title-teal">Datos del País Vasco</span>
      </h1>
      <p class="hero-subtitle">
        Gestiona la información de Euskal Herria de forma sencilla a través de nuestra interfaz cristalina.
      </p>
    </div>

    <div class="home-container">
      <div class="cards-grid">
        <!-- Provincias Card -->
        <div class="glass-panel card" @click="emit('navigate', 'provincias')">
          <div class="card-header">
            <div class="icon-circle icon-teal">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M3 6l6 3 6-3 6 3v12l-6-3-6 3-6-3V6z"></path>
                <path d="M9 9v12"></path>
                <path d="M15 3v12"></path>
              </svg>
            </div>
          </div>
          <div class="card-content">
            <h3 class="card-title">Provincias</h3>
            <p class="card-desc">
              Accede al listado completo de territorios históricos de la comunidad.
            </p>
          </div>
          <span class="card-link">Explorar Territorios →</span>
        </div>

        <!-- Capitales Card -->
        <div class="glass-panel card" @click="emit('navigate', 'capitales')">
          <div class="card-header">
            <div class="icon-circle icon-purple">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M3 21h18"></path>
                <path d="M3 7v1a3 3 0 0 0 6 0V7m0 1a3 3 0 0 0 6 0V7m0 1a3 3 0 0 0 6 0V7H3z"></path>
                <path d="M13 21v-7a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v7"></path>
                <path d="M9 21v-4a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v4"></path>
                <path d="M17 21v-10a1 1 0 0 0-1-1h-2a1 1 0 0 0-1 1v10"></path>
              </svg>
            </div>
          </div>
          <div class="card-content">
            <h3 class="card-title">Capitales</h3>
            <p class="card-desc">
              Vitoria-Gasteiz, Bilbao y San Sebastián. Datos clave de los núcleos urbanos.
            </p>
          </div>
          <span class="card-link">Ver Capitales →</span>
        </div>

        <!-- Municipios Card -->
        <div class="glass-panel card" @click="emit('navigate', 'municipios')">
          <div class="card-header">
            <div class="icon-circle icon-blue">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                <circle cx="9" cy="7" r="4"></circle>
                <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
                <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
              </svg>
            </div>
          </div>
          <div class="card-content">
            <h3 class="card-title">Municipios</h3>
            <p class="card-desc">
              Explora los más de 250 municipios que conforman el tejido de Euskadi.
            </p>
          </div>
          <span class="card-link">Listar Municipios →</span>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.home-wrapper {
  width: 100%;
  max-width: 1200px;
  padding: 80px 20px;
}

.hero-section {
  text-align: left;
  margin-bottom: 60px;
}

.hero-title {
  font-size: 52px;
  font-weight: 900;
  margin-bottom: 24px;
  letter-spacing: -1.5px;
  line-height: 1.1;
}

.title-dark {
  color: #0F172A; /* Slate 900 */
}

.title-teal {
  color: #0D9488; /* Teal 600 */
  margin-left: 12px;
}

.hero-subtitle {
  font-size: 20px;
  color: #64748B; /* Slate 500 */
  max-width: 600px;
  line-height: 1.5;
  font-weight: 400;
}

.home-container {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
}

.cards-grid {
  display: grid;
  grid-template-columns: repeat(1, 1fr);
  gap: 24px;
  width: 100%;
}

@media (min-width: 768px) {
  .cards-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}

.card {
  padding: 32px;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  display: flex;
  flex-direction: column;
  gap: 20px;
  height: 100%;
  border: 1px solid rgba(255, 255, 255, 0.3);
}

.card:hover {
  transform: translateY(-8px);
  border-color: rgba(13, 148, 136, 0.4);
  box-shadow: 0 20px 40px rgba(15, 23, 42, 0.08);
}

.card-header {
  margin-bottom: 4px;
}

.icon-circle {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.icon-teal { 
  background-color: rgba(20, 184, 166, 0.1); 
  color: #0D9488;
}

.icon-purple { 
  background-color: rgba(168, 85, 247, 0.1); 
  color: #9333EA;
}

.icon-blue { 
  background-color: rgba(59, 130, 246, 0.1); 
  color: #2563EB;
}

.card-title {
  font-size: 24px;
  font-weight: 700;
  color: #0F172A;
  margin-bottom: 12px;
}

.card-desc {
  font-size: 15px;
  color: #64748B;
  line-height: 1.6;
  font-weight: 400;
}

.card-link {
  color: #0D9488;
  font-weight: 600;
  font-size: 15px;
  display: flex;
  align-items: center;
  transition: color 0.2s ease;
  margin-top: auto;
}

.card:hover .card-link {
  color: #0F766E;
  text-decoration: underline;
}
</style>
