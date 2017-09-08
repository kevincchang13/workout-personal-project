from project.models import Exercise, BodyPart
from project import db

#Exercises
DumbbellBenchPress = Exercise('Dumbbell Bench Press', """Lie down on a flat bench with a dumbbell in each hand resting on top of your thighs. The palms of your hands will be facing each other.
Then, using your thighs to help raise the dumbbells up, lift the dumbbells one at a time so that you can hold them in front of you at shoulder width.
Once at shoulder width, rotate your wrists forward so that the palms of your hands are facing away from you. The dumbbells should be just to the sides of your chest, with your upper arm and forearm creating a 90 degree angle. Be sure to maintain full control of the dumbbells at all times. This will be your starting position.
Then, as you breathe out, use your chest to push the dumbbells up. Lock your arms at the top of the lift and squeeze your chest, hold for a second and then begin coming down slowly. Tip: Ideally, lowering the weight should take about twice as long as raising it.
Repeat the movement for the prescribed amount of repetitions of your training program.""")
OverheadPress = Exercise("Overhead Press", """Start by placing a barbell that is about chest high on a squat rack. Once you have selected the weights, grab the barbell using a pronated (palms facing forward) grip. Make sure to grip the bar wider than shoulder width apart from each other.
Slightly bend the knees and place the barbell on your collar bone. Lift the barbell up keeping it lying on your chest. Take a step back and position your feet shoulder width apart from each other.
Once you pick up the barbell with the correct grip length, lift the bar up over your head by locking your arms. Hold at about shoulder level and slightly in front of your head. This is your starting position.
Lower the bar down to the collarbone slowly as you inhale.
Lift the bar back up to the starting position as you exhale.
Repeat for the recommended amount of repetitions.""")
FrontSquat = Exercise('Front Squat', """This exercise is best performed inside a squat rack for safety purposes. To begin, first set the bar on a rack that best matches your height. Once the correct height is chosen and the bar is loaded, bring your arms up under the bar while keeping the elbows high and the upper arm slightly above parallel to the floor. Rest the bar on top of the deltoids and cross your arms while grasping the bar for total control.
Lift the bar off the rack by first pushing with your legs and at the same time straightening your torso.
Step away from the rack and position your legs using a shoulder width medium stance with the toes slightly pointed out. Keep your head up at all times as looking down will get you off balance and also maintain a straight back. This will be your starting position. (Note: For the purposes of this discussion we will use the medium stance described above which targets overall development; however you can choose any of the three stances described in the foot positioning section).
Begin to slowly lower the bar by bending the knees as you maintain a straight posture with the head up. Continue down until the angle between the upper leg and the calves becomes slightly less than 90-degrees (which is the point in which the upper legs are below parallel to the floor). Inhale as you perform this portion of the movement. Tip: If you performed the exercise correctly, the front of the knees should make an imaginary straight line with the toes that is perpendicular to the front. If your knees are past that imaginary line (if they are past your toes) then you are placing undue stress on the knee and the exercise has been performed incorrectly.
Begin to raise the bar as you exhale by pushing the floor mainly with the middle of your foot as you straighten the legs again and go back to the starting position.
Repeat for the recommended amount of repetitions.""")
Deadlift = Exercise('Deadlift', """Approach the bar so that it is centered over your feet. Your feet should be about hip-width apart. Bend at the hip to grip the bar at shoulder-width allowing your shoulder blades to protract. Typically, you would use an alternating grip.
With your feet and your grip set, take a big breath and then lower your hips and flex the knees until your shins contact the bar. Look forward with your head. Keep your chest up and your back arched, and begin driving through the heels to move the weight upward.
After the bar passes the knees aggressively pull the bar back, pulling your shoulder blades together as you drive your hips forward into the bar.
Lower the bar by bending at the hips and guiding it to the floor.""")
CloseGripBenchPress = Exercise('Close Grip Bench Press', """Lie back on a flat bench. Using a close grip (around shoulder width), lift the bar from the rack and hold it straight over you with your arms locked. This will be your starting position.
As you breathe in, come down slowly until you feel the bar on your middle chest. Tip: Make sure that - as opposed to a regular bench press - you keep the elbows close to the torso at all times in order to maximize triceps involvement.
After a second pause, bring the bar back to the starting position as you breathe out and push the bar using your triceps muscles. Lock your arms in the contracted position, hold for a second and then start coming down slowly again. Tip: It should take at least twice as long to go down than to come up.
Repeat the movement for the prescribed amount of repetitions.
When you are done, place the bar back in the rack.""")
BarbellCurl = Exercise('Barbell Curl', """Stand up with your torso upright while holding a barbell at a shoulder-width grip. The palm of your hands should be facing forward and the elbows should be close to the torso. This will be your starting position.
While holding the upper arms stationary, curl the weights forward while contracting the biceps as you breathe out. Tip: Only the forearms should move.
Continue the movement until your biceps are fully contracted and the bar is at shoulder level. Hold the contracted position for a second and squeeze the biceps hard.
Slowly begin to bring the bar back to starting position as your breathe in.
Repeat for the recommended amount of repetitions.""")
BarbellHipThrust = Exercise('Barbell Hip Thrust', """Begin seated on the ground with a bench directly behind you. Have a loaded barbell over your legs. Using a fat bar or having a pad on the bar can greatly reduce the discomfort caused by this exercise.
Roll the bar so that it is directly above your hips, and lean back against the bench so that your shoulder blades are near the top of it.
Begin the movement by driving through your feet, extending your hips vertically through the bar. Your weight should be supported by your shoulder blades and your feet. Extend as far as possible, then reverse the motion to return to the starting position.""")

