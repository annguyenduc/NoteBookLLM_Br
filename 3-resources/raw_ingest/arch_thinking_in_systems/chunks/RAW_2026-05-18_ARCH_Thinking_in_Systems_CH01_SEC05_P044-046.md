---
audit_stamp: true
audit:
  score: 1.00
  date: "2026-05-18"
  status: "PASSED"
  auditor: "v1.0"
  verify_scope: "chunk"
  verify_result: "PASS"
  verify_gaps: []
  signature: "UNSIGNED"
  verify_range: [44, 46]
  verify_range_source: "frontmatter"
  verify_manifest_range: [44, 46]
---

# HD SOURCE: ARCH_Thinking_in_Systems_CH01_SEC05_P044-046
Source PDF: ARCH_Thinking_in_Systems.pdf
Extracted Images: 3
Structure Mode: chapter>section>page
Chunk Unit ID: CH01_SEC05
Part Title: PART ONE System Structure and Behavior
Chapter Title: Chapter One The Basics
Section Title: Stabilizing Loops-Balancing Feedback
Chunk Range: Pages 44 to 46
Manifest File: RAW_2026-05-18_ARCH_Thinking_in_Systems_MANIFEST.md
---

Not all systems have feedback loops. Some systems are relatively simple open-ended chains of stocks and fl  ows. The chain may be affected by outside factors, but the levels of the chain's stocks don't affect its fl  ows. However, those systems that contain feedback loops are common and may be quite elegant or rather surprising, as we shall see.

A  feedback  loop  is  a  closed chain of causal connections from a stock, through a set of decisions  or  rules  or  physical laws or actions that are dependent on the level of the stock, and back again through a fl  ow to change the stock .

## Stabilizing Loops-Balancing Feedback

One common kind of feedback loop stabilizes the stock level, as in the checking-account  example.  The  stock  level  may  not  remain  completely fi   xed, but it does stay within an acceptable range. What follows are some more stabilizing feedback loops that may be familiar to you. These examples start to detail some of the steps within a feedback loop.

If you're a coffee drinker, when you feel your energy level run low, you may grab a cup of hot black stuff to perk you up again. You, as the coffee drinker, hold in your mind a desired stock level (energy for work). The purpose of this caffeine-delivery system is to keep your actual stock level near or at your desired level. (You may have other purposes for drinking coffee as well: enjoying the fl  avor or engaging in a social activity.) It is the gap, the discrepancy, between your actual and desired levels of energy for work that drives your decisions to adjust your daily caffeine intake.

Figure 9. Energy level of a coff  ee drinker.


![[RAW_2026-05-18_ARCH_Thinking_in_Systems_CH01_SEC05_P044-046_fig_00.png]]


Notice that the labels in Figure 9, like all the diagram labels in this book, are direction-free. The label says 'stored energy in body' not ' low energy level,'  'coffee intake' not ' more coffee.' That's because feedback loops often can operate in two directions. In this case, the feedback loop can correct an oversupply as well as an undersupply. If you drink too much coffee and fi   nd yourself bouncing around with extra energy, you'll lay off the caffeine for a while. High energy creates a discrepancy that says 'too much,' which then causes you to reduce your coffee intake until your energy level settles down. The diagram is intended to show that the loop works to drive the stock of energy in either direction.

I could have shown the infl  ow of energy coming from a cloud, but instead I  made  the  system  diagram  slightly  more  complicated. Remember-all system diagrams are simplifi  cations of the real world . We each choose how much complexity to look at. In this example, I drew another stock-the stored energy in the body that can be activated by the caffeine. I did that to indicate that there is more to the system than one simple loop. As every coffee drinker knows, caffeine is only a short-term stimulant. It lets you run your motor faster, but it doesn't refi  ll your personal fuel tank. Eventually the caffeine high wears off, leaving the body more energy-defi  cient than it  was  before.  That  drop  could  reactivate  the  feedback  loop  and  generate another trip to the coffee pot. (See the discussion of addiction later in this book.) Or it could activate some longer-term and healthier feedback responses: Eat some food, take a walk, get some sleep.

This kind of stabilizing, goal-seeking, regulating loop is called a balancing feedback loop , so I put a B inside the loop in the diagram. Balancing feedback  loops  are goal-seeking or stability-seeking .  Each  tries  to  keep  a stock at a given value or within a range of values. A balancing feedback loop opposes whatever direction of change is imposed on the system. If you push a stock too far up, a balancing loop will try to pull it back down. If you shove it too far down, a balancing loop will try to bring it back up.

Here's  another  balancing  feedback  loop  that  involves  coffee,  but  one that works through physical law rather than human decision. A hot cup of coffee will gradually cool down to room temperature. Its rate of cooling depends on the difference between the temperature of the coffee and the temperature of the room. The greater the difference, the faster the coffee will cool. The loop works the other way too-if you make iced coffee on a hot day, it will warm up until it has the same temperature as the room. The function of this system is to bring the discrepancy between coffee's temperature and room's temperature to zero, no matter what the direction of the discrepancy.

Figure 10. A cup of coff  ee cooling ( left ) or warming ( right ).


![[RAW_2026-05-18_ARCH_Thinking_in_Systems_CH01_SEC05_P044-046_fig_01.png]]


Starting with coffee at different temperatures, from just below boiling to just above freezing, the graphs in Figure 11 show what will happen to the temperature over time (if you don't drink the coffee). You can see here the 'homing' behavior of a balancing feedback loop. Whatever the initial value of the system stock (coffee temperature in this case), whether it is above or below the 'goal' (room temperature), the feedback loop brings it toward

Figure 11. Coff  ee temperature as it approaches a room temperature of 18°C.


![[RAW_2026-05-18_ARCH_Thinking_in_Systems_CH01_SEC05_P044-046_fig_02.png]]
