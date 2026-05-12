---
audit:
  score: 1.00
  date: "2026-05-12"
  status: "PASSED"
  auditor: "v1.0"
  verify_result: "SKIPPED"
  verify_gaps: []
---

# HD SOURCE: ARCH_Thinking_in_Systems_CHUNK_15_P211-225
Source PDF: ARCH_Thinking_in_Systems.pdf
Extracted Images: 8
Chunk Range: Pages 211 to 225
---

## Places to Intervene in a System (in increasing order of eff   ectiveness)

12. Numbers: Constants  and  parameters  such  as  subsidies,  taxes,  and
2. standards
11. Buffers: The sizes of stabilizing stocks relative to their fl  ows
10. Stock-and-Flow  Structures: Physical  systems  and  their  nodes  of intersection
9. Delays: The lengths of time relative to the rates of system changes
8.   Balancing Feedback Loops: The strength of the feedbacks relative to the impacts they are trying to correct
7.   Reinforcing  Feedback  Loops: The  strength  of  the  gain  of  driving loops
6.   Information  Flows: The  structure  of  who  does  and  does  not  have access to information
5. Rules: Incentives, punishments, constraints
4.   Self-Organization: The  power  to  add,  change,  or  evolve  system structure
3. Goals: The purpose of the system
2.   Paradigms: The mind-set out of which the system-its goals, structure, rules, delays, parameters-arises
1. Transcending Paradigms

## Guidelines for Living in a World of Systems

1. Get the beat of the system.
2. Expose your mental models to the light of day.
3. Honor, respect, and distribute information.
4. Use language with care and enrich it with systems concepts.
5. Pay attention to what is important, not just what is quantifi  able.
6. Make feedback policies for feedback systems.
7. Go for the good of the whole.
8. Listen to the wisdom of the system.
9. Locate responsibility within the system.
10. Stay humble-stay a learner.
11. Celebrate complexity.

12. Expand time horizons.
13. Defy the disciplines.
14. Expand the boundary of caring.
15. Don't erode the goal of goodness.

## Model Equations

There  is  much  to  be  learned  about  systems  without  using  a  computer. However, once you have started to explore the behavior of even very simple systems, you may well fi  nd that you wish to learn more about building your  own  formal  mathematical  models  of  systems.  The  models  in  this book were originally developed using STELLA modeling software, by isee systems Inc. (formerly High Performance Systems). The equations in this section are written to be easily translated into various modeling software, such as Vensim by Ventana Systems Inc. as well as STELLA and iThink by isee systems Inc.

The  following  model  equations  are  those  used  for  the  nine  dynamic models discussed in chapters 1 and 2. 'Converters' can be constants or calculations based on other elements of the system model. Time is abbreviated (t) and the change in time from one calculation to the next, the time interval, is noted as (dt).

## Chapter One

## Bathtub -for Figures 5, 6 and 7

Stock: water in tub(t) = water in tub(t - dt) + (infl  ow - outfl  ow) x dt

Initial stock value: water in tub = 50 gal

t = minutes dt = 1 minute Run time = 10 minutes Infl  ow: Outfl  ow: outfl  ow = 5 gal/min

infl  ow = 0 gal/min . . . for time 0 to 5; 5 gal/min . . . for time 6 to 10

## Coffee Cup Cooling or Warming -for Figures 10 and 11

Cooling

Stock: coffee temperature(t) = coffee temperature(t - dt) -(cooling x dt)

Initial stock value: coffee temperature = 100°C, 80°C, and 60°C . . . for three comparative model runs.

t = minutes

dt = 1 minute

Run time = 8 minutes

Outfl  ow:

cooling = discrepancy x 10%

Converters:

discrepancy = coffee temperature - room temperature

room temperature = 18°C

## Warming

Stock: coffee temperature(t) = coffee temperature(t - dt) + (heating x dt) Initial stock value: coffee temperature = 0°C, 5°C, and 10°C . . . for three comparative model runs.

t = minutes

dt = 1 minute

Run time = 8 minutes

Infl  ow:

heating = discrepancy x 10%

Converters:

discrepancy = room temperature - coffee temperature

room temperature = 18°C

## Bank Account -for Figures 12 and 13

Stock: money in bank account(t) = money in bank account(t - dt) + (interest added x dt)

Initial stock value: money in bank account = $100

t = years

dt = 1 year

Run time = 12 years

Infl  ow:

interest added ($/year) = money in bank account x interest rate

Converter: interest rate = 2%, 4%, 6%, 8%, &amp; 10% annual interest . . . for fi   ve comparative model runs.

## Chapter Two

## Thermostat -For Figures 14-20

