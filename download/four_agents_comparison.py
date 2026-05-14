# -*- coding: utf-8 -*-
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily

# Register fonts
pdfmetrics.registerFont(TTFont('Times New Roman', '/usr/share/fonts/truetype/english/Times-New-Roman.ttf'))
registerFontFamily('Times New Roman', normal='Times New Roman', bold='Times New Roman')

# Create document
doc = SimpleDocTemplate(
    "/home/z/my-project/download/four_agents_comparison.pdf",
    pagesize=A4,
    title="AI Coding Agents: Complete Comparison",
    author="Z.ai",
    creator="Z.ai",
    subject="Cline vs Cursor vs Kilocode vs OpenCode comparison"
)

# Define styles
styles = getSampleStyleSheet()

title_style = ParagraphStyle(name='TitleStyle', fontName='Times New Roman', fontSize=20, leading=26, alignment=TA_CENTER, spaceAfter=16)
subtitle_style = ParagraphStyle(name='SubtitleStyle', fontName='Times New Roman', fontSize=12, leading=16, alignment=TA_CENTER, spaceAfter=24)
h1_style = ParagraphStyle(name='H1Style', fontName='Times New Roman', fontSize=14, leading=18, alignment=TA_LEFT, spaceBefore=14, spaceAfter=8)
h2_style = ParagraphStyle(name='H2Style', fontName='Times New Roman', fontSize=11, leading=14, alignment=TA_LEFT, spaceBefore=8, spaceAfter=5)
body_style = ParagraphStyle(name='BodyStyle', fontName='Times New Roman', fontSize=9.5, leading=13, alignment=TA_JUSTIFY, spaceAfter=5)
cell_style = ParagraphStyle(name='CellStyle', fontName='Times New Roman', fontSize=8, leading=10, alignment=TA_LEFT)
header_style = ParagraphStyle(name='HeaderStyle', fontName='Times New Roman', fontSize=8, leading=10, alignment=TA_CENTER, textColor=colors.white)

story = []

# Title
story.append(Spacer(1, 40))
story.append(Paragraph("<b>AI Coding Agents: Complete Comparison</b>", title_style))
story.append(Paragraph("Cline vs Cursor vs Kilocode vs OpenCode<br/>Finding the Optimal Solution with OpenRouter Integration", subtitle_style))
story.append(Spacer(1, 20))

# Executive Summary
story.append(Paragraph("<b>1. Executive Summary</b>", h1_style))
story.append(Paragraph(
    "This comprehensive analysis compares four leading AI coding agents: Cline, Cursor, Kilocode, and OpenCode. "
    "OpenCode emerges as a particularly compelling option with 95K+ GitHub stars and 2.5 million monthly developers, "
    "positioning it as one of the most popular open-source AI coding tools. The comparison evaluates each platform against "
    "the core requirements: cloud-based inference, top-tier model access, strong coding capabilities, and generous free usage "
    "through OpenRouter integration. OpenCode distinguishes itself with a terminal-first approach, built-in free models, "
    "and support for 75+ LLM providers while remaining completely open-source.",
    body_style
))

# Main Comparison Table
story.append(Paragraph("<b>2. Feature Comparison Matrix</b>", h1_style))

