async function register() {
    const data = {
        first_name: document.querySelector("#first_name").value,
        last_name: document.querySelector("#last_name").value,
        email: document.querySelector("#email").value,
        password: document.querySelector("#password").value,
        phone: document.querySelector("#phone").value,
        address: document.querySelector("#address").value,
        horaire_travail: document.querySelector("#horaire_travail").value
    };

    const response = await fetch("/api/register/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    });

    const result = await response.json(); // JSON renvoyé par Django
    console.log(result);

    if (result.status === "success") {
        alert("Inscription réussie !");
    } else {
        alert("Erreur : " + result.message);
    }
}




