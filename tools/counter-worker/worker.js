// Your own visitor and click counter. Runs free on Cloudflare Workers, data lives in a KV store in YOUR account.
// No cookies, no IP addresses stored. A random id in the visitor's browser is used only to count unique visitors.
const ALLOWED_ORIGIN = "https://agshivam.github.io";
const EVENTS = ["view", "resume-download", "email-click", "whatsapp-click", "form-sent"];

const cors = (extra = {}) => ({
  "Access-Control-Allow-Origin": ALLOWED_ORIGIN,
  "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type",
  ...extra,
});
const json = (obj, status = 200) =>
  new Response(JSON.stringify(obj), { status, headers: cors({ "Content-Type": "application/json", "Cache-Control": "no-store" }) });

async function bump(kv, key) {
  const n = parseInt((await kv.get(key)) || "0", 10);
  await kv.put(key, String(n + 1));
}

export default {
  async fetch(request, env) {
    const kv = env.COUNTS;
    const url = new URL(request.url);
    if (request.method === "OPTIONS") return new Response(null, { status: 204, headers: cors() });

    if (request.method === "GET" && url.pathname === "/stats") {
      const get = async (k) => parseInt((await kv.get(k)) || "0", 10);
      const [uv, resume, mail, wa, form] = await Promise.all(
        ["uv", "resume-download", "email-click", "whatsapp-click", "form-sent"].map((e) => get("c:" + e))
      );
      return json({ visitors: uv, resume, mail, wa, form });
    }

    if (request.method === "POST" && url.pathname === "/hit") {
      if (request.headers.get("Origin") !== ALLOWED_ORIGIN) return json({ ok: false }, 403);
      let body;
      try { body = JSON.parse(await request.text()); } catch { return json({ ok: false }, 400); }
      const { id, e } = body || {};
      if (!EVENTS.includes(e) || typeof id !== "string" || !/^[a-z0-9]{8,40}$/.test(id)) return json({ ok: false }, 400);

      // ignore the same visitor repeating the same event within 60 seconds (double clicks, reloads)
      const rl = `r:${id}:${e}`;
      if (await kv.get(rl)) return json({ ok: true, counted: false });
      await kv.put(rl, "1", { expirationTtl: 60 });

      if (e === "view") {
        if (!(await kv.get("v:" + id))) {
          await kv.put("v:" + id, "1");
          await bump(kv, "c:uv");
        }
      } else {
        await bump(kv, "c:" + e);
      }
      return json({ ok: true, counted: true });
    }
    return json({ ok: false }, 404);
  },
};
