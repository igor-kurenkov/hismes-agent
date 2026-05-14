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
    "/home/z/my-project/download/cline_cursor_kilo_comparison.pdf",
    pagesize=A4,
    title="Cline vs Cursor vs Kilocode Comparison",
    author="Z.ai",
    creator="Z.ai",
    subject="Detailed comparison of top AI coding agents"
)

# Define styles
styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    name='TitleStyle',
    fontName='Times New Roman',
    fontSize=22,
    leading=28,
    alignment=TA_CENTER,
    spaceAfter=20
)

subtitle_style = ParagraphStyle(
    name='SubtitleStyle',
    fontName='Times New Roman',
    fontSize=13,
    leading=17,
    alignment=TA_CENTER,
    spaceAfter=30
)

h1_style = ParagraphStyle(
    name='H1Style',
    fontName='Times New Roman',
    fontSize=15,
    leading=19,
    alignment=TA_LEFT,
    spaceBefore=16,
    spaceAfter=10
)

h2_style = ParagraphStyle(
    name='H2Style',
    fontName='Times New Roman',
    fontSize=12,
    leading=15,
    alignment=TA_LEFT,
    spaceBefore=10,
    spaceAfter=6
)

body_style = ParagraphStyle(
    name='BodyStyle',
    fontName='Times New Roman',
    fontSize=10,
    leading=14,
    alignment=TA_JUSTIFY,
    spaceBefore=0,
    spaceAfter=6
)

cell_style = ParagraphStyle(
    name='CellStyle',
    fontName='Times New Roman',
    fontSize=8.5,
    leading=11,
    alignment=TA_LEFT
)

header_style = ParagraphStyle(
    name='HeaderStyle',
    fontName='Times New Roman',
    fontSize=9,
    leading=12,
    alignment=TA_CENTER,
    textColor=colors.white
)

story = []

# Title
story.append(Spacer(1, 50))
story.append(Paragraph("<b>Cline vs Cursor vs Kilocode</b>", title_style))
story.append(Paragraph("Comprehensive Comparison of Top AI Coding Agents<br/>With Recommendations Based on User Requirements", subtitle_style))
story.append(Spacer(1, 30))

# Executive Summary
story.append(Paragraph("<b>1. Executive Summary</b>", h1_style))
story.append(Paragraph(
    "This analysis compares three leading AI coding solutions: Cline (open-source VS Code extension), Cursor (AI-native IDE), "
    "and Kilocode (open-source fork combining Cline and Roo Code). Each platform represents a distinct philosophy: Cline prioritizes "
    "flexibility and model agnosticism, Cursor offers a polished integrated experience, and Kilocode aims to deliver the best of both "
    "worlds through unified features and built-in model access. The comparison evaluates architecture, model support, pricing, "
    "autonomous capabilities, and suitability for the user's requirements: cloud-based inference, top-tier models, strong coding abilities, "
    "and generous free usage with OpenRouter integration.",
    body_style
))

# Overview Table
story.append(Paragraph("<b>2. Quick Comparison Overview</b>", h1_style))

