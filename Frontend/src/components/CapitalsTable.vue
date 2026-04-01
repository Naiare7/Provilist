<script setup lang="ts">
const capitales = [
  { 
    nombre: 'Vitoria-Gasteiz', 
    provincia: 'Álava', 
    poblacion: 253093, 
    img: 'https://images.unsplash.com/photo-1541818290-7d7210e3032d?ixlib=rb-1.2.1&auto=format&fit=crop&w=100&q=80' 
  },
  { 
    nombre: 'Bilbao', 
    provincia: 'Bizkaia', 
    poblacion: 346096, 
    img: 'https://images.unsplash.com/photo-1579730243422-eb16886e0996?ixlib=rb-1.2.1&auto=format&fit=crop&w=100&q=80' 
  },
  { 
    nombre: 'Donostia-San Sebastián', 
    provincia: 'Gipuzkoa', 
    poblacion: 188102, 
    img: 'https://images.unsplash.com/photo-1557683316-973673baf926?ixlib=rb-1.2.1&auto=format&fit=crop&w=100&q=80' 
  },
]

const formatNumber = (num: number) => {
  return num.toLocaleString('de-DE') 
}
</script>

<template>
  <div class="view-container">
    <!-- Hero Header Section -->
    <div class="hero-header">
      <div class="header-left">
        <span class="region-chip">REGIÓN: NORTE</span>
        <h2 class="title-main">Capitales del País Vasco</h2>
        <p class="subtitle-main">
          Explora y gestiona las sedes administrativas de las provincias de Euskadi dentro del ecosistema ProviList.
        </p>
      </div>
      <div class="header-right">
        <button class="btn-add-teal">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
            <line x1="12" y1="5" x2="12" y2="19"></line>
            <line x1="5" y1="12" x2="19" y2="12"></line>
          </svg>
          Añadir Capital
        </button>
      </div>
    </div>

    <!-- Table Section -->
    <div class="glass-panel table-wrapper">
      <table class="prov-table">
        <thead>
          <tr>
            <th style="width: 40%">CAPITAL</th>
            <th style="width: 20%">PROVINCIA</th>
            <th style="width: 20%">POBLACIÓN</th>
            <th style="width: 20%; text-align: center;">ACCIONES</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="cap in capitales" :key="cap.nombre">
            <td class="col-name">
              <div class="name-wrapper">
                <img :src="cap.img" :alt="cap.nombre" class="avatar-img" />
                <span class="prov-name-text">{{ cap.nombre }}</span>
              </div>
            </td>
            <td class="col-prov">
              <span class="prov-badge">{{ cap.provincia }}</span>
            </td>
            <td class="col-poblacion text-secondary">{{ formatNumber(cap.poblacion) }}</td>
            <td class="col-actions">
              <div class="action-buttons">
                <!-- Icono Editar (Pencil) con estilo verde -->
                <button class="icon-btn edit-btn" title="Editar">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M12 20h9"></path>
                    <path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"></path>
                  </svg>
                </button>
                <!-- Icono Eliminar (Trash) con estilo rojo -->
                <button class="icon-btn delete-btn" title="Eliminar">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                    <polyline points="3 6 5 6 21 6"></polyline>
                    <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path>
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
  color: #008196;
  letter-spacing: 0.8px;
  margin-bottom: 8px;
  display: block;
}

.title-main {
  font-size: 40px;
  font-weight: 900;
  color: #242D33;
  margin-bottom: 12px;
  letter-spacing: -1px;
}

.subtitle-main {
  font-size: 16px;
  color: #64748B;
  max-width: 550px;
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
}

.table-wrapper {
  overflow: hidden;
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
  color: #94A3B8;
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

.prov-badge {
  background-color: #E2F8FA;
  color: #008196;
  font-size: 12px;
  font-weight: 700;
  padding: 6px 16px;
  border-radius: 10px;
}

.text-secondary {
  color: #475569;
  font-size: 14px;
}

.action-buttons {
  display: flex;
  justify-content: center;
  gap: 16px;
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
}

.edit-btn { color: #008196; }
.delete-btn { color: #CD1E1E; } /* Red for deletion */

.icon-btn:hover {
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
