<h1>dbt Fundamentals Transcript Extraction & Organization</h1>

Note: This is purely to facilitate learning, please visit the official learning pages for the courses.

These scripts are designed to read the json outputs for the course and the captions, stored in the relevant areas, to generate one combined file for learning.

<p>
<a href="https://www.getdbt.com/dbt-assets/certifications/dbt-certificate-study-guide">dbt Study Guide resourse</a>
</p>

<hr/>

<h2>Overview</h2>
<p>
This repository contains a lightweight Python utility and supporting files for extracting, cleaning, and organizing dbt Fundamentals course transcripts from raw HTML-like text sources.
</p>

<p>
The primary script processes transcript data, cleans escape sequences, aligns transcript titles with content, and outputs both combined and individual transcript files in a structured directory layout. The repository also includes generated transcript outputs and supplementary study resources.
</p>

<hr/>

<h2>Features</h2>
<ul>
  <li>Extracts transcript text and corresponding titles using regex-based parsing.</li>
  <li>Removes duplicate transcript entries while preserving order.</li>
  <li>Cleans escaped characters (e.g., <code>\n</code>) into readable formatting.</li>
  <li>Generates:
    <ul>
      <li>A combined transcript file per input source.</li>
      <li>Individual transcript files per lesson with safe filenames.</li>
    </ul>
  </li>
  <li>Organizes outputs into a structured folder hierarchy.</li>
  <li>Uses only Python standard library modules (no external dependencies).</li>
</ul>

<hr/>

<h2>Setup</h2>
<p>No external dependencies are required.</p>

<p>Ensure you have Python installed (3.9+ recommended due to type hints and pathlib usage).</p>

<p>Repository structure should remain intact so the script can locate input and output directories correctly.</p>

<hr/>

<h2>Usage</h2>

<h3>1. Prepare Input</h3>
<p>
Place one or more HTML-like transcript text files into:
</p>

<pre><code>response/fundamentals/</code></pre>

<p>
Each file should contain transcript and name metadata in a format compatible with the script’s regex patterns.
</p>

<h3>2. Run the Script</h3>

<pre><code>python dbt_fundamentals_captions.py</code></pre>

<h3>3. Generated Outputs</h3>
<p>The script will:</p>
<ul>
  <li>Create a combined transcript file for each input file.</li>
  <li>Create individual transcript files for each extracted lesson.</li>
  <li>Store outputs in:</li>
</ul>

<pre><code>dbt Scripts/dbt Fundamentals Scripts/</code></pre>

<p>Individual files are organized into:</p>

<pre><code>dbt Scripts/dbt Fundamentals Scripts/Individual Scripts/&lt;input_filename&gt;/</code></pre>

<hr/>

<h2>Project Structure</h2>

<pre><code>.
├── dbt_fundamentals_captions.py
├── README.md
├── response/
│   └── fundamentals/
│       └── html_example.txt
├── dbt Scripts/
│   └── dbt Fundamentals Scripts/
│       ├── html_example_all_transcripts.txt
│       └── Individual Scripts/
│           └── html_example/
│               ├── html_example_transcript_01_...
│               └── ...
└── Additional Resourses/
    └── dbt_Certificate Study Guide_Analytics_Engineer_Developer.pdf
</code></pre>

<hr/>

<h2>How It Works</h2>

<h3>Extraction</h3>
<ul>
  <li>Regex patterns locate transcript text blocks and associated titles.</li>
  <li>Duplicate entries are removed while preserving first occurrence.</li>
  <li>Transcript/title pairs are aligned safely to avoid mismatches.</li>
</ul>

<h3>Cleaning</h3>
<ul>
  <li>Escaped characters (e.g., newline sequences) are converted into readable formatting.</li>
  <li>Filenames are sanitized to be cross-platform safe.</li>
</ul>

<h3>Output Generation</h3>
<ul>
  <li>Combined transcript file per source input.</li>
  <li>Individual transcript files named using lesson titles.</li>
  <li>Clear folder structure for easy navigation and reuse.</li>
</ul>

<hr/>

<h2>Notes / Design</h2>
<ul>
  <li>Uses only Python standard library modules: <code>re</code>, <code>pathlib</code>, and <code>typing</code>.</li>
  <li>Designed for repeatable processing of transcript sources.</li>
  <li>Output folders are created automatically if they do not exist.</li>
  <li>If transcript/title counts differ, processing safely truncates to the shortest set.</li>
</ul>

<hr/>

<h2>Contributing</h2>
<p>
Contributions are welcome if they improve parsing reliability, structure, or maintainability.
</p>

<p>When contributing:</p>
<ul>
  <li>Preserve existing folder structure expectations.</li>
  <li>Avoid introducing unnecessary external dependencies.</li>
  <li>Keep outputs deterministic and filesystem-safe.</li>
</ul>

<hr/>

<h2>Summary</h2>
<p>
This repository provides a focused utility for transforming raw dbt Fundamentals transcript exports into clean, structured text files suitable for study, reference, or documentation workflows.
</p>
