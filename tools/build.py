import html, json

E = html.escape
EMAIL = "agshivam201599@gmail.com"
WA = "https://wa.me/919872907228?text=Hi%20Shivam%2C%20I%20saw%20your%20portfolio%20and%20would%20like%20to%20connect."
RESUME = "Shivam-Agarwal-Resume.pdf"
SITE = "https://agshivam.github.io/"
LIVE = "https://patient-360.streamlit.app/"

tools = [
 ("Snowflake","Stored procedures, streams, tasks, MERGE-based incremental loads and SCD 1 and 2 history.","Near-real-time pipelines at about 6 million records per hour for Intelsat. Snowflake Core certified.",["Kipi.ai","V4C.ai","Kipi.bi","Intelsat","Myriad Genetics"]),
 ("dbt","Reusable models and macros, team standards, code reviews and CI checks on every change.","Set the dbt development standards for the team at Kipi.bi. dbt Fundamentals certified.",["Kipi.bi","Myriad Genetics","Intelsat"]),
 ("Fivetran","Automated ingestion from databases, SaaS platforms and MongoDB, replacing manual loads.","Automated SaaS and MongoDB ingestion for Vena Health. Fivetran Technical certified.",["Kipi.bi","Vena Health"]),
 ("Python and Airflow","API ingestion, Snowpark, Lambda connectors and scheduled orchestration with CI/CD.","Introduced CI/CD for dbt, Airflow and Python on the Intelsat platform.",["Kipi.bi","Intelsat","Vena Health"]),
 ("AWS and Azure","S3, Lambda and Redshift on AWS, and Azure Data Lake Storage for lake-based pipelines.","Built ETL for the Johnson & Johnson APAC data lake migration.",["Capgemini","Johnson & Johnson","Kipi.bi"]),
 ("Data quality","Source-to-target reconciliation, lineage and dependency analysis, and root-cause work on defects.","Built SQL checks across sources, warehouse layers, marts and Tableau dashboards.",["Kipi.ai","KetteQ"]),
]
roles = [
 ("Jan 2026 to now","Senior Data Engineer","Kipi.ai, for client GoHealth, remote",["Maintain the Snowflake pipelines behind healthcare analytics and enterprise reporting.","Harmonize data from several EMR systems, including Epic and eClinicalWorks.","Built SQL reconciliation that finds duplicates and mismatches across sources, warehouse layers, marts and Tableau dashboards.","Added REST API sources with error handling, audit logging, monitoring and alerts."],["Snowflake","SQL","REST APIs","Epic","eClinicalWorks","Tableau","SCD","Data lineage"]),
 ("Oct 2025 to Jan 2026","Senior Lead Data Engineer","V4C.ai, for client Kymeta, Pune",["Led a team of seven data engineers building reusable ELT frameworks.","Designed cloud-native ingestion and transformation pipelines bringing APIs and structured sources into Snowflake.","Applied governance: column masking, access policies and standard documentation.","Contributed to about 20% lower cloud spend and 40% higher deployment reliability."],["Snowflake","SQL","Python","Azure","Git","CI/CD"]),
 ("Dec 2024 to Aug 2025","Solution Consultant","KetteQ, Noida",["Built Talend pipelines that bring Salesforce API data into analytics and reporting.","Kept Tableau dashboards trustworthy with validation and reconciliation checks.","Cut the daily batch from 45 to 18 minutes and made reporting 25% faster."],["Talend","Salesforce APIs","Tableau","SQL","Jira","Git"]),
 ("Dec 2021 to Dec 2024","Lead Engineer, promoted from Senior Software Engineer","Kipi.bi, Noida",["Engineered end-to-end pipelines with Snowflake, Fivetran, dbt, Airflow, Azure, SQL and Python.","Automated ingestion from databases, SaaS platforms and custom APIs.","Set dbt standards and code reviews, and put CI/CD in place with GitHub, GitLab and Bitbucket.","Cut ETL runtime by 60%, to under two hours nightly, and cut data-transfer costs by 25% quarter over quarter."],["Snowflake","dbt Core and Cloud","Fivetran","Airflow","Matillion","Azure","Python"]),
 ("Jan 2020 to Dec 2021","Software Engineer, promoted from Business Intelligence Intern","Capgemini India, Chandigarh",["Developed ETL and BI solutions in Informatica, Tableau, SQL and Python.","Integrated AWS S3, Azure Data Lake, flat files, Excel, SFTP, APIs and SQL and NoSQL systems into data lakes.","Monitored scheduled jobs in Control-M and supported production alerting."],["Informatica","Tableau","SQL","Python","AWS S3","ADLS Gen2","Control-M"]),
]
clients = [
 ("Intelsat","Moved legacy pipelines to Snowflake for near-real-time processing, and added CI/CD for dbt, Airflow and Python."),
 ("Myriad Genetics","Centralized healthcare data in Snowflake under HIPAA, with dbt models and dynamic data masking."),
 ("Vena Health","Automated SaaS and MongoDB ingestion with Fivetran, Snowpark and AWS Lambda for Power BI."),
 ("Johnson & Johnson","Built ETL for an APAC data lake on AWS and Redshift, and supported migration and validation."),
]
# title, note, stack, tags, status, code, live
projects = [
 ("Patient-360 governed data platform","Synthetic patient records become a governed warehouse: duplicate records merged, sensitive fields masked, layered enterprise models.","dbt, DuckDB, Splink, Streamlit, Snowflake","Snowflake","Live: stage 1 to 4","https://github.com/agshivam/patient-360",LIVE),
 ("Snowflake cost lab","Measured query and warehouse cost cuts, and a pull request that fails when a change makes queries slower or costlier.","Snowflake, dbt, GitHub Actions","Snowflake Cost","Scripts ready, live run next","https://github.com/agshivam/snowflake-cost-lab",None),
 ("Chaos-proof pipelines","A generator breaks the source on purpose. Contracts, reconciliation and alerts catch it.","Dagster, dbt tests, Python","Reliability","Code and tests done","https://github.com/agshivam/chaos-proof-pipelines","https://app-patient-lakehouse.streamlit.app/"),
 ("Job Radar","Job postings from public sources become one clean list, tagged by skill, scored against a resume and sent as alerts.","Python, DuckDB, Streamlit, Telegram","Reliability","Code and tests done","https://github.com/agshivam/job-radar","https://job-radar-dashboard.streamlit.app/"),
 ("Portable platform layer","One dbt project runs on Snowflake and DuckDB, with Terraform and a daily automated run.","dbt, DuckDB, Terraform","Snowflake","Verified on DuckDB","https://github.com/agshivam/portable-data-platform","https://app-portable-data-platform.streamlit.app/"),
 ("Patient-360 on Databricks","The same platform rebuilt as a lakehouse and compared with the Snowflake version.","Databricks, Delta, Unity Catalog","Databricks","Code written, run next","https://github.com/agshivam/patient-360-lakehouse","https://patient-360-lakehouse.streamlit.app/"),
]
filters = ["All","Snowflake","Databricks","Reliability","Cost"]

