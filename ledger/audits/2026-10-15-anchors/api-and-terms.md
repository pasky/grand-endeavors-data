# Forecast API research (checked 2026-10-15)

## Metaculus: access and reuse

**No anonymous API reads.** Direct unauthenticated `curl` requests returned HTTP **403** and body `Permission Error: The API is only available to authenticated users. Please create an account and use your API token to access the API.` Tested:

- `GET https://www.metaculus.com/api/posts/?search=AGI&limit=5` — 403
- `GET https://www.metaculus.com/api/posts/5121/` — 403
- `GET https://www.metaculus.com/api2/questions/5121/` — 403
- `GET https://www.metaculus.com/api2/questions/?search=AGI&limit=5` — 403

So no question fields/aggregations could be observed anonymously; the returned error contains no question JSON. Open question 5121 is [Date of Artificial General Intelligence](https://www.metaculus.com/questions/5121/date-of-artificial-general-intelligence/), but the web page request hit a Cloudflare challenge in this environment. The official API docs page [metaculus.com/api](https://www.metaculus.com/api/) also failed to load its OpenAPI definition (`Forbidden /static/openapi...`). The official docs and announcement say API users authenticate; the announcement directs builders to the [data-needs form](https://docs.google.com/forms/d/e/1FAIpQLSeJhtZzHl5qMvBjbXbatyaqoS4IU7RE0GGw_vlhs6I9syqn1g/viewform) to request API access. A free account alone is not evidence of aggregate data entitlement. Once issued, pass token in `Authorization: Token <token>` (e.g. `curl -H 'Authorization: Token …' URL`); see [official API launch post](https://www.metaculus.com/notebooks/15141/officially-launching-the-metaculus-api/) and its linked docs. Current public rate limit could not be established from accessible official docs; do not assume a limit.

**Critical 2026 change:** Metaculus’s [March 9, 2026 API-change announcement](https://www.metaculus.com/notebooks/42554/changes-to-the-metaculus-api/) says: “The Community Prediction and other aggregates are no longer generally available through the API.” A small varied test-question set was planned; it is not a general-purpose public feed. It explicitly says non-commercial data users should “please get in touch,” and commercial uses are case-by-case. This blocks the requested general weekly community-prediction collector absent express access approval; do not treat valid credentials as access to every aggregate.

**Terms:** [Terms of Use](https://www.metaculus.com/terms-of-use/) (modified Sep 21, 2026) apply to API use. The “Your License to Use Site Content” clause permits only a “limited, personal, non-exclusive, non-commercial, revocable and non-transferable license to view” content, and prohibits copying/extracting except “through and subject to the terms of an API provided by Metaculus” or written authorization. The API-change post asks non-commercial projects to get in touch. I found **no CC BY-NC or other open data license**. Thus a public dashboard that persistently stores and redisplays API values is **not clearly authorized merely by attribution / non-commercial status**; request written permission and the specific API terms before implementing it. Attribution alone does not cure the restrictions.

## Metaculus JSON/schema notes (source code, not a verified live response)

The live API’s current aggregate access restrictions mean the following is the source-code schema/algorithm, **not a claim that these fields are currently returned to this caller**. Relevant official repo source fetched: [`questions/serializers/aggregate_forecasts.py`](https://github.com/Metaculus/metaculus/blob/main/questions/serializers/aggregate_forecasts.py), [`questions/serializers/common.py`](https://github.com/Metaculus/metaculus/blob/main/questions/serializers/common.py), [`utils/the_math/measures.py`](https://github.com/Metaculus/metaculus/blob/main/utils/the_math/measures.py), [`utils/the_math/formulas.py`](https://github.com/Metaculus/metaculus/blob/main/utils/the_math/formulas.py).

In the historical/current serializer shape, paths are under `question`:

- Latest aggregation: `question.aggregations.<method>.latest`; usual method is `recency_weighted`. Its basic fields include `start_time`, `end_time`, `forecaster_count`, `interval_lower_bounds`, `centers`, `interval_upper_bounds`. Full mode additionally includes `forecast_values`, `means`, `histogram`. `forecast_values` is a CDF for continuous/date questions; in binary aggregation values are probability mass/probabilities (binary serializer removes the no-side element for centers/intervals; use the positive/YES probability in the CDF/probability representation).
- Date/continuous scale: `question.scaling.range_min`, `range_max`, `zero_point`, `open_lower_bound`, `open_upper_bound`, `inbound_outcome_count`, `continuous_range`; plus question `unit`. Date bounds/`continuous_range` are Unix epoch seconds converted to UTC datetimes in JSON. Status/time/resolution are question fields: `question.status`, `question.resolution`, `question.open_time`, `question.scheduled_close_time`, `question.actual_close_time`, `question.scheduled_resolve_time`, `question.actual_resolve_time`, `question.resolution_set_time` (serializer `actual_close_time` can fall back to scheduled close or earlier actual resolve). `forecaster_count` is on each aggregation snapshot, not necessarily a top-level question field.
- Binary: `question.type == "binary"`; the API’s single latest community probability/YES chance, if entitled, is the binary forecast probability. Scaling/range is not applicable. Count is still latest aggregate `forecaster_count`; status/resolution/times are as above.

**CDF to p10/p50/p90 (date):** For CDF array `cdf` length `L`, derive each percentile’s unscaled location `u` by inverting linearly over the regular grid `x_i=i/(L−1)`: if `p/100` falls between `cdf[i]` and `cdf[i+1]`, `u=(i+(p/100−cdf[i])/(cdf[i+1]−cdf[i]))/(L−1)`. This is the repo `percent_point_function`; below first CDF value it returns `u=0`, and at/above last returns `u=1`. Convert to epoch-second date `v` by:

- linear: `v=range_min+(range_max−range_min)u`;
- if `zero_point` is set: `r=(range_max−zero_point)/(range_min−zero_point)` and `v=range_min+(range_max−range_min)(r^u−1)/(r−1)`.

Convert `v` to UTC date/time; decimal calendar year can be `year + elapsed_seconds/(seconds between UTC Jan 1 of year and next Jan 1)`. Do not simply divide epoch time by a fixed 365-day year. If a percentile falls outside the covered range and the corresponding bound is open, represent it as **censored `<range_min` / `>range_max`**, not as a precise boundary date: the repo’s percentile function clips to `u=0/1`, while scaling maps these to nominal endpoints. Preserve the open-bound flag in storage. The scale equations above are transcribed from the cited repo formula implementation.

**Date worked example:** Unable to supply genuine raw CDF/scaling values or computed live p10/p50/p90: the sampled question/API endpoints all returned 403 and the open page hit Cloudflare; plus the 2026 policy change says aggregates are no longer generally available. Inventing illustrative numbers would not satisfy “real live question fetched.” A Metaculus API credential/explicit aggregate access is required to complete this example.

## Manifold: API and live example

Official [API docs](https://docs.manifold.markets/api) state market reads require no auth and public API limit is **500 requests/minute/IP** (do not evade via multiple IPs). `GET https://api.manifold.markets/v0/market/<id>` returns one market; binary snapshot values include `probability` (0–1), `uniqueBettorCount`, `volume`, `closeTime` (Unix ms), `isResolved`, `resolution` (null if unresolved), `outcomeType`. `prob` can also appear in payloads, but use documented `probability`. Docs’ licensing section says API use is subject to Terms; API access allows bots/integrations, but Terms prohibit systematic retrieval to compile a database without written permission and say commercial uses need approval; commercial AI training needs a data license. For a weekly stored/redispayed public dataset, ask Manifold for written data permission rather than relying on attribution. Sources: [API docs](https://docs.manifold.markets/api), [Terms](https://manifold.markets/terms).

**Live worked example**, fetched anonymously 2026-10-15:

- `GET https://api.manifold.markets/v0/market/htqCSZdcgS` returned HTTP 200.
- Raw fields: `id="htqCSZdcgS"`, question `"Will Republicans have low turnout of voters in 2026 midterms?"`, `outcomeType="BINARY"`, `probability=0.4999999999752476`, `uniqueBettorCount=1`, `volume=1.9999999950495415`, `closeTime=1794697200000`, `isResolved=false`, `resolution=null`, `createdTime=1792049936608`, `url="https://manifold.markets/DudleyDOODOO/will-republicans-have-low-turnout-o"`.
- Interpretation: 49.9999999975% YES, one distinct bettor, volume about M$2; close timestamp is 2026-11-15T21:40:00Z; unresolved, hence no resolution.
