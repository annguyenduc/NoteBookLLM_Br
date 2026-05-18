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
  verify_range: [68, 74]
  verify_range_source: "frontmatter"
  verify_manifest_range: [68, 74]
---

# HD SOURCE: ARCH_Thinking_in_Systems_CH02_SEC01_P02_P068-074
Source PDF: ARCH_Thinking_in_Systems.pdf
Extracted Images: 8
Structure Mode: chapter>section>page
Chunk Unit ID: CH02_SEC01_P02
Part Title: PART ONE System Structure and Behavior
Chapter Title: Chapter Two A Brief Visit to the Systems Zoo
Section Title: One-Stock Systems
Chunk Range: Pages 68 to 74
Manifest File: RAW_2026-05-18_ARCH_Thinking_in_Systems_MANIFEST.md
---

and having more babies and dying. But from a systems point of view these systems, so dissimilar in many ways, have one important thing in common: their feedback-loop structures. Both have a stock governed by a reinforcing growth loop and a balancing death loop. Both also have an aging process. Steel mills and lathes and turbines get older and die just as people do.

One of the central insights of systems theory, as central as the observation  that  systems  largely  cause  their  own  behavior,  is  that  systems  with similar feedback structures produce similar dynamic behaviors, even if the outward appearance of these systems is completely dissimilar.

A population is nothing like an industrial economy, except that both can reproduce themselves out of themselves and thus grow exponentially. And both age and die. A coffee cup cooling is like a warmed room cooling, and like a radioactive substance decaying, and like a population or industrial economy aging and dying. Each declines as the result of a balancing feedback loop.

## A System with Delays-Business Inventory

Picture a stock of inventory in a store-a car dealership-with an infl  ow of deliveries from factories and an outfl  ow of new car sales. By itself, this stock of cars on the dealership lot would behave like the water in a bathtub.

Figure 29. Inventory at a car dealership is kept steady by two competing balancing loops, one through sales and  one through deliveries.


![[RAW_2026-05-18_ARCH_Thinking_in_Systems_CH02_SEC01_P02_P068-074_fig_00.png]]


Now picture a regulatory feedback system designed to keep the inventory high enough so that it can always cover ten days' worth of sales (see Figure 29). The car dealer needs to keep some inventory because deliveries and purchases don't match perfectly every day. Customers make purchases that are unpredictable on a day-to-day basis. The car dealer also needs to provide herself with some extra inventory (a buffer) in case deliveries from suppliers are delayed occasionally.

The dealer monitors sales (perceived sales), and if, for example, they seem to be rising, she adjusts orders to the factory to bring inventory up to her new desired inventory that provides ten days' coverage at the higher sales rate. So, higher sales mean higher perceived sales, which means a higher discrepancy between inventory and desired inventory, which means higher orders, which will bring in more deliveries, which will raise inventory so it can comfortably supply the higher rate of sales.

This system is a version of the thermostat system-one balancing loop of sales draining the inventory stock and a competing balancing loop maintaining the inventory by resupplying what is lost in sales. Figure 30 shows the not very surprising result of an increase in consumer demand of 10 percent.

In Figure 31, I am putting something else into this simple model-three delays that are typical of what we experience in the real world.

First, there is a perception delay, intentional in this case. The car dealer doesn't react to just any blip in sales. Before she makes ordering decisions, she averages sales over the past fi  ve days to sort out real trends from temporary dips and spikes.

Figure  30. Inventory  on  the  car  dealership's  lot  with  a  permanent  10-percent  increase  in consumer demand starting on day 25.


![[RAW_2026-05-18_ARCH_Thinking_in_Systems_CH02_SEC01_P02_P068-074_fig_01.png]]


Figure 31. Inventory at a car dealership with three common delays now included in the picture-a perception delay, a response delay, and a delivery delay.


![[RAW_2026-05-18_ARCH_Thinking_in_Systems_CH02_SEC01_P02_P068-074_fig_02.png]]


Second, there is a response delay. Even when it's clear that orders need to be adjusted, she doesn't try to make up the whole adjustment in a single order.  Rather,  she  makes  up  one-third  of  any  shortfall  with  each  order. Another way of saying that is, she makes partial adjustments over three days to be extra sure the trend is real. Third, there is a delivery delay. It takes fi   ve days for the supplier at the factory to receive an order, process it, and deliver it to the dealership.

Figure 32. Response of inventory to a 10-percent increase in sales when there are delays in the system.


![[RAW_2026-05-18_ARCH_Thinking_in_Systems_CH02_SEC01_P02_P068-074_fig_03.png]]


Although  this  system  still  consists  of  just  two  balancing  loops,  like the simplifi  ed thermostat system, it doesn't behave like the thermostat system. Look at what happens, for example, as shown in Figure 32, when the business experiences the same permanent 10-percent jump in sales from an increase in customer demand.

