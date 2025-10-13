
document.getElementById('loadJobsBtn').addEventListener('click', (event) => {
  // ATTENTION NE PAS METTRE LE BOUTON EN SUBMIT le bouton est type="button SINON 9A FAIT QUE AFFICHER PUIS DISPARAIRE"
  
  fetch('http://localhost:8000/myflashjob/api/jobs/')
    .then(response => response.json())
    .then(data => {
      const container = document.getElementById('jobsContainer');
      container.innerHTML = '';
      data.forEach(job => {
        const div = document.createElement('div');
        div.innerHTML = `<h3>${job.title} chez ${job.company}</h3> 
                         <p>${job.description}</p>
                         <p><i>${job.location}</i></p>
                         <p>${job.posted_at}</p>
                         <button onclick="window.location.href='details.html';" type="button">Voir plus</button>`;
        container.appendChild(div);
      });
    })
    .catch(error => console.error('Erreur:', error));
});