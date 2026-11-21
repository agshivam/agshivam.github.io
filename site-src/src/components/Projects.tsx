import { useRef } from "react";
import { motion, useScroll, useTransform, type MotionValue } from "framer-motion";
import FadeIn from "./FadeIn";
import { GhostButton } from "./Buttons";
import content from "../content.json";

const R = "rounded-[40px] sm:rounded-[50px] md:rounded-[60px]";
type P = (typeof content.projects)[number];

function Card({ p, i, total, progress }: { p: P; i: number; total: number; progress: MotionValue<number> }) {
  const target = 1 - (total - 1 - i) * 0.03;
  const scale = useTransform(progress, [i / total, 1], [1, target]);
  const k = p.shot;
  const img = (n: number) => `shots/${k}-${n}.jpg`;
  return (
    <div className="h-[85vh] sm:h-[95vh]" style={{ position: "relative" }}>
      <motion.div className={`sticky top-24 md:top-32 ${R} border-2 border-[#D7E2EA] p-4 sm:p-6 md:p-8`} style={{ scale, background: "#0C0C0C", top: `calc(6rem + ${i * 28}px)`, transformOrigin: "top center" }}>
        <div className="flex flex-col md:flex-row md:items-start md:justify-between gap-4 mb-4 sm:mb-6 md:mb-8">
          <div className="flex items-start gap-4 sm:gap-8">
            <span className="font-black leading-none text-[#D7E2EA]" style={{ fontSize: "clamp(3rem, 10vw, 140px)" }}>{String(i + 1).padStart(2, "0")}</span>
            <div className="flex flex-col gap-1 pt-1">
              <span className="font-light uppercase tracking-widest text-[#D7E2EA] opacity-70" style={{ fontSize: "clamp(0.75rem, 1.3vw, 1.1rem)" }}>{p.tag} · {p.status}</span>
              <h3 className="font-medium uppercase text-[#D7E2EA]" style={{ fontSize: "clamp(1.1rem, 2.4vw, 2.2rem)" }}>{p.title}</h3>
              <p className="font-light text-[#D7E2EA] opacity-60 max-w-xl hidden sm:block" style={{ fontSize: "clamp(0.8rem, 1.2vw, 1.05rem)" }}>{p.note}</p>
            </div>
          </div>
          <div className="flex gap-3 flex-wrap">
            {p.live && <GhostButton href={p.live} gc={i === 0 ? undefined : undefined}>Live Project</GhostButton>}
            <GhostButton href={p.code}>Code</GhostButton>
          </div>
        </div>
        <div className="flex gap-3 sm:gap-4 md:gap-5">
          <div className="flex flex-col gap-3 sm:gap-4 md:gap-5" style={{ width: "40%" }}>
            <img src={img(1)} alt={`${p.title}: first view`} loading="lazy" className={`w-full object-cover object-top ${R}`} style={{ height: "clamp(130px, 16vw, 230px)" }} />
            <img src={img(2)} alt={`${p.title}: second view`} loading="lazy" className={`w-full object-cover object-top ${R}`} style={{ height: "clamp(160px, 22vw, 340px)" }} />
          </div>
          <div style={{ width: "60%" }}>
            <img src={img(3)} alt={`${p.title}: third view`} loading="lazy" className={`w-full h-full object-cover object-top ${R}`} />
          </div>
        </div>
      </motion.div>
    </div>
  );
}

export default function Projects() {
  const ref = useRef<HTMLDivElement>(null);
  const { scrollYProgress } = useScroll({ target: ref, offset: ["start start", "end end"] });
  const list = content.projects;
  return (
    <section id="projects" className="relative z-10 -mt-10 sm:-mt-12 md:-mt-14 rounded-t-[40px] sm:rounded-t-[50px] md:rounded-t-[60px] px-5 sm:px-8 md:px-10 pt-20 sm:pt-24 md:pt-32" style={{ background: "#0C0C0C" }}>
      <FadeIn y={40}><h2 className="hero-heading font-black uppercase leading-none tracking-tight text-center mb-16 sm:mb-20 md:mb-28" style={{ fontSize: "clamp(3rem, 12vw, 160px)" }}>Project</h2></FadeIn>
      <div ref={ref} className="max-w-7xl mx-auto">
        {list.map((p, i) => <Card key={p.title} p={p} i={i} total={list.length} progress={scrollYProgress} />)}
      </div>
    </section>
  );
}
