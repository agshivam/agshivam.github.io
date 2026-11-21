# Own visitor and click counter (Cloudflare Worker, free)

Counts unique visitors, resume downloads, email clicks, contact-form sends and WhatsApp clicks. No cookies, no IP addresses stored. A random id in the visitor's browser is used only to count unique visitors. Free plan limit: about 1,000 KV writes a day, which is roughly 400 events a day. Past that, counting pauses until the next day and the site keeps working.

## Set up (about 10 minutes, works in Safari on an iPad)
1. Sign up free at dash.cloudflare.com (no card needed).
2. Left menu: Storage and databases, then KV, then Create a namespace. Name it `counts`.
3. Left menu: Compute (Workers), then Create, then Create Worker. Name it `portfolio-counter`, then Deploy.
4. On the Worker, tap Edit code, delete the sample, paste the whole of `worker.js` from this folder, then Deploy.
5. Worker, Settings, Bindings, Add, KV namespace. Variable name must be exactly `COUNTS`, namespace `counts`. Save and deploy.
6. Copy the Worker address (it looks like `https://portfolio-counter.<your-name>.workers.dev`) and send it to Claude. It is a public address, not a secret.

## Check it works
Open `<worker address>/stats` in a browser. You should see `{"visitors":0,"resume":0,"mail":0,"wa":0,"form":0}`.

## Test locally
`node tools/counter-worker/test.mjs` runs the counting rules against a fake store.

## Notes
- The Worker only accepts writes from https://agshivam.github.io. If you move the site, change `ALLOWED_ORIGIN` in `worker.js`.
- Counts are approximate: two visitors at the same instant can be counted once, and anyone who clears browser storage counts again as a new visitor. Fine for a portfolio, not for billing.
