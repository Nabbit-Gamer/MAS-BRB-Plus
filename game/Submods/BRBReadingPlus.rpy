init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Nabbi_brb_reading",
            category=["be right back +"],
            prompt="I'm going to do some reading, [m_name]. (BRB+)",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label Nabbi_brb_reading:
    m 1eta "Oh?{w=0.4}{nw}"
    extend 1hub " Okay!"
    m 3eub "What genre are you going to read?{nw}"
    $ _history_list.pop()
    menu:
        m "What genre are you going to read?{fast}"

        "Fiction":
         m 6sub "Fiction always has so many possibilities!"
         m 1hub "I hope you read something truly unique!"
         m 1eua "Enjoy your reading, [player]!"

        "Dystopian":
         m 1suw "Ooh!"
         m 4eub "Dystopias have always interested me."
         m 1hua "Well, I hope you enjoy it, [player]!"

        "Mystery":
         m 1sub "Trying to get to the bottom of a mystery?"
         m 3tubsu "I promise I'm not the Guilty Party this time."
         m 1hubsa "Ehehe~"
         m 1hubsb "Enjoy your reading, [player]!"

        "Horror":
         m 6sud "Ooh, you like scary stories?"
         m 4eubsa "I can always tell you some."
         m 1hubsb "But for now, enjoy your reading, [player]!"

        "A different Genre":
         m 1eksdrc "Oh, sorry it's not on the list."
         m 4ekbfsdra "But that shouldn't affect your enjoyment of reading it."
         m 1hubsb "So, Happy Reading, [player]!"
        
        "I'm reading somehting other than a book":
         m 2ekblb "Oh, sorry for the confusion."
         m 1ekbla "Even if it's not a book, I hope you find whatever your reading interesting!"
         m 1hublb "Happy Reading, [player]!"

$ mas_idle_mailbox.send_idle_cb("Nabbi_brb_reading_callback")
return "idle"

label Nabbi_brb_reading_callback:
        m 1hua "Welcome back, [player]!"
        m 3eua "I hope you enjoyed your reading."
        m 2eubsa "Hopefully one day I can read with you."
        m 5rubsa "One day..."
        return
