const params = new URLSearchParams(window.location.search);
const personneId = params.get('personneId') || localStorage.getItem('personneId');
const entrepriseId = params.get('entrepriseId') || localStorage.getItem('entrepriseId');

document.getElementById('loadAnnoncesBtn').addEventListener('click', () => {
    fetch('http://localhost:8000/api/annonces/')
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('AnnoncesContainer');
            container.innerHTML = '';

            data.forEach(annonce => {
                const div = document.createElement('div');

                // Détermine l'id à passer dans l'URL
                let url = `detail.html?id=${annonce.id}`;
                if (personneId) url += `&personneId=${personneId}`;
                else if (entrepriseId) url += `&entrepriseId=${entrepriseId}`;

                div.innerHTML = `
                    <h3>${annonce.intitule_emploi} chez ${annonce.entreprise}</h3>
                    <p><i>${annonce.departement}</i></p>
                    <p>Type de contrat : ${annonce.type_contrat}</p>
                    <button onclick="window.location.href='${url}'" type="button">Voir plus</button>
                `;
                container.appendChild(div);
            });
        })
        .catch(error => console.error('Erreur Annonces:', error));
});
