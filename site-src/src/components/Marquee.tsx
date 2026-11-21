import { useEffect, useRef, useState } from "react";
const shots = ["patient-360", "chaos-proof-pipelines", "job-radar", "portable-data-platform", "patient-360-lakehouse"].flatMap((n) => [1, 2, 3].map((i) => `shots/${n}-${i}.jpg`));
const row1 = shots.slice(0, 8), row2 = shots.slice(8);
function Row({ imgs, dir, offset }: { imgs: string[]; dir: 1 | -1; offset: number }) {
  const tiles = [...imgs, ...imgs, ...imgs];
  return (
    <div className="flex gap-3" style={{ transform: `translateX(${dir * (offset - 200)}px)`, willChange: "transform", marginLeft: "-1400px" }}>
      {tiles.map((s, i) => <img key={i} src={s} alt="" loading="lazy" className="rounded-2xl object-cover object-top shrink-0" style={{ width: 420, height: 270 }} />)}
    </div>
  );
}
export default function Marquee() {
  const ref = useRef<HTMLElement>(null);
  const [offset, setOffset] = useState(0);
  useEffect(() => {
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    const on = () => { const el = ref.current; if (!el) return; const top = el.getBoundingClientRect().top + window.scrollY; setOffset((window.scrollY - top + window.innerHeight) * 0.3); };
    on(); window.addEventListener("scroll", on, { passive: true }); return () => window.removeEventListener("scroll", on);
  }, []);
  return (
    <section ref={ref} aria-label="Dashboards from my projects" className="pt-24 sm:pt-32 md:pt-40 pb-10 flex flex-col gap-3" style={{ background: "#0C0C0C", overflow: "hidden" }}>
      <Row imgs={row1} dir={1} offset={offset} />
      <Row imgs={row2} dir={-1} offset={offset} />
    </section>
  );
}
