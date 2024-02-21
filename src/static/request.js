const xhr = new XMLHttpRequest();

// Récupération de la réponse de la requête
xhr.onreadystatechange = function () {
	if (xhr.readyState === XMLHttpRequest.DONE) {
		if (xhr.status === 200) {
			const result = xhr.responseText;
			const cds = JSON.parse(result);
			let html = `<table> <thead><tr>
				<th>ID</th>
				<th>Titre</th> 
				<th>Artiste</th>
				<th>Genre</th>
				<th>Prix</th></tr></thead> <tbody>`;
			for (const cd in cds) {
				const element = cds[cd];
				html += `
					<tr>
						<td>${cd}</td>
						<td>${element.Titre}</td>
						<td>${element.Artiste}</td>
						<td>${element.Genre}</td>
						<td>${element.Prix}</td>
					</tr>`;
			}
			html += '</tbody></table>';
			document.getElementById('liste-cd').innerHTML = html;
		} else {
			console.error('Erreur lors de la récupération des CD: ', xhr.status);
		}
	}
};

// Envoi de la requête pour récupérer les CD
xhr.open('GET', 'getCD');
xhr.send();
