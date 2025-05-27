document.addEventListener("DOMContentLoaded", () => {
  const headerContainer = document.getElementById("header");

  const today = new Date();
  const options = { day: '2-digit', month: 'long', year: 'numeric' };
  const formattedDate = today.toLocaleDateString('es-ES', options);

  const headerHTML = `
    <h1 style="text-align: center;">Pan y Arte</h1>
    <p style="text-align: center; font-weight: bold;">Fecha: ${formattedDate}</p>
    <hr>
  `;

  headerContainer.innerHTML = headerHTML;
});