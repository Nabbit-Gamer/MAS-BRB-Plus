init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Nabbi_brb_homework",
            category=["be right back +"],
            prompt="I'm going to do some homework, [m_name]. (BRB+)",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label Nabbi_brb_homework:
    m 1eua "Got some homework to finish up?"
    m 2eub "If you don't mind me asking..."
    m 3eub "What class is the homework from?{nw}"
    $ _history_list.pop()
    menu:
        m "What class is the homework from?{fast}"

        "Math":
         m 1eub "Oh, okay!"
         m 3eusdra "Math can be tough,{w=0.5} but don't give up!"
         m 7ekbsa "Don't be afraid to use a calculator or ask for help if you need it.{w=0.4}"
         m 1hua "Good luck with the math, [player]!"

        "Science":
         m 6sub "Science has always interested me."
         m 1hub "I hope you learn something new!"
         m 1eua "Good luck, [player]!"

        "History":
         m 1suw "Ooh!"
         m 4eub "History has always interested me."
         m 1hub "Well, I hope you learn something new!"
         m 3hubfa "Good luck, [player]!"

        "ELA":
         m 6tubsu "Your not just doing the work to impress me, right?"
         m 1hubsa "Ehehe~"
         m 1tubsu "I'm just teasing~"
         m 1hubsa "Anyways, Good luck, [player]!"

        "A Different Language Class":
         m 6sub "Ooh, trying to learn a new language?"
         m 4tublu "It's always fun for you and a friend to speak in a different language so no one knows what your saying."
         m 2gublu "Just don't do it to much~"
         m 1hubla "Anyways, Good luck, [player]!"

        "The Homework is for a club I'm in":
         m 1sub "Ooh, club homework?"
         m 4tubfu "I bet it's 100 times less fun then our poem writing~"
         m 1hubfa "Ehehe~"
         m 1tubfb "I'm just teasing~"
         m 1eubsa "If your in a club for it, it's interesting for you anyways."
         m 3hubsb "So, Good luck, [player]!"
        
        "I have multiple class with homework":
         m 2esx "Ooh, that can suck."
         m 1eka "Hopefully they didn't assign to much."
         m 3esd "It can be hard to do homework for multiple classes, especially if you already had plans for the day."
         m 1hua "But I believe you can get it all done in one go!"
         m 3eub "Good luck, [player]!"

$ mas_idle_mailbox.send_idle_cb("Nabbi_brb_homework_callback")
return "idle"

label Nabbi_brb_homework_callback:
        m 1hua "Welcome back, [player]!"
        m 3eua "I hope you finished all your homework."
        m 1tubfu "But I also wouldn't mind if you left just a little to be with me sooner~"
        m 1hubfa "Ehehe~"
        return