def tool_btns():
    return "".join(f'<button class="tab" role="tab" id="tab-{i}" aria-controls="pane-{i}" aria-selected="{"true" if i==0 else "false"}" data-i="{i}">{E(t[0])}</button>' for i,t in enumerate(tools))
def tool_panes():
    out=""
    for i,(k,lead,proof,used) in enumerate(tools):
        chips="".join(f'<span class="chip">{E(u)}</span>' for u in used)
        out+=f'<div class="pane" role="tabpanel" id="pane-{i}" aria-labelledby="tab-{i}"{"" if i==0 else " hidden"}><p class="lead">{E(lead)}</p><p class="proof">{E(proof)}</p><div class="used"><span>Used at</span>{chips}</div></div>'
    return out
def role_html():
    out=""
    for i,(d,r,c,pts,tech) in enumerate(roles):
        op = i==0
        lis="".join(f'<li>{E(p)}</li>' for p in pts)
        ch="".join(f'<span class="chip">{E(t)}</span>' for t in tech)
        out+=f'''<div class="role{' open' if op else ''}"><div class="rail"><div class="dot"></div><div class="line"></div></div><div class="rbody">
<button class="rolebtn" aria-expanded="{'true' if op else 'false'}" aria-controls="rp-{i}"><span class="dates num">{E(d)}</span><span class="rt"><span class="rname">{E(r)}</span><span class="rco">{E(c)}</span></span><span class="chev" aria-hidden="true"><svg width="18" height="18" viewBox="0 0 18 18"><path d="M4 7l5 5 5-5" fill="none" stroke="#5B6778" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></span></button>
<div class="rpanel" id="rp-{i}"><div class="rin"><ul class="pts">{lis}</ul><div class="chips">{ch}</div></div></div></div></div>'''
    return out
