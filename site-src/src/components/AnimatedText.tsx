import { useRef } from "react";
import { motion, useScroll, useTransform, type MotionValue } from "framer-motion";
function Char({ ch, i, n, progress }: { ch: string; i: number; n: number; progress: MotionValue<number> }) {
  const start = i / n, end = Math.min(1, start + 1.5 / n);
  const opacity = useTransform(progress, [start, end], [0.2, 1]);
  return (<span style={{ position: "relative", display: "inline-block" }}><span style={{ opacity: 0 }}>{ch}</span><motion.span style={{ opacity, position: "absolute", left: 0, top: 0 }}>{ch}</motion.span></span>);
}
export default function AnimatedText({ text, className, style }: { text: string; className?: string; style?: React.CSSProperties }) {
  const ref = useRef<HTMLParagraphElement>(null);
  const { scrollYProgress } = useScroll({ target: ref, offset: ["start 0.8", "end 0.2"] });
  const words = text.split(" "); const n = text.length; let idx = 0;
  return (
    <p ref={ref} className={className} style={style} aria-label={text}>
      {words.map((w, wi) => {
        const chars = (w + (wi < words.length - 1 ? " " : "")).split("");
        const el = (<span key={wi} aria-hidden="true" style={{ display: "inline-block", whiteSpace: "nowrap" }}>{chars.map((c, ci) => <Char key={ci} ch={c} i={idx + ci} n={n} progress={scrollYProgress} />)}</span>);
        idx += chars.length; return <span key={wi}>{el}{" "}</span>;
      })}
    </p>
  );
}
