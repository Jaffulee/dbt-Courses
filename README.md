<p><a href="https://jaffulee.github.io/Jaffulee/">Visit my website</a></p>

<hr/>

<h1>Course Transcript Extraction &amp; Markdown Course Builder (dbt Learning Content)</h1>

<p>
This repository contains small, focused Python utilities to:
</p>
<ul>
  <li>Extract and organize transcripts from raw HTML-like text exports (dbt Fundamentals).</li>
  <li>Parse a course <code>slug</code> JSON plus captions JSON files and render a single, structured Markdown document (e.g. “Refactoring SQL for Modularity”).</li>
</ul>

<p>
<strong>Note:</strong> This is intended to facilitate personal learning. Please use the official course pages for the authoritative learning experience and materials.
</p>

<p>
<a href="https://www.getdbt.com/dbt-assets/certifications/dbt-certificate-study-guide">dbt Study Guide resource</a>
and 
<a href="https://learn.getdbt.com/learn/learning-path/dbt-certified-developer">dbt Certified Developer path</a>
</p>

<hr/>

<h2>Overview</h2>

<p>There are two primary workflows in this repo:</p>
<ol>
  <li>
    <strong>dbt Fundamentals transcript extraction</strong>: reads one or more HTML-like text files from
    <code>response/fundamentals/</code>, extracts transcript/name pairs via regex, cleans escape sequences, and writes:
    <ul>
      <li>a combined transcript file, and</li>
      <li>individual transcript files per lesson</li>
    </ul>
    into <code>dbt Scripts/dbt Fundamentals Scripts/</code>.
  </li>
  <li>
    <strong>Course Markdown builder (slug + captions)</strong>: reads a course “slug” JSON (course structure/content) plus caption JSON payloads,
    aligns video topics to captions via a hashed asset id, and renders a full Markdown document with a nested ToC.
  </li>
</ol>

<hr/>

<h2>Features</h2>

<ul>
  <li>
    <strong>Transcript extraction (dbt Fundamentals)</strong>
    <ul>
      <li>Regex-based extraction of <code>name</code> and <code>transcript</code> fields from HTML-like source text.</li>
      <li>De-duplicates transcript entries while preserving first occurrence and order.</li>
      <li>Converts escaped sequences (e.g. literal <code>\n</code>) into real newlines for readability.</li>
      <li>Writes both combined and per-lesson transcript files with filesystem-safe filenames.</li>
    </ul>
  </li>
  <li>
    <strong>Slug + captions parsing (course_parser package)</strong>
    <ul>
      <li>Loads a course slug JSON into ordered sections → lessons → topics.</li>
      <li>Converts HTML bodies to Markdown via <code>course_parser.content_cleaner.html_to_markdown</code>.</li>
      <li>Indexes captions from nested JSON shapes and associates them to video topics by hashed asset id.</li>
      <li>Renders a single Markdown file with stable anchors and a nested contents list.</li>
      <li>Optionally writes a ToC-only Markdown file for quick inspection.</li>
    </ul>
  </li>
</ul>

<hr/>

<h2>Setup</h2>

<p>
This is a Python project packaged as <code>course_parser</code> (see <code>setup.py</code>). The repository context does not define external dependencies.
</p>

<p>Install the package locally (optional):</p>
<pre><code>python -m pip install -e .
</code></pre>

<p>
If you only plan to run the scripts in-place, you can typically run them directly with your Python interpreter.
</p>

<hr/>

<h2>Usage</h2>

<h3>1) Extract dbt Fundamentals transcripts</h3>

<p><strong>Inputs</strong></p>
<ul>
  <li>Place one or more <code>.txt</code>, <code>.html</code>, or <code>.htm</code> files in:</li>
</ul>

<pre><code>response/fundamentals/
</code></pre>

<p>
The extractor expects HTML-like text containing embedded transcript and name metadata compatible with the script’s regex patterns.
</p>

<p><strong>Run</strong></p>
<pre><code>python dbt_fundamentals_captions.py
</code></pre>

<p><strong>Outputs</strong></p>
<ul>
  <li>Combined transcript file(s):</li>
</ul>
<pre><code>dbt Scripts/dbt Fundamentals Scripts/&lt;input_stem&gt;_all_transcripts.txt
</code></pre>

<ul>
  <li>Individual transcript files:</li>