overview_data = [
    [
        Paragraph('<b>Feature</b>', header_style),
        Paragraph('<b>Cline</b>', header_style),
        Paragraph('<b>Cursor</b>', header_style),
        Paragraph('<b>Kilocode</b>', header_style)
    ],
    [
        Paragraph('<b>Type</b>', cell_style),
        Paragraph('VS Code Extension', cell_style),
        Paragraph('Standalone IDE (VS Code fork)', cell_style),
        Paragraph('VS Code / JetBrains / CLI', cell_style)
    ],
    [
        Paragraph('<b>Open Source</b>', cell_style),
        Paragraph('Yes (Apache 2.0)', cell_style),
        Paragraph('No (Proprietary)', cell_style),
        Paragraph('Yes (Apache 2.0)', cell_style)
    ],
    [
        Paragraph('<b>Users</b>', cell_style),
        Paragraph('5M+', cell_style),
        Paragraph('~2M+', cell_style),
        Paragraph('1M+', cell_style)
    ],
    [
        Paragraph('<b>Model Support</b>', cell_style),
        Paragraph('Any (BYO API key)', cell_style),
        Paragraph('Built-in (GPT, Claude, Gemini)', cell_style),
        Paragraph('500+ via Gateway + BYO', cell_style)
    ],
    [
        Paragraph('<b>OpenRouter</b>', cell_style),
        Paragraph('Full support', cell_style),
        Paragraph('Not directly', cell_style),
        Paragraph('#1 ranked integration', cell_style)
    ],
    [
        Paragraph('<b>Free Tier</b>', cell_style),
        Paragraph('Unlimited with free models', cell_style),
        Paragraph('Limited agent requests', cell_style),
        Paragraph('$20 free credits + free models', cell_style)
    ],
    [
        Paragraph('<b>Cloud Inference</b>', cell_style),
        Paragraph('Via provider (OpenRouter)', cell_style),
        Paragraph('Via Cursor cloud', cell_style),
        Paragraph('Via Kilo Gateway / OpenRouter', cell_style)
    ],
    [
        Paragraph('<b>MCP Support</b>', cell_style),
        Paragraph('Full', cell_style),
        Paragraph('Limited', cell_style),
        Paragraph('Full', cell_style)
    ],
    [
        Paragraph('<b>Best For</b>', cell_style),
        Paragraph('Flexibility, control, cost optimization', cell_style),
        Paragraph('Polished experience, teams', cell_style),
        Paragraph('All-in-one, quick start', cell_style)
    ]
]

overview_table = Table(overview_data, colWidths=[85, 115, 115, 115])
overview_table.setStyle(TableStyle([
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
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('LEFTPADDING', (0, 0), (-1, -1), 5),
    ('RIGHTPADDING', (0, 0), (-1, -1), 5),
    ('TOPPADDING', (0, 0), (-1, -1), 4),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
]))

story.append(Spacer(1, 10))
story.append(overview_table)
story.append(Spacer(1, 6))
story.append(Paragraph("<i>Table 1: High-level comparison of Cline, Cursor, and Kilocode</i>", 
    ParagraphStyle(name='Caption', fontName='Times New Roman', fontSize=9, alignment=TA_CENTER)))
story.append(Spacer(1, 14))

# Cline Deep Dive
story.append(Paragraph("<b>3. Cline - The Flexible Open-Source Leader</b>", h1_style))
story.append(Paragraph(
    "Cline represents the most established open-source AI coding agent, with over 5 million installations worldwide. "
    "It operates as a VS Code extension, transforming the familiar editor into an agentic coding environment. "
    "The core philosophy centers on developer control: users choose their LLM provider, configure their own API keys, "
    "and maintain complete transparency over how AI interacts with their codebase. Cline supports Plan and Act modes, "
    "allowing developers to review proposed changes before implementation, with user permission required at each step.",
    body_style
))

story.append(Paragraph("<b>3.1 Key Strengths</b>", h2_style))
story.append(Paragraph(
    "<b>Model Agnosticism:</b> Cline supports virtually any LLM provider with an OpenAI-compatible API. This includes OpenRouter, "
    "Anthropic, OpenAI, Google Gemini, AWS Bedrock, Azure, GCP Vertex, Cerebras, and local models via Ollama. "
    "Users can switch between providers based on cost, performance, or availability without changing their workflow. "
    "This flexibility makes Cline ideal for developers who want to optimize their AI spending by selecting the most "
    "cost-effective model for each task.",
    body_style
))
story.append(Paragraph(
    "<b>MCP Ecosystem:</b> The Model Context Protocol integration enables extensive extensibility. Developers can connect Cline "
    "to databases, APIs, deployment services, GitHub, testing frameworks, and custom tools through community-maintained MCP servers. "
    "This transforms Cline from a coding assistant into a comprehensive development automation platform capable of handling "
    "entire workflows from code generation to deployment.",
    body_style
))
story.append(Paragraph(
    "<b>Cost Control:</b> With Cline, users pay directly to their chosen LLM provider at provider rates. Combined with OpenRouter's "
    "free models (Llama 4 Maverick, DeepSeek R1, etc.), developers can access powerful AI coding assistance at zero ongoing cost. "
    "There are no middleman fees or subscription requirements beyond what the model provider charges.",
    body_style
))

