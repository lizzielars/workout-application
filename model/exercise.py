from dataclasses import dataclass

from db.db import db


@dataclass
class Exercise(db.Model):
    exerciseID: int = db.Column(db.Integer, primary_key=True)
    exerciseName: str = db.Column(db.String(30), nullable=False)
    exerciseLink: str = db.Column(db.String(50), nullable=False)
    muscleGroup: str = db.Column(db.String(15), nullable=False)
    muscleGroupID: int = db.Column(db.Integer, nullable=False)
    exerciseDescription: str = db.Column(db.String(600), nullable=False)


def init_model(app):
    with app.app_context():
        db.create_all()
        db.session.add(Exercise(
            exerciseID=101, exerciseName='Pushups', exerciseLink='https://www.youtube.com/embed/IODxDxX7oi4',
            muscleGroup='Chest', muscleGroupID=100, exerciseDescription="Get into a plank position with your arms "
                                                                        "straight, aligned with chest/nipples and "
                                                                        "shoulder width apart. Look down at the floor "
                                                                        "to keep your spine in perfect alignment. "
                                                                        "While squeezing your glutes and core "
                                                                        "muscles, lower your chest so that it almost "
                                                                        "touches the floor, keeping your elbows close "
                                                                        "to the body. Push yourself back up to the "
                                                                        "starting position and repeat. "
        ))
        db.session.add(Exercise(
            exerciseID=102, exerciseName='Diamond Pushups', exerciseLink='https://www.youtube.com/embed/8_ILkbB9an8',
            muscleGroup='Chest', muscleGroupID=100, exerciseDescription="Get into a plank position with your arms "
                                                                        "straight. Move your hands together "
                                                                        "underneath your chest connecting your thumbs "
                                                                        "and index fingers to each other to create a "
                                                                        "diamond shape. Look down at the floor to "
                                                                        "keep your spine in perfect alignment. While "
                                                                        "squeezing your glutes and core muscles, "
                                                                        "lower your chest so that it almost touches "
                                                                        "your hands, keeping your elbows close to the "
                                                                        "body. Push yourself back up to the starting "
                                                                        "position and repeat. "
        ))
        db.session.add(Exercise(
            exerciseID=103, exerciseName='Plyometric Pushups',
            exerciseLink='https://www.youtube.com/embed/Z1hBVYb3Gi0',
            muscleGroup='Chest', muscleGroupID=100, exerciseDescription="Get into a plank position with your arms "
                                                                        "straight, aligned with chest/nipples and "
                                                                        "shoulder width apart. Look down at the floor "
                                                                        "to keep your spine in perfect alignment. "
                                                                        "While squeezing your glutes and core "
                                                                        "muscles, lower your chest so that it almost "
                                                                        "touches the floor, keeping your elbows close "
                                                                        "to the body. Use an explosion of energy to "
                                                                        "push your body up and off the ground leaving "
                                                                        "only your feet in contact with the floor. "
        ))
        db.session.add(Exercise(
            exerciseID=201, exerciseName='Squats',
            exerciseLink='https://www.youtube.com/embed/XNzS1vr4JxE',
            muscleGroup='Legs', muscleGroupID=200, exerciseDescription="Standing with your feet shoulder width apart, "
                                                                       "back straight, head facing forward and core "
                                                                       "muscles tightened, lower your butt to the "
                                                                       "floor as if sitting on a chair. Once your "
                                                                       "knees are at a 90-degree angle, pause for a "
                                                                       "second and then push through your heels to "
                                                                       "stand back up into the starting position. "
        ))
        db.session.add(Exercise(
            exerciseID=202, exerciseName='Calf Raises',
            exerciseLink='https://www.youtube.com/embed/-M4-G8p8fmc',
            muscleGroup='Legs', muscleGroupID=200, exerciseDescription="Standing with your feet together or just "
                                                                       "slightly apart, back straight, head facing "
                                                                       "forward and core muscles tightened, "
                                                                       "raise your heels off the ground putting all "
                                                                       "of your weight on your toes. Pause for a "
                                                                       "second or two at the top of the exercise and "
                                                                       "then lower heels back to the ground. "
        ))
        db.session.add(Exercise(
            exerciseID=203, exerciseName='Lunges',
            exerciseLink='https://www.youtube.com/embed/3XDriUn0udo',
            muscleGroup='Legs', muscleGroupID=200, exerciseDescription="Start in a kneeling position, back straight, "
                                                                       "head facing forward, core muscles tightened, "
                                                                       "with one leg’s knee touching the ground in a "
                                                                       "90-degree angle and in perfect alignment with "
                                                                       "your spine and head. The other leg’s knee "
                                                                       "should be in front of your body and in a "
                                                                       "90-degree angle, foot flat on the ground and "
                                                                       "parallel with the knee. Pushing through your "
                                                                       "heel, lift your body into the air and then "
                                                                       "back down into the starting position. Do each "
                                                                       "leg for half the duration of the exercise time."
        ))
        db.session.add(Exercise(
            exerciseID=204, exerciseName='Step-ups',
            exerciseLink='https://www.youtube.com/embed/WCFCdxzFBa4',
            muscleGroup='Legs', muscleGroupID=200, exerciseDescription="Standing at the bottom of a staircase, keep "
                                                                       "your back straight, head facing forward and "
                                                                       "core muscles tightened. Lift either one of "
                                                                       "your feet onto a step making sure your entire "
                                                                       "foot is on the step and not hanging off. "
                                                                       "Pushing through the heel of the foot on the "
                                                                       "step, slowly lift your entire weight up and "
                                                                       "bring your other foot onto the step. Slowly "
                                                                       "step down from the step in reverse order. Do "
                                                                       "each leg for half the duration of the exercise "
                                                                       "time."
        ))
        db.session.add(Exercise(
            exerciseID=205, exerciseName='Bulgarian Splits Squats',
            exerciseLink='https://www.youtube.com/embed/2C-uNgKwPLE',
            muscleGroup='Legs', muscleGroupID=200, exerciseDescription="Standing up with your back facing a bench or "
                                                                       "staircase, keep your back straight, head "
                                                                       "facing forward and core muscles tightened. "
                                                                       "Lift one of your legs up onto the bench or "
                                                                       "staircase behind you, lower your body into a "
                                                                       "lunge position so that your leading leg is at "
                                                                       "a 90-degree angle and perfectly in line with "
                                                                       "your foot. The trailing leg’s knee should "
                                                                       "almost touch the ground. Lift yourself back "
                                                                       "up, pushing through the heel of your leading "
                                                                       "foot to the starting position. Do each leg "
                                                                       "for half the duration of the exercise time."
        ))
        db.session.add(Exercise(
            exerciseID=206, exerciseName='Jump Squats',
            exerciseLink='https://www.youtube.com/embed/SDJIQq-BrCc',
            muscleGroup='Legs', muscleGroupID=200, exerciseDescription="Standing with your feet shoulder width apart, "
                                                                       "back straight, head facing forward and core "
                                                                       "muscles tightened, lower your butt to the "
                                                                       "floor as if sitting on a chair. Once your "
                                                                       "knees are at a 90-degree angle, use an "
                                                                       "explosion of energy to jump off the ground, "
                                                                       "bending your knees when returning to the "
                                                                       "ground to land softly."
        ))
        db.session.add(Exercise(
            exerciseID=207, exerciseName='High Knees',
            exerciseLink='https://www.youtube.com/embed/D0GwAezTvtg',
            muscleGroup='Legs', muscleGroupID=200, exerciseDescription="While running in place, alternate lifting your "
                                                                       "knees up to waist height and then back down."
        ))
        db.session.add(Exercise(
            exerciseID=208, exerciseName='Butt Kicks',
            exerciseLink='https://www.youtube.com/embed/vXVPvY1UbJI',
            muscleGroup='Legs', muscleGroupID=200, exerciseDescription="While running in place, alternate lifting your "
                                                                       "heels up until they hit your butt and then "
                                                                       "back down."
        ))
        db.session.add(Exercise(
            exerciseID=301, exerciseName='Superman',
            exerciseLink='https://www.youtube.com/embed/cc6UVRS7PW4',
            muscleGroup='Back', muscleGroupID=300, exerciseDescription="Lay down on your stomach with your arms "
                                                                       "straight out above your head to an “I” "
                                                                       "position. Keeping both your elbows and knees "
                                                                       "locked lift both of your arms and legs "
                                                                       "straight up into the air with your head "
                                                                       "looking forward. Lower your arms and legs to "
                                                                       "the starting position."
        ))
        db.session.add(Exercise(
            exerciseID=302, exerciseName='Aquaman',
            exerciseLink='https://www.youtube.com/embed/arK_BGQjwWY',
            muscleGroup='Back', muscleGroupID=300, exerciseDescription="Lay down on your stomach with your arms "
                                                                       "straight out above your head to an “I” "
                                                                       "position. Keeping both your elbows and knees "
                                                                       "locked lift your left arm and right leg up "
                                                                       "into the air with your head looking forward. "
                                                                       "Lower your arm and leg back to the starting "
                                                                       "position. Now lift your right arm and left leg "
                                                                       "the same way. Alternate switching left-right "
                                                                       "and right-left arms and legs respectively."
        ))
        db.session.add(Exercise(
            exerciseID=303, exerciseName='Prone Kneeling Leg Extension',
            exerciseLink='https://www.youtube.com/embed/kGyjr8goY3Q',
            muscleGroup='Back', muscleGroupID=300, exerciseDescription="Get down on all fours with your arms straight "
                                                                       "and underneath your shoulders, knees should be "
                                                                       "touching the ground and make a 90-degree angle "
                                                                       "at the joint. Starting with either leg, extend "
                                                                       "your leg straight out until it is parallel "
                                                                       "with your head and spine, squeezing your "
                                                                       "glutes and core muscles at the top of each "
                                                                       "extension. Lower your leg back to the starting "
                                                                       "position. Do each leg for half the duration of "
                                                                       "the exercise time."
        ))
        db.session.add(Exercise(
            exerciseID=401, exerciseName='Tricep Dips',
            exerciseLink='https://www.youtube.com/embed/0326dy_-CzM',
            muscleGroup='Arms', muscleGroupID=400, exerciseDescription="Sitting down on a bench, chair or couch put "
                                                                       "your palms face down on the edge of the seat "
                                                                       "just outside your hips. Keeping your feet "
                                                                       "together, move them outwards from the seat "
                                                                       "keeping your legs straight until your butt "
                                                                       "just hangs off the edge. Lower your butt "
                                                                       "towards the ground until your arms hit a "
                                                                       "90-degree angle and then lift yourself back up."
        ))
        db.session.add(Exercise(
            exerciseID=402, exerciseName='Arm Circles',
            exerciseLink='https://www.youtube.com/embed/bP52FXTlzjA',
            muscleGroup='Arms', muscleGroupID=400, exerciseDescription="Stand straight up, shoulders back and core "
                                                                       "muscles tightened. Extend both arms out from "
                                                                       "your body to a “T” pose. Rotate your arms "
                                                                       "either clockwise or counter clockwise making "
                                                                       "small circles."
        ))
        db.session.add(Exercise(
            exerciseID=403, exerciseName='Extended Arm Side Plank',
            exerciseLink='https://www.youtube.com/embed/ZudZjUqENyg',
            muscleGroup='Arms', muscleGroupID=400, exerciseDescription="Starting in a pushup plank position and arms "
                                                                       "straight, turn your body to either side until "
                                                                       "you are perpendicular with the floor, lifting "
                                                                       "one arm straight into the air and resting one "
                                                                       "foot on top of the other. You should look like "
                                                                       "a tipped over “T” pose. Hold for the duration "
                                                                       "of the exercise time. Rotate sides of every "
                                                                       "other set."
        ))
        db.session.add(Exercise(
            exerciseID=404, exerciseName='Inchworm',
            exerciseLink='https://www.youtube.com/embed/t6EjIe4A-oI',
            muscleGroup='Arms', muscleGroupID=400, exerciseDescription="Get into a pushup position. Lift your hips "
                                                                       "into the air and slowly inch your feet towards "
                                                                       "your hands. Make sure you don’t bend your "
                                                                       "knees or elbows. Once you get to a point where "
                                                                       "you can’t move your feet any closer, Inch your "
                                                                       "hands away from your feet back to the pushup "
                                                                       "position. Repeat."
        ))
        db.session.add(Exercise(
            exerciseID=501, exerciseName='Forearm Plank',
            exerciseLink='https://www.youtube.com/embed/kL_NJAkCQBg',
            muscleGroup='Abs', muscleGroupID=500, exerciseDescription="Get into a pushup position and place forearms "
                                                                      "on the floor with elbows aligned below "
                                                                      "shoulders and arms parallel to your body at "
                                                                      "about shoulder width. Squeeze your glutes and "
                                                                      "core muscles and hold for the duration of the "
                                                                      "exercise length of time."
        ))
        db.session.add(Exercise(
            exerciseID=502, exerciseName='Sit-Ups',
            exerciseLink='https://www.youtube.com/embed/1fbU_MkV7NE',
            muscleGroup='Abs', muscleGroupID=500, exerciseDescription="Start with your back on the ground, knees about "
                                                                      "a fists width apart bent towards the ceiling "
                                                                      "and feet on the ground. Lift yourself up "
                                                                      "towards your knees until you are in a seated "
                                                                      "position. Slowly lower yourself back to the "
                                                                      "ground along your spine."
        ))
        db.session.add(Exercise(
            exerciseID=503, exerciseName='Crunches',
            exerciseLink='https://www.youtube.com/embed/Xyd_fa5zoEU',
            muscleGroup='Abs', muscleGroupID=500, exerciseDescription="Start with your back on the ground, knees "
                                                                      "together bent towards the ceiling and feet "
                                                                      "together on the ground. Lift yourself a few "
                                                                      "inches up off the ground squeezing your core "
                                                                      "muscles and then back down."
        ))
        db.session.add(Exercise(
            exerciseID=504, exerciseName='Mountain Climbers',
            exerciseLink='https://www.youtube.com/embed/nmwgirgXLYM',
            muscleGroup='Abs', muscleGroupID=500, exerciseDescription="Get into a pushup plank position. Starting "
                                                                      "with either leg, bring your knee to your chest "
                                                                      "and then back to the starting position. Switch "
                                                                      "legs and bring the other knee to your chest "
                                                                      "and back to the starting position. Repeat "
                                                                      "switching legs at a jog or sprint like pace. "
        ))
        db.session.add(Exercise(
            exerciseID=601, exerciseName='Pike Pushups',
            exerciseLink='https://www.youtube.com/embed/sposDXWEB0A',
            muscleGroup='Shoulders', muscleGroupID=600, exerciseDescription="Get into a standard push up position. "
                                                                            "Walk your feet towards your hands while "
                                                                            "lifting your butt into the air until you "
                                                                            "create an ‘A’ shape. While keeping your "
                                                                            "core muscles tight, lower the top of "
                                                                            "your head towards the ground. You should "
                                                                            "be looking through the space between "
                                                                            "your legs in the end position and not at "
                                                                            "the ground. Push yourself back up to the "
                                                                            "starting ‘A’ position. "
        ))
        db.session.add(Exercise(
            exerciseID=602, exerciseName='Shoulder Shrugs',
            exerciseLink='https://www.youtube.com/embed/6buT-g-zEZg',
            muscleGroup='Shoulders', muscleGroupID=600, exerciseDescription="Stand straight up with shoulders back "
                                                                            "and core muscles tight. Raise your "
                                                                            "shoulders up, squeeze and hold for 2 "
                                                                            "seconds and then lower your shoulders "
                                                                            "back to the starting position. "
        ))
        db.session.add(Exercise(
            exerciseID=603, exerciseName='Wall Walk',
            exerciseLink='https://www.youtube.com/embed/NK_OcHEm8yM',
            muscleGroup='Shoulders', muscleGroupID=600, exerciseDescription="Start in a push-up position with your "
                                                                            "feet toward a wall. Slowly back up, "
                                                                            "placing feet higher and higher on the "
                                                                            "wall and moving your arms backward "
                                                                            "toward your body until you’re in a "
                                                                            "handstand position with your stomach "
                                                                            "toward the wall. Slowly crawl back down "
                                                                            "into a push-up position. "
        ))
        db.session.commit()
