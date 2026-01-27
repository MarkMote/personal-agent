# Resume

LaTeX resume with yellow section headers matching the academic style.

## Files

- `resume.tex` - Main resume (Chief Engineer / general variant)
- `resume.pdf` - Compiled output

## Compile

```bash
# Install LaTeX if needed (Ubuntu/Debian)
sudo apt install texlive-latex-recommended texlive-fonts-recommended texlive-latex-extra

# Compile
pdflatex resume.tex
```

Or use Overleaf: upload `resume.tex` and compile there.

## Variants

To create variants:
1. Copy `resume.tex` to `resume_founder.tex` (or similar)
2. Adjust content emphasis
3. Keep same structure/formatting

## Content Updates

Key content sources in `../ref/`:
- `mark_profile.md` - Timeline, credentials, narrative hooks
- `roostr/roostr.md` - Current company details
- `pytheia/full_context.md` - Previous company details

Update citation counts periodically from Google Scholar.