story.append(Paragraph("<b>3.2 Limitations</b>", h2_style))
story.append(Paragraph(
    "<b>Setup Complexity:</b> Cline requires manual configuration of API keys and provider settings. While documentation is comprehensive, "
    "new users may find the initial setup more involved compared to turnkey solutions. Users must also manage their own API keys "
    "and monitor usage across providers if using multiple services.",
    body_style
))
story.append(Paragraph(
    "<b>IDE Dependence:</b> As a VS Code extension, Cline requires the VS Code editor. Developers committed to other IDEs like "
    "JetBrains products cannot use Cline directly, though alternatives like Roo Code and Kilocode address this gap.",
    body_style
))

# Cursor Deep Dive
story.append(Paragraph("<b>4. Cursor - The Polished AI-Native IDE</b>", h1_style))
story.append(Paragraph(
    "Cursor takes a fundamentally different approach as a standalone IDE built on a VS Code fork. Rather than extending an existing "
    "editor, Cursor reimagines the development environment with AI as a first-class citizen. The result is a more integrated experience "
    "where AI features feel native rather than additive. Cursor has gained significant popularity among developers who prioritize "
    "a seamless, polished experience over maximum flexibility.",
    body_style
))

story.append(Paragraph("<b>4.1 Key Strengths</b>", h2_style))
story.append(Paragraph(
    "<b>Integrated Experience:</b> Cursor's AI features are deeply woven into the editor experience. Tab completions, code generation, "
    "chat assistance, and agent mode all work together without the friction of extension boundaries. The UI is refined, with thoughtful "
    "design decisions that make AI assistance feel natural within the coding flow.",
    body_style
))
story.append(Paragraph(
    "<b>Cloud Agents:</b> Cursor's cloud agent capability allows AI to work autonomously in the background, running tasks in parallel "
    "and presenting results for review. This enables longer-running operations without blocking the developer's local environment. "
    "The Bugbot feature can automatically identify and suggest fixes for issues in the codebase.",
    body_style
))
story.append(Paragraph(
    "<b>Model Variety:</b> Cursor provides built-in access to multiple top-tier models including GPT-4, GPT-5, Claude, and Gemini. "
    "Users don't need to manage API keys or provider relationships; everything is handled through Cursor's backend. "
    "The $20/month Pro plan includes $20 worth of model usage at published rates.",
    body_style
))

story.append(Paragraph("<b>4.2 Limitations</b>", h2_style))
story.append(Paragraph(
    "<b>Closed Source:</b> Cursor is proprietary software. Users cannot inspect the codebase, contribute improvements, or customize "
    "the core functionality. This limits transparency and community-driven development compared to open-source alternatives.",
    body_style
))
story.append(Paragraph(
    "<b>Vendor Lock-in:</b> By using Cursor, developers commit to its ecosystem. The IDE must be installed separately from VS Code, "
    "and while it supports VS Code extensions, the core AI features are Cursor-specific. Migrating away requires adjusting to a "
    "different toolset.",
    body_style
))
story.append(Paragraph(
    "<b>Free Tier Constraints:</b> Cursor's free Hobby tier provides limited agent requests (approximately 50-500 depending on model). "
    "Serious development work requires the $20/month Pro subscription. Unlike Cline or Kilocode, there's no path to unlimited free usage "
    "through external providers like OpenRouter.",
    body_style
))

# Kilocode Deep Dive
story.append(Paragraph("<b>5. Kilocode - The Hybrid Innovator</b>", h1_style))
story.append(Paragraph(
    "Kilocode emerged as a fork combining the best features of Cline and Roo Code (itself a Cline fork), creating a unified platform "
    "that aims to deliver flexibility with convenience. Ranked #1 on OpenRouter and used by over 1 million developers, Kilocode has "
    "quickly established itself as a compelling option. The platform is available across VS Code, JetBrains IDEs, CLI, and Slack, "
    "offering broader platform support than either Cline or Cursor.",
    body_style
))