main_data = [
    [Paragraph('<b>Feature</b>', header_style), Paragraph('<b>Cline</b>', header_style), Paragraph('<b>Cursor</b>', header_style), Paragraph('<b>Kilocode</b>', header_style), Paragraph('<b>OpenCode</b>', header_style)],
    [Paragraph('<b>Type</b>', cell_style), Paragraph('VS Code Extension', cell_style), Paragraph('Standalone IDE', cell_style), Paragraph('VS Code/JetBrains/CLI', cell_style), Paragraph('Terminal/Desktop/IDE', cell_style)],
    [Paragraph('<b>GitHub Stars</b>', cell_style), Paragraph('~40K', cell_style), Paragraph('N/A (closed)', cell_style), Paragraph('~15K', cell_style), Paragraph('<b>95K+</b>', cell_style)],
    [Paragraph('<b>Users</b>', cell_style), Paragraph('5M+', cell_style), Paragraph('~2M+', cell_style), Paragraph('1M+', cell_style), Paragraph('<b>2.5M/month</b>', cell_style)],
    [Paragraph('<b>Open Source</b>', cell_style), Paragraph('Apache 2.0', cell_style), Paragraph('No', cell_style), Paragraph('Apache 2.0', cell_style), Paragraph('Apache 2.0', cell_style)],
    [Paragraph('<b>Free Models</b>', cell_style), Paragraph('Via OpenRouter', cell_style), Paragraph('Limited requests', cell_style), Paragraph('Via Gateway', cell_style), Paragraph('<b>Included</b>', cell_style)],
    [Paragraph('<b>LLM Providers</b>', cell_style), Paragraph('10+', cell_style), Paragraph('Built-in only', cell_style), Paragraph('500+ Gateway', cell_style), Paragraph('<b>75+</b>', cell_style)],
    [Paragraph('<b>OpenRouter</b>', cell_style), Paragraph('Full support', cell_style), Paragraph('No', cell_style), Paragraph('#1 ranked', cell_style), Paragraph('Full support', cell_style)],
    [Paragraph('<b>LSP Support</b>', cell_style), Paragraph('Via VS Code', cell_style), Paragraph('Built-in', cell_style), Paragraph('Via VS Code', cell_style), Paragraph('<b>Auto-load</b>', cell_style)],
    [Paragraph('<b>MCP/Agents</b>', cell_style), Paragraph('Full MCP', cell_style), Paragraph('Limited', cell_style), Paragraph('Full MCP', cell_style), Paragraph('Custom agents', cell_style)],
    [Paragraph('<b>Terminal CLI</b>', cell_style), Paragraph('No', cell_style), Paragraph('No', cell_style), Paragraph('Yes', cell_style), Paragraph('<b>Primary (TUI)</b>', cell_style)],
    [Paragraph('<b>Desktop App</b>', cell_style), Paragraph('No', cell_style), Paragraph('Yes (IDE)', cell_style), Paragraph('No', cell_style), Paragraph('Yes', cell_style)],
    [Paragraph('<b>JetBrains</b>', cell_style), Paragraph('No', cell_style), Paragraph('No', cell_style), Paragraph('Yes', cell_style), Paragraph('No', cell_style)]
]

main_table = Table(main_data, colWidths=[70, 75, 75, 85, 90])
main_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1F4E79')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('BACKGROUND', (0, 1), (0, -1), colors.HexColor('#E8EEF4')),
    ('BACKGROUND', (1, 1), (-1, 1), colors.white),
    ('BACKGROUND', (1, 2), (-1, 2), colors.HexColor('#F5F5F5')),
    ('BACKGROUND', (1, 3), (-1, 3), colors.white),
    ('BACKGROUND', (1, 4), (-1, 4), colors.HexColor('#F5F5F5')),
    ('BACKGROUND', (1, 5), (-1, 5), colors.white),
    ('BACKGROUND', (1, 6), (-1, 6), colors.HexColor('#F5F5F5')),
    ('BACKGROUND', (1, 7), (-1, 7), colors.white),
    ('BACKGROUND', (1, 8), (-1, 8), colors.HexColor('#F5F5F5')),
    ('BACKGROUND', (1, 9), (-1, 9), colors.white),
    ('BACKGROUND', (1, 10), (-1, 10), colors.HexColor('#F5F5F5')),
    ('BACKGROUND', (1, 11), (-1, 11), colors.white),
    ('BACKGROUND', (1, 12), (-1, 12), colors.HexColor('#F5F5F5')),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('LEFTPADDING', (0, 0), (-1, -1), 4),
    ('RIGHTPADDING', (0, 0), (-1, -1), 4),
    ('TOPPADDING', (0, 0), (-1, -1), 3),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
]))

story.append(Spacer(1, 8))
story.append(main_table)
story.append(Spacer(1, 4))
story.append(Paragraph("<i>Table 1: Feature comparison across all four AI coding agents</i>", 
    ParagraphStyle(name='Caption', fontName='Times New Roman', fontSize=8, alignment=TA_CENTER)))
story.append(Spacer(1, 12))

# OpenCode Deep Dive
story.append(Paragraph("<b>3. OpenCode - The Terminal-First Powerhouse</b>", h1_style))
story.append(Paragraph(
    "OpenCode has rapidly become one of the most popular open-source AI coding agents, boasting 95,000+ GitHub stars "
    "and serving 2.5 million developers monthly. The platform takes a terminal-first approach with a native Terminal User Interface (TUI), "
    "while also offering desktop applications and IDE extensions. This architecture appeals to developers who prefer keyboard-driven "
    "workflows and want AI assistance without leaving the terminal environment.",
    body_style
))

