import { useEffect, useState, type FormEvent } from "react";
import { Mail, MessageCircle, FileDown, Linkedin, Github, Copy } from "lucide-react";
import FadeIn from "./FadeIn";
import content from "../content.json";
import { loadStats, track, type Stats } from "../track";

const KEY = "46a7ce2f-5a9c-4b15-b354-db6879b01ded"; // Web3Forms public access key (it is meant to be in the page)
const row = "flex items-center justify-between gap-4 rounded-[28px] border border-[#D7E2EA]/25 px-6 py-5 text-[#D7E2EA] transition-colors duration-200 hover:bg-[#D7E2EA]/10";

export default function Contact() {
  const [state, setState] = useState<"idle" | "sending" | "done" | "error">("idle");
  const [stats, setStats] = useState<Stats | null>(null);
  const [copied, setCopied] = useState(false);
  useEffect(() => { loadStats().then(setStats); }, []);

  async function submit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    const f = new FormData(e.currentTarget);
    if (f.get("botcheck")) return;
    setState("sending");
    try {
      const r = await fetch("https://api.web3forms.com/submit", { method: "POST", headers: { "Content-Type": "application/json", Accept: "application/json" },
        body: JSON.stringify({ access_key: KEY, subject: "Portfolio message from " + f.get("name"), from_name: "Portfolio site", name: f.get("name"), email: f.get("email"), message: f.get("message") }) });
      const d = await r.json();
      if (d.success) { track("form-sent"); setState("done"); } else throw new Error(d.message);
    } catch { setState("error"); }
  }
  const copy = () => { navigator.clipboard?.writeText(content.email).then(() => { setCopied(true); setTimeout(() => setCopied(false), 1800); }).catch(() => {}); };
  const f = (n?: number) => (n ?? 0).toLocaleString("en-IN");

  return (
    <section id="contact" className="px-5 sm:px-8 md:px-10 pt-24 sm:pt-32 md:pt-40 pb-16">
      <FadeIn y={40}><h2 className="hero-heading font-black uppercase leading-none tracking-tight text-center mb-8" style={{ fontSize: "clamp(3rem, 12vw, 160px)" }}>Contact</h2></FadeIn>
      <FadeIn><p className="text-center font-light text-[#D7E2EA] max-w-xl mx-auto mb-16 sm:mb-20" style={{ fontSize: "clamp(1rem, 1.6vw, 1.3rem)" }}>Open to remote senior and lead data engineering roles in India and worldwide. A short note is enough, I reply within a day.</p></FadeIn>
      <div className="max-w-5xl mx-auto grid gap-10 md:grid-cols-2">
        <FadeIn>
          {state === "done" ? (
            <div className="rounded-[28px] border border-[#D7E2EA]/25 p-8" role="status"><b className="block text-2xl font-medium mb-2">Message sent</b><span className="font-light">Thank you. I will reply to the email you gave.</span></div>
          ) : (
            <form onSubmit={submit} className="flex flex-col gap-4">
              <input name="botcheck" type="checkbox" tabIndex={-1} autoComplete="off" className="hidden" />
              <label className="sr-only" htmlFor="f-name">Your name</label><input id="f-name" name="name" required placeholder="Your name" className="field" autoComplete="name" />
              <label className="sr-only" htmlFor="f-mail">Your email</label><input id="f-mail" name="email" type="email" required placeholder="Your email" className="field" autoComplete="email" />
              <label className="sr-only" htmlFor="f-msg">Message</label><textarea id="f-msg" name="message" required rows={5} placeholder="How can I help?" className="field" />
              <button type="submit" disabled={state === "sending"} className="self-start rounded-full px-10 py-3.5 text-sm sm:text-base font-medium uppercase tracking-widest text-white disabled:opacity-60"
                style={{ background: "linear-gradient(123deg, #18011F 7%, #B600A8 37%, #7621B0 72%, #BE4C00 100%)", boxShadow: "0px 4px 4px rgba(181, 1, 167, 0.25), 4px 4px 12px #7721B1 inset", outline: "2px solid white", outlineOffset: "-3px" }}>
                {state === "sending" ? "Sending" : "Send message"}
              </button>
              {state === "error" && <p role="alert" className="text-[#ffb4a8]">Could not send. Please email <a className="underline" href={`mailto:${content.email}`}>{content.email}</a> directly.</p>}
            </form>
          )}
        </FadeIn>
        <FadeIn delay={0.1} className="flex flex-col gap-3">
          <div className={row}><a data-gc="email-click" href={`mailto:${content.email}?subject=Opportunity%20for%20Shivam`} className="flex items-center gap-3 min-w-0"><Mail size={22} aria-hidden="true" /><span className="truncate">{content.email}</span></a><button type="button" onClick={copy} className="flex items-center gap-2 text-sm opacity-80 hover:opacity-100"><Copy size={16} aria-hidden="true" />{copied ? "Copied" : "Copy"}</button></div>
          <a data-gc="whatsapp-click" href={content.wa} target="_blank" rel="noopener" className={row}><span className="flex items-center gap-3"><MessageCircle size={22} aria-hidden="true" />Message me on WhatsApp</span></a>
          <a data-gc="resume-download" href={content.resume} download className={row}><span className="flex items-center gap-3"><FileDown size={22} aria-hidden="true" />Download resume (PDF)</span></a>
          <a href="https://www.linkedin.com/in/shivamagarwal-/" target="_blank" rel="noopener" className={row}><span className="flex items-center gap-3"><Linkedin size={22} aria-hidden="true" />LinkedIn</span></a>
          <a href="https://github.com/agshivam" target="_blank" rel="noopener" className={row}><span className="flex items-center gap-3"><Github size={22} aria-hidden="true" />GitHub</span></a>
          <a href="https://x.com/deyogiShivamAg" target="_blank" rel="noopener" className={row}><span className="flex items-center gap-3"><span aria-hidden="true" className="font-bold w-[22px] text-center">X</span>@deyogiShivamAg</span></a>
        </FadeIn>
      </div>
      {stats && (
        <div className="max-w-5xl mx-auto mt-20 pt-8 grid grid-cols-2 md:grid-cols-4 gap-6" style={{ borderTop: "1px solid rgba(215,226,234,0.15)" }} aria-label="Site activity">
          {[["Unique visitors", stats.visitors], ["Resume downloads", stats.resume], ["Emails and messages", (stats.mail || 0) + (stats.form || 0)], ["WhatsApp chats opened", stats.wa]].map(([l, v]) => (
            <div key={l as string} className="flex flex-col"><b className="text-3xl font-semibold text-[#D7E2EA]">{f(v as number)}</b><span className="text-sm text-[#D7E2EA]/70">{l}</span></div>
          ))}
          <p className="col-span-full text-xs text-[#D7E2EA]/60">Counted by a small service I run myself, with no cookies. Emails and WhatsApp are clicks and form sends, not confirmed messages.</p>
        </div>
      )}
      <footer className="max-w-5xl mx-auto mt-16 text-sm text-[#D7E2EA]/60 leading-relaxed">All projects on this site use public or synthetic data. No employer data is used.</footer>
    </section>
  );
}
