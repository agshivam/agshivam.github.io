import FadeIn from "./FadeIn";
const items = [
  ["Snowflake Platforms", "Architecture, incremental loads with streams, tasks and MERGE, and governance with masking and access policies."],
  ["dbt Modeling", "Reusable models and macros, tests on every model, team standards, code reviews and CI checks."],
  ["Pipelines and Ingestion", "Ingestion from APIs, databases and SaaS with Fivetran, Airflow and Python, built so reruns are safe."],
  ["Data Quality", "Source-to-target reconciliation, contracts and alerts so bad data is caught before anyone sees it."],
  ["Cost and Performance", "Measure first, change one thing, measure again. Lower warehouse spend and shorter nightly runs."],
];
export default function Services() {
  return (
    <section id="services" className="bg-white rounded-t-[40px] sm:rounded-t-[50px] md:rounded-t-[60px] px-5 sm:px-8 md:px-10 py-20 sm:py-24 md:py-32 relative">
      <FadeIn y={40}><h2 className="font-black uppercase leading-none tracking-tight text-center text-[#0C0C0C] mb-16 sm:mb-20 md:mb-28" style={{ fontSize: "clamp(3rem, 12vw, 160px)" }}>Services</h2></FadeIn>
      <ol className="max-w-5xl mx-auto list-none">
        {items.map(([n, d], i) => (
          <FadeIn as="li" key={n} delay={i * 0.1} className="flex gap-4 sm:gap-8 md:gap-12 items-start py-8 sm:py-10 md:py-12" style={{ borderTop: i ? "1px solid rgba(12,12,12,0.15)" : "none" }}>
            <span className="font-black leading-none text-[#0C0C0C]" style={{ fontSize: "clamp(3rem, 10vw, 140px)" }}>0{i + 1}</span>
            <div className="flex flex-col gap-2 sm:gap-3 pt-1">
              <h3 className="font-medium uppercase text-[#0C0C0C]" style={{ fontSize: "clamp(1rem, 2.2vw, 2.1rem)" }}>{n}</h3>
              <p className="font-light leading-relaxed max-w-2xl text-[#0C0C0C] opacity-60" style={{ fontSize: "clamp(0.85rem, 1.6vw, 1.25rem)" }}>{d}</p>
            </div>
          </FadeIn>
        ))}
      </ol>
    </section>
  );
}