story.append(Paragraph("<b>3.1 Key Differentiators</b>", h2_style))
story.append(Paragraph(
    "<b>Built-in Free Models:</b> Unlike Cline or Kilocode which require external provider setup, OpenCode includes free models out of the box. "
    "New users can start coding immediately without configuring API keys. The OpenCode Zen tier provides curated, optimized models specifically "
    "tested and benchmarked for coding agent workflows.",
    body_style
))
story.append(Paragraph(
    "<b>LSP Integration:</b> OpenCode automatically loads the appropriate Language Server Protocols for the LLM, enabling intelligent code understanding "
    "without manual configuration. This ensures the AI has proper context about syntax, types, and project structure.",
    body_style
))
story.append(Paragraph(
    "<b>Provider Agnostic:</b> OpenCode acts as a neutral layer between developers and AI models, supporting 75+ LLM providers including OpenAI, Anthropic, Google, "
    "OpenRouter, and local models via Ollama. Users can switch providers seamlessly based on cost, availability, or performance preferences.",
    body_style
))
story.append(Paragraph(
    "<b>Parallel Execution:</b> Community feedback indicates OpenCode excels at parallel execution and subagent-related tasks compared to Cline. "
    "This makes it particularly effective for complex, multi-step operations that benefit from concurrent processing.",
    body_style
))

story.append(Paragraph("<b>3.2 Pricing Tiers</b>", h2_style))
pricing_oc = [
    [Paragraph('<b>Tier</b>', header_style), Paragraph('<b>Cost</b>', header_style), Paragraph('<b>Features</b>', header_style)],
    [Paragraph('Free (Core)', cell_style), Paragraph('$0', cell_style), Paragraph('Open-source, free models included, BYO API keys', cell_style)],
    [Paragraph('OpenCode Go', cell_style), Paragraph('$5 first month, then $10/mo', cell_style), Paragraph('Generous limits, open-source models, reliable access', cell_style)],
    [Paragraph('OpenCode Zen', cell_style), Paragraph('$20/mo', cell_style), Paragraph('Curated optimized coding models, transparent pricing', cell_style)],
    [Paragraph('OpenCode Black', cell_style), Paragraph('Custom', cell_style), Paragraph('All world\'s best models (Claude, GPT, Gemini), paused', cell_style)]
]
pricing_table = Table(pricing_oc, colWidths=[90, 100, 220])
pricing_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1F4E79')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('BACKGROUND', (0, 1), (-1, 1), colors.HexColor('#E8F4E8')),
    ('BACKGROUND', (0, 2), (-1, 2), colors.white),
    ('BACKGROUND', (0, 3), (-1, 3), colors.HexColor('#F5F5F5')),
    ('BACKGROUND', (0, 4), (-1, 4), colors.white),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('LEFTPADDING', (0, 0), (-1, -1), 5),
    ('RIGHTPADDING', (0, 0), (-1, -1), 5),
    ('TOPPADDING', (0, 0), (-1, -1), 4),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
]))
story.append(Spacer(1, 6))
story.append(pricing_table)
story.append(Spacer(1, 4))
story.append(Paragraph("<i>Table 2: OpenCode pricing tiers</i>", 
    ParagraphStyle(name='Caption', fontName='Times New Roman', fontSize=8, alignment=TA_CENTER)))
story.append(Spacer(1, 10))

# Comparison on Requirements
story.append(Paragraph("<b>4. Requirements Evaluation</b>", h1_style))

