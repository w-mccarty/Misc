# PyRSScraper
RSS scraper with pre-tagged html output designed to be easily formatted and embedded.


**Requires:**

- Feedparser - https://pypi.org/project/feedparser/
- Unidecode - https://pypi.org/project/Unidecode/
- Eventlet - https://pypi.org/project/eventlet/
- pytz - https://pypi.org/project/pytz/
- dateutil - https://pypi.org/project/python-dateutil/
- ```mkdir /var/www/html/rss/```

**spits out html in the following format:**

from https://www.reddit.com/r/technology/hot.rss
```
<div id="rssheadlink">Reddit Technology</div><div id="rssheadupdate">Last updated: 17:02,07-18-2024</div><div id="fdiv_26_20240718182105000013" class="dfeed_day rssdiv"><div class="tfeed_day rssdate" id="rssdate_26_13">07-18</div><div class="tfeed_day rsslink" id="rsslink_26_13"><a href="https://www.reddit.com/r/technology/comments/1e6i5mu/exclusive_usps_shared_customer_postal_addresses/" target="_blank">Exclusive: USPS shared customer postal addresses with Meta, LinkedIn and Snap</a></div><br></div>
<div id="fdiv_26_2024071818152200005" class="dfeed_day rssdiv"><div class="tfeed_day rssdate" id="rssdate_26_5">07-18</div><div class="tfeed_day rsslink" id="rsslink_26_5"><a href="https://www.reddit.com/r/technology/comments/1e6i03b/teslas_california_registrations_fell_24_in_second/" target="_blank">Tesla's California registrations fell 24% in second quarter, dealer data shows</a></div><br></div>
<div id="fdiv_26_20240718180120000012" class="dfeed_day rssdiv"><div class="tfeed_day rssdate" id="rssdate_26_12">07-18</div><div class="tfeed_day rsslink" id="rsslink_26_12"><a href="https://www.reddit.com/r/technology/comments/1e6hqva/apple_breaks_silence_on_claims_it_used_swiped/" target="_blank">Apple breaks silence on claims it used 'swiped YouTube videos' to train AI</a></div><br></div>
<div id="fdiv_26_20240718171649000017" class="dfeed_day rssdiv"><div class="tfeed_day rssdate" id="rssdate_26_17">07-18</div><div class="tfeed_day rsslink" id="rsslink_26_17"><a href="https://www.reddit.com/r/technology/comments/1e6grea/with_the_selection_of_jd_vance_for_trumps_vp_we/" target="_blank">With the selection of JD Vance for Trump's VP, we should be even more worried about KOSA and other censorship bills</a></div><br></div>
<div id="fdiv_26_20240718155102000022" class="dfeed_day rssdiv"><div class="tfeed_day rssdate" id="rssdate_26_22">07-18</div><div class="tfeed_day rsslink" id="rsslink_26_22"><a href="https://www.reddit.com/r/technology/comments/1e6et48/labgrown_meat_for_pets_was_just_approved_in_the_uk/" target="_blank">Lab-Grown Meat for Pets Was Just Approved in the UK</a></div><br></div>
<div id="fdiv_26_20240718145406000025" class="dfeed_day rssdiv"><div class="tfeed_day rssdate" id="rssdate_26_25">07-18</div><div class="tfeed_day rsslink" id="rsslink_26_25"><a href="https://www.reddit.com/r/technology/comments/1e6df16/nasa_cancels_450m_viper_moon_mission_dashing_ice/" target="_blank">NASA cancels $450M Viper moon mission, dashing ice prospecting dreams</a></div><br></div>
<div id="fdiv_26_2024071814423800009" class="dfeed_day rssdiv"><div class="tfeed_day rssdate" id="rssdate_26_9">07-18</div><div class="tfeed_day rsslink" id="rsslink_26_9"><a href="https://www.reddit.com/r/technology/comments/1e6d57k/accused_of_using_algorithms_to_fix_rental_prices/" target="_blank">Accused of using algorithms to fix rental prices, RealPage goes on offensive</a></div><br></div>
<div id="fdiv_26_20240718143548000018" class="dfeed_day rssdiv"><div class="tfeed_day rssdate" id="rssdate_26_18">07-18</div><div class="tfeed_day rsslink" id="rsslink_26_18"><a href="https://www.reddit.com/r/technology/comments/1e6czg2/ford_pivots_from_ev_plans_to_heavyduty_trucks_at/" target="_blank">Ford pivots from EV plans to heavy-duty trucks at Canada facility</a></div><br></div>
<div id="fdiv_26_2024071814171900004" class="dfeed_day rssdiv"><div class="tfeed_day rssdate" id="rssdate_26_4">07-18</div><div class="tfeed_day rsslink" id="rsslink_26_4"><a href="https://www.reddit.com/r/technology/comments/1e6cjrp/amazon_is_reportedly_now_tracking_individual/" target="_blank">Amazon is reportedly now tracking individual hours employees spend at the office in latest worker crackdown | Amazon is clamping down on "coffee badging" workers</a></div><br></div>
<div id="fdiv_26_2024071814111900003" class="dfeed_day rssdiv"><div class="tfeed_day rssdate" id="rssdate_26_3">07-18</div><div class="tfeed_day rsslink" id="rsslink_26_3"><a href="https://www.reddit.com/r/technology/comments/1e6ceut/netflixs_password_sharing_crackdown_backfires/" target="_blank">Netflix's Password Sharing Crackdown Backfires With Slow Subscriber Growth in Q2</a></div><br></div>
<div id="fdiv_26_20240718135646000015" class="dfeed_day rssdiv"><div class="tfeed_day rssdate" id="rssdate_26_15">07-18</div><div class="tfeed_day rsslink" id="rsslink_26_15"><a href="https://www.reddit.com/r/technology/comments/1e6c2r8/many_people_think_ai_is_already_sentient_and/" target="_blank">Many people think AI is already sentient - and that's a big problem</a></div><br></div>
<div id="fdiv_26_2024071813495300007" class="dfeed_day rssdiv"><div class="tfeed_day rssdate" id="rssdate_26_7">07-18</div><div class="tfeed_day rsslink" id="rsslink_26_7"><a href="https://www.reddit.com/r/technology/comments/1e6bxcs/labgrown_diamonds_are_everywhere_this_company/" target="_blank">Lab-Grown Diamonds Are Everywhere. This Company Thinks It Has the Secret to Making Them High-End | Now that it's possible to grow affordable gems in the time it takes to watch a movie, the race is on to save the value of the most precious stone</a></div><br></div>
<div id="fdiv_26_2024071812060000006" class="dfeed_day rssdiv"><div class="tfeed_day rssdate" id="rssdate_26_6">07-18</div><div class="tfeed_day rsslink" id="rsslink_26_6"><a href="https://www.reddit.com/r/technology/comments/1e69r85/are_russian_fishing_boats_sabotaging_subsea/" target="_blank">Are Russian Fishing Boats Sabotaging Subsea Cables? - Bloomberg</a></div><br></div>
<div id="fdiv_26_2024071812015900008" class="dfeed_day rssdiv"><div class="tfeed_day rssdate" id="rssdate_26_8">07-18</div><div class="tfeed_day rsslink" id="rsslink_26_8"><a href="https://www.reddit.com/r/technology/comments/1e69ok9/mark_cuban_social_media_algorithms_could/" target="_blank">Mark Cuban: Social media algorithms could determine election</a></div><br></div>
<div id="fdiv_26_2024071811493600001" class="dfeed_day rssdiv"><div class="tfeed_day rssdate" id="rssdate_26_1">07-18</div><div class="tfeed_day rsslink" id="rsslink_26_1"><a href="https://www.reddit.com/r/technology/comments/1e69g7y/californias_grid_passed_the_reliability_test_this/" target="_blank">California's grid passed the reliability test this heat wave. It's all about giant batteries</a></div><br></div>
<div id="fdiv_26_20240718113218000011" class="dfeed_day rssdiv"><div class="tfeed_day rssdate" id="rssdate_26_11">07-18</div><div class="tfeed_day rsslink" id="rsslink_26_11"><a href="https://www.reddit.com/r/technology/comments/1e695dj/nasa_cancels_its_moon_rover_mission_citing_cost/" target="_blank">NASA cancels its moon rover mission, citing cost overruns and launch delays</a></div><br></div>
<div id="fdiv_26_20240718111556000014" class="dfeed_day rssdiv"><div class="tfeed_day rssdate" id="rssdate_26_14">07-18</div><div class="tfeed_day rsslink" id="rsslink_26_14"><a href="https://www.reddit.com/r/technology/comments/1e68vf2/new_drug_reverses_diabetes_in_mice_boosting/" target="_blank">New drug reverses diabetes in mice, boosting insulin-making cells by 700% | One day this research could lead to game-changing new treatments for diabetes</a></div><br></div>
<div id="fdiv_26_20240718100838000023" class="dfeed_day rssdiv"><div class="tfeed_day rssdate" id="rssdate_26_23">07-18</div><div class="tfeed_day rsslink" id="rsslink_26_23"><a href="https://www.reddit.com/r/technology/comments/1e67syq/after_breach_senators_ask_why_att_stores_call/" target="_blank">After breach, senators ask why AT&T stores call records on "AI Data Cloud" | AT&T ditched internal system, stores user call logs on "trusted" cloud service.</a></div><br></div>
<div id="fdiv_26_2024071809212300002" class="dfeed_day rssdiv"><div class="tfeed_day rssdate" id="rssdate_26_2">07-18</div><div class="tfeed_day rsslink" id="rsslink_26_2"><a href="https://www.reddit.com/r/technology/comments/1e6742z/big_tech_withholds_its_products_from_the_eu_in/" target="_blank">Big Tech withholds its products from the EU in response to regulation</a></div><br></div>
<div id="fdiv_26_20240718051006000016" class="dfeed_day rssdiv"><div class="tfeed_day rssdate" id="rssdate_26_16">07-18</div><div class="tfeed_day rsslink" id="rsslink_26_16"><a href="https://www.reddit.com/r/technology/comments/1e63fq9/what_happened_to_the_artificialintelligence/" target="_blank">What happened to the Artificial-Intelligence Revolution? So far the technology has had almost no economic impact</a></div><br></div>
<div id="fdiv_26_20240718010510000021" class="dfeed_day rssdiv"><div class="tfeed_day rssdate" id="rssdate_26_21">07-18</div><div class="tfeed_day rsslink" id="rsslink_26_21"><a href="https://www.reddit.com/r/technology/comments/1e5yt94/tsmc_set_to_report_strong_profit_stock_pressured/" target="_blank">TSMC set to report strong profit; stock pressured by Trump comments</a></div><br></div>
<div id="fdiv_26_20240717235216000010" class="dfeed_day rssdiv"><div class="tfeed_day rssdate" id="rssdate_26_10">07-17</div><div class="tfeed_day rsslink" id="rsslink_26_10"><a href="https://www.reddit.com/r/technology/comments/1e5x9yn/more_than_40_of_japanese_companies_have_no_plan/" target="_blank">More than 40% of Japanese companies have no plan to make use of AI</a></div><br></div>
<div id="fdiv_26_20240717123023000020" class="dfeed_old rssdiv"><div class="tfeed_old rssdate" id="rssdate_26_20">07-17</div><div class="tfeed_old rsslink" id="rsslink_26_20"><a href="https://www.reddit.com/r/technology/comments/1e5h00x/poll_shows_84_of_pc_users_unwilling_to_pay_extra/" target="_blank">Poll shows 84% of PC users unwilling to pay extra for AI-enhanced hardware</a></div><br></div>
<div id="fdiv_26_20240717122823000024" class="dfeed_old rssdiv"><div class="tfeed_old rssdate" id="rssdate_26_24">07-17</div><div class="tfeed_old rsslink" id="rsslink_26_24"><a href="https://www.reddit.com/r/technology/comments/1e5gylm/valve_runs_its_massive_pc_gaming_ecosystem_with/" target="_blank">Valve runs its massive PC gaming ecosystem with only about 350 employees | Ars' leak analysis shows a large "Games" department and a very well-paid "Admin" team.</a></div><br></div>
<div id="fdiv_26_20240717120105000019" class="dfeed_old rssdiv"><div class="tfeed_old rssdate" id="rssdate_26_19">07-17</div><div class="tfeed_old rsslink" id="rsslink_26_19"><a href="https://www.reddit.com/r/technology/comments/1e5gffe/the_maga_plan_to_end_free_weather_reports/" target="_blank">The MAGA Plan to End Free Weather Reports</a></div><br></div>
<div id="fdiv_26_2024061814543100000" class="dfeed_old rssdiv"><div class="tfeed_old rssdate" id="rssdate_26_0">06-18</div><div class="tfeed_old rsslink" id="rsslink_26_0"><a href="https://www.reddit.com/r/technology/comments/1dismwu/we_are_jocelyn_gecker_and_barbara_ortutay/" target="_blank">We are Jocelyn Gecker and Barbara Ortutay, reporters for The Associated Press. We reported on how social media can impact teen's mental health. Ask us anything!</a></div><br></div>
```

