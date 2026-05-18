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
  verify_range: [53, 67]
  verify_range_source: "frontmatter"
  verify_manifest_range: [53, 67]
---

# HD SOURCE: ARCH_Thinking_in_Systems_CH02_SEC01_P01_P053-067
Source PDF: ARCH_Thinking_in_Systems.pdf
Extracted Images: 14
Structure Mode: chapter>section>page
Chunk Unit ID: CH02_SEC01_P01
Part Title: PART ONE System Structure and Behavior
Chapter Title: Chapter Two A Brief Visit to the Systems Zoo
Section Title: One-Stock Systems
Chunk Range: Pages 53 to 67
Manifest File: RAW_2026-05-18_ARCH_Thinking_in_Systems_MANIFEST.md
---

## One-Stock Systems

A Stock with T wo Competing Balancing Loops-a Thermostat You already have seen the 'homing in' behavior of the goal-seeking balancing feedback loop-the coffee cup cooling. What happens if there are two such loops, trying to drag a single stock toward two different goals?

One example of such a system is the thermostat mechanism that regulates  the  heating  of  your  room  (or  cooling,  if  it  is  connected  to  an  air conditioner instead of a furnace). Like all models, the representation of a thermostat in Figure 15 is a simplifi  cation of a real home heating system.

Figure 15. Room temperature regulated by a thermostat and furnace.


![[RAW_2026-05-18_ARCH_Thinking_in_Systems_CH02_SEC01_P01_P053-067_fig_00.png]]


Whenever the room temperature falls below the thermostat setting, the thermostat detects a discrepancy and sends a signal that turns on the heat fl   ow  from the furnace, warming the room. When the room temperature rises again, the thermostat turns off the heat fl  ow. This straightforward, stock-maintaining, balancing feedback loop is shown on the left side of Figure 15. If there were nothing else in the system, and if you start with a  cold  room with the thermostat set at 18°C (65°F), it would behave as shown in Figure 16. The furnace comes on, and the room warms up. When the room temperature reaches the thermostat setting, the furnace goes off, and the room stays right at the target temperature.

However, this is not the only loop in the system. Heat also leaks to the outside. The outfl  ow of heat is governed by the second balancing feedback loop, shown on the right side of Figure 15. It is always trying to make the room temperature equal to the outside, just like a coffee cup cooling. If this were the only loop in the system (if there were no furnace), Figure 17 shows what would happen, starting with a warm room on a cold day.

Figure 16. A cold room warms quickly to the thermostat setting.


![[RAW_2026-05-18_ARCH_Thinking_in_Systems_CH02_SEC01_P01_P053-067_fig_01.png]]


Figure 17. A warm room cools very slowly to the outside temperature of 10°C.


![[RAW_2026-05-18_ARCH_Thinking_in_Systems_CH02_SEC01_P01_P053-067_fig_02.png]]


The assumption is that room insulation is not perfect, and so some heat leaks out of the warm room to the cool outdoors. The better the insulation, the slower the drop in temperature would be.

Now,  what  happens  when  these  two  loops  operate  at  the  same  time? Assuming that there is suffi  cient insulation and a properly sized furnace, the  heating  loop  dominates  the  cooling  loop. You  end  up  with  a  warm room (see Figure 18), even starting with a cold room on a cold day.

Figure 18. The furnace warms a cool room, even as heat continues to leak from the room.


![[RAW_2026-05-18_ARCH_Thinking_in_Systems_CH02_SEC01_P01_P053-067_fig_03.png]]


As the room heats up, the heat fl  owing out of it increases, because there's a  larger  gap  between  inside  and  outside  temperatures.  But  the  furnace keeps putting in more heat than the amount that leaks out, so the room warms nearly to the target temperature. At that point, the furnace cycles off and on as it compensates for the heat constantly fl  owing out of the room.

The thermostat is set  at  18°C  (65°F)  in  this  simulation,  but  the  room temperature levels off slightly below 18°C (65°F). That's because of the leak to the outside, which is draining away some heat even as the furnace is getting the signal to put it back. This is a characteristic and sometimes surprising behavior of a system with competing balancing loops. It's like trying to keep a bucket full when there's a hole in the bottom. To make things worse, water leaking out of the hole is governed by a feedback loop; the more water in the bucket, the more the water pressure at the hole increases, so the fl  ow out increases! In this case, we are trying to keep the room warmer than the outside and the warmer the room is, the faster it loses heat to the outside. It takes time for the furnace to correct for the increased heat loss-and in that minute still more heat leaks out. In a well-insulated house, the leak will be slower and so the house more comfortable than a poorly insulated one, even a poorly insulated house with a big furnace.

