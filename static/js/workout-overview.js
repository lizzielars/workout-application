if(document.readyState === "loading") {
    document.addEventListener('DOMContentLoaded', ready)
} else {
    ready()
}


function ready() {
    fetch('/get_exercises')
        .then(response => {
            if (response.ok) {
                response.json().then((data) => {
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

function getWorkout(json){

    const obj = JSON.parse(json)
    const exercises = obj.exercises
    const exerciseTime = 'Exercise Time: ' + obj.exerciseTime + ' sec.'
    const restTime = 'Rest Time: ' + obj.restTime + ' sec.'
    const numSets = 'Number of Sets: ' + obj.numSets
    document.getElementById('exercise-time').innerText = exerciseTime
    document.getElementById('rest-time').innerText = restTime
    document.getElementById('num-sets').innerText = numSets


    var exerciseButtons = document.getElementById('exercise-buttons')
    for (exercise of exercises) {

    var newButton = populateButtons(exercise)

    exerciseButtons.appendChild(newButton)
    }

}

function populateButtons(exercise){

    let newLabel = document.createElement('label')
    newLabel.innerHTML = `
      <input type="radio" name="exercises" value="${exercise.exercise}" autocomplete="off" onchange="getVideo('${exercise.video}','${exercise.description}')"><i class="fa fa-angle-right button-icon"></i>
      ${exercise.exercise}`

    newLabel.classList.add('toggle-btn')
    newLabel.classList.add('add-button')
    newLabel.classList.add('image-toggle')
    newLabel.classList.add('btn')

    return newLabel

}

function getVideo(video, description){
    console.log(video, description)
    var videoContainer = document.getElementById('video-description')

    let videoRow = document.createElement('col-md-12')
    videoRow.classList.add('video-descr-cont')
    videoRow.innerHTML = `<div class="video-wrapper"><iframe width="100%" height="auto" src="${video}" frameborder="0"></iframe></div>`

    let descriptionRow = document.createElement('col-md-12')
    descriptionRow.innerHTML = `<p style="color: #ffffffff;">${description}</p>`

    let newRow = document.createElement('row')
    newRow.appendChild(videoRow)
    newRow.appendChild(descriptionRow)

    videoContainer.replaceChildren(newRow)
}

function complete_workout() {
    let requestInit = {
        method: 'POST',
    }

    fetch('/mark_workout_completed', requestInit)
        .then(response => {
            if (response.ok) {
                response.json().then(() => {
                    window.location.href= '/workout_completed';
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