req_data = [
    [Paragraph('<b>Requirement</b>', header_style), Paragraph('<b>Cline</b>', header_style), Paragraph('<b>Cursor</b>', header_style), Paragraph('<b>Kilocode</b>', header_style), Paragraph('<b>OpenCode</b>', header_style)],
    [Paragraph('Cloud Inference', cell_style), Paragraph('Via OpenRouter', cell_style), Paragraph('Via Cursor cloud', cell_style), Paragraph('Via Gateway/OR', cell_style), Paragraph('Via providers', cell_style)],
    [Paragraph('Top-tier Models', cell_style), Paragraph('Any (BYO)', cell_style), Paragraph('Built-in GPT/Claude', cell_style), Paragraph('500+ models', cell_style), Paragraph('75+ providers', cell_style)],
    [Paragraph('Coding Quality', cell_style), Paragraph('Excellent', cell_style), Paragraph('Excellent', cell_style), Paragraph('Excellent', cell_style), Paragraph('Excellent', cell_style)],
    [Paragraph('Free Usage', cell_style), Paragraph('Via OR free models', cell_style), Paragraph('Limited (50-500)', cell_style), Paragraph('$20 credits + OR', cell_style), Paragraph('<b>Included + OR</b>', cell_style)],
    [Paragraph('Setup Ease', cell_style), Paragraph('Medium', cell_style), Paragraph('Easy', cell_style), Paragraph('Easy', cell_style), Paragraph('<b>Very Easy</b>', cell_style)],
    [Paragraph('GitHub Integration', cell_style), Paragraph('Via Git/MCP', cell_style), Paragraph('Built-in', cell_style), Paragraph('Via Git/MCP', cell_style), Paragraph('Via Git', cell_style)]
]

req_table = Table(req_data, colWidths=[75, 75, 75, 85, 90])
req_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1F4E79')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('BACKGROUND', (0, 1), (0, -1), colors.HexColor('#E8EEF4')),
    ('BACKGROUND', (1, 1), (-1, 1), colors.white),
    ('BACKGROUND', (1, 2), (-1, 2), colors.HexColor('#F5F5F5')),
    ('BACKGROUND', (1, 3), (-1, 3), colors.white),
    ('BACKGROUND', (1, 4), (-1, 4), colors.HexColor('#E8F4E8')),
    ('BACKGROUND', (1, 5), (-1, 5), colors.white),
    ('BACKGROUND', (1, 6), (-1, 6), colors.HexColor('#F5F5F5')),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('LEFTPADDING', (0, 0), (-1, -1), 4),
    ('RIGHTPADDING', (0, 0), (-1, -1), 4),
    ('TOPPADDING', (0, 0), (-1, -1), 3),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
]))

story.append(Spacer(1, 6))
story.append(req_table)
story.append(Spacer(1, 4))
story.append(Paragraph("<i>Table 3: Evaluation against original requirements</i>", 
    ParagraphStyle(name='Caption', fontName='Times New Roman', fontSize=8, alignment=TA_CENTER)))
story.append(Spacer(1, 10))

# Winner Matrix
story.append(Paragraph("<b>5. Category Winners</b>", h1_style))

winner_data = [
    [Paragraph('<b>Category</b>', header_style), Paragraph('<b>Winner</b>', header_style), Paragraph('<b>Reasoning</b>', header_style)],
    [Paragraph('Popularity', cell_style), Paragraph('<b>OpenCode</b> (95K stars)', cell_style), Paragraph('Largest open-source community and active development', cell_style)],
    [Paragraph('Free Start', cell_style), Paragraph('<b>OpenCode</b>', cell_style), Paragraph('Free models included, no API key setup required', cell_style)],
    [Paragraph('Model Selection', cell_style), Paragraph('<b>Kilocode</b> (500+)', cell_style), Paragraph('Largest model catalog via Kilo Gateway', cell_style)],
    [Paragraph('IDE Integration', cell_style), Paragraph('<b>Cursor</b>', cell_style), Paragraph('Native AI-IDE with polished experience', cell_style)],
    [Paragraph('Terminal/CLI', cell_style), Paragraph('<b>OpenCode</b>', cell_style), Paragraph('Primary TUI design, keyboard-driven workflow', cell_style)],
    [Paragraph('JetBrains Support', cell_style), Paragraph('<b>Kilocode</b>', cell_style), Paragraph('Only option with JetBrains IDE support', cell_style)],
    [Paragraph('Cost Efficiency', cell_style), Paragraph('<b>OpenCode / Cline</b>', cell_style), Paragraph('Both offer unlimited free via OpenRouter', cell_style)],
    [Paragraph('Ease of Setup', cell_style), Paragraph('<b>OpenCode</b>', cell_style), Paragraph('Works immediately with built-in free models', cell_style)],
    [Paragraph('LSP Integration', cell_style), Paragraph('<b>OpenCode</b>', cell_style), Paragraph('Auto-loads appropriate LSPs for context', cell_style)],
    [Paragraph('Parallel Execution', cell_style), Paragraph('<b>OpenCode</b>', cell_style), Paragraph('Better subagent/parallel task support', cell_style)]
]

