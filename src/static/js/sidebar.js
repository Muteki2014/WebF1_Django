// static/js/sidebar.js
document.addEventListener("DOMContentLoaded", function () {
    const sidebar = document.getElementById("sidebar");
    const content = document.getElementById("content");
    const btn = document.getElementById("toggleBtn");

    // Inicia colapsado (como vos querías)
    //sidebar.classList.add("collapsed");
    //content.classList.add("collapsed");

    btn.addEventListener("click", () => {
        sidebar.classList.toggle("collapsed");
        content.classList.toggle("collapsed");  // ← ESTA LÍNEA ES LA QUE FALTABA
    });
});