With home heating systems, people have learned to set the thermostat slightly higher than the actual temperature they are aiming at. Exactly how much higher can be a tricky question, because the outfl  ow rate is higher on cold days than on warm days. But for thermostats this control problem isn't serious. Y ou can muddle your way to a thermostat setting you can live with.

For other systems with this same structure of competing balancing loops, the fact that the stock goes on changing while you're trying to control it can create real problems. For example, suppose you're trying to maintain a store inventory at a certain level. You can't instantly order new stock to make up an immediately apparent shortfall. If you don't account for the goods that will be sold while you are waiting for the order to come in, your inventory will never be quite high enough. You can be fooled in the same way if you're trying to maintain a cash balance at a certain level, or the level of water in a reservoir, or the concentration of a chemical in a continuously fl   owing reaction system.

There's an important general principle here, and also one specifi  c to the thermostat structure. First the general one: The information delivered by a feedback loop can only affect future behavior; it can't deliver the information, and so can't have an impact fast enough to correct behavior that drove the current feedback. A person in the system who makes a decision based on the feedback can't change the behavior of the system that drove the

current  feedback;  the  decisions  he  or  she  makes will affect only future behavior.

Why is that important? Because it means there will  always  be  delays  in  responding.  It  says  that a fl  ow can't react instantly to a fl  ow. It can react only to a change in a stock, and only after a slight delay to register the incoming information. In the bathtub, it takes a split second of time to assess the depth of the water and decide to adjust the fl  ows. Many  economic  models  make  a  mistake  in  this matter by assuming that consumption or production can respond immediately, say, to a change in The information delivered by a feedback loop-even nonphysical feedbackcan only aff   ect future behavior;  it  can't  deliver a  signal  fast  enough  to correct behavior that drove  the  current  feedback. Even nonphysical information  takes  time  to feedback into the system.

price.  That's  one  of  the  reasons  why  real  economies tend not to behave exactly like many economic models.

The specifi  c principle you can deduce from this simple system is that you must remember in thermostat-like systems to take into account whatever draining or fi  lling processes are going on. If you don't, you won't achieve the target level of your stock. If you want your room temperature to be at  18°C (65°F), you have to set the thermostat a little above the desired temperature. If you want to pay off your credit card (or the national debt), you have to raise your repayment rate high enough to cover the charges you  incur  while  you're  paying  (including  interest).  If  you're  gearing  up your work force to a higher level, you have to hire fast enough to correct for A  stock-maintaining  balancing feedback loop must have its goal set appropriately to  compensate  for  draining or  infl  owing  processes  that aff   ect that stock. Otherwise, the feedback process will fall short of or exceed the target for the stock.

those who quit while you are hiring. In other words, your mental model of the system needs to include all the important fl  ows, or you will be surprised by the system's behavior.

Before we leave the thermostat, we should see how it behaves with a varying outside temperature.  Figure  19  shows  a  twenty-four-hour period  of  normal  operation  of  a  well-functioning  thermostat  system,  with  the  outside temperature dipping well below freezing. The

infl  ow  of  heat  from  the  furnace nicely tracks the outfl  ow of heat to the outside. The temperature in the room varies hardly at all once the room has warmed up.

Every  balancing  feedback  loop  has  its  breakdown  point,  where  other loops pull the stock away from its goal more strongly than it can pull back. That can happen in this simulated thermostat system, if I weaken the power of the heating loop (a smaller furnace that cannot put out as much heat), or if I strengthen the power of the cooling loop (colder outside tempera- ture, less insulation, or larger leaks). Figure 20 shows what happens with the same outside temperatures as in Figure 19, but with faster heat loss from the room. At very cold temperatures, the furnace just can't keep up with the heat drain. The loop that is trying to bring the room temperature down to the outside temperature dominates the system for a while. The room gets pretty uncomfortable!

Figure 19. The furnace warms a cool room, even as heat leaks from the room and outside temperatures drop below freezing.


![[RAW_2026-05-18_ARCH_Thinking_in_Systems_CH02_SEC01_P01_P053-067_fig_04.png]]


