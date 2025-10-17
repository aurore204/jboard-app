const API_URL = "http://127.0.0.1:8000/register/";
const result = document.getElementById("result");

// --- CANDIDAT ---
document.getElementById("formCandidat").addEventListener("submit", async (e) => {
  e.preventDefault();

  const data = {
    role: "people",
    first_name: document.getElementById("first-name").value,
    last_name: document.getElementById("last-name").value,
    email: document.getElementById("emailCandidat").value,
    phone: document.getElementById("phone").value,
    address: document.getElementById("addressCandidat").value,
    password: document.getElementById("passwordCandidat").value,
  };

  await register(data);
});

// --- ENTREPRISE ---
document.getElementById("formEntreprise").addEventListener("submit", async (e) => {
  e.preventDefault();

  const data = {
    role: "companies",
    name: document.getElementById("name").value,
    email: document.getElementById("emailEntreprise").value,
    phone: document.getElementById("phoneEntreprise").value,
    address: document.getElementById("address").value,
    password: document.getElementById("passwordEntreprise").value,
  };

  await register(data);
});

// --- Fonction générique ---
async function register(data) {
  try {
    console.log("Données envoyées:", data); // Debug

    const response = await fetch(API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-Requested-With": "XMLHttpRequest",//c'est pour que le serveur sache qu il s agit d une requete ajax
        "X-CSRFToken": csrfToken  // Ici on utilise le token récupéré

      },
      body: JSON.stringify(data),
    });

    console.log("Réponse du serveur:", response.status); // Debug

    const res = await response.json();
    console.log("Données reçues:", res); // Debug

    if (response.ok) {
      result.textContent = `Inscription réussie pour ${data.role === 'people' ? 'le candidat' : 'l entreprise'} `;
      result.style.color = "green";
      result.style.display = "block";
    } else {
      result.textContent = res.message || "Erreur lors de l'inscription.";
      result.style.color = "red";
      result.style.display = "block";
    }
  } catch (error) {
    console.error("Erreur:", error);
    result.textContent = "Erreur de connexion au serveur.";
    result.style.color = "red";
    result.style.display = "block";
  }
}
