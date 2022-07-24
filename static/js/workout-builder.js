if(document.readyState === "loading") {
    document.addEventListener('DOMContentLoaded', ready)
} else {
    ready()
}

function ready() {
    fetch('/get_skill_level')
        .then(response => {
            if (response.ok) {
                response.json().then((data) => {
                    let skill_level = data['difficulty']
                    let elements = document.getElementById("difficulty").children

                    for (let i = 0; i < elements.length; i++) {
                        elements[i].classList.remove("active")
                        if (elements[i].textContent.includes(skill_level)) {
                            elements[i].classList.add("active")
                        }
                    }

                    console.log('Success:', response);
                })
            } else {
                console.error('Error:', response);
            }

        })
        .catch((error) => {
            console.error('Error:', error);
        });

    fetch('/get_exercises')
        .then(response => {
            if (response.ok) {
                response.json().then((data) => {
                    for(let i = 0; i < data.length; i++){
                        addMuscleToCart(data[i].exerciseID, data[i].exerciseName)
                    }
                    console.log('Success:', response);
                })
            } else {
                console.error('Error:', response);
            }

        })
        .catch((error) => {
            console.error('Error:', error);
        });

    var removeMuscleButtons = document.getElementsByClassName('remove-button')
    console.log(removeMuscleButtons)
    for(var i = 0; i < removeMuscleButtons.length; i++){
        var button = removeMuscleButtons[i]
        button.addEventListener('click', removeMuscle)
    }

    var addToWorkoutButton = document.getElementById('selected-muscle')
    console.log(addToWorkoutButton.innerText)
    addToWorkoutButton.addEventListener('click', addToCartClicked)

    let continueButton = document.getElementById('continue')
    continueButton.addEventListener('click', continueButtonClicked)
}

function removeMuscle(event) {
    let button_target = event.target.tagName === 'I' ? event.currentTarget : event.target

    let body = {
        exerciseID: parseInt(button_target.id),
        exerciseName: button_target.innerText
    };

    let requestInit = {
        method: 'DELETE',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(body)
    }

    fetch('/delete_exercises', requestInit)
        .then(response => {
            if (response.ok) {
                response.json().then(() => {
                    button_target.remove()
                    document.getElementById('total-muscles').innerText = String(document.getElementsByClassName('remove-button').length)
                    console.log('Success:', response);
                })
            } else {
                console.error('Error:', response);
            }
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}

function addToCartClicked(event) {
    let name = event.currentTarget.innerText

    let body = {name: name};
    let requestInit = {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(body)
    }

    fetch('/add_exercise', requestInit)
        .then(response => {
            if (response.ok) {
                response.json().then((data) => {
                    addMuscleToCart(data.exerciseID, data.exerciseName)
                    console.log('Success:', response);
                })
            } else {
                response.json().then((data) => {
                    alertModal(data.message);
                    console.log('Error:', data.message);
                })
            }
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}

function addMuscleToCart(id, name) {
    let button = document.createElement('button')
    button.classList.add('btn')
    button.classList.add('image-toggle')
    button.classList.add('btn-block')
    button.classList.add('add-button')
    button.classList.add('remove-button')
    button.id = id
    button.innerHTML = `<i class="fa fa-minus button-icon"></i>${name}`
    let addedMuscles = document.getElementsByClassName('selected-muscles')[0]
    addedMuscles.append(button)

    document.getElementById('total-muscles').innerText = String(document.getElementsByClassName('remove-button').length)

    button.addEventListener('click', removeMuscle)
}

function checkValue(string) {
    switch(string){
        case "chest":
            document.getElementById("human-fig").src = 'static/images/chest.png'
            document.getElementById("selected-muscle").innerHTML = '<button class="btn image-toggle btn-block add-button"><i class="fa fa-plus button-icon"></i>Chest</button>'
            break;
        case "back":
            document.getElementById("human-fig").src = 'static/images/back.png'
            document.getElementById("selected-muscle").innerHTML = '<button class="btn image-toggle btn-block add-button"><i class="fa fa-plus button-icon"></i>Back</button>'
            break;
        case "arms":
            document.getElementById("human-fig").src = 'static/images/arms.png'

            document.getElementById("selected-muscle").innerHTML = '<button class="btn image-toggle btn-block add-button"><i class="fa fa-plus button-icon"></i>Arms</button>'
            break;
        case "abs":
            document.getElementById("human-fig").src = 'static/images/abs.png'

            document.getElementById("selected-muscle").innerHTML = '<button class="btn image-toggle btn-block add-button"><i class="fa fa-plus button-icon"></i>Abs</button>'
            break;
        case "legs":
            document.getElementById("human-fig").src = 'static/images/legs.png'

            document.getElementById("selected-muscle").innerHTML = '<button class="btn image-toggle btn-block add-button"><i class="fa fa-plus button-icon"></i>Legs</button>'
            break;
        case "shoulders":
            document.getElementById("human-fig").src = 'static/images/shoulders.png'
            document.getElementById("selected-muscle").innerHTML = '<button class="btn image-toggle btn-block add-button"><i class="fa fa-plus button-icon"></i>Shoulders</button>'
            break;
        default:
            document.getElementById("human-fig").src = 'static/images/default-human-fig.png'
            break;
    }
}

function continueButtonClicked() {
    let skill_level = document.getElementById("difficulty").querySelector('.active')?.innerText

    let requestInit = {
        method: 'POST',
        body: JSON.stringify({difficulty: skill_level})
    }

    fetch('/submit_workout', requestInit)
        .then(response => {
            if (response.ok) {
                response.json().then((data) => {
                    console.log('Success:', response);
                    window.location.href = "/workout_overview"
                })
            } else {
                response.json().then((data) => {
                    alertModal(data.message);
                    console.log('Error:', response);
                })


                /* Example Call to Modals */
                //confirmModal('Do you want to continue?', "/workout_overview");
                //alertModal('Error message');
            }

        })
        .catch((error) => {
            console.error('Error:', error);
            alertModal(error);
        });
}

function changeSkill(skillLevel) {
    //document.getElementById("difficulty").querySelector('.active')?.innerText

    let requestInit = {
        method: 'POST',
        body: JSON.stringify({difficulty: skillLevel})
    }

    fetch('/set_skill_level', requestInit)
        .then(response => {
            if (response.ok) {
                response.json().then(() => {
                    console.log('Success:', response);
                })
            } else {
                console.error('Error:', response);
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

function confirmModal(body, confirmLink) {
    // Display error message to the user in a modal
    // Body is the modal message and confirmLink is the page to be routed to
    $("#confirmed-button").click(function(){
        window.location.href= confirmLink;
      });
    $('#confirm-modal-body').html(body);
    $('#confirmModal').modal('show');
}