Figure 20. On a cold day, the furnace can't keep the room warm in this leaky house!


![[RAW_2026-05-18_ARCH_Thinking_in_Systems_CH02_SEC01_P01_P053-067_fig_05.png]]


See if you can follow, as time unfolds, how the variables in Figure 20 relate  to  one  another. At  fi  rst,  both  the  room  and  the  outside  temperatures are cool. The infl  ow of heat from the furnace exceeds the leak to the outside, and the room warms up. For an hour or two, the outside is mild enough that the furnace replaces most of the heat that's lost to the outside, and the room temperature stays near the desired temperature.

But  as  the  outside  temperature  falls  and  the  heat  leak  increases,  the furnace cannot replace the heat fast enough. Because the furnace is generating less heat than is leaking out, the room temperature falls. Finally, the outside temperature rises again, the heat leak slows, and the furnace, still operating at full tilt, fi  nally  can  pull  ahead and start to warm the room again.

Just as in the rules for the bathtub, whenever the furnace is putting in more  heat  than  is  leaking  out,  the  room  temperature  rises.  Whenever the infl  ow rate falls behind the outfl  ow rate, the temperature falls. If you study the system changes on this graph for a while and relate them to the feedback-loop diagram of this system, you'll get a good sense of how the structural  interconnections  of  this  system-its  two  feedback  loops  and how they shift in strength relative to each other-lead to the unfolding of the system's behavior over time.

## A Stock with One Reinforcing Loop and One Balancing Loop-Population and

## Industrial Economy

What happens when a reinforcing and a balancing loop are both pulling on the same stock? This is one of the most common and important system structures. Among other things, it describes every living population and every economy.

Figure 21. Population governed by a reinforcing loop of births and a balancing loop of deaths.


![[RAW_2026-05-18_ARCH_Thinking_in_Systems_CH02_SEC01_P01_P053-067_fig_06.png]]


A population has a reinforcing loop causing it to grow through its birth rate, and a balancing loop causing it to die off through its death rate.

As long as fertility and mortality are constant (which in real systems they rarely are), this system has a simple behavior. It grows exponentially or  dies  off,  depending  on  whether  its  reinforcing  feedback  loop  determining births is stronger than its balancing feedback loop determining deaths.

For example, the 2007 world population of 6.6 billion people had a fertility rate of roughly 21 births a year for every 1,000 people in the population. Its mortality rate was 9 deaths a year out of every 1,000 people. Fertility was higher than mortality, so the reinforcing loop dominated the system. If  those  fertility  and  mortality  rates  continue  unchanged,  a  child  born now will see the world population more than double by the time he or she reaches the age of 60, as shown in Figure 22.

Figure 22. Population growth if fertility and mortality maintain their 2007 levels of 21 births and nine deaths per 1,000 people.


![[RAW_2026-05-18_ARCH_Thinking_in_Systems_CH02_SEC01_P01_P053-067_fig_07.png]]


If, because of a terrible disease, the mortality rate were higher, say at 30 deaths per 1,000, while the fertility rate remained at 21, then the death loop

Figure 23. Population decline if fertility remains at 2007 level (21 births per 1,000) but mortality is much higher, 30 deaths per 1,000.


![[RAW_2026-05-18_ARCH_Thinking_in_Systems_CH02_SEC01_P01_P053-067_fig_08.png]]


would dominate the system. More people would die each year than would be born, and the population would gradually decrease (Figure 23).

Things  get  more  interesting  when  fertility  and  mortality  change  over time. When the United Nations makes long-range population projections, it  generally  assumes  that,  as  countries  become  more  developed,  average fertility  will  decline  (approaching  replacement  where  on  average  each woman has 1.85  children).  Until  recently,  assumptions  about  mortality were that it would also decline, but more slowly (because it is already low in most parts of the world). However, because of the epidemic of HIV/ AIDS, the UN now assumes the trend of increasing life expectancy over the next fi  fty years will slow in regions affected by HIV/AIDS.

Changing fl  ows (fertility and mortality) create a change in the behavior over time of the stock (population)-the line bends. If, for example, world fertility falls steadily to equal mortality by the year 2035 and they both stay

Figure 24. Population stabilizes when fertility equals mortality.


![[RAW_2026-05-18_ARCH_Thinking_in_Systems_CH02_SEC01_P01_P053-067_fig_09.png]]