def client_html():
    return "".join(f'<div class="client"><span class="cname">{E(n)}</span><span class="cnote">{E(t)}</span></div>' for n,t in clients)
def proj_html():
    out=""
    for t,n,s,tags,st,code,live in projects:
        links=f'<a href="{code}" rel="noopener">Code</a>'
        if live: links+=f'<a href="{live}" rel="noopener">Live report</a>'
        else: links+='<span class="soon">Report and video coming soon</span>'
        badge='<span class="badge live">'+E(st)+'</span>' if live else '<span class="badge">'+E(st)+'</span>'
        out+=f'<article class="pcard" data-tags="{E(tags)}"><div class="bar"></div>{badge}<h3>{E(t)}</h3><p>{E(n)}</p><span class="stack">{E(s)}</span><div class="plinks">{links}</div></article>'
    return out
def filter_html():
    return "".join(f'<button class="tab" aria-pressed="{"true" if i==0 else "false"}" data-f="{f}">{f}</button>' for i,f in enumerate(filters))

CSS = """
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:#F6F7F9;color:#0F1B2D;font-family:'IBM Plex Sans',system-ui,-apple-system,'Segoe UI',sans-serif;-webkit-font-smoothing:antialiased}
a{color:#1F6F8B;text-underline-offset:3px}a:hover{color:#164F63}
a:focus-visible,button:focus-visible,input:focus-visible,textarea:focus-visible{outline:2px solid #1F6F8B;outline-offset:3px}
h1,h2,h3{margin:0;font-weight:500;letter-spacing:-.8px;color:#0F1B2D}
p{margin:0}
.num{font-variant-numeric:tabular-nums}
.wrap{position:relative;width:100%;max-width:1120px;margin:0 auto;padding:0 24px}
.btn{display:inline-block;padding:13px 22px;border-radius:10px;font-weight:500;font-size:15px;text-decoration:none;font-family:inherit;cursor:pointer;border:0;transition:transform .15s ease,box-shadow .15s ease}
.btn:hover{transform:translateY(-2px);box-shadow:0 8px 20px rgba(15,27,45,.14)}
.btn.dark{background:#0F1B2D;color:#fff}.btn.dark:hover{color:#fff}
.btn.light{border:1px solid #B8C0CC;color:#0F1B2D;background:#fff}
.field{width:100%;padding:13px 14px;border-radius:10px;border:1px solid #CBD1DA;background:#fff;font-family:inherit;font-size:15px;color:#0F1B2D;transition:border-color .15s ease,box-shadow .15s ease}
.field:focus{border-color:#1F6F8B;box-shadow:0 0 0 4px rgba(31,111,139,.14);outline:0}
.tab{font-family:inherit;font-size:14px;font-weight:500;padding:8px 14px;border-radius:999px;cursor:pointer;background:#fff;color:#3E4A5C;border:1px solid #D3D9E1;transition:background .2s ease,color .2s ease,border-color .2s ease}
.tab:hover{border-color:#0F1B2D}
.tab[aria-selected=true],.tab[aria-pressed=true]{background:#0F1B2D;color:#fff;border-color:#0F1B2D}
.chip{padding:5px 11px;border-radius:999px;background:#EEF1F5;font-size:13px;color:#3E4A5C}
.orb{position:absolute;border-radius:50%;pointer-events:none;animation:drift 26s ease-in-out infinite;will-change:transform}
.o1{top:-220px;right:-160px;width:720px;height:720px;background:radial-gradient(circle,rgba(31,111,139,.20) 0%,rgba(31,111,139,0) 68%)}
.o2{top:120px;left:-260px;width:640px;height:640px;background:radial-gradient(circle,rgba(110,98,220,.14) 0%,rgba(110,98,220,0) 68%);animation-delay:-9s}
@keyframes drift{0%{transform:translate(0,0)}50%{transform:translate(40px,30px)}100%{transform:translate(0,0)}}
.top{position:sticky;top:0;z-index:10;background:rgba(246,247,249,.82);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);border-bottom:1px solid rgba(225,229,235,.9)}
.top .in2{max-width:1120px;margin:0 auto;padding:14px 24px;display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:12px}
.brand{font-weight:600;font-size:17px}
.nav{display:flex;flex-wrap:wrap;align-items:center;gap:22px;font-size:15px}
.nav a{color:#5B6778;text-decoration:none}.nav a:hover{color:#0F1B2D}
.nav a.res{padding:8px 14px;border-radius:8px;border:1px solid #B8C0CC;color:#0F1B2D;font-weight:500}
header.hero{display:flex;flex-wrap:wrap;gap:56px;align-items:center;padding:80px 0 72px}
.hl{flex:1 1 500px;min-width:0;display:flex;flex-direction:column;gap:26px}
.where{font-size:16px;color:#5B6778}
h1{font-size:clamp(42px,6.6vw,80px);line-height:1.03;letter-spacing:-2.2px;background:linear-gradient(115deg,#0F1B2D 40%,#1F6F8B 100%);-webkit-background-clip:text;background-clip:text;color:transparent}
.sub{font-size:19px;line-height:1.65;color:#3E4A5C;max-width:560px}
.row{display:flex;flex-wrap:wrap;gap:12px}
.links{display:flex;flex-wrap:wrap;gap:24px;font-size:15px}
.card{flex:1 1 440px;min-width:0;background:#fff;border:1px solid #E1E5EB;border-radius:20px;padding:26px;box-shadow:0 1px 2px rgba(15,27,45,.04),0 24px 56px rgba(15,27,45,.08);display:flex;flex-direction:column;gap:20px}
.card .ct{font-size:20px;font-weight:600;letter-spacing:-.3px}
.card .cs{font-size:14px;color:#5B6778;margin-top:4px;display:block}
.tabs{display:flex;flex-wrap:wrap;gap:8px}
.panes{min-height:190px}
.pane{display:flex;flex-direction:column;gap:14px;animation:pane .35s ease both}
.pane[hidden]{display:none}
.pane .lead{font-size:17px;line-height:1.6}
.pane .proof{font-size:15px;line-height:1.6;color:#3E4A5C;padding:12px 14px;border-radius:10px;background:#EEF5F8}
.used{display:flex;flex-wrap:wrap;gap:8px;align-items:center}.used>span:first-child{font-size:13px;color:#5B6778}
@keyframes pane{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}
@keyframes rise{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:none}}
.in{animation:rise .8s cubic-bezier(.2,.7,.2,1) both}
.d1{animation-delay:.05s}.d2{animation-delay:.15s}.d3{animation-delay:.25s}.d4{animation-delay:.35s}.d5{animation-delay:.45s}
.results{display:flex;flex-wrap:wrap;border-top:1px solid #E1E5EB;border-bottom:1px solid #E1E5EB;background:rgba(255,255,255,.5)}
.res1{flex:1 1 220px;padding:32px 24px;display:flex;flex-direction:column;gap:6px}
.res1:first-child{padding-left:0}.res1:last-child{padding-right:0}
.big{font-size:52px;font-weight:500;letter-spacing:-1.5px;line-height:1}
.res1 .cap{font-size:15px;line-height:1.5;color:#5B6778}
@property --n{syntax:'<integer>';initial-value:0;inherits:false}
@keyframes count{from{--n:0}}
.cnt{animation:count 1.5s cubic-bezier(.2,.7,.2,1) both;counter-reset:n var(--n)}
.cnt::before{content:counter(n)}
section.sec{scroll-margin-top:80px;padding:96px 0 24px;display:flex;flex-direction:column;gap:36px}
.sh{display:flex;flex-direction:column;gap:10px}
h2{font-size:clamp(30px,4vw,40px)}
.sh p{font-size:17px;line-height:1.6;color:#5B6778;max-width:600px}
.role{display:flex;gap:22px}
.rail{display:flex;flex-direction:column;align-items:center;flex:0 0 16px;padding-top:12px}
.dot{width:12px;height:12px;border-radius:50%;background:#F6F7F9;border:2px solid #9AA5B5;transition:all .25s ease}
.role.open .dot{background:#1F6F8B;border-color:#1F6F8B;box-shadow:0 0 0 5px rgba(31,111,139,.18)}
.line{flex:1;width:2px;background:#D6DBE3;margin-top:6px}
.rbody{flex:1;min-width:0;padding-bottom:28px}
.rolebtn{all:unset;box-sizing:border-box;width:100%;cursor:pointer;display:flex;flex-wrap:wrap;align-items:center;gap:6px 24px;padding:6px 0}
.rolebtn:focus-visible{outline:2px solid #1F6F8B;outline-offset:3px;border-radius:6px}
.dates{flex:0 0 168px;font-size:15px;color:#1F6F8B;font-weight:500}
.rt{flex:1 1 280px;display:flex;flex-direction:column;gap:2px}
.rname{font-size:20px;font-weight:600;line-height:1.3}.rco{font-size:15px;color:#5B6778}
.chev{display:inline-flex;transition:transform .3s ease}
.role.open .chev{transform:rotate(180deg)}
.rpanel{display:grid;grid-template-rows:0fr;transition:grid-template-rows .35s ease}
.role.open .rpanel{grid-template-rows:1fr}
.rin{overflow:hidden;min-height:0;display:flex;flex-direction:column;gap:16px}
.pts{list-style:none;margin:0;padding:18px 0 0;display:flex;flex-direction:column;gap:10px}
.pts li{display:flex;gap:12px;font-size:16px;line-height:1.6;color:#3E4A5C}
.pts li::before{content:"\\203A";color:#1F6F8B}
.chips{display:flex;flex-wrap:wrap;gap:8px;padding-bottom:6px}
.edu{display:flex;gap:22px}.edu .rail{padding-top:12px}
.edu .e2{flex:1;display:flex;flex-wrap:wrap;gap:6px 24px;padding:6px 0}
.clients{display:flex;flex-wrap:wrap;gap:14px}
.client{flex:1 1 240px;padding:22px;border-radius:14px;border:1px solid #E1E5EB;display:flex;flex-direction:column;gap:8px;transition:background .2s ease,border-color .2s ease}
.client:hover{background:#fff;border-color:#CBD1DA}
.cname{font-size:18px;font-weight:600}.cnote{font-size:15px;line-height:1.6;color:#3E4A5C}
.grid{display:flex;flex-wrap:wrap;gap:18px}
.pcard{flex:1 1 300px;max-width:100%;background:#fff;border:1px solid #E1E5EB;border-radius:16px;padding:26px;display:flex;flex-direction:column;gap:12px;overflow:hidden;position:relative;transition:transform .22s ease,box-shadow .22s ease,border-color .22s ease}
.pcard:hover{transform:translateY(-5px);box-shadow:0 18px 44px rgba(15,27,45,.11);border-color:#B8C0CC}
.pcard[hidden]{display:none}
.pcard .bar{position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,#1F6F8B,#6E62DC)}
.pcard h3{font-size:21px;font-weight:600;line-height:1.3;letter-spacing:-.3px}
.pcard p{font-size:15px;line-height:1.6;color:#3E4A5C;flex:1}
.stack{font-size:13px;color:#5B6778}
.badge{align-self:flex-start;font-size:12px;font-weight:500;padding:3px 10px;border-radius:999px;background:#EEF1F5;color:#5B6778}
.badge.live{background:#E3F3EA;color:#1D6B43}
.plinks{display:flex;flex-wrap:wrap;gap:18px;font-size:15px;padding-top:10px;border-top:1px solid #EEF1F5}
.soon{font-size:14px;color:#8A94A4}
.banner{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:18px;padding:24px 28px;border-radius:16px;background:#0F1B2D;color:#fff;text-decoration:none;transition:transform .22s ease,box-shadow .22s ease}
.banner:hover{transform:translateY(-5px);box-shadow:0 18px 44px rgba(15,27,45,.2);color:#fff}
.banner .bt{display:flex;flex-direction:column;gap:4px}.banner b{font-size:20px;font-weight:600}.banner span span{font-size:15px;color:#B8C4D6}
.banner .go{font-size:15px;font-weight:500;color:#7FD3E6}
.contact{display:flex;flex-wrap:wrap;gap:48px}
.form{flex:1 1 420px;min-width:0;background:#fff;border:1px solid #E1E5EB;border-radius:20px;padding:28px;box-shadow:0 1px 2px rgba(15,27,45,.04),0 20px 48px rgba(15,27,45,.06);display:flex;flex-direction:column;gap:16px}
.form label{font-size:14px;color:#3E4A5C;display:block;margin-bottom:6px}
.form textarea{resize:vertical}
.hp{position:absolute;left:-9999px;opacity:0;height:0;width:0}
.msg{font-size:15px;line-height:1.5}.msg.err{color:#A12B2B}
.done[hidden]{display:none}
.done{padding:12px 0;display:flex;flex-direction:column;gap:8px}.done b{font-size:22px;font-weight:600}.done span{font-size:16px;line-height:1.6;color:#3E4A5C}
.clist{flex:1 1 300px;min-width:0;display:flex;flex-direction:column}
.crow{display:flex;justify-content:space-between;align-items:center;gap:16px;padding:18px 0;border-top:1px solid #E1E5EB;text-decoration:none;color:#0F1B2D}
.crow:first-child{border-top:0;padding-top:0}.crow:last-child{border-bottom:1px solid #E1E5EB}
.crow .k{display:flex;flex-direction:column;gap:3px;min-width:0}
.crow .k small{font-size:14px;color:#5B6778}.crow .lbl{font-size:17px;overflow-wrap:anywhere}
.crow .arr{color:#1F6F8B;transition:transform .2s ease}
a.crow:hover .arr{transform:translateX(6px)}a.crow:hover .lbl{color:#1F6F8B}
.copy{font-family:inherit;font-size:14px;font-weight:500;padding:8px 14px;border-radius:8px;border:1px solid #B8C0CC;background:#fff;color:#0F1B2D;cursor:pointer;flex:0 0 auto}
.mail{color:#0F1B2D;text-decoration:none}.mail:hover{color:#1F6F8B}
footer{padding:32px 0 64px;border-top:1px solid #E1E5EB;font-size:14px;color:#5B6778;line-height:1.6;margin-top:48px}
@media (max-width:640px){.dates{flex-basis:100%}.role{gap:14px}header.hero{padding:48px 0 48px;gap:36px}.big{font-size:44px}.res1,.res1:first-child,.res1:last-child{padding:24px 12px 24px 0}}
@media (prefers-reduced-motion:reduce){.in,.cnt,.orb,.pane{animation:none}html{scroll-behavior:auto}.btn,.pcard,.banner,.rpanel{transition:none}}
"""

