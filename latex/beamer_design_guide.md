# Beamer Design Guide

Lessons learned from building presentations. Reference this when creating new slides.

## Images

### Side-by-side images
- **Match aspect ratios first.** Pre-crop images to the same ratio (e.g., 4:3) using Python/PIL before placing them. Don't rely on LaTeX trim/clip for this - it's guess and check.
- Use `columns` with equal widths (0.495 each) and no `\hspace` for minimal gap.
- Set `width=\textwidth` on both images. Equal column widths + equal aspect ratios = equal heights automatically.
- Keep originals in `figures/`, save cropped versions as `*_crop.*`.

### Cropping with Python
```python
from PIL import Image
img = Image.open('input.png')
w, h = img.size
target_ratio = 4/3
new_w = int(h * target_ratio)
trim = (w - new_w) // 2
crop = img.crop((trim, 0, w - trim, h))
crop.save('output.png')
```

### Single images
- `\includegraphics[width=0.85\textwidth]{fig}` for full-width with breathing room.
- For constrained height: `\includegraphics[height=0.65\textheight]{fig}`.
- Never use both `width` and `height` - pick one and let the other scale.

## Layout

### Margins and spacing
- Text margins: `\setbeamersize{text margin left=12mm, text margin right=12mm}`.
- The frame title rule, footline, and content should all respect these margins visually.
- Content should start close to the title rule, not float in the middle. Use `\nointerlineskip` in the frametitle template and control spacing with beamercolorbox `ht`/`dp`.

### Slide numbers / footline
- Don't use `\hfill` with `\vskip` for footlines - they clip off the page.
- Use the pattern: `\hfill{content}\hspace*{12mm}\vskip4mm` to match text margins.
- Always visually verify footline is on the page after changes.

### Frame title
- Use `beamercolorbox` for the title to get precise height/depth control.
- Put the rule in its own `beamercolorbox` to avoid artifacts.
- Pattern that works:
```latex
\setbeamertemplate{frametitle}{%
  \nointerlineskip%
  \begin{beamercolorbox}[wd=\paperwidth, leftskip=12mm, rightskip=12mm, ht=8mm, dp=1mm]{frametitle}%
    \usebeamerfont{frametitle}\insertframetitle\strut%
  \end{beamercolorbox}%
  \nointerlineskip%
  \begin{beamercolorbox}[wd=\paperwidth, ht=0.4pt, leftskip=12mm, rightskip=12mm]{rule}%
    {\color{slate400}\rule{\dimexpr\paperwidth-24mm}{0.4pt}}%
  \end{beamercolorbox}%
  \nointerlineskip%
  \vskip4pt%
}
```

## Colors

### Tailwind Slate + Blue palette
```latex
\definecolor{slate900}{RGB}{15, 23, 42}      % headings
\definecolor{slate700}{RGB}{51, 65, 85}      % body text
\definecolor{slate400}{RGB}{148, 163, 184}   % muted (rules, page numbers, sub-bullets)
\definecolor{slate100}{RGB}{241, 245, 249}   % block backgrounds
\definecolor{blue600}{RGB}{37, 99, 235}      % accent (use sparingly)
```
- Headings: slate900
- Body: slate700
- Bullets: slate900 (level 1), slate400 (level 2)
- Rules and page numbers: slate400
- Block titles: white on slate900
- Don't use blue for bullets or rules - it looks dated. Reserve blue600 for emphasis only.

## Fonts
- TeX Gyre Heros (`tgheros`) is a clean Helvetica-style sans-serif available in most TeX installs.
- Use `sfmath` package to match math font to body.
- Title: `\LARGE\bfseries`, frame titles: `\large\bfseries`, subtitles: `\normalsize\mdseries`.

## Bullets
- Level 1: filled circle (slate900)
- Level 2: open circle (slate400)
- Level 3: endash (slate400)
- Keep margins tight: `\setlength{\leftmargini}{1.2em}`

## Sources / Footnotes
- `\source{Display text}` - plain text, bottom right corner
- `\sourceurl{Display text}{https://...}` - clickable hyperlink, bottom right corner
- Both render in tiny slate400, above the page number
- Use short display text (e.g., "Archer Investor Relations, Dec 2024"), not full URLs

## General principles
- **Content over design.** Don't spend hours on styling.
- **One idea per slide.** If you're cramming, split it.
- **Equations in blocks.** Use `\begin{block}{Title}` for key equations - gives them visual weight.
- **Speaker notes after frames.** `\note{...}` right after `\end{frame}`. pdfpc reads them automatically.
- **Always verify visually.** Read the compiled PDF, don't trust the code alone.