constant thereafter, the population will level off, births exactly balancing deaths in dynamic equilibrium, as in Figure 24.

This behavior is an example of shifting dominance of  feedback loops. Dominance is an important concept in systems thinking. When one loop dominates another, it has a stronger impact on behavior. Because systems often  have  several  competing  feedback  loops  operating  simultaneously, those loops that dominate the system will determine the behavior.

At fi  rst,  when fertility is higher than mortality, the reinforcing growth loop  dominates  the  system  and  the  resulting  behavior  is  exponential growth.  But  that  loop  is  gradually  weakened  as  fertility  falls.  Finally,  it exactly equals the strength of the balancing loop of mortality. At that point neither loop dominates, and we have dynamic equilibrium.

You  saw  shifting  dominance  in  the  thermostat  system,  when  the  outside  temperature  fell and the heat leaking out of the poorly insulated house  overwhelmed  the  ability  of  the  furnace to  put  heat  into  the  room.  Dominance shifted from the heating loop to the cooling loop.

There  are  only  a  few  ways  a  population system could behave, and these depend on what

happens to the 'driving' variables, fertility and mortality. These are the only ones possible for a simple system of one reinforcing and one balancing loop. A stock governed by linked reinforcing and balancing loops will grow exponentially if the reinforcing loop dominates the balancing one. It will die off if the balancing loop dominates the reinforcing one. It will level off if the two loops are of equal strength (see Figure 25). Or it will do a sequence of these things, one after another, if the relative strengths of the two loops change over time (see Figure 26).

I chose some provocative population scenarios here to illustrate a point about  models  and  the  scenarios  they  can  generate.  Whenever  you  are confronted with a scenario (and you are, every time you hear about an economic prediction, a corporate budget, a weather forecast, future climate change, a stockbroker saying what is going to happen to a particular holding),  there  are  questions you need to ask that will help you decide how good a representation of reality is the underlying model.

-   Are the driving factors likely to unfold this way? (What are birth rate and death rate likely to do?)
-   If they did, would the system react this way? (Do birth and death rates really cause the population stock to behave as we think it will?)
-   What is driving the driving factors? (What affects birth rate? What affects death rate?)

The fi  rst question can't be answered factually. It's a guess about the future, and the future is  inherently  uncertain. Although  you  may  have  a  strong

Complex behaviors of systems  often  arise  as  the relative  strengths  of  feedback loops shift, causing fi  rst one loop and then another to dominate behavior.

Figure 25. Three possible behaviors of a population: growth, decline, and stabilization.


![[RAW_2026-05-18_ARCH_Thinking_in_Systems_CH02_SEC01_P01_P053-067_fig_10.png]]


opinion about it, there's no way to prove you're right until the future actually happens. A systems analysis can test a number of scenarios to see what happens if the driving factors do different things. That's usually one purpose of a systems analysis. But you have to be the judge of which scenario, if any, should be taken seriously as a future that might really be possible.

Figure 26. Shifting dominance of fertility and mortality loops.


![[RAW_2026-05-18_ARCH_Thinking_in_Systems_CH02_SEC01_P01_P053-067_fig_11.png]]


Dynamic systems studies usually are not designed to predict what will happen. Rather, they're designed to explore what would happen , if a number of driving factors unfold in a range of different ways.

The second question-whether the system really will react this way-is more scientifi  c. It's a question about how good the model is. Does it capture the inherent dynamics of the system? Regardless of whether you think the

driving  factors will do  that, would  the  system behave like that if they did?

In  the  population  scenarios  above,  however likely  you  think  they  are,  the  answer  to  this second question is roughly yes, the population System dynamics models explore possible futures and ask 'what if' questions.

would behave like this, if the fertility and mortality did that. The population model I have used here is very simple. A more detailed model would distinguish age groups, for example. But basically this model responds the way a real population would, growing under the conditions when a real

## QUESTIONS FOR TESTING THE VALUE OF A MODEL

1. Are the driving factors likely to unfold this way?
2. If they did, would the system react this way?
3. What is driving the driving factors?

Model utility depends not on whether its driving scenarios  are realistic (since no one can know that for  sure),  but  on  whether it  responds  with  a  realistic pattern of behavior.

system.

Is there anything about the size of the population, for instance, that might feed back to infl  uence fertility or mortality? Do other factors-economics, the environment, social trends-infl  uence fertility and mortality? Does the size of the population affect those economic and environmental and social factors?

