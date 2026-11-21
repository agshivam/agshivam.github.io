import worker from "./worker.js";
const store = new Map();
const kv = { get: async (k) => store.get(k) ?? null, put: async (k, v) => void store.set(k, v) };
const env = { COUNTS: kv };
const O = "https://agshivam.github.io";
const hit = (id, e, origin = O) => worker.fetch(new Request("https://w.dev/hit", { method: "POST", headers: { Origin: origin }, body: JSON.stringify({ id, e }) }), env).then((r) => r.json());
const stats = () => worker.fetch(new Request("https://w.dev/stats"), env).then((r) => r.json());
const eq = (a, b, m) => { if (JSON.stringify(a) !== JSON.stringify(b)) { console.error("FAIL", m, a, b); process.exit(1); } };

await hit("aaaaaaaa1", "view"); await hit("aaaaaaaa1", "view");           // same visitor twice: one unique
await hit("bbbbbbbb2", "view");
await hit("aaaaaaaa1", "resume-download");
await hit("aaaaaaaa1", "resume-download");                                   // repeat within 60s ignored
await hit("bbbbbbbb2", "whatsapp-click"); await hit("bbbbbbbb2", "form-sent"); await hit("bbbbbbbb2", "email-click");
eq(await stats(), { visitors: 2, resume: 1, mail: 1, wa: 1, form: 1 }, "counts");
eq((await hit("cccccccc3", "view", "https://evil.example")).ok, false, "origin blocked");
eq((await hit("cccccccc3", "hack")).ok, false, "bad event rejected");
eq((await hit("x", "view")).ok, false, "bad id rejected");
eq((await stats()).visitors, 2, "still 2");
console.log("worker tests passed");