JS = """
(function(){
  var KEY="__WEB3FORMS_KEY__",TO="__EMAIL__";
  function $(s,r){return (r||document).querySelector(s)}
  function $$(s,r){return Array.prototype.slice.call((r||document).querySelectorAll(s))}
  // tool tabs
  var tabs=$$('[role=tab]');
  tabs.forEach(function(t){t.addEventListener('click',function(){pick(+t.dataset.i)});
    t.addEventListener('keydown',function(e){var i=+t.dataset.i;if(e.key==='ArrowRight')pick((i+1)%tabs.length,1);if(e.key==='ArrowLeft')pick((i+tabs.length-1)%tabs.length,1)})});
  function pick(i,f){tabs.forEach(function(t,j){t.setAttribute('aria-selected',j===i?'true':'false');t.tabIndex=j===i?0:-1;$('#pane-'+j).hidden=j!==i});if(f)tabs[i].focus()}
  tabs.forEach(function(t,j){t.tabIndex=j===0?0:-1});
  // roles
  $$('.rolebtn').forEach(function(b){b.addEventListener('click',function(){
    var r=b.closest('.role'),open=!r.classList.contains('open');
    $$('.role').forEach(function(x){x.classList.remove('open');$('.rolebtn',x).setAttribute('aria-expanded','false')});
    if(open){r.classList.add('open');b.setAttribute('aria-expanded','true')}})});
  // filters
  $$('[data-f]').forEach(function(b){b.addEventListener('click',function(){
    var f=b.dataset.f;$$('[data-f]').forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false')});
    $$('.pcard').forEach(function(c){c.hidden=!(f==='All'||c.dataset.tags.split(' ').indexOf(f)!==-1)})})});
  // copy email
  var cb=$('#copy');if(cb)cb.addEventListener('click',function(){
    try{navigator.clipboard.writeText(TO)}catch(e){}
    cb.textContent='Copied';setTimeout(function(){cb.textContent='Copy'},2000)});
  // contact form
  var form=$('#cform');
  if(form)form.addEventListener('submit',function(e){
    e.preventDefault();
    var name=$('#f-name').value.trim(),mail=$('#f-mail').value.trim(),msg=$('#f-msg').value.trim(),note=$('#note'),btn=$('#send');
    if($('#botcheck').checked)return;
    if(!name||!mail||!msg){note.className='msg err';note.textContent='Please fill in your name, email and message.';return}
    if(KEY.indexOf('__')===0){
      location.href='mailto:'+TO+'?subject='+encodeURIComponent('Message from '+name)+'&body='+encodeURIComponent(msg+'\\n\\n'+name+' ('+mail+')');
      return}
    btn.disabled=true;btn.textContent='Sending';note.className='msg';note.textContent='';
    fetch('https://api.web3forms.com/submit',{method:'POST',headers:{'Content-Type':'application/json',Accept:'application/json'},
      body:JSON.stringify({access_key:KEY,subject:'Portfolio message from '+name,from_name:'Portfolio site',name:name,email:mail,message:msg})})
    .then(function(r){return r.json()}).then(function(d){
      if(d.success){form.style.display='none';$('#thanks').hidden=false}else{throw new Error(d.message||'failed')}})
    .catch(function(){btn.disabled=false;btn.textContent='Send message';note.className='msg err';
      note.innerHTML='Could not send. Please email <a href="mailto:'+TO+'">'+TO+'</a> directly.'});
  });
})();
"""

