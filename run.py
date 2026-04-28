"""
NullCTF — Ishga tushirish nuqtasi
"""
import re
from backend.app import create_app

app = create_app()

# ── Markdown → HTML filtr (Jinja2 uchun) ───────────────────────────────────
@app.template_filter('markdown_to_html')
def markdown_to_html(text):
    """Oddiy Markdown → HTML konvertatsiya"""
    import html as html_mod

    # Avval HTML escape (xavfsizlik)
    # Lekin kod bloklari ichini saqlab qolish kerak
    lines = text.split('\n')
    result = []
    in_code_block = False
    code_buffer = []

    i = 0
    while i < len(lines):
        line = lines[i]

        # Kod bloki boshi/oxiri
        if line.startswith('```'):
            if not in_code_block:
                in_code_block = True
                lang = line[3:].strip()
                code_buffer = []
            else:
                in_code_block = False
                code = '\n'.join(code_buffer)
                code_escaped = html_mod.escape(code)
                result.append(f'<pre><code class="language-{lang}">{code_escaped}</code></pre>')
            i += 1
            continue

        if in_code_block:
            code_buffer.append(line)
            i += 1
            continue

        # Sarlavhalar
        if line.startswith('## '):
            result.append(f'<h2>{html_mod.escape(line[3:])}</h2>')
        elif line.startswith('### '):
            result.append(f'<h3>{html_mod.escape(line[4:])}</h3>')
        elif line.startswith('#### '):
            result.append(f'<h4>{html_mod.escape(line[5:])}</h4>')
        elif line.startswith('> '):
            result.append(f'<blockquote>{_inline_md(line[2:])}</blockquote>')
        elif line.startswith('- ') or line.startswith('* '):
            result.append(f'<ul><li>{_inline_md(line[2:])}</li></ul>')
        elif re.match(r'^\d+\. ', line):
            content = re.sub(r'^\d+\. ', '', line)
            result.append(f'<ol><li>{_inline_md(content)}</li></ol>')
        elif line.strip() == '':
            result.append('<br>')
        elif line.startswith('---'):
            result.append('<hr>')
        else:
            result.append(f'<p>{_inline_md(line)}</p>')

        i += 1

    # Ketma-ket ul/ol larni birlashtirish
    html_out = '\n'.join(result)
    html_out = re.sub(r'</ul>\s*<ul>', '', html_out)
    html_out = re.sub(r'</ol>\s*<ol>', '', html_out)

    return html_out


def _inline_md(text):
    """Inline markdown: **bold**, *italic*, `code`, [link](url)"""
    import html as html_mod
    text = html_mod.escape(text)
    # **bold**
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    # *italic*
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    # `code`
    text = re.sub(r'`(.+?)`', r'<code>\1</code>', text)
    # [text](url)
    text = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', text)
    return text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
