document.addEventListener("DOMContentLoaded", () => {
  // Header
  const headerContainer = document.getElementById("header");
  const today = new Date();
  const options = { day: '2-digit', month: 'long', year: 'numeric' };
  const formattedDate = today.toLocaleDateString('es-ES', options);
  headerContainer.innerHTML = `
    <h1 style="text-align: center;">Pan y Arte</h1>
    <p style="text-align: center; font-weight: bold;">Fecha: ${formattedDate}</p>
    <hr>
  `;

  // Proveedores
  fetch('/reporte_provee/api/proveedores/')
    .then(response => response.json())
    .then(data => {
      console.log("Datos recibidos:", data);
      const container = document.getElementById('proveedores-container');

      data.forEach(proveedor => {
        const card = document.createElement('div');
        card.innerHTML = `
          <h2>Proveedor: ${proveedor.nombre}</h2>
          <p><strong>ID:</strong> ${proveedor.id}</p>
          <p><strong>Dirección:</strong> ${proveedor.direccion}</p>
          <p><strong>Teléfono:</strong> ${proveedor.telefono}</p>
          <hr>
        `;
        container.appendChild(card);
      });
    })
    .catch(error => {
      console.error('Error cargando proveedores:', error);
    });
});
