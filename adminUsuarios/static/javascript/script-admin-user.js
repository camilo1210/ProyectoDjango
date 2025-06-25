// Configuración del swiper
var swiper = new Swiper(".mySwiper", {
  effect: "coverflow",
  grabCursor: true,
  centeredSlides: true,
  slidesPerView: "auto",
  loop: true,
  coverflowEffect: {
    depth: 500,
    modifier: 1,
    slideShadows: true,
    rotate: 0,
    stretch: 0,
  },
});

const userContainer = document.querySelector(".swiper-wrapper");

// Función para renderizar las tarjetas de usuario
function renderUsers(users) {
  users.forEach((user) => {
    const userSlide = document.createElement("div");
    userSlide.className = "swiper-slide";

    userSlide.innerHTML = `
      <div class="icons">
        <i class="fa-solid fa-circle-arrow-left"></i>
        <img src="/static/imagenes/Designer.png" alt="">
        <i class="fa-solid fa-pencil"></i>
      </div>
      <div class="product-content">
        <div class="product-txt">
          <span>${user.name}</span>
          <h3>Usuario</h3>
          <p>Usuario registrado en el sistema.</p>
        </div>
        <div class="product-img">
          <img src="/static/imagenes/avatar.jpg" alt="">
        </div>
      </div>
      <a href="/html/add_materia.html" class="btn-1">INICIAR SESION</a>
    `;

    userContainer.appendChild(userSlide);
  });
}
// Seleccionamos el modal y sus elementos
const modal = document.getElementById("userModal");
const closeModal = document.querySelector(".close");

// Evento para cerrar el modal
closeModal.onclick = () => {
  modal.style.display = "none";
};

// Cerrar modal al hacer clic fuera del contenido
window.onclick = (event) => {
  if (event.target === modal) {
    modal.style.display = "none";
  }
};

// Evento para abrir el modal cuando se hace clic en el ícono del lápiz
document.addEventListener("click", (event) => {
  if (event.target.classList.contains("fa-pencil")) {
    console.log("Se hizo clic en el lápiz"); // ← Agrega esto
    modal.style.display = "block";
  }
});
let selectedUsername = null;

// Mostrar el modal al hacer clic en el ícono del lápiz
document.addEventListener("click", (e) => {
  if (e.target.classList.contains("fa-pencil")) {
    const username = e.target
      .closest(".swiper-slide")
      .querySelector("span").innerText;
    selectedUsername = username;
    document.getElementById("userModal").style.display = "flex";
  }
});

// Eliminar usuario al hacer clic en "Eliminar"
document.getElementById("deleteUserBtn").addEventListener("click", () => {
  if (!selectedUsername) return;

  fetch("http://127.0.0.1:8000/api/delete-user/", {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ username: selectedUsername }),
  })
    .then((res) => res.json())
    .then((data) => {
      alert(data.message || data.error);
      // Cierra el modal y recarga la página
      document.getElementById("userModal").style.display = "none";
      location.reload();
    })
    .catch((err) => {
      console.error("Error eliminando el usuario:", err);
      alert("Hubo un error al eliminar el usuario.");
    });
});
const editModal = document.getElementById("editModal");
const newUsernameInput = document.getElementById("newUsername");
const newFirstNameSelect = document.getElementById("newFirstName");
const confirmEditBtn = document.getElementById("confirmEdit");
const cancelEditBtn = document.getElementById("cancelEdit");
document.getElementById("editUserBtn").addEventListener("click", () => {
  editModal.style.display = "flex";
  newUsernameInput.value = selectedUsername; // Rellenamos con el actual
});

cancelEditBtn.addEventListener("click", () => {
  editModal.style.display = "none";
});

confirmEditBtn.addEventListener("click", () => {
  const newUsername = newUsernameInput.value.trim();
  const newFirstName = newFirstNameSelect.value;

  if (!newUsername) {
    alert("El nombre de usuario no puede estar vacío.");
    return;
  }

  fetch("http://127.0.0.1:8000/api/update-user/", {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      old_username: selectedUsername,
      new_username: newUsername,
      new_first_name: newFirstName,
    }),
  })
    .then((res) => res.json())
    .then((data) => {
      alert(data.message || data.error);
      editModal.style.display = "none";
      location.reload();
    })
    .catch((err) => {
      console.error("Error actualizando usuario:", err);
      alert("Hubo un error al actualizar el usuario.");
    });
});
// 🔗 Aquí es donde pedimos los datos al backend
fetch("/adminUsuarios/api/usernames/")
  .then((response) => response.json())
  .then((data) => {
    renderUsers(data); // 👈 Aquí se pasa el array con { name: ... }
  })
  .catch((error) => console.error("Error cargando los usuarios:", error));

// Llamar a la función para renderizar usuarios