Stock: room temperature(t) = room temperature(t - dt) + (heat from furnace - heat to outside) x dt Initial stock value: room temperature = 10°C for cold room warming; 18°C for warm room cooling t = hours dt = 1 hour Run time = 8 hours and 24 hours Infl  ow: heat from furnace =  minimum of discrepancy between desired and actual room temperature or 5

Outfl  ow: heat to outside = discrepancy between inside and outside temperature x 10% . . . for 'normal' house; discrepancy between inside and outside temperature x 30% . . . for very leaky house

Converters: thermostat setting = 18°C

discrepancy between desired and actual room temperature = maximum of ( thermostat setting -room temperature ) or 0

discrepancy between inside and outside temperature =

room temperature - 10°C . . . for constant outside temperature (Figures 16 - 18); room temperature -24-hour outside temp . . . for full day and night cycle (Figures 19 and 20)

24-hour outside temp ranges from 10°C (50°F) during the day to - 5°C (23°F) at night, as shown in graph

## Population -for Figures 21-26

Stock: population(t) = population(t - dt) + ( births -deaths ) x dt Initial stock value: population = 6.6 billion people t = years


![[RAW_2026-05-11_ARCH_Thinking_in_Systems_CHUNK_15_P211-225_fig_00.png]]


dt = 1 year

Run time = 100 years

Infl  ow:

births = population x fertility

Outfl  ow:

deaths = population x mortality

Converters:

Figure 22:

mortality

= .009 . . . or 9 deaths per 1000 population

fertility = .021 . . . or 21 births per 1000 population

Figure 23:

mortality = .030

fertility = .021

Figure 24:

mortality = .009

fertility starts at .021 and falls over time to .009 as shown in graph

Figure 26:

mortality = .009

fertility starts at .021, drops to .009, but then rises .030 as shown in graph

## Capital -for Figures 27 and 28


![[RAW_2026-05-11_ARCH_Thinking_in_Systems_CHUNK_15_P211-225_fig_01.png]]


Stock: capital stock(t) = capital stock(t - dt) + ( investment -depreciation ) x dt Initial stock value: capital stock = 100

t = years

dt = 1 year


![[RAW_2026-05-11_ARCH_Thinking_in_Systems_CHUNK_15_P211-225_fig_02.png]]


Run time = 50 years

Infl  ow:

investment = annual output x investment fraction

Outfl  ow:

depreciation = capital stock / capital lifetime

Converters: annual output = capital stock x output per unit capital capital lifetime = 10 years, 15 years, and 20 years . . . for three comparative model runs.

investment fraction = 20% output per unit capital = 1/3

## Business Inventory -for Figures 29 - 36

Stock: inventory of cars on the lot(t) =

inventory of cars on the lot(t - dt) + ( deliveries - sales ) x dt

Initial stock values: inventory of cars on the lot = 200 cars

t = days

dt = 1 day

Run time = 100 days

Infl  ows: deliveries = 20 . . . for time 0 to 5; orders to factory (t - delivery delay) . . . for time 6 to 100

Outfl  ows: sales = minimum of inventory of cars on the lot or customer demand

Converters: customer demand = 20 cars per day . . . for time 0 to 25; 22 cars per day . . . for time 26 to 100

perceived sales = sales averaged over perception delay (i.e. sales smoothed over perception delay )

desired inventory = perceived sales x 10

discrepancy = desired inventory -inventory of cars on the lot

orders to factory = maximum of ( perceived sales + discrepancy

) or 0 . . . for

Figure 32;  maximum of ( perceived sales + discrepancy / response delay 0 . . . for Figures 34-36

Delays, Figure 30: perception delay = 0 response delay = 0 delivery delay = 0

Delays, Figure 32: perception delay = 5 days response delay = 3 days delivery delay = 5 days

Delays, Figure 34: = 2 days

perception delay response delay = 3 days delivery delay = 5 days

Delays, Figure 35: perception delay = 5 days response delay = 2 days delivery delay = 5 days

Delays, Figure 36: perception delay = 5 days response delay = 6 days delivery delay = 5 days

A Renewable Stock Constrained by a Non-Renewable Resource -for Figures 37-41 Stock: resource(t) = resource(t - dt) - ( extraction x dt ) Initial stock values: resource = 1000 . . . for Figures 38, 40, and 41; 1000,

) or

2000, and 4000 . . . for three comparative model runs in Figure 39 Outfl  ow: extraction = capital x yield per unit capital

t = years

dt = 1 year

Run time = 100 years

Stock: capital(t) = capital(t - dt) + ( investment -depreciation ) x dt Initial stock values: capital = 5

Infl  ow: investment = minimum of profi  t or growth goal

Outfl  ow: depreciation = capital / capital lifetime

Converters: capital lifetime = 20 years

profi  t = ( price x extraction ) - ( capital x 10%)

