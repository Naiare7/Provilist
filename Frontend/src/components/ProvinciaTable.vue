<script setup lang="ts">
const provincias = [
  { 
    nombre: 'Álava', 
    capital: 'Vitoria-Gasteiz', 
    poblacion: 333940, 
    img: 'https://images.unsplash.com/photo-1541818290-7d7210e3032d?ixlib=rb-1.2.1&auto=format&fit=crop&w=100&q=80' 
  },
  { 
    nombre: 'Vizcaya', 
    capital: 'Bilbao', 
    poblacion: 1159443, 
    img: 'https://images.unsplash.com/photo-1579730243422-eb16886e0996?ixlib=rb-1.2.1&auto=format&fit=crop&w=100&q=80' 
  },
  { 
    nombre: 'Guipúzcoa', 
    capital: 'San Sebastián', 
    poblacion: 727121, 
    img: 'https://images.unsplash.com/photo-1557683316-973673baf926?ixlib=rb-1.2.1&auto=format&fit=crop&w=100&q=80' 
  },
]

const formatNumber = (num: number) => {
  return num.toLocaleString('de-DE') // Formato con puntos para miles
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
          Explora la demografía de las siete provincias vascas.
        </p>
      </div>
      <div class="header-right">
        <button class="btn-add-teal">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
            <line x1="12" y1="5" x2="12" y2="19"></line>
            <line x1="5" y1="12" x2="19" y2="12"></line>
          </svg>
          Añadir Provincia
        </button>
      </div>
    </div>

    <!-- Table Section -->
    <div class="glass-panel table-wrapper">
      <table class="prov-table">
        <thead>
          <tr>
            <th style="width: 40%">NOMBRE</th>
            <th style="width: 20%">CAPITAL</th>
            <th style="width: 20%">POBLACIÓN</th>
            <th style="width: 20%; text-align: center;">ACCIONES</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="prov in provincias" :key="prov.nombre">
            <td class="col-name">
              <div class="name-wrapper">
                <img :src="prov.img" :alt="prov.nombre" class="avatar-img" />
                <span class="prov-name-text">{{ prov.nombre }}</span>
              </div>
            </td>
            <td class="col-capital text-secondary">{{ prov.capital }}</td>
            <td class="col-poblacion text-secondary">{{ formatNumber(prov.poblacion) }}</td>
            <td class="col-actions">
              <div class="action-buttons">
                <!-- Icono Editar (Pencil) -->
                <button class="icon-btn edit-btn" title="Editar">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M12 20h9"></path>
                    <path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"></path>
                  </svg>
                </button>
                <!-- Icono Eliminar (Trash) -->
                <button class="icon-btn delete-btn" title="Eliminar">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                    <polyline points="3 6 5 6 21 6"></polyline>
                    <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path>
                  </svg>
                </button>
                <!-- Icono Detalles (Chevron) -->
                <button class="icon-btn arrow-btn" title="Ver detalles">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                    <polyline points="9 18 15 12 9 6"></polyline>
                  </svg>
                </button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
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

.table-wrapper {
  overflow: hidden;
  padding: 0;
  border-radius: 20px;
  border: 1px solid rgba(226, 232, 240, 0.3);
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.03);
}

.prov-table {
  width: 100%;
  border-collapse: collapse;
}

.prov-table th {
  padding: 24px 32px;
  font-size: 11px;
  font-weight: 800;
  color: #475569;
  letter-spacing: 1px;
  text-align: left;
  border-bottom: 1px solid rgba(226, 232, 240, 0.5);
  background: rgba(255, 255, 255, 0.2);
}

.prov-table td {
  padding: 16px 32px;
  background-color: rgba(255, 255, 255, 0.7);
  border-bottom: 1px solid rgba(226, 232, 240, 0.4);
}

.prov-table tr:hover td {
  background-color: rgba(255, 255, 255, 0.9);
}

.name-wrapper {
  display: flex;
  align-items: center;
  gap: 16px;
}

.avatar-img {
  width: 42px;
  height: 42px;
  border-radius: 50%;
  object-fit: cover;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

.prov-name-text {
  font-weight: 800;
  color: #0F172A;
  font-size: 16px;
}

.text-secondary {
  color: #475569;
  font-size: 14px;
}

.action-buttons {
  display: flex;
  justify-content: center;
  gap: 12px;
}

.icon-btn {
  background: none;
  border: none;
  cursor: pointer;
  padding: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s ease;
  border-radius: 8px;
}

.edit-btn { color: #00ABC5; }
.delete-btn { color: #EF4444; }
.arrow-btn { color: #94A3B8; }

.icon-btn:hover {
  background-color: rgba(241, 245, 249, 0.8);
  transform: scale(1.1);
}

@media (max-width: 768px) {
  .hero-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 24px;
  }
}
</style>