winner_table = Table(winner_data, colWidths=[85, 100, 225])
winner_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1F4E79')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('BACKGROUND', (0, 1), (-1, 1), colors.HexColor('#E8F4E8')),
    ('BACKGROUND', (0, 2), (-1, 2), colors.HexColor('#E8F4E8')),
    ('BACKGROUND', (0, 3), (-1, 3), colors.white),
    ('BACKGROUND', (0, 4), (-1, 4), colors.white),
    ('BACKGROUND', (0, 5), (-1, 5), colors.HexColor('#E8F4E8')),
    ('BACKGROUND', (0, 6), (-1, 6), colors.white),
    ('BACKGROUND', (0, 7), (-1, 7), colors.HexColor('#E8F4E8')),
    ('BACKGROUND', (0, 8), (-1, 8), colors.HexColor('#E8F4E8')),
    ('BACKGROUND', (0, 9), (-1, 9), colors.HexColor('#E8F4E8')),
    ('BACKGROUND', (0, 10), (-1, 10), colors.HexColor('#E8F4E8')),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('LEFTPADDING', (0, 0), (-1, -1), 5),
    ('RIGHTPADDING', (0, 0), (-1, -1), 5),
    ('TOPPADDING', (0, 0), (-1, -1), 4),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
]))

story.append(Spacer(1, 6))
story.append(winner_table)
story.append(Spacer(1, 4))
story.append(Paragraph("<i>Table 4: Category winners with reasoning (green = OpenCode wins)</i>", 
    ParagraphStyle(name='Caption', fontName='Times New Roman', fontSize=8, alignment=TA_CENTER)))
story.append(Spacer(1, 10))

# Final Recommendations
story.append(Paragraph("<b>6. Final Recommendations</b>", h1_style))

story.append(Paragraph("<b>6.1 Best Overall for Free Usage: OpenCode</b>", h2_style))
story.append(Paragraph(
    "OpenCode emerges as the optimal choice for developers seeking powerful AI coding assistance without ongoing costs. "
    "With free models included out-of-the-box, 95K+ GitHub stars indicating strong community support, and support for 75+ LLM providers "
    "including OpenRouter, it offers the best combination of accessibility, capability, and cost efficiency. The terminal-first design "
    "appeals to experienced developers, while the desktop app provides options for those preferring GUI interfaces.",
    body_style
))

story.append(Paragraph("<b>6.2 Best for VS Code Users: Kilocode</b>", h2_style))
story.append(Paragraph(
    "Developers deeply integrated into the VS Code ecosystem should consider Kilocode for its seamless extension experience, "
    "$20 free signup credits, and #1 ranked OpenRouter integration. It combines the best features of Cline and Roo Code while "
    "adding unique capabilities like JetBrains support.",
    body_style
))

story.append(Paragraph("<b>6.3 Best for Maximum Control: Cline</b>", h2_style))
story.append(Paragraph(
    "Power users who prioritize complete control over their AI coding environment should choose Cline. Its mature MCP ecosystem, "
    "transparent provider relationships, and 5M+ user base make it a reliable choice for developers comfortable with configuration.",
    body_style
))

story.append(Paragraph("<b>6.4 Best for Polished IDE Experience: Cursor</b>", h2_style))
story.append(Paragraph(
    "Developers willing to pay $20/month for a refined, all-in-one experience should choose Cursor. Its native AI-IDE integration, "
    "cloud agents, and Bugbot feature provide premium capabilities at a reasonable subscription cost.",
    body_style
))

# Conclusion
story.append(Paragraph("<b>7. Conclusion</b>", h1_style))
story.append(Paragraph(
    "OpenCode represents a compelling new contender that challenges previous recommendations. Its combination of built-in free models, "
    "terminal-first design, massive community (95K+ stars), and support for 75+ providers positions it as potentially the best choice "
    "for developers seeking accessible yet powerful AI coding assistance. For users prioritizing zero-cost operation with OpenRouter integration, "
    "both OpenCode and Cline/Kilocode offer viable paths, with OpenCode having the edge in ease of setup and included free models, "
    "while Kilocode offers superior IDE integration and broader model catalog. The final choice depends on workflow preferences: "
    "terminal-centric developers should choose OpenCode, while VS Code devotees may prefer Kilocode's extension-based approach.",
    body_style
))

# Build PDF
doc.build(story)
print("PDF generated successfully!")
