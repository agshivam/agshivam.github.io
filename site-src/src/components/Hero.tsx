import { useState } from "react";
import FadeIn from "./FadeIn";
import Magnet from "./Magnet";
import { ContactButton } from "./Buttons";

const links = [["About", "#about"], ["Services", "#services"], ["Projects", "#projects"], ["Contact", "#contact"]];

function Portrait() {
  const [failed, setFailed] = useState(false);
  if (!failed) return <img src="portrait.png" alt="Shivam Agarwal" onError={() => setFailed(true)} className="w-full h-auto block select-none" draggable={false} />;
  return (
    <div className="aspect-[4/5] w-full rounded-[40px] sm:rounded-[56px] flex items-end justify-center overflow-hidden" aria-label="Shivam Agarwal monogram"
      style={{ background: "linear-gradient(180deg, rgba(100,105,115,.35) 0%, rgba(187,204,215,.12) 100%)", border: "1px solid rgba(215,226,234,.25)" }}>
      <span className="hero-heading font-black leading-none" style={{ fontSize: "clamp(110px, 22vw, 260px)", marginBottom: "-0.08em" }}>SA</span>
    </div>
  );
}

export default function Hero() {
  return (
    <section className="relative h-screen min-h-[560px] flex flex-col" style={{ overflowX: "clip" }}>
      <FadeIn delay={0} y={-20}>
        <nav aria-label="Main" className="flex justify-between px-6 md:px-10 pt-6 md:pt-8">
          {links.map(([l, h]) => (
            <a key={l} href={h} className="text-[#D7E2EA] font-medium uppercase tracking-wider text-sm md:text-lg lg:text-[1.4rem] hover:opacity-70 transition-opacity duration-200">{l}</a>
          ))}
        </nav>
      </FadeIn>
      <div className="overflow-hidden">
        <FadeIn delay={0.15} y={40}>
          <h1 className="hero-heading font-black uppercase tracking-tight leading-none whitespace-nowrap w-full text-center mt-6 sm:mt-4 md:-mt-5 text-[12vw] sm:[font-size:13vw] md:[font-size:14vw] lg:[font-size:14.6vw]">Hi, i&apos;m shivam</h1>
        </FadeIn>
      </div>
      <div className="flex-1" />
      <div className="flex justify-between items-end px-6 md:px-10 pb-7 sm:pb-8 md:pb-10 relative z-20">
        <FadeIn delay={0.35} y={20}>
          <p className="font-light uppercase tracking-wide leading-snug text-[#D7E2EA] max-w-[160px] sm:max-w-[220px] md:max-w-[260px]" style={{ fontSize: "clamp(0.75rem, 1.4vw, 1.5rem)" }}>a senior data engineer building snowflake platforms that last</p>
        </FadeIn>
        <FadeIn delay={0.5} y={20}><ContactButton /></FadeIn>
      </div>
      <div className="absolute left-1/2 -translate-x-1/2 z-10 top-1/2 -translate-y-1/2 sm:top-auto sm:translate-y-0 sm:bottom-0 w-[240px] sm:w-[320px] md:w-[400px] lg:w-[460px]">
        <FadeIn delay={0.6} y={30}><Magnet padding={150} strength={3} className="w-full"><Portrait /></Magnet></FadeIn>
      </div>
    </section>
  );
}
