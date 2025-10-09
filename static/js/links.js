document.addEventListener("DOMContentLoaded", () => {
  const container = document.getElementById("links-container");

  fetch("static/data/linksRefs.json")
    .then((response) => {
      if (!response.ok) throw new Error("Erro ao carregar JSON");
      return response.json();
    })
    .then((data) => {
      const links = data.linksRefs;

      if (!links || links.length === 0) {
        container.innerHTML = "<p>Nenhum link encontrado.</p>";
        return;
      }

      links.forEach((link) => {
        const card = document.createElement("div");
        card.classList.add("link-card");

        card.innerHTML = `
          <a href="${link.url}" target="_blank" rel="noopener noreferrer">
            <img src="${link.icon}" alt="${link.label}">
            <strong>${link.label}</strong>
          </a>
          <p>${link.descricao}</p>
        `;

        container.appendChild(card);
      });
    })
    .catch((error) => {
      container.innerHTML = `<p>Erro ao carregar links.</p>`;
      console.error(error);
    });
});