story.append(Paragraph("<b>5.1 Key Strengths</b>", h2_style))
story.append(Paragraph(
    "<b>Best of Both Worlds:</b> Kilocode merges Cline's robust agent capabilities with Roo Code's optimizations and faster update cycle. "
    "The result is a more refined experience that retains the flexibility of open-source software while adding convenience features "
    "like built-in model access through the Kilo Gateway.",
    body_style
))
story.append(Paragraph(
    "<b>Built-in Model Access:</b> Unlike Cline which requires users to bring their own API keys, Kilocode offers direct access to 500+ models "
    "through its Kilo Gateway. Users get $20 in free credits upon signup, and the platform offers transparent pricing that matches "
    "provider rates exactly. This eliminates setup friction while maintaining cost transparency. Kilocode also supports BYO API keys "
    "for users who prefer their own provider relationships.",
    body_style
))
story.append(Paragraph(
    "<b>Multi-Platform Support:</b> Kilocode is the only option among the three that supports JetBrains IDEs in addition to VS Code. "
    "It also offers a CLI tool and Slack integration, making it versatile across different development workflows. The App Builder "
    "feature enables rapid prototyping directly from the agent interface.",
    body_style
))
story.append(Paragraph(
    "<b>OpenRouter Integration:</b> As the #1 ranked integration on OpenRouter, Kilocode provides seamless access to free models "
    "including Llama 4 Maverick and DeepSeek R1. The platform almost always has a free model available in the gateway, "
    "enabling genuinely free usage for cost-conscious developers.",
    body_style
))

story.append(Paragraph("<b>5.2 Limitations</b>", h2_style))
story.append(Paragraph(
    "<b>Newer Platform:</b> Kilocode is younger than both Cline and Cursor. While rapid development has added many features, some users "
    "report occasional rough edges compared to the more established alternatives. The community and documentation ecosystem is still growing.",
    body_style
))
story.append(Paragraph(
    "<b>Feature Parity Challenges:</b> Combining two codebases (Cline and Roo Code) into one platform creates complexity. Some features "
    "may not work identically to their source implementations, and users familiar with Cline may need to adapt to Kilocode's variations.",
    body_style
))

# Pricing Comparison
story.append(Paragraph("<b>6. Pricing and Free Usage Analysis</b>", h1_style))

pricing_data = [
    [
        Paragraph('<b>Aspect</b>', header_style),
        Paragraph('<b>Cline</b>', header_style),
        Paragraph('<b>Cursor</b>', header_style),
        Paragraph('<b>Kilocode</b>', header_style)
    ],
    [
        Paragraph('Base Cost', cell_style),
        Paragraph('Free (extension)', cell_style),
        Paragraph('Free (Hobby tier)', cell_style),
        Paragraph('Free (extension)', cell_style)
    ],
    [
        Paragraph('Paid Tier', cell_style),
        Paragraph('N/A (pay provider directly)', cell_style),
        Paragraph('$20/month Pro', cell_style),
        Paragraph('Pay-as-you-go credits', cell_style)
    ],
    [
        Paragraph('Free Credits/Models', cell_style),
        Paragraph('Via OpenRouter free models', cell_style),
        Paragraph('50-500 agent requests/month', cell_style),
        Paragraph('$20 signup + free models', cell_style)
    ],
    [
        Paragraph('Cost with OpenRouter Free', cell_style),
        Paragraph('$0 (unlimited)', cell_style),
        Paragraph('Not supported', cell_style),
        Paragraph('$0 (unlimited)', cell_style)
    ],
    [
       Paragraph('Premium Models', cell_style),
        Paragraph('Pay provider rates', cell_style),
        Paragraph('$20 usage included in Pro', cell_style),
        Paragraph('Pay provider rates via Gateway', cell_style)
    ],
    [
        Paragraph('Maximum Free Usage', cell_style),
        Paragraph('Unlimited with free models', cell_style),
        Paragraph('Limited by requests', cell_style),
        Paragraph('Unlimited with free models', cell_style)
    ]
]

