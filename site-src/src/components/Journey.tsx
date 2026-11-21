import FadeIn from "./FadeIn";
import content from "../content.json";
export default function Journey() {
  return (
    <section id="journey" className="px-5 sm:px-8 md:px-10 pt-24 sm:pt-32 md:pt-40 pb-10">
      <FadeIn y={40}><h2 className="hero-heading font-black uppercase leading-none tracking-tight text-center mb-16 sm:mb-20 md:mb-28" style={{ fontSize: "clamp(3rem, 12vw, 160px)" }}>Journey</h2></FadeIn>
      <ol className="max-w-5xl mx-auto list-none">
        {content.roles.map((r, i) => (
          <FadeIn as="li" key={r.title + r.dates} delay={0.05} className="py-8 sm:py-10 md:py-12 grid gap-4 md:grid-cols-[220px_1fr] md:gap-12" style={{ borderTop: "1px solid rgba(215,226,234,0.15)" }}>
            <span className="font-light uppercase tracking-wide text-[#D7E2EA] opacity-70 text-sm md:text-base">{r.dates}</span>
            <div className="flex flex-col gap-3">
              <h3 className="font-medium uppercase text-[#D7E2EA]" style={{ fontSize: "clamp(1rem, 2.2vw, 1.8rem)" }}>{r.title}</h3>
              <p className="font-light text-[#D7E2EA] opacity-60" style={{ fontSize: "clamp(0.9rem, 1.5vw, 1.15rem)" }}>{r.company}</p>
              <ul className="list-disc pl-5 flex flex-col gap-2 font-light leading-relaxed text-[#D7E2EA] opacity-80" style={{ fontSize: "clamp(0.9rem, 1.4vw, 1.1rem)" }}>
                {r.points.map((p) => <li key={p}>{p}</li>)}
              </ul>
              <div className="flex flex-wrap gap-2 pt-1">
                {r.tech.map((t) => <span key={t} className="rounded-full border border-[#D7E2EA]/30 px-3 py-1 text-xs sm:text-sm text-[#D7E2EA]/80">{t}</span>)}
              </div>
            </div>
          </FadeIn>
        ))}
      </ol>
      <div className="max-w-5xl mx-auto mt-20">
        <FadeIn><h3 className="font-medium uppercase text-[#D7E2EA] mb-8" style={{ fontSize: "clamp(1.1rem, 2.4vw, 2rem)" }}>Selected client work</h3></FadeIn>
        <div className="grid sm:grid-cols-2 gap-4 sm:gap-5">
          {content.clients.map((c, i) => (
            <FadeIn key={c.name} delay={i * 0.08} className="rounded-[28px] border border-[#D7E2EA]/25 p-6 sm:p-8">
              <h4 className="font-medium uppercase text-[#D7E2EA] mb-2">{c.name}</h4>
              <p className="font-light leading-relaxed text-[#D7E2EA] opacity-70">{c.note}</p>
            </FadeIn>
          ))}
        </div>
      </div>
    </section>
  );
}
