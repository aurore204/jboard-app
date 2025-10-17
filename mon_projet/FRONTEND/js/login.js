const LOGIN_API_URL = "http://127.0.0.1:8000/login/";
document.getElementById("loginForm").addEventListener("submit", async (e) => {
    e.preventDefault()
        const data = {
            email: document.getElementById("email").value,
            password: document.getElementById("password").value
        };
    await login(data);
});

function getCSRFToken() {//fonction pour recuperer le token csrf
    const token = document.querySelector('[name=csrfmiddlewaretoken]');
    return token ? token.value : '';
}
async function login(data) {
    try {
        console.log("Tentative de connexion..."); // Debug

            console.log("Données envoyées:", data); // Debug

            const response = await fetch(LOGIN_API_URL, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-Requested-With": "XMLHttpRequest",
                    "X-CSRFToken": getCSRFToken()  // ici on utilise le token récupéré

                },
                body: JSON.stringify(data)
            });

            console.log("Réponse du serveur:", response.status); // Debug

            const result = await response.json();// permet de convertir la reponse en json
            console.log("Données reçues:", result); // Debug

            if (result.status === "success") {
                alert("Connexion réussie !");

                if (result.role === "people") {
                    window.location.href = "http://localhost:8000/index/";
                } else if (result.role === "companies") {
                    window.location.href = "http://localhost:8000/annonces/";
                } else if (result.role === "admin") {
                    window.location.href = "http://localhost:8000/admin/";
                } else {
                    window.location.href = "/";
                }
            } else {
                alert("Erreur : " + result.message);
            }
    } catch (error) {
            console.error("Erreur lors de la connexion:", error);
            alert("Erreur de connexion au serveur. Vérifiez la console pour plus de détails.");
        }
}