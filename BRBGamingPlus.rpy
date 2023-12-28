init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Nabbi_brb_gaming",
            category=["be right back +"],
            prompt="I'm going to game for a bit, [m_name]. (BRB+)",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label Nabbi_brb_gaming:
    m 3tubsu "Gotten a little bored? Or perhaps you challenged a friend to a duel?"
    m 2hubsa "Well, if you don't mind me asking..."
    m 3eub "What type of game are you going to play?{nw}"
    $ _history_list.pop()
    menu:
        m "What type of game are you going to play?{fast}"

        "Shooter":
         m 6esc "Oh..."
         m 3euc "Well, shooters aren't my favorite type of game, But I can't really blame you for enjoying them."
         m 1hubssdra "Just don't yell at your friends or something if you die, ok?"
         m 1eubsb "Enjoy your Game, [player]!"
         m 3hubsb "I'll be cheering you on!"

        "Platformer":
         m 2tub "Back to the basics, huh?"
         m 3hubsa "Well, there's nothing wrong with that!"
         m 1eubsb "Even something basic can be enjoyable."
         m 3hubsa "Have fun, [player]!"
         m 3hubsb "I'll be cheering you on!"

        "Racing":
         m 2tub "Challegning someone to a race?"
         m 6hubssdrb "Just don't crash!"
         m 1hubsa "Ehehe~"
         m 3eubsa "Enjoy your Game, [player]!"
         m 3hubsb "I'll be cheering you on!"

        "Party":
         m 1hua "Ooh, Party games are always fun!"
         m 6ekbssdra "Just don't get mad if you lose because of somehting you think is weird or dumb."
         m 3hubsb "That's part of the appeal, after all!"
         m 1hubsa "Have Fun!"
         m 3hubsb "I'll be cheering you on!"

        "The Type isn't in this list":
         m 6eksdrc "Oh, sorry it's not on the list."
         m 3ekbsa "But that shouldn't affect your enjoyment of playing it."
         m 1hubsa "So, Happy Gaming, [player]!"
         m 3hubsb "I'll be cheering you on!"

        "Board and Card Games":
         m 2tubsu "Going against what everyone else is downloading this submod for, huh?"
         m 3hubsb "I'm just teasing~"
         m 1eubsa "Also, I can't blame you. Board and card games are fun in their own right."
         m 3hubsb "Happy Gaming, [player]!"
         m 3hubsb "I'll be cheering you on!"

$ mas_idle_mailbox.send_idle_cb("Nabbi_brb_gaming_callback")
return "idle"

label Nabbi_brb_gaming_callback:
        m 1hua "Welcome back, [player]!"
        m 3eua "I hope you enjoyed your game."
        m 2eubsb "I hope I can play with you one day."
        m 5rubsa "One day..."
        return