Oscillations! A single step up in sales causes inventory to drop. The car dealer watches long enough to be sure the higher sales rate is going to last. Then she begins to order more cars to both cover the new rate of sales and bring the inventory up. But it takes time for the orders to come in. During that time inventory drops further, so orders have to go up a little more, to bring inventory back up to ten days' coverage.

Eventually,  the  larger  volume  of  orders  starts  arriving,  and  inventory recovers-and more than recovers, because during the time of uncertainty about the actual trend, the owner has ordered too much. She now sees her mistake, and cuts back, but there are still high past orders coming in, so she orders even less. In fact, almost inevitably, since she still can't be sure of what is going to happen next, she orders too little. Inventory gets too low again. And so forth, through a series of oscillations around the new desired  inventory  level. As  Figure  33  illustrates,  what  a  difference  a  few delays make!

We'll see in a moment that there are ways to damp these oscillations in inventory, but fi  rst  it's  important  to  understand  why  they  occur.  It  isn't because the car dealer is stupid. It's because she is struggling to operate

A  delay  in  a  balancing feedback  loop  makes  a system likely to oscillate.

in  a  system  in  which  she  doesn't  have,  and  can't have,  timely  information  and  in  which  physical delays prevent her actions from having an immediate effect on inventory. She doesn't know what her customers will do next. When they do something,

she's not sure they'll keep doing it. When she issues an order, she doesn't see  an  immediate  response.  This  situation  of  information  insuffi  ciency and physical delays is very common. Oscillations like these are frequently encountered in inventories and in many other systems. Try taking a shower sometime where there's a very long pipe between the hot- and cold-water mixer and the showerhead, and you'll experience directly the joys of hot and cold oscillations because of a long response delay.

How much of a delay causes what kind of oscillation under what circum- stances is not a simple matter. I can use this inventory system to show you why.

Figure 33. The response of orders and deliveries to an increase in demand. A shows the small but sharp step up in sales on day 25 and the car dealer's 'perceived' sales, in which she averages the change over 3 days. B shows the resulting ordering pattern, tracked by the actual deliveries from the factory.


![[RAW_2026-05-18_ARCH_Thinking_in_Systems_CH02_SEC01_P02_P068-074_fig_04.png]]


'These oscillations are intolerable,' says the car dealer (who is herself a learning system, determined now to change the behavior of the inventory system). 'I'm going to shorten the delays. There's not much I can do about the delivery delay from the factory, so I'm going to react faster myself. I'll average sales trends over only two days instead of fi  ve before I make order adjustments.'

Figure 34 illustrates what happens when the dealer's perception delay is shortened from fi  ve days to two.

Not much happens when the car dealer shortens her perception delay. If  anything  the  oscillations  in  the  inventory  of  cars  on  the  lot  are  a  bit worse. And if, instead of shortening her perception time, the car dealer tries shortening her reaction time-making up perceived shortfalls in two days instead of three-things get very much worse, as shown in Figure 35.

Something has to change and, since this system has a learning person within  it,  something  will  change. 'High  leverage,  wrong  direction,'  the system-thinking car dealer says to herself as she watches this failure of a policy intended to stabilize the oscillations. This perverse kind of result can be seen all the time-someone trying to fi  x a system is attracted intuitively to a policy lever that in fact does have a strong effect on the system. And then the well-intentioned fi  xer pulls the lever in the wrong direction! This is  just  one  example of how we can be surprised by the counterintuitive behavior of systems when we start trying to change them.

Figure 34. The response of inventory to the same increase in demand with a shortened perception delay.


![[RAW_2026-05-18_ARCH_Thinking_in_Systems_CH02_SEC01_P02_P068-074_fig_05.png]]


Figure 35. The response of inventory to the same increase in demand with a shortened reaction time. Acting faster makes the oscillations worse!


![[RAW_2026-05-18_ARCH_Thinking_in_Systems_CH02_SEC01_P02_P068-074_fig_06.png]]


Part of the problem here is that the car dealer has been reacting not too

slowly, but too quickly. Given the confi  guration of this system, she has been

overreacting. Things would go better if, instead of decreasing her response

delay from three days to two, she would increase the delay from three days to six, as illustrated in Figure 36.

As Figure 36 shows, the oscillations are greatly damped with this change, and the system fi  nds its new equilibrium fairly effi  ciently.

The most important delay in this system is the one that is not under the direct control of the car dealer. It's the delay in delivery from the factory. But even without the ability to change that part of her system, the dealer can learn to manage inventory quite well.

Delays are pervasive in systems, and  they  are  strong  determinants  of  behavior. Changing the length of a delay may (or may  not,  depending  on  the type  of  delay  and  the  relative lengths of other delays) make a large change in the behavior of a system.

Figure 36. The response of inventory to the same increase in demand with a slowed reaction time.


![[RAW_2026-05-18_ARCH_Thinking_in_Systems_CH02_SEC01_P02_P068-074_fig_07.png]]