Squats = Exercise("Squats", """Stand with your head facing forward and your chest held up and out.
Place your feet shoulder-width apart or slightly wider. Extend your hands straight out in front of you to help keep your balance. You can also bend the elbows or clasp the fingers.
Sit back and down like you're sitting into an imaginary chair. Keep your head facing forward as your upper body bends forward a bit. Rather than allowing your back to round, let your lower back arch slightly as you descend.
Lower down so your thighs are as parallel to the floor as possible, with your knees over your ankles. Press your weight back into your heels.
Keep your body tight, and push through your heels to bring yourself back to the starting position.""")
BroadJump = Exercise('Broad Jump', """This drill is best done in sand or other soft landing surface. Ensure that you are able to measure distance. Stand in a partial squat stance with feet shoulder width apart.
Utilizing a big arm swing and a countermovement of the legs, jump forward as far as you can.
Attempt to land with your feet out in front you, reaching as far as possible with your legs.
Measure the distance from your landing point to the starting point and track results.""")
PushUp = Exercise('Push-Up', """Get on the floor on all fours, positioning your hands slightly wider than your shoulders.
Extend your legs back so that you are balanced on your hands and toes. Keep your body in a straight line from head to toe without sagging in the middle or arching your back. You can position you feet to be close together or a bit wider depending upon what is most comfortable for you.
Before you begin any movement, contract your abs and tighten your core by pulling your belly button toward your spine. Keep a tight core throughout the entire push up.
Inhale as you slowly bend your elbows and lower yourself until your elbows are at a 90 degree angle.
Exhale as you begin contracting your chest muscles and pushing back up through your hands to the start position. Don't lock out the elbows; keep them slightly bent.""")
TricepDips = Exercise('Tricep Dips', """Position your hands shoulder-width apart on a secured bench or stable chair.
Slide your butt off the front of the bench with your legs extended out in front of you.
Straighten your arms, keeping a little bend in your elbows to keep tension on your triceps and off your elbow joints.
Slowly bend your elbows to lower your body toward the floor until your elbows are at about a 90-degree angle. Be sure to keep your back close to the bench.
Once you reach the bottom of the movement, press down into the bench to straighten your elbows, returning to the starting position. This completes one rep.
Keep your shoulders down as you lower and raise your body. You can bend your legs to modify this exercise.""")
PullUp = Exercise('Pull-Up', """Grab the pull-up bar with the palms facing forward using the prescribed grip. Note on grips: For a wide grip, your hands need to be spaced out at a distance wider than your shoulder width. For a medium grip, your hands need to be spaced out at a distance equal to your shoulder width and for a close grip at a distance smaller than your shoulder width.
As you have both arms extended in front of you holding the bar at the chosen grip width, bring your torso back around 30 degrees or so while creating a curvature on your lower back and sticking your chest out. This is your starting position.
Pull your torso up until the bar touches your upper chest by drawing the shoulders and the upper arms down and back. Exhale as you perform this portion of the movement. Tip: Concentrate on squeezing the back muscles once you reach the full contracted position. The upper torso should remain stationary as it moves through space and only the arms should move. The forearms should do no other work other than hold the bar.
After a second on the contracted position, start to inhale and slowly lower your torso back to the starting position when your arms are fully extended and the lats are fully stretched.
Repeat this motion for the prescribed amount of repetitions.""")
Plank = Exercise('Plank', """Plant the hands directly under the shoulders (slightly wider than shoulder-width apart) like you’re about to do a push-up.
Ground the toes into the floor and squeeze the glutes to stabilize the body. Your legs should be working in the move too; careful not to lock or hyperextend your knees.
Neutralize the neck and spine by looking at a spot on the floor about a foot beyond the hands. Your head should be in line with your back.
Hold the position for 20 seconds. As you get more comfortable with the move, hold your plank for as long as possible without compromising form or breath.""")
MountainClimbers = Exercise('Mountain Climbers', """Assume a push-up position with your arms straight and your body in a straight line from your head to your ankles. Without changing the posture of your lower back (it should be arched), raise your right knee toward your chest.
Pause, return to the starting position and repeat with your left leg. That’s one rep. Alternate until you’ve completed all your reps.""")
HangingLegRaises = Exercise('Hanging Leg Raises', """Hang from a chin-up bar with both arms extended at arms length in top of you using either a wide grip or a medium grip. The legs should be straight down with the pelvis rolled slightly backwards. This will be your starting position.
Raise your legs until the torso makes a 90-degree angle with the legs. Exhale as you perform this movement and hold the contraction for a second or so.
Go back slowly to the starting position as you breathe in.
Repeat for the recommended amount of repetitions.""")
Burpees = Exercise('Burpees', """Begin standing with your legs shoulder-width apart.
Place your hands on the floor and kick your legs back so you end up with your stomach and thighs on the floor. Your elbows should be bent.
From this position, press up like you're doing a push-up and push your hips up.
Jump your feet under your hips and stand.
Finish the movement by jumping in the air and bringing your hands over your head.
Repeat.""")
RickshawCarry=Exercise('Rickshaw Carry', "Position the frame at the starting point, and load with the appropriate weight. Standing in the center of the frame, begin by gripping the handles and driving through your heels to lift the frame. Ensure your chest and head are up and your back is straight. Immediately begin walking briskly with quick, controlled steps. Keep your chest up and head forward, and make sure you continue breathing. Bring the frame to the ground after you have reached the end point.")
AbRoller=Exercise('Ab Roller', "Hold the Ab Roller with both hands and kneel on the floor. Now place the ab roller on the floor in front of you so that you are on all your hands and knees (as in a kneeling push up position). This will be your starting position. Slowly roll the ab roller straight forward, stretching your body into a straight position. Tip: Go down as far as you can without touching the floor with your body. Breathe in during this portion of the movement. After a pause at the stretched position, start pulling yourself back to the starting position as you breathe out. Tip: Go slowly and keep your abs tight at all times.")