pricing_table = Table(pricing_data, colWidths=[100, 110, 105, 115])
pricing_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1F4E79')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('BACKGROUND', (0, 1), (0, -1), colors.HexColor('#E8EEF4')),
    ('BACKGROUND', (1, 1), (-1, 1), colors.white),
    ('BACKGROUND', (1, 2), (-1, 2), colors.HexColor('#F5F5F5')),
    ('BACKGROUND', (1, 3), (-1, 3), colors.white),
    ('BACKGROUND', (1, 4), (-1, 4), colors.HexColor('#E8F4E8')),
    ('BACKGROUND', (1, 5), (-1, 5), colors.white),
    ('BACKGROUND', (1, 6), (-1, 6), colors.HexColor('#E8F4E8')),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('LEFTPADDING', (0, 0), (-1, -1), 5),
    ('RIGHTPADDING', (0, 0), (-1, -1), 5),
    ('TOPPADDING', (0, 0), (-1, -1), 4),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
]))

story.append(Spacer(1, 10))
story.append(pricing_table)
story.append(Spacer(1, 6))
story.append(Paragraph("<i>Table 2: Pricing comparison with focus on free usage opportunities</i>", 
    ParagraphStyle(name='Caption', fontName='Times New Roman', fontSize=9, alignment=TA_CENTER)))
story.append(Spacer(1, 14))

# Recommendations
story.append(Paragraph("<b>7. Recommendations Based on User Requirements</b>", h1_style))

story.append(Paragraph("<b>7.1 For Maximum Free Usage with Quality Models: Kilocode or Cline</b>", h2_style))
story.append(Paragraph(
    "Both Kilocode and Cline, when paired with OpenRouter's free models, fully satisfy the original requirements. They offer cloud-based "
    "inference, access to top-tier models (Llama 4 Maverick, DeepSeek R1), excellent coding capabilities with autonomous agents, "
    "and genuinely unlimited free usage. Kilocode edges ahead with its $20 signup credits and simpler initial setup, while Cline "
    "offers maximum control and flexibility for power users willing to configure their own provider relationships.",
    body_style
))

story.append(Paragraph("<b>7.2 For Polished Experience: Cursor</b>", h2_style))
story.append(Paragraph(
    "Cursor is the best choice for developers who prioritize a refined, integrated experience and are willing to pay $20/month for "
    "serious usage. The standalone IDE provides seamless AI integration, cloud agents for background processing, and built-in access "
    "to premium models without API key management. However, it does not support OpenRouter integration, limiting free usage options.",
    body_style
))

story.append(Paragraph("<b>7.3 For JetBrains Users: Kilocode</b>", h2_style))
story.append(Paragraph(
    "Kilocode is the only option among the three that supports JetBrains IDEs (IntelliJ IDEA, PyCharm, WebStorm, etc.). Developers "
    "committed to the JetBrains ecosystem should choose Kilocode for AI coding assistance without switching editors.",
    body_style
))

story.append(Paragraph("<b>7.4 For Maximum Customization: Cline</b>", h2_style))
story.append(Paragraph(
    "Cline remains the best choice for developers who want complete control over their AI coding environment. The MCP ecosystem "
    "enables extensive customization through community-built servers, and the model-agnostic approach allows optimization across "
    "any provider. Power users comfortable with configuration will appreciate Cline's transparency and flexibility.",
    body_style
))

# Final Verdict
story.append(Paragraph("<b>8. Final Verdict</b>", h1_style))

