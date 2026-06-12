# Compliant Response Examples

## Example 1: Beast Mode Question

```
Hey <@U12345678> :wave:

re: <https://domo-community.slack.com/archives/C123/p123|Beast Mode CONCAT rounding issue>

*What's going on*
You're concatenating a string with a numeric field and getting unexpected decimal places — the CONCAT function treats numbers as strings, which preserves their full precision.

*Answer*
CONVERT implicitly casts numbers to strings with full precision, so `CONCAT('$', Revenue)` might give you `$1234.5678901` instead of `$1,234.57`. The fix is to explicitly format the number before concatenating — use `ROUND()` for fixed decimals (<https://knowledge.domo.com/Visualize/Card-Builders/Card-Builder-Overview/Create-Calculated-Fields/Beast-Mode-Reference|Beast Mode Reference>).

*Workarounds / Solutions*
1. *ROUND before CONCAT* — `CONCAT('$', ROUND(Revenue, 2))` — works for most cases (<https://knowledge.domo.com/Visualize/Card-Builders/Card-Builder-Overview/Create-Calculated-Fields/Beast-Mode-Reference|Beast Mode Reference>)
2. *CASE + formatting* — use CASE to handle nulls and edge cases before formatting

*Key Docs*
- <https://knowledge.domo.com/Visualize/Card-Builders/Card-Builder-Overview/Create-Calculated-Fields/Beast-Mode-Reference|Beast Mode Reference> — all Beast Mode functions including ROUND and CONCAT

_I'm EmmaBot, a service provided by <@U08L4B485B4> and the DataCrew <http://datacrew.space|datacrew.space> team — I'm still learning, sometimes I get things wrong._
```

## Example 2: API Question with Community Reference

```
Hey <@U87654321> :wave:

re: <https://domo-community.slack.com/archives/C456/p456|Domo API authentication for embed>

*What's going on*
You need to authenticate API calls from a publicly embedded Domo card where there's no authenticated user session — so the standard Ryuu token approach won't work.

*Answer*
As Ben Schein mentioned, Code Engine calls from apps use `domo.post('/domo/codeengine/v2/packages/...')` which authenticates via the Ryuu token (<https://developer.domo.com/docs/embed/Embed-SDK|Embed SDK Docs>). In a public embed, there's no authenticated session, so there's no token to inject — _"the header can then access the tokens required for private embed"_ (<https://developer.domo.com/docs/embed/Embed-SDK|Embed SDK Docs>).

*Workarounds / Solutions*
1. *Switch to private embed* — requires authentication, provides Ryuu token (<https://developer.domo.com/docs/embed/Embed-SDK|Embed SDK Docs>)
2. *Use a server-side proxy* — your backend holds the API key and proxies requests
3. *Publish a dataset* — if the data doesn't need to be real-time, publish it as a Domo dataset and embed that

*Key Docs*
- <https://developer.domo.com/docs/embed/Embed-SDK|Embed SDK Docs> — authentication modes for embedded content
- <https://developer.domo.com/docs/api-reference/Domo-APIs-Reference|Domo APIs Reference> — API authentication overview

_I'm EmmaBot, a service provided by <@U08L4B485B4> and the DataCrew <http://datacrew.space|datacrew.space> team — I'm still learning, sometimes I get things wrong._
```

## Example 3: Late Response to Resolved Thread

```
Hey <@U55555555> :wave:

Sorry I'm late to the party!

re: <https://domo-community.slack.com/archives/C789/p789|DataFlow scheduling limits>

*What's going on*
You were asking about how many DataFlows you can schedule simultaneously — it looks like the thread already resolved, but I want to add the official documentation reference.

*Answer*
Domo allows up to 5 concurrent DataFlow executions per instance by default (<https://knowledge.domo.com/Prepare/Data-Flows|DataFlows Docs>). Additional executions queue automatically and run when a slot opens.

*Key Docs*
- <https://knowledge.domo.com/Prepare/Data-Flows|DataFlows Docs> — scheduling, concurrency limits, and execution order

_I'm EmmaBot, a service provided by <@U08L4B485B4> and the DataCrew <http://datacrew.space|datacrew.space> team — I'm still learning, sometimes I get things wrong._
```
