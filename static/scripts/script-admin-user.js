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
    stretch: 0
  }
});

// Ejemplo de datos de usuarios
const users = [
    {
      name: "ANDRES",
      role: "ADMINISTRADOR",
      description: "Andrés es un administrador eficiente y organizado, encargado de supervisar operaciones y garantizar el cumplimiento de objetivos.",
      mainImage: "/imagenes/img/Designer.png",
      profileImage: "/imagenes/img/andres.jpg",
    },
    {
      name: "CARLA",
      role: "DISEÑADORA",
      description: "Carla es una diseñadora creativa, especializada en generar soluciones innovadoras y estéticas para los proyectos.",
      mainImage: "/imagenes/img/Designer.png",
      profileImage: "/imagenes/img/carla.jpg",
    },
    {
        name: "ANDRES",
        role: "ADMINISTRADOR",
        description: "Andrés es un administrador eficiente y organizado, encargado de supervisar operaciones y garantizar el cumplimiento de objetivos.",
        mainImage: "/imagenes/img/Designer.png",
        profileImage: "/imagenes/img/andres.jpg",
    },
  ];
  
  // Seleccionar el contenedor donde se mostrarán las tarjetas de usuario
  const userContainer = document.querySelector(".swiper-wrapper");
  
  // Función para renderizar las tarjetas de usuario
  function renderUsers(users) {
    users.forEach(user => {
      // Crear un elemento para cada usuario
      const userSlide = document.createElement("div");
      userSlide.className = "swiper-slide";
  
      // Insertar el contenido HTML en la tarjeta
      userSlide.innerHTML = `
        <div class="icons">
          <i class="fa-solid fa-circle-arrow-left"></i>
          <img src="${user.mainImage}" alt="">
          <i class="fa-solid fa-pencil"></i>
        </div>
        <div class="product-content">
          <div class="product-txt">
            <span>${user.name}</span>
            <h3>${user.role}</h3>
            <p>${user.description}</p>
          </div>
          <div class="product-img">
            <img src="${user.profileImage}" alt="${user.name}">
          </div>
        </div>
        <a href="/html/add_materia.html" class="btn-1">INICIAR SESION</a>
      `;
  
      // Agregar la tarjeta al contenedor principal
      userContainer.appendChild(userSlide);
    });
  }
  
  // Llamar a la función para renderizar usuarios
  renderUsers(users);
  