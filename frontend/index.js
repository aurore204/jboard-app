document.getElementById('loadJobsBtn').addEventListener('click', () => {
    fetch('http://localhost:8000/myflashjob/api/jobs/')
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('jobsContainer');
            container.innerHTML = '';  // vide le conteneur
            data.forEach(job => {
                const div = document.createElement('div');
                div.innerHTML = `<h3>${job.title} chez ${job.company}</h3>
                                 <p>${job.description}</p>
                                 <p><i>${job.location}</i></p>`;
                container.appendChild(div);
            });
        })
        .catch(error => console.error('Erreur:', error));
});