#BodyParts
Chest = BodyPart('Chest')
Back = BodyPart('Back')
Forearm = BodyPart('Forearm')
Bicep = BodyPart('Bicep')
Tricep = BodyPart('Tricep')
Shoulder = BodyPart('Shoulder')
Abs = BodyPart('Abs')
Quad = BodyPart('Quad')
Hamstring = BodyPart('Hamstring')
Glutes = BodyPart('Glutes')
Calves = BodyPart('Calves')
Deltoids = BodyPart("Deltoids")
Lumbar = BodyPart('Lumbar')

PectoralisMajor = BodyPart('Pectoralis Major')
LatissimusDorsi = BodyPart("Latissimus Dorsi")
Trapezius = BodyPart("Trapezius")




#Relationship
DumbbellBenchPress.bodyparts.extend([Chest, Tricep, Forearm])
OverheadPress.bodyparts.extend([Shoulder])
FrontSquat.bodyparts.extend([Abs, Quad])
Deadlift.bodyparts.extend([Hamstring])
CloseGripBenchPress.bodyparts.extend([Tricep])
BarbellCurl.bodyparts.extend([Bicep])
BarbellHipThrust.bodyparts.extend([Glutes])
Squats.bodyparts.extend([Glutes, Quad, Hamstring])
BroadJump.bodyparts.extend([Glutes, Quad, Hamstring, Calves])
PushUp.bodyparts.extend([Chest, Tricep, Deltoids])
TricepDips.bodyparts.extend([Tricep])
PullUp.bodyparts.extend([Back, Forearm, Bicep])
Plank.bodyparts.extend([Abs,Lumbar])
MountainClimbers.bodyparts.extend([Abs])
HangingLegRaises.bodyparts.extend([Abs])
Burpees.bodyparts.extend([Tricep,Abs, Shoulder, Hamstring, Quad, Calves])
RickshawCarry.bodyparts.extend([Forearm])
AbRoller.bodyparts.extend([Abs])


db.session.add_all([Chest,
Back,
Forearm,
Bicep,
Tricep,
Shoulder,
Abs,
Quad,
Hamstring,
Glutes,
Calves,
Deltoids,
Lumbar,
Squats,
BroadJump,
PushUp,
TricepDips,
PullUp,
Plank,
MountainClimbers,
HangingLegRaises,
Burpees,
DumbbellBenchPress,
OverheadPress,
FrontSquat,
Deadlift,
CloseGripBenchPress,
BarbellCurl,
BarbellHipThrust,
PectoralisMajor,
LatissimusDorsi,
Trapezius,
RickshawCarry])
db.session.commit()
