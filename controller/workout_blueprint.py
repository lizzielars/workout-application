import json
import random
from typing import List

from flask import Blueprint, render_template, request, jsonify
from flask_login import current_user
from flask_login import login_required
from sqlalchemy import not_
from sqlalchemy.orm.collections import InstrumentedList

from db.db import db
from model.cart_item import CartItem
from model.exercise import Exercise
from model.muscle_groups_type import MuscleGroupType
from model.user import User
from model.workout import Workout

app = Blueprint('workout', __name__)

selected_exercises: List[Exercise] = []


@app.route("/workout_builder")
@login_required
def workout_builder():
    # Check if user has unfinished workouts
    user = current_user

    # If user has workouts
    if user.workouts:
        existing_workout = user.workouts.filter(
            Workout.userID == user.userID,
            Workout.isCompleted == False
        ).first()

        # If workouts exist but none of them are unfinished
        if not existing_workout:
            create_workout_in_db(user.userID)
    else:
        # User does not have workouts. Create one
        create_workout_in_db(user.userID)

    return render_template("workout-builder.html", title="HIIT Workout Builder")


@app.route("/workout_overview")
@login_required
def workout_overview():
    # Call Db and get exercises for the user
    cart_items: List[CartItem] = get_selected_exercises()
    cart_items_ids: List[int] = [ci.exerciseID for ci in cart_items]
    exercises: List[Exercise] = get_available_exercises_from_ids(cart_items_ids)

    user: User = current_user

    modified_cart_items = []
    for exercise in exercises:
        modified_cart_items.append({
            "exercise": exercise.exerciseName,
            "description": exercise.exerciseDescription,
            "video": exercise.exerciseLink
        })

    # Built workout json hardcoded for now. Need to replace with calculated workout
    exampleJson = {
        "exerciseTime": user.exerciseTime,
        "restTime": user.exerciseRest,
        "numSets": user.exerciseSets,
        "exercises": modified_cart_items
    }
    json_string = json.dumps(exampleJson)
    return render_template("workout-overview.html", title="HIIT Workout Overview", json=json_string)


@app.route("/workout_completed")
@login_required
def workout_completed():
    return render_template("workout-completed.html", title="HIIT Workout Completed")


@app.route('/get_exercises', methods=['GET'])
@login_required
def get_exercises():
    exercises: InstrumentedList = get_workout_from_db().cartItems
    response = jsonify(list(exercises))
    return response


@app.route('/get_skill_level', methods=['GET'])
@login_required
def get_skill_level():
    workout: Workout = get_workout_from_db()
    response = jsonify({"difficulty": workout.difficulty})
    return response


@app.route('/add_exercise', methods=['POST'])
@login_required
def add_exercise():
    # Get data from request and find exercise name
    data = json.loads(request.data)
    muscle_group_name = data['name']

    # Make sure no more than 3 exercises of type are created
    selected_cart_items_total: List[CartItem] = get_selected_exercises()
    selected_cart_items_muscle_group: List[CartItem] = get_selected_exercises_by_type(
        muscle_group_name)
    exercise_ids = [ci.exerciseID for ci in selected_cart_items_muscle_group]

    available_exercises = get_available_exercises_by_type(muscle_group_name, exercise_ids)

    if get_num_allowed_exercises() <= len(selected_cart_items_total):
        return jsonify(message="Maximum workouts selected for the difficulty level."), 400

    selected_exercise = None
    if len(selected_cart_items_muscle_group) < 3 and available_exercises:
        selected_exercise = random.choice(available_exercises)

        db.session.add(CartItem(
            exerciseID=selected_exercise.exerciseID,
            workoutID=get_workout_from_db().workoutID,
            muscleGroup=muscle_group_name,
            exerciseName=selected_exercise.exerciseName
        ))
        db.session.commit()

        # Jsonify a response that will be sent to JS
        response = jsonify(selected_exercise)
    elif len(selected_cart_items_muscle_group) >= 3:
        return jsonify(message="No more than 3 workouts can be selected per muscle group"), 400
    else:
        return jsonify(message="There are no more workouts for this muscle group"), 400

    return response


@app.route('/set_skill_level', methods=['POST'])
@login_required
def set_skill_level():
    data = json.loads(request.data)
    skill_level = data['difficulty']

    workout: Workout = get_workout_from_db()

    workout.difficulty = skill_level
    db.session.commit()

    return jsonify(success=True)


