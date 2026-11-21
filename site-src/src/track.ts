// Own counter (Cloudflare Worker in my account): no cookies, a random id in this browser counts unique visitors.
export const COUNTER = "https://portfolio-counter.agshivam201599.workers.dev";
function vid(): string {
  try { let v = localStorage.getItem("sa_vid"); if (!v) { v = Math.random().toString(36).slice(2, 12) + Date.now().toString(36); localStorage.setItem("sa_vid", v); } return v; }
  catch { return "anon" + Math.random().toString(36).slice(2, 12); }
}
export function track(name: string) {
  try { fetch(COUNTER + "/hit", { method: "POST", keepalive: true, body: JSON.stringify({ id: vid(), e: name }) }).catch(() => {}); } catch { /* ignore */ }
}
export type Stats = { visitors: number; resume: number; mail: number; wa: number; form: number };
export async function loadStats(): Promise<Stats | null> {
  try { const r = await fetch(COUNTER + "/stats"); if (!r.ok) return null; return await r.json(); } catch { return null; }
}
