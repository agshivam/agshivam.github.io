import { useEffect } from "react";
import Hero from "./components/Hero";
import Marquee from "./components/Marquee";
import About from "./components/About";
import Services from "./components/Services";
import Projects from "./components/Projects";
import Journey from "./components/Journey";
import Contact from "./components/Contact";
import { track } from "./track";

export default function App() {
  useEffect(() => {
    track("view");
    const on = (e: MouseEvent) => { const a = (e.target as HTMLElement).closest?.("[data-gc]"); if (a) track(a.getAttribute("data-gc")!); };
    document.addEventListener("click", on);
    return () => document.removeEventListener("click", on);
  }, []);
  return (
    <main style={{ background: "#0C0C0C", overflowX: "clip" }}>
      <Hero /><Marquee /><About /><Services /><Projects /><Journey /><Contact />
    </main>
  );
}
