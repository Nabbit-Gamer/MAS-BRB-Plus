init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Nabbi_brb_bathroom",
            category=["be right back +"],
            prompt="I have to use the bathroom, [m_name]. (BRB+)",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label Nabbi_brb_bathroom:
    m 1eua "Okay."
    m 3eub "Just don't be on your phone the whole time!"
    m 1hua "Come back soon, [player]~"

$ mas_idle_mailbox.send_idle_cb("Nabbi_brb_bathroom_callback")
return "idle"

label Nabbi_brb_bathroom_callback:
    m 2wub "You're back!"
    m 3tubsu "You listened to me and weren't on your phone the whole time, right?"
    m 2hubsa "Ehehe~"
    m 1eubsa "I'm just teasing you, [player]."
    m 1esc "Although, it's true you shouldn't be on your phone while in the bathroom."
    m 3eka "If you do, just don't lose track of time!"
    m 1rkbsa "...I don't want to wait a while for you to come back just because you were on your phone...{fast}{nw}"
    $ _history_list.pop()
    menu:
        m " {fast}"

        "Huh?":
         m 2eubsa "Nothing, ehehe~"
    return