def build(key="__WEB3FORMS_KEY__"):
    js = JS.replace("__WEB3FORMS_KEY__", key).replace("__EMAIL__", EMAIL)
    ld = json.dumps({"@context":"https://schema.org","@type":"Person","name":"Shivam Agarwal","jobTitle":"Senior Data Engineer","url":SITE,
        "sameAs":["https://www.linkedin.com/in/shivamagarwal-/","https://github.com/agshivam","https://x.com/deyogiShivamAg"],
        "knowsAbout":["Snowflake","dbt","Fivetran","Python","Airflow","AWS","Data engineering"]})
    fav = "data:image/svg+xml," + "%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%230F1B2D'/%3E%3Ctext x='32' y='43' font-family='Arial' font-size='30' font-weight='700' fill='%237FD3E6' text-anchor='middle'%3ESA%3C/text%3E%3C/svg%3E"
    desc = "Senior data engineer with six years building Snowflake, dbt and Fivetran platforms across SaaS, telecom and enterprise clients. Projects, journey, resume and contact."
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Shivam Agarwal, Senior Data Engineer</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{SITE}">
<meta property="og:type" content="website">
<meta property="og:title" content="Shivam Agarwal, Senior Data Engineer">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{SITE}">
<meta name="twitter:card" content="summary">
<meta name="theme-color" content="#F6F7F9">
<link rel="icon" href="{fav}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<script type="application/ld+json">{ld}</script>
<style>{CSS}</style>
</head>
<body>
<div style="position:relative;overflow:hidden">
<div class="orb o1"></div><div class="orb o2"></div>
<nav class="top"><div class="in2"><span class="brand">Shivam Agarwal</span>
<div class="nav"><a href="#journey">Journey</a><a href="#projects">Projects</a><a href="#contact">Contact</a><a class="res" href="{RESUME}" download>Resume</a></div></div></nav>
<main class="wrap">
<header class="hero">
<div class="hl">
<span class="where in d1">Shivam Agarwal, Gurugram, India</span>
<h1 class="in d2">Senior data engineer, building Snowflake platforms that last.</h1>
<p class="sub in d3">Six years designing and tuning cloud data pipelines, warehouses and analytics models across SaaS, telecom and enterprise clients.</p>
<div class="row in d4"><a class="btn dark" href="{RESUME}" download>Download resume</a><a class="btn light" href="#contact">Get in touch</a></div>
<div class="links in d5"><a href="https://www.linkedin.com/in/shivamagarwal-/" rel="me noopener">LinkedIn</a><a href="https://github.com/agshivam" rel="me noopener">GitHub</a><a href="https://x.com/deyogiShivamAg" rel="me noopener">X</a></div>
</div>
<div class="card in d3">
<div><span class="ct">What I use, and where</span><span class="cs">Pick a tool to see how I've used it</span></div>
<div class="tabs" role="tablist" aria-label="Tools">{tool_btns()}</div>
<div class="panes">{tool_panes()}</div>
</div>
</header>
<section class="results" aria-label="Results">
<div class="res1" aria-label="60 percent shorter nightly ETL runtime"><span class="big num"><span class="cnt" style="--n:60"></span>%</span><span class="cap">shorter nightly ETL runtime at Kipi.bi</span></div>
<div class="res1" aria-label="18 minute daily batch, down from 45"><span class="big num"><span class="cnt" style="--n:18"></span> min</span><span class="cap">daily batch, down from 45, at KetteQ</span></div>
<div class="res1" aria-label="6 million records per hour"><span class="big num"><span class="cnt" style="--n:6"></span>M</span><span class="cap">records per hour, near real time, for Intelsat</span></div>
<div class="res1" aria-label="Led a team of 7 engineers"><span class="big num"><span class="cnt" style="--n:7"></span></span><span class="cap">data engineers led at V4C.ai</span></div>
</section>
<section id="journey" class="sec">
<div class="sh"><h2>My journey</h2><p>From business intelligence intern to leading engineers. Select a role to see what I did there.</p></div>
<div>{role_html()}
<div class="edu"><div class="rail"><div class="dot"></div></div><div class="e2"><span class="dates num">Graduated 2020</span><span class="rt"><span class="rname">B.Tech, Computer Science Engineering</span><span class="rco">Chandigarh Group of Colleges, Landran, Punjab</span></span></div></div>
</div>
</section>
<section class="sec" style="padding-top:56px" aria-label="Client engagements"><h2 style="font-size:26px">Client engagements</h2><div class="clients">{client_html()}</div></section>
<section id="projects" class="sec">
<div class="sh"><h2>Projects</h2><p>Six platforms built on public or synthetic data. Each has its code, a short decision record, a live report and a walkthrough video. Finished ones are marked live.</p></div>
<div class="row" role="group" aria-label="Filter projects" style="gap:8px">{filter_html()}</div>
<div class="grid">{proj_html()}</div>
<a class="banner" href="{LIVE}" rel="noopener"><span class="bt"><b>Live Patient-360 report</b><span><span>Synthetic records: encounters, readmissions, data quality checks, duplicate-record merge.</span></span></span><span class="go">Open report &#8594;</span></a>
</section>
<section id="contact" class="sec" style="padding-bottom:56px">
<div class="sh"><h2>Let's talk</h2><p>Hiring for a data role, or have a platform to build? Send a message and I'll reply by email.</p></div>
<div class="contact">
<div class="form">
<form id="cform" novalidate style="display:flex;flex-direction:column;gap:16px">
<div><label for="f-name">Your name</label><input id="f-name" class="field" type="text" autocomplete="name" required></div>
<div><label for="f-mail">Your email</label><input id="f-mail" class="field" type="email" autocomplete="email" required></div>
<div><label for="f-msg">Message</label><textarea id="f-msg" class="field" rows="5" required></textarea></div>
<input type="checkbox" id="botcheck" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
<div><button id="send" class="btn dark" type="submit">Send message</button></div>
<div id="note" class="msg" role="status" aria-live="polite"></div>
</form>
<div id="thanks" class="done" hidden><b>Message sent</b><span>Thank you. I'll reply to the email you provided.</span></div>
</div>
<div class="clist">
<div class="crow"><span class="k"><small>Email</small><a class="lbl mail" href="mailto:{EMAIL}?subject=Opportunity%20for%20Shivam">{EMAIL}</a></span><button id="copy" class="copy" type="button">Copy</button></div>
<a class="crow" href="{WA}" rel="noopener"><span class="k"><small>WhatsApp</small><span class="lbl">Message me on WhatsApp</span></span><span class="arr" aria-hidden="true">&#8594;</span></a>
<a class="crow" href="{RESUME}" download><span class="k"><small>Resume</small><span class="lbl">Download as PDF</span></span><span class="arr" aria-hidden="true">&#8594;</span></a>
<a class="crow" href="https://www.linkedin.com/in/shivamagarwal-/" rel="noopener"><span class="k"><small>LinkedIn</small><span class="lbl">Connect with me</span></span><span class="arr" aria-hidden="true">&#8594;</span></a>
<a class="crow" href="https://github.com/agshivam" rel="noopener"><span class="k"><small>GitHub</small><span class="lbl">See my code</span></span><span class="arr" aria-hidden="true">&#8594;</span></a>
<a class="crow" href="https://x.com/deyogiShivamAg" rel="noopener"><span class="k"><small>X</small><span class="lbl">Follow me</span></span><span class="arr" aria-hidden="true">&#8594;</span></a>
</div>
</div>
</section>
<footer>All projects on this site use public or synthetic data. No employer data is used.</footer>
</main>
</div>
<script>{js}</script>
</body>
</html>
'''

if __name__ == "__main__":
    import sys
    key = sys.argv[1] if len(sys.argv) > 1 else "__WEB3FORMS_KEY__"
    open("index.html", "w", encoding="utf-8").write(build(key))
    print("wrote index.html", len(build(key)), "bytes")
