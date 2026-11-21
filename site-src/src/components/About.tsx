import { Snowflake, Database, GitBranch, ShieldCheck } from "lucide-react";
import FadeIn from "./FadeIn";
import AnimatedText from "./AnimatedText";
import { ContactButton } from "./Buttons";
const tile = "absolute rounded-[28px] flex items-center justify-center text-[#BBCCD7]";
const bg = { background: "linear-gradient(160deg, rgba(100,105,115,.45), rgba(187,204,215,.10))", border: "1px solid rgba(215,226,234,.22)" };
export default function About() {
  return (
    <section id="about" className="relative min-h-screen flex flex-col items-center justify-center px-5 sm:px-8 md:px-10 py-20" style={{ overflowX: "clip" }}>
      <FadeIn x={-80} y={0} duration={0.9} delay={0.1} className={`${tile} w-[90px] h-[90px] sm:w-[120px] sm:h-[120px] md:w-[160px] md:h-[160px] top-[4%] left-[1%] sm:left-[2%] md:left-[4%]`} style={bg}><Snowflake className="w-1/2 h-1/2" strokeWidth={1.2} aria-hidden="true" /></FadeIn>
      <FadeIn x={-80} y={0} duration={0.9} delay={0.25} className={`${tile} w-[80px] h-[80px] sm:w-[110px] sm:h-[110px] md:w-[140px] md:h-[140px] bottom-[8%] left-[3%] sm:left-[6%] md:left-[10%]`} style={bg}><Database className="w-1/2 h-1/2" strokeWidth={1.2} aria-hidden="true" /></FadeIn>
      <FadeIn x={80} y={0} duration={0.9} delay={0.15} className={`${tile} w-[90px] h-[90px] sm:w-[120px] sm:h-[120px] md:w-[160px] md:h-[160px] top-[4%] right-[1%] sm:right-[2%] md:right-[4%]`} style={bg}><GitBranch className="w-1/2 h-1/2" strokeWidth={1.2} aria-hidden="true" /></FadeIn>
      <FadeIn x={80} y={0} duration={0.9} delay={0.3} className={`${tile} w-[100px] h-[100px] sm:w-[130px] sm:h-[130px] md:w-[170px] md:h-[170px] bottom-[8%] right-[3%] sm:right-[6%] md:right-[10%]`} style={bg}><ShieldCheck className="w-1/2 h-1/2" strokeWidth={1.2} aria-hidden="true" /></FadeIn>
      <div className="flex flex-col items-center gap-10 sm:gap-14 md:gap-16 relative z-10">
        <FadeIn y={40}><h2 className="hero-heading font-black uppercase leading-none tracking-tight text-center" style={{ fontSize: "clamp(3rem, 12vw, 160px)" }}>About me</h2></FadeIn>
        <AnimatedText className="font-medium text-center leading-relaxed max-w-[560px] text-[#D7E2EA]" style={{ fontSize: "clamp(1rem, 2vw, 1.35rem)" }}
          text="With more than six years of experience building data platforms, i focus on Snowflake, dbt and pipelines that fail loudly instead of silently. I enjoy working with teams that want data they can trust. Let's build something reliable together!" />
      </div>
      <div className="mt-16 sm:mt-20 md:mt-24 relative z-10"><ContactButton /></div>
    </section>
  );
}