Of course, the answer to all of these questions is yes. Fertility and mortality  are  governed by feedback loops too. At least some of those feedback loops are themselves affected by the size of the population. This population 'animal' is only one piece of a much larger system. 3

One important piece of the larger system that affects population is the economy. At the heart of the economy is another reinforcing-loop-plusbalancing-loop system-the same kind of structure, with the same kinds

Figure 27. Like  a  living  population,  economic  capital  has  a  reinforcing  loop  (investment  of output) governing growth and a balancing loop (depreciation) governing decline.


![[RAW_2026-05-18_ARCH_Thinking_in_Systems_CH02_SEC01_P01_P053-067_fig_12.png]]


population  would  grow,  declining  when  a  real population would decline. The numbers are off, but the basic behavior pattern is realistic.

Finally,  there  is  the  third  question.  What  is driving the driving factors? What is adjusting the infl  ows  and  outfl  ows?  This  is  a  question  about system  boundaries.  It  requires  a  hard  look  at those  driving  factors  to  see  if  they  are  actually independent, or if they are also embedded in the of behavior, as the population (see Figure 27).

The greater the stock of physical capital (machines and factories) in the economy and the effi  ciency of production (output per unit of capital), the more output (goods and services) can be produced each year.

The more output that is produced, the more can be invested to make new capital. This is a reinforcing loop, like the birth loop for a population. The investment fraction is equivalent to the fertility. The greater the fraction of its output a society invests, the faster its capital stock will grow.

Physical capital is drained by depreciation-obsolescence and wearingout. The balancing loop controlling depreciation is equivalent to the death loop in a population. The 'mortality' of capital is determined by the average  capital  lifetime.  The  longer  the  lifetime,  the  smaller  the  fraction  of capital that must be retired and replaced each year.

If this system has the same structure as the population system, it must have the same repertoire of behaviors. Over recent history world capital, like world population, has been dominated by its reinforcing loop and has been growing exponentially. Whether in the future it grows or stays constant or dies off depends on whether its reinforcing growth loop remains stronger than its balancing depreciation loop. That depends on

-   the investment fraction-how much output the society invests rather than consumes,
-   the effi  ciency of capital-how much capital it takes to produce a given amount of output, and
- the average capital lifetime.

If a constant fraction of output is reinvested in the capital stock and the effi  ciency of that capital (its ability to produce output) is also constant, the capital stock may decline, stay constant, or grow, depending on the lifetime of the capital. The lines in Figure 28 show systems with different average capital lifetimes. With a relatively short lifetime, the capital wears out faster than it is replaced. Reinvestment does not keep up with depreciation and the economy slowly declines. When depreciation just balances investment, the economy is in dynamic equilibrium. With a long lifetime, the capital stock grows exponentially. The longer the lifetime of capital, the faster it grows.

This is another example of a principle we've already encountered: You can make a stock grow by decreasing its outfl  ow rate as well as by increas-

Figure 28. Growth in capital stock with changes in the lifetime of the capital. In a system with output per unit capital ratio of 1:3 and an investment fraction of 20 percent, capital with a lifetime of 15 years just keeps up with depreciation. A shorter lifetime leads to a declining stock of capital.


![[RAW_2026-05-18_ARCH_Thinking_in_Systems_CH02_SEC01_P01_P053-067_fig_13.png]]


## ing its infl  ow rate!

Just  as  many factors infl  uence the fertility and mortality of a population, so many factors infl  uence the output ratio, investment fraction, and the lifetime of capital-interest rates, technology, tax policy, consumption habits, and prices, to name just a few. Population itself infl  uences investment, both by contributing labor to output, and by increasing demands on consumption, thereby decreasing the investment fraction. Economic output  also  feeds  back  to  infl  uence  population  in  many  ways.  A  richer economy usually has better health care and a lower death rate. A richer economy also usually has a lower birth rate.

In fact, just about any long-term model of a real economy should link together the two structures of population and capital to show how they affect each other. The central question of economic development is how to keep the reinforcing loop of capital accumulation from growing more slowly than the reinforcing loop of population growth-so that people are

Systems with similar feedback structures produce similar dynamic behaviors.

getting richer instead of poorer. 4

It may seem strange to you that I call the capital system the same kind of 'zoo animal' as the population system. A production system with factories and shipments and economic fl  ows doesn't look

much like a population system with babies being born and people aging