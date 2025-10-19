// ---------- Annonces ----------

const params1 = new URLSearchParams(window.location.search);
const personneId = params1.get('id');
const params2 = new URLSearchParams(window.location.search);
const entrepriseId = params2.get('id');

if (personneId) {
    document.getElementById('loadAnnoncesBtn').addEventListener('click', () => {
        fetch('http://localhost:8000/api/annonces/')
            .then(response => response.json())
            .then(data => {
                const container = document.getElementById('AnnoncesContainer');
                container.innerHTML = '';
                data.forEach(annonce => {
                    const div = document.createElement('div');
                    div.innerHTML = `<h3>${annonce.intitule_emploi} chez ${annonce.entreprise}</h3>
                             <p><i>${annonce.departement}</i></p>
                             <p>Type de contrat : ${annonce.type_contrat}</p>
                             <button onclick="window.location.href='details.html?personneId=${personneId}&id=${annonce.id}';" type="button">Voir plus</button>`;
                    container.appendChild(div);
                });
            })
            .catch(error => console.error('Erreur Annonces:', error));
    });

} else if (entrepriseId) {
    document.getElementById('loadAnnoncesBtn').addEventListener('click', () => {
        fetch('http://localhost:8000/api/annonces/')
            .then(response => response.json())
            .then(data => {
                const container = document.getElementById('AnnoncesContainer');
                container.innerHTML = '';
                data.forEach(annonce => {
                    const div = document.createElement('div');
                    div.innerHTML = `<h3>${annonce.intitule_emploi} chez ${annonce.entreprise}</h3>
                             <p><i>${annonce.departement}</i></p>
                             <p>Type de contrat : ${annonce.type_contrat}</p>
                             <button onclick="window.location.href='details.html?entrepriseId=${entrepriseId}&id=${annonce.id}';" type="button">Voir plus</button>`;
                    container.appendChild(div);
                });
            })
            .catch(error => console.error('Erreur Annonces:', error));
    });

} else {
    document.getElementById('loadAnnoncesBtn').addEventListener('click', () => {
        fetch('http://localhost:8000/api/annonces/')
            .then(response => response.json())
            .then(data => {
                const container = document.getElementById('AnnoncesContainer');
                container.innerHTML = '';
                data.forEach(annonce => {
                    const div = document.createElement('div');
                    div.innerHTML = `<h3>${annonce.intitule_emploi} chez ${annonce.entreprise}</h3>
                             <p><i>${annonce.departement}</i></p>
                             <p>Type de contrat : ${annonce.type_contrat}</p>
                             <button onclick="window.location.href='detail.html?id=${annonce.id}';" type="button">Voir plus</button>`;
                    container.appendChild(div);
                });
            })
            .catch(error => console.error('Erreur Annonces:', error));
    });
}