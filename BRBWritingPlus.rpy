init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Nabbi_brb_writing",
            category=["be right back +"],
            prompt="I'm going to do some Writing, [m_name]. (BRB+)",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label Nabbi_brb_writing:
    m 1sua "Doing some more writing?"
    m 2rua "If you don't mind me asking..."
    m 3eub "What are you writing?{nw}"
    $ _history_list.pop()
    menu:
        m "What are you writing?{fast}"

        "I'm writing a Poem.":
         m 6sub "Ooh, a poem?"
         m 2tubsu "It's not for me,{w=0.5} is it?"
         m 1hubsa "Ehehe~"
         m 3eubsa "I'm just teasing you, [player]."
         m 1hubsb "Happy Writing!"

        "I'm writing a Essay.":
         m 6eua "Got an essay to write?"
         m 3hubssdrb "Just don't wait until the last minute to finish it!"
         m 1eubsa "Happy Writing, [player]!"

        "I'm writing something for a newsletter/newspaper.":
         m 1suw "Ooh!"
         m 3esc "Hopefully your working on a story you find interesting."
         m 2rssdrp "It would suck if you had to work on something you don't have interest in."
         m 3hubsb "Well, I hope you make the front page!"
         m 1hubsa "Good luck, [player]!"

        "I'm writing a book.":
         m 3tubsu "Your not just doing it to impress me, right?"
         m 1hubsa "Ehehe~"
         m 2eubsb "I'm just teasing~"
         m 1hubsa "Anyways, I can't wait to see what you write!"
         m 3hubsb "Happy Writing, [player]!"

        "I'm updating my Diary.":
         m 1eub "Giving the diary a update?"
         m 2eua "It's always good to get your thoughts down somewhere."
         m 3rkbssdrb "Just don't forget to mention in there from time to time, ok?"
         m 1hubsa "Enjoy your writing, [player]!"

        "I'm writing something other than these options say.":
         m 1eksdrd "Oh, I'm sorry."
         m 1ekbsa "Well, it should't really affect how much you enjoy writing anyways."
         m 3hubsb "Just remember to have fun!"
         m 1hubsa "Happy Writing, [player]!"

$ mas_idle_mailbox.send_idle_cb("Nabbi_brb_writing_callback")
return "idle"

label Nabbi_brb_writing_callback:
        m 1hua "Welcome back, [player]!"
        m 3eua "I hope you had fun writing."
        m 1tubsu "...Maybe I could even get a little peak of what you wrote?"
        m 1hubsa "Ehehe~"
        return
