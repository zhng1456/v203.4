#   [Job Adv] (Lv.30)   Becoming a Blade Acolyte
sm.setSpeakerID(1056000)
if sm.hasQuest(parentID):
    if sm.canHold(1052244):
        sm.giveItem(1052244)
        sm.setJob(431)
        sm.addSP(3, True)
        sm.completeQuest(parentID)
    else:
        sm.sendSay("Empty one or more Equip slots before you can advance to Blade Acolyte.")
        sm.dispose()