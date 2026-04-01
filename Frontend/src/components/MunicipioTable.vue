<script setup lang="ts">
const municipios = [
  { nombre: 'Barakaldo', provincia: 'Bizkaia', cp: '48901', poblacion: 100535, area: 14.5, lat: 43.2976, lon: -2.9904 },
  { nombre: 'Irún', provincia: 'Gipuzkoa', cp: '20300', poblacion: 62635, area: 42.4, lat: 43.3391, lon: -1.7892 },
  { nombre: 'Galdakao', provincia: 'Bizkaia', cp: '48960', poblacion: 29334, area: 31.7, lat: 43.2307, lon: -2.8453 },
  { nombre: 'Vitoria-Gasteiz', provincia: 'Araba', cp: '01001', poblacion: 253093, area: 276.8, lat: 42.8467, lon: -2.6716 },
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
        <span class="region-chip">EUSKADI / DIRECTORIO</span>
        <h2 class="title-main">Municipios de <span class="title-accent">Euskal Herria</span></h2>
        <p class="subtitle-main">
          Listado detallado de los municipios con información demográfica, geográfica y códigos postales.
        </p>
      </div>
      <div class="header-right">
        <button class="btn-add-teal">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
            <line x1="12" y1="5" x2="12" y2="19"></line>
            <line x1="5" y1="12" x2="19" y2="12"></line>
          </svg>
          Añadir Municipio
        </button>
      </div>
    </div>

    <!-- Table Section -->
    <div class="glass-panel table-wrapper">
      <table class="prov-table">
        <thead>
          <tr>
            <th>MUNICIPIO</th>
            <th>PROVINCIA</th>
            <th class="text-center">C.P.</th>
            <th class="text-right">POBLACIÓN</th>
            <th class="text-right">ÁREA (km²)</th>
            <th class="text-center">COORDENADAS</th>
            <th class="text-center">ACCIONES</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="mun in municipios" :key="mun.nombre">
            <td class="col-name">
              <span class="prov-name-text">{{ mun.nombre }}</span>
            </td>
            <td class="col-capital text-secondary">{{ mun.provincia }}</td>
            <td class="text-center text-secondary">{{ mun.cp }}</td>
            <td class="text-right text-secondary">{{ formatNumber(mun.poblacion) }}</td>
            <td class="text-right text-secondary">{{ mun.area }}</td>
            <td class="text-center">
              <span class="coords-badge">{{ mun.lat }}, {{ mun.lon }}</span>
            </td>
            <td class="col-actions">
              <div class="action-buttons">
                <!-- Ver detalles (Eye) -->
                 <!-- Icono Eliminar (Trash) con estilo rojo -->
               <button class="icon-btn edit-btn" title="Editar">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M12 20h9"></path>
                    <path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"></path>
                  </svg>
                </button> 
                <!-- Editar (Pencil) -->
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
  max-width: 1200px;
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
  font-size: 40px;
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
}

.table-wrapper {
  overflow-x: auto;
  border-radius: 20px;
  border: 1px solid rgba(226, 232, 240, 0.3);
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.03);
}

.prov-table {
  width: 100%;
  border-collapse: collapse;
}

.prov-table th {
  padding: 24px 20px;
  font-size: 11px;
  font-weight: 800;
  color: #475569;
  letter-spacing: 1px;
  text-align: left;
  border-bottom: 1px solid rgba(226, 232, 240, 0.5);
  background: rgba(255, 255, 255, 0.2);
}

.prov-table td {
  padding: 16px 20px;
  background-color: rgba(255, 255, 255, 0.7);
  border-bottom: 1px solid rgba(226, 232, 240, 0.4);
}

.prov-table tr:hover td {
  background-color: rgba(255, 255, 255, 0.9);
}

.prov-name-text {
  font-weight: 800;
  color: #0F172A;
  font-size: 15px;
}

.text-secondary {
  color: #475569;
  font-size: 14px;
}

.coords-badge {
  background: rgba(148, 163, 184, 0.1);
  padding: 4px 8px;
  border-radius: 6px;
  font-size: 12px;
  color: #64748B;
  font-family: monospace;
}

.action-buttons {
  display: flex;
  justify-content: center;
  gap: 8px;
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
.arrow-btn { color: #94A3B8; }
.delete-btn { color: #CD1E1E; } /* Red for deletion */

.icon-btn:hover {
  background-color: rgba(241, 245, 249, 0.8);
  transform: scale(1.1);
}

.text-center { text-align: center; }
.text-right { text-align: right; }

@media (max-width: 768px) {
  .hero-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 24px;
  }
}
</style>