</ul>
<pre><code>dbt Scripts/dbt Fundamentals Scripts/Individual Scripts/&lt;input_stem&gt;/
  &lt;input_stem&gt;_transcript_01_&lt;safe_title&gt;.txt
  ...
</code></pre>

<hr/>

<h3>2) Build a full course Markdown document (Refactoring SQL for Modularity)</h3>

<p><strong>Inputs</strong></p>
<ul>
  <li>Course slug JSON (course structure + bodies):</li>
</ul>
<pre><code>response/refactoring SQL for modularity/slug/refactoring SQL for modularity.json
</code></pre>

<ul>
  <li>Caption JSON files somewhere under <code>response/refactoring SQL for modularity/</code> (excluding the <code>slug</code> directory).</li>
</ul>

<p><strong>Run</strong></p>
<pre><code>python scripts/build_course_markdown_refactoring_sql_for_modularity.py
</code></pre>

<p><strong>Outputs</strong></p>
<ul>
  <li>Full rendered course Markdown:</li>
</ul>
<pre><code>dbt Scripts/refactoring SQL for modularity/Refactoring SQL for Modularity (dbt Studio).md
</code></pre>

<ul>
  <li>ToC-only file:</li>
</ul>
<pre><code>dbt Scripts/refactoring SQL for modularity/Contents.md
</code></pre>

<hr/>

<h2>Project Structure</h2>

<pre><code>course_parser/
  __init__.py
  captions_loader.py
  content_cleaner.py
  course_structure.py
  html_to_md.py
  io_utils.py
  markdown_render.py
  slug_loader.py
dbt Scripts/
  dbt Fundamentals Scripts/
    Individual Scripts/
      dbt_fundamentals/
        dbt_fundamentals_transcript_01_C1-L1-meet your instructor.txt
        ...
    dbt_fundamentals_all_transcripts.txt
  refactoring SQL for modularity/
    Contents.md
    Refactoring SQL for Modularity (dbt Studio).md
response/
  fundamentals/
    .gitkeep
  refactoring SQL for modularity/
    slug/
      .gitkeep
    .gitkeep
scripts/
  build_course_markdown_refactoring_sql_for_modularity.py
  inspect_captions_payload.py
  inspect_slug_payload.py
.gitignore
README.md
dbt_fundamentals_captions.py
inspect_json_keys.py
setup.py
</code></pre>

<hr/>

<h2>Notes / Design</h2>

<h3>Transcript extraction (<code>dbt_fundamentals_captions.py</code>)</h3>
<ul>
  <li>Uses regex patterns to extract transcript blocks and names, then aligns them by truncating to the shortest list to avoid index errors.</li>
  <li>De-duplicates names and transcripts independently (preserving first occurrence), matching the current behavior in the script.</li>
  <li>Applies <code>unicode_escape</code> decoding to turn literal backslash sequences into readable formatting (e.g. <code>\n</code> → newline).</li>
  <li>Creates safe filenames for cross-platform output.</li>
</ul>

<h3>Course Markdown builder (<code>course_parser</code>)</h3>
<ul>
  <li>
    <strong>Slug parsing</strong> (<code>course_parser/slug_loader.py</code>): loads sections and lessons in the order they appear in the slug JSON, and converts topic bodies to Markdown.
  </li>
  <li>
    <strong>Captions indexing</strong> (<code>course_parser/captions_loader.py</code>): walks arbitrary nested JSON, finds media objects (heuristic: dicts containing <code>hashedId</code>),
    extracts caption text, and indexes by <code>hashedId</code>.
  </li>
  <li>
    <strong>Rendering</strong> (<code>course_parser/markdown_render.py</code>): creates a nested ToC and stable anchors, then renders section → lesson → topics in order.
    Video topics append extracted captions when present.
  </li>
  <li>
    <strong>PDF topics</strong>: if a topic type is <code>pdfViewer</code> and an <code>asset</code> is present, the renderer includes a Markdown link and a note that access may be permission-restricted.
  </li>
  <li>
    The final output includes a small metadata footer (course title, generation time in UTC, and source paths used).
  </li>
</ul>

<hr/>

<h2>Contributing</h2>

<p>Contributions are welcome if they improve parsing reliability, structure, or maintainability.</p>
<ul>
  <li>Preserve existing folder structure expectations.</li>
  <li>Avoid introducing unnecessary external dependencies.</li>
  <li>Keep outputs deterministic and filesystem-safe.</li>
</ul>
