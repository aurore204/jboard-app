async function login() {
    const response = await fetch("/api/login/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            email: document.querySelector("#email").value,
            password: document.querySelector("#password").value
        })
    });

    const result = await response.json(); // ici on récupère le JSON renvoyé par Django
    console.log(result);

    if (result.status === "success") {
        alert("Connexion réussie !");
    } else {
        alert("Erreur : " + result.message);
    }
}
