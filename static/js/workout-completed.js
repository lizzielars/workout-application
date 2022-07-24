function rate() {
    let workout_rating = document.getElementById("finished-difficulty").querySelector('.active')?.children[0].id

    let requestInit = {
        method: 'POST',
        body: JSON.stringify({workout_rating: workout_rating})
    }

    fetch('/submit_rating', requestInit)
        .then(response => {
            if (response.ok) {
                response.json().then(() => {
                    window.location.href= '/';
                    console.log('Success:', response);
                })
            } else {
                response.json().then((data) => {
                    alertModal(data.message)
                    console.log('Error:', response);
                })
            }
        })
        .catch((error) => {
            console.error('Error:', error);
            alertModal(error);
        });
}

function alertModal(body) {
    // Display error message to the user in a modal
    // Body is the error message
    $('#alert-modal-body').html(body);
    $('#errorModal').modal('show');
}

