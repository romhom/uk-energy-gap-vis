The response to my last post on UK temperature stripes was great, so I thought I'd try something similar in the two sectors I've spent most of my career in: nuclear and offshore wind. At FNC I worked on keeping the AGR fleet running, combining operational data with physical modelling to support the safety case work behind it. More recently I've been working with the Crown Estate on optimising offshore renewables.

It grew into something a bit different to what I'd planned!

UK energy data is scattered across DESNZ, DUKES, and NESO in a dozen different tables, each with its own conventions, and my AI friend and I ended up doing a fair bit of jiggery pokery to get everything to line up properly. Wasn't as easy as I thought going in, but I think we got there in the end.

Between us we pulled together generation, capacity, and grid constraint/curtailment cost data stretching back to 2000, right through to today. Here's what it shows:

UK generation has transformed since 2000. Coal's essentially gone, and offshore wind has gone from nothing to one of the largest single sources on the system. Nuclear's been dropping off too, as the Magnox and AGR fleet retires (graphite core ageing, my old FNC specialist subject!) faster than new build is coming online to replace it.

Gas capacity has barely moved, but it's sitting idle more and more. Some of that's down to wind growth in recent years, but a chunk of the early-2000s gap predates wind entirely, just gas capacity outpacing flat demand.

The cost of the wind-to-gas handover has climbed sharply since 2017, broadly tracking wind's growth. We're paying to curtail the wind, separately paying to keep gas plants idling as backup, and paying even more again to fire them up at short notice. I found good data for the curtailment cost, but didn't have time to wrangle gas auction prices into a usable dataset to plot the other side properly.

A key problem I think is wider co-ordination of big interconnected infrastructure. Good interconnectors are needed to get power from where it's generated to where it's used, and that build hasn't kept pace. For example, Eastern Green Link 2 is on schedule, but it's still a five-year build from construction starting in 2024 to going live in 2029. And on the equivalent link to Wales, the Western Link, National Grid and Scottish Power were fined £158m by Ofgem over a two-year delay [https://www.ofgem.gov.uk/press-release/ps158-million-redress-two-year-delay-major-western-link-subsea-cable].

Early investment in combined scenario and cost modelling in the presence of deep uncertainties would have shown these impacts in advance and, if well presented, highlighted the longer term risks much earlier.

Full dataset and the code behind these charts are on GitHub [link] if you fancy a dig around yourself.
