document.addEventListener("DOMContentLoaded", () => {
  const container = document.getElementById("links");

  fetch("static/data/linkscontatos.json")
    .then((response) => {
      if (!response.ok) throw new Error("Erro ao carregar JSON");
      return response.json();
    })
    .then((data) => {
      const links = data.linksC;

      if (!links || links.length === 0) {
        container.innerHTML = "<p>Nenhum link encontrado.</p>";
        return;
      }

      links.forEach((link) => {
        const card = document.createElement("div");
        card.classList.add("link");

        card.innerHTML = `
          <a href="${link.url}" target="_blank" rel="noopener noreferrer">
            <i class="${link.icon}"></i>
            <strong>${link.label}</strong>
          </a>
          
        `;

        container.appendChild(card);
      });
    })
    .catch((error) => {
      container.innerHTML = `<p>Erro ao carregar links.</p>`;
      console.error(error);
    });
});