Jquery code to add html to webpage and format css by the last hour/day/older:
```
$(document).ready(function() {
        //ARTICLES PUBLISHED TODAY
        $("<style type='text/css'> .tfeed_day {color:"+ cssligB2 +"; } </style>").appendTo("head");
        $("<style type='text/css'> .tfeed_day a:link {color:"+ cssligB2 +";} </style>").appendTo("head");
        $("<style type='text/css'> .tfeed_day a:visited {color:"+ cssligB2 +";} </style>").appendTo("head");
        $("<style type='text/css'> .tfeed_day a:hover {color:"+ cssligB2 +"; text-decoration: underline;}</style>").appendTo("head");
        //ARTICLES PUBLISHED YESTERDAY & OLDER
        $("<style type='text/css'> .tfeed_old {color:"+ cssligA2 +"; } </style>").appendTo("head");
        $("<style type='text/css'> .tfeed_old a:link {color:"+ cssligA2 +";} </style>").appendTo("head");
        $("<style type='text/css'> .tfeed_old a:visited {color:"+ cssligA2 +";} </style>").appendTo("head");
        $("<style type='text/css'> .tfeed_old a:hover {color:"+ cssligA2 +"; text-decoration: underline;}</style>").appendTo("head");
        //ARTICLES PUBLISHED IN THE PAST HOUR
        $("<style type='text/css'> .tfeed_now {color:"+ cssligB1 +";} </style>").appendTo("head");
        $("<style type='text/css'> .tfeed_now a:link {color:"+ cssligB1 +";} </style>").appendTo("head");
        $("<style type='text/css'> .tfeed_now a:visited {color:"+ cssligB1 +";} </style>").appendTo("head");
        $("<style type='text/css'> .tfeed_now a:hover {color:"+ cssligB1 +"; text-decoration: underline;}</style>").appendTo("head");
        //ARTICLES PUBLISHED IN THE FUTURE
        $("<style type='text/css'> .tfeed_fut {color:"+ cssligB1 +";} </style>").appendTo("head");
        $("<style type='text/css'> .tfeed_fut a:link {color:"+ cssligB1 +";} </style>").appendTo("head");
        $("<style type='text/css'> .tfeed_fut a:visited {color:"+ cssligB1 +";} </style>").appendTo("head");
        $("<style type='text/css'> .tfeed_fut a:hover {color:"+ cssligB1 +"; text-decoration: underline;}</style>").appendTo("head");

        ("#contentb12").load("rss/RedditTechnology.html");
});

```
