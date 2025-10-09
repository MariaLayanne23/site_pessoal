async function loadHeader() {
  try {
    const response = await fetch("/header.html");
    const headerHTML = await response.text();
    document.getElementById("header-container").innerHTML = headerHTML;

    // Função dropdown do header
    window.myFunction = function () {
      document.getElementById("myDropdown").classList.toggle("show");
    };
    window.onclick = function (event) {
      if (!event.target.matches(".dropbtn")) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        for (var i = 0; i < dropdowns.length; i++) {
          var openDropdown = dropdowns[i];
          if (openDropdown.classList.contains("show")) {
            openDropdown.classList.remove("show");
          }
        }
      }
    };
  } catch (err) {
    console.error("Erro ao carregar header:", err);
  }
}

// Carrega o header quando o DOM estiver pronto
document.addEventListener("DOMContentLoaded", loadHeader);