verdict_data = [
    [
        Paragraph('<b>Criterion</b>', header_style),
        Paragraph('<b>Winner</b>', header_style),
        Paragraph('<b>Reason</b>', header_style)
    ],
    [
        Paragraph('Free Usage (with OpenRouter)', cell_style),
        Paragraph('<b>Kilocode / Cline</b> (tie)', cell_style),
        Paragraph('Both support unlimited free usage via OpenRouter free models', cell_style)
    ],
    [
        Paragraph('Ease of Setup', cell_style),
        Paragraph('<b>Kilocode</b>', cell_style),
        Paragraph('$20 free credits, built-in Gateway, no API key setup required', cell_style)
    ],
    [
        Paragraph('Model Selection', cell_style),
        Paragraph('<b>Kilocode</b>', cell_style),
        Paragraph('500+ models via Gateway + BYO support', cell_style)
    ],
    [
        Paragraph('IDE Integration', cell_style),
        Paragraph('<b>Cursor</b>', cell_style),
        Paragraph('Native AI-IDE experience, polished UI', cell_style)
    ],
    [
        Paragraph('Platform Support', cell_style),
        Paragraph('<b>Kilocode</b>', cell_style),
        Paragraph('VS Code, JetBrains, CLI, Slack', cell_style)
    ],
    [
        Paragraph('Extensibility', cell_style),
        Paragraph('<b>Cline / Kilocode</b> (tie)', cell_style),
        Paragraph('Full MCP support for custom tools', cell_style)
    ],
    [
        Paragraph('Open Source', cell_style),
        Paragraph('<b>Cline / Kilocode</b> (tie)', cell_style),
        Paragraph('Both are Apache 2.0 licensed', cell_style)
    ],
    [
        Paragraph('Overall Best for Requirements', cell_style),
        Paragraph('<b>Kilocode</b>', cell_style),
        Paragraph('Best balance of free access, features, and convenience', cell_style)
    ]
]

verdict_table = Table(verdict_data, colWidths=[130, 90, 210])
verdict_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1F4E79')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('BACKGROUND', (0, 1), (-1, 1), colors.HexColor('#E8F4E8')),
    ('BACKGROUND', (0, 2), (-1, 2), colors.white),
    ('BACKGROUND', (0, 3), (-1, 3), colors.HexColor('#E8F4E8')),
    ('BACKGROUND', (0, 4), (-1, 4), colors.white),
    ('BACKGROUND', (0, 5), (-1, 5), colors.HexColor('#E8F4E8')),
    ('BACKGROUND', (0, 6), (-1, 6), colors.white),
    ('BACKGROUND', (0, 7), (-1, 7), colors.HexColor('#E8F4E8')),
    ('BACKGROUND', (0, 8), (-1, 8), colors.HexColor('#D4EDDA')),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('LEFTPADDING', (0, 0), (-1, -1), 5),
    ('RIGHTPADDING', (0, 0), (-1, -1), 5),
    ('TOPPADDING', (0, 0), (-1, -1), 4),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
]))

story.append(Spacer(1, 10))
story.append(verdict_table)
story.append(Spacer(1, 6))
story.append(Paragraph("<i>Table 3: Category winners with reasoning</i>", 
    ParagraphStyle(name='Caption', fontName='Times New Roman', fontSize=9, alignment=TA_CENTER)))
story.append(Spacer(1, 14))

# Conclusion
story.append(Paragraph("<b>9. Conclusion</b>", h1_style))
story.append(Paragraph(
    "For the user's specific requirements - cloud-based inference, top-tier models, strong coding capabilities, and generous free usage - "
    "<b>Kilocode emerges as the optimal choice</b>. It combines the open-source flexibility of Cline with built-in convenience features, "
    "offers the broadest platform support including JetBrains IDEs, provides $20 in free credits upon signup, and maintains seamless "
    "OpenRouter integration for unlimited access to free models. Cline remains an excellent alternative for developers who prefer "
    "maximum control and are comfortable managing their own provider relationships. Cursor, while offering the most polished experience, "
    "does not support the OpenRouter-based free usage strategy and requires a subscription for serious development work.",
    body_style
))
story.append(Paragraph(
    "The rapid evolution of AI coding tools has produced multiple viable options, each with distinct strengths. "
    "Kilocode's positioning as a superset of Cline and Roo Code features, combined with its built-in model gateway and cross-platform support, "
    "makes it the most versatile and accessible option for developers seeking powerful AI assistance without ongoing costs. "
    "The open-source nature ensures long-term sustainability and community-driven improvement, addressing concerns about vendor lock-in "
    "while still providing the convenience that accelerates developer onboarding.",
    body_style
))

# Build PDF
doc.build(story)
print("PDF generated successfully!")
