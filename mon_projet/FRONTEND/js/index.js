// ---------- Annonces ----------
document.getElementById('loadAnnoncesBtn').addEventListener('click', () => {
    fetch('http://localhost:8000/api/annonces/')
    .then(response => response.json())
    .then(data => {
        const container = document.getElementById('AnnoncesContainer');
        container.innerHTML = '';
        data.forEach(annonce => {
            const div = document.createElement('div');
            div.innerHTML = `<h3>${annonce.intitule_emploi} chez ${annonce.entreprise__nom}</h3>
                             <p><i>${annonce.departement}</i></p>
                             <p>Type de contrat : ${annonce.type_contrat}</p>
                             <button onclick="window.location.href='details.html?id=${annonce.id}';" type="button">Voir plus</button>`;
            container.appendChild(div);
        });
    })
    .catch(error => console.error('Erreur Annonces:', error));
});