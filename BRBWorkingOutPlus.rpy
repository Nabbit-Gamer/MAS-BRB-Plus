init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Nabbi_brb_workout",
            category=["be right back +"],
            prompt="I'm going to workout, [m_name]. (BRB+)",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label Nabbi_brb_workout:
    m 1eta "Oh?{w=0.4}{nw}"
    extend 1hub " Okay!"
    m 3eub "What type of workout are you doing?{nw}"
    $ _history_list.pop()
    menu:
        m "What type of workout are you doing?{fast}"

        "Aerobic Exercises":
         m 1eub "Oh, okay!{w=0.4}"
         m 3husdrb "Exercise can be tough,{w=0.5} but don't give up!"
         m 7eub "Don't be afraid to drink water or take a little break.{w=0.4}"
         m 1hua "Good luck with the workout, [player]!"

        "Strength Training":
         m 1eub "Time to build up those muscles?"
         m 3eksdra "Remember you might not see imediate progress. These things take time!"
         m 1hua "Good luck, [player]!"

        "Streching":
         m 1esd "Not feeling flexible yet?"
         m 6ekbssdra "That's ok, we all start somewhere!"
         m 1hua "Enjoy your streching, [player]!"

        "Balance Exercises":
         m 6esd "Can't find your balance?"
         m 1hubsa "Well, I'm glad your working on improving!"
         m 1hua "Good luck, [player]!"

        "Multiple Different Types of Exercise":
         m 6sub "Going for a bit bigger of a workout?"
         m 1eub "Just don't push yourself to hard."
         m 3eksdrd "There isn't much of anything worse then getting hurt while you want to exercise."
         m 1hua "Good luck, [player]!"

$ mas_idle_mailbox.send_idle_cb("Nabbi_brb_workout_callback")
return "idle"

label Nabbi_brb_workout_callback:
        m 1hua "Welcome back, [player]!"
        m 3hub "I hope you enjoyed your workout."
        m 1eub "One day, I'll get to go on a workout with you."
        m 5rubsa "One day..."
        return
