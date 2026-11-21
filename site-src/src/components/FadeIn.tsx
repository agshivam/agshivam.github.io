import { motion } from "framer-motion";
import type { ReactNode, CSSProperties } from "react";
type Props = { children: ReactNode; delay?: number; duration?: number; x?: number; y?: number; className?: string; style?: CSSProperties; as?: "div" | "h1" | "h2" | "p" | "li" | "section" };
export default function FadeIn({ children, delay = 0, duration = 0.7, x = 0, y = 30, className, style, as = "div" }: Props) {
  const Tag = motion[as] as typeof motion.div;
  return (
    <Tag className={className} style={style} initial={{ opacity: 0, x, y }} whileInView={{ opacity: 1, x: 0, y: 0 }}
      viewport={{ once: true, margin: "50px", amount: 0 }} transition={{ duration, delay, ease: [0.25, 0.1, 0.25, 1] }}>
      {children}
    </Tag>
  );
}