@app.route('/delete_exercises', methods=['DELETE'])
@login_required
def delete_exercises():
    exercise_to_remove = CartItem(**json.loads(request.data))
    workout_id = get_workout_from_db().workoutID

    db_object = CartItem.query.filter(
        CartItem.workoutID == workout_id,
        CartItem.exerciseID == exercise_to_remove.exerciseID
    ).one()

    db.session.delete(db_object)
    db.session.commit()

    response = jsonify(success=True)
    return response


@app.route('/get_workout', methods=['GET'])
@login_required
def get_workout():
    data = json.loads(request.data)

    response = jsonify(success=True)
    return response


@app.route('/submit_workout', methods=['POST'])
@login_required
def submit_exercises():
    data = json.loads(request.data)

    if len(data) == 0:
        return "Unspecified skill level", 400
    else:
        difficulty = data['difficulty']

        min_cart_items = 1
        max_cart_items = get_num_allowed_exercises(difficulty)
        if difficulty != 'Beginner':
            if difficulty == 'Intermediate':
                min_cart_items = get_num_allowed_exercises('Beginner')
            else:
                min_cart_items = get_num_allowed_exercises('Intermediate')

        num_items_in_cart = len(get_selected_exercises())

        if num_items_in_cart > max_cart_items:
            return jsonify(message=f"Too many workouts selected for the given skill level. "
                                   f"{difficulty} level can only have {max_cart_items} exercises selected"), 400
        elif num_items_in_cart < min_cart_items:
            return jsonify(message=f"Not enough workouts selected. "
                                   f"{difficulty} level must have at least {min_cart_items} exercises selected"), 400

        response = jsonify(success=True)
    return response


@app.route('/mark_workout_completed', methods=['POST'])
@login_required
def mark_workout_completed():
    workout: Workout = get_workout_from_db()
    workout.isCompleted = True
    db.session.commit()

    response = jsonify(success=True)
    return response


@app.route('/submit_rating', methods=['POST'])
@login_required
def submit_rating():
    data = json.loads(request.data)
    workout_rating = data['workout_rating'] if data else None
    if workout_rating and workout_rating != '':
        workout_rating = int(workout_rating)
    else:
        return jsonify(message=f"Must select a rating"), 400

    user: User = current_user

    if workout_rating == 1:
        if user.exerciseTime < 60:
            user.exerciseTime += 15
        if user.exerciseTime == 60:
            pass
        if user.exerciseSets < 6:
            user.exerciseSets += 1
        if user.exerciseSets == 6:
            pass
        if user.exerciseRest > 30:
            user.exerciseRest -= 15
        if user.exerciseRest == 30:
            pass
    elif workout_rating == 2:
        pass
    elif workout_rating == 3:
        if 30 < user.exerciseTime:
            user.exerciseTime -= 15
        if user.exerciseTime == 30:
            pass
        if 3 < user.exerciseSets:
            user.exerciseSets -= 1
        if user.exerciseSets == 3:
            pass
        if user.exerciseRest < 60:
            user.exerciseRest += 15
        if user.exerciseRest == 60:
            pass

    db.session.commit()

    response = jsonify(success=True)
    return response


def create_workout_in_db(user_id: int) -> Workout:
    workout = Workout(userID=user_id)
    db.session.add(workout)
    db.session.commit()
    return workout


def get_workout_from_db() -> Workout:
    existing_workout = current_user.workouts.filter(
        Workout.userID == current_user.userID,
        Workout.isCompleted == False
    ).first()
    return existing_workout


def get_selected_exercises_by_type(muscle_group: MuscleGroupType) -> List[CartItem]:
    exercises = get_workout_from_db().cartItems.filter(CartItem.muscleGroup == muscle_group).all()
    return exercises


def get_selected_exercises() -> List[CartItem]:
    exercises = get_workout_from_db().cartItems.all()
    return exercises


def get_available_exercises_by_type(muscle_group: MuscleGroupType, selected_exercise_ids: List) -> \
        List[Exercise]:
    exercises = Exercise.query.filter(
        Exercise.muscleGroup == muscle_group,
        not_(Exercise.exerciseID.in_(selected_exercise_ids))
    ).all()
    return exercises


def get_available_exercises_from_ids(selected_exercise_ids: List) -> \
        List[Exercise]:
    exercises = Exercise.query.filter(
        (Exercise.exerciseID.in_(selected_exercise_ids))
    ).all()
    return exercises


def get_num_allowed_exercises(level: str = None) -> int:
    if not level:
        workout: Workout = get_workout_from_db()
        level = workout.difficulty

    if level == 'Beginner':
        return 3
    elif level == 'Intermediate':
        return 6
    else:
        return 9