growth goal = capital x 10% . . . for Figures 30-40; capital x 6%, 8%, 10%, and 12% . . . . . . for four comparative model runs in Figure 40

price = 3 . . . for Figures 38, 39, and 40; for Figure 41, price starts at 1.2 when yield per unit capital is high and rises to 10 as yield per unit capital falls, as shown in graph

yield per unit capital starts at 1 when resource stock is high and falls to 0 as the resource stock declines, as shown in graph

## A Renewable Stock Constrained by a Renewable Resource -for Figures 42-45


![[RAW_2026-05-11_ARCH_Thinking_in_Systems_CHUNK_15_P211-225_fig_03.png]]



![[RAW_2026-05-11_ARCH_Thinking_in_Systems_CHUNK_15_P211-225_fig_04.png]]


Stock: resource(t) = resource(t - dt) + ( regeneration -harvest ) x dt Initial stock value: resource = 1000

Infl  ow:

regeneration = resource x regeneration rate

Outfl  ow:

harvest = capital x yield per unit capital

t = years

dt = 1 year

Run time = 100 years

Stock: capital(t) = capital(t - dt) + ( investment - depreciation ) x dt Initial stock value: capital = 5

Infl  ow:

investment = minimum of profi  t or growth goal

Outfl  ow:

depreciation = capital / capital lifetime

capital lifetime = 20

Converters: growth goal = capital x 10%

profi  t = ( price x harvest ) -capital

price starts at 1.2 when yield per unit capital is high and rises to 10 as yield per unit capital falls. This is the same non-linear relationship for price and yield as in the previous model.

regeneration rate is 0 when the resource is either fully stocked or completely depleted. In the middle of the resource range, regeneration yield per unit capital starts at 1 when the resource is fully stocked, but falls (non-linearly) as the resource stock declines. Yield per unit capital increases overall from least effi  cient in Figure 43, to slightly more effi  cient in Figure 44, to most effi  cient in Figure 45.


![[RAW_2026-05-11_ARCH_Thinking_in_Systems_CHUNK_15_P211-225_fig_05.png]]


rate peaks near 0.5.


![[RAW_2026-05-11_ARCH_Thinking_in_Systems_CHUNK_15_P211-225_fig_06.png]]



![[RAW_2026-05-11_ARCH_Thinking_in_Systems_CHUNK_15_P211-225_fig_07.png]]


## Introduction

1. Russell Ackoff, 'The Future of Operational Research Is Past,' Journal of the Operational Research Society 30, no. 2 (February 1979): 93-104.
2. Idries Shah, Tales of the Dervishes (New York: E. P. Dutton, 1970), 25.

## Chapter One

1. Poul Anderson, quoted in Arthur Koestler, The Ghost in the Machine (New York: Macmillan, 1968), 59.
2. Ramon Margalef, 'Perspectives in Ecological Theory,' Co-Evolution Quarterly (Summer 1975), 49.
3. Jay W. Forrester, Industrial Dynamics (Cambridge, MA: The MIT Press, 1961), 15.
4. Honoré Balzac, quoted in George P. Richardson, Feedback Thought in Social Science and Systems Theory (Philadelphia: University of Pennsylvania Press, 1991), 54.
5. Jan Tinbergen, quoted in ibid, 44.

## Chapter Two

1. Albert Einstein, 'On the Method of Theoretical Physics,' The Herbert Spencer Lecture, delivered at Oxford (10 June 1933); also published in Philosophy of Science 1, no. 2 (April 1934): 163-69.
2. The concept of a 'systems zoo' was invented by Prof. Hartmut Bossel of the University of Kassel in Germany. His three recent 'System Zoo' books contain system descriptions and simulation-model documentations of more than 100 'animals,' some of which are included in modifi  ed form here. Hartmut Bossel, System Zoo Simulation Models - Vol. 1: Elementary Systems, Physics, Engineering; Vol. 2: Climate, Ecosystems, Resources; Vol. 3: Economy, Society, Development. (Norderstedt, Germany: Books on Demand, 2007).
3. For a more complete model, see the chapter 'Population Sector' in Dennis L. Meadows et al., Dynamics of Growth in a Finite World, (Cambridge MA: Wright-Allen Press, 1974).
4. For an example, see Chapter 2 in Donella Meadows, Jørgen Randers, and Dennis Meadows, Limits to Growth: The 30-Year Update (White River Junction, VT: Chelsea Green Publishing Co., 2004).
5. Jay W. Forrester, 1989. 'The System Dynamics National Model: Macrobehavior from Microstructure,' in P. M. Milling and E. O. K. Zahn, eds., Computer-Based Management of Complex Systems: International System Dynamics Conference (Berlin: Springer-Verlag, 1989).

## Notes