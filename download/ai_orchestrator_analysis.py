# -*- coding: utf-8 -*-
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily

pdfmetrics.registerFont(TTFont('Times New Roman', '/usr/share/fonts/truetype/english/Times-New-Roman.ttf'))
registerFontFamily('Times New Roman', normal='Times New Roman', bold='Times New Roman')

doc = SimpleDocTemplate(
    "/home/z/my-project/download/ai_orchestrator_analysis.pdf",
    pagesize=A4,
    title="AI Agent Orchestrator Analysis",
    author="Z.ai",
    creator="Z.ai",
    subject="General purpose AI agent platforms with OpenRouter support"
)

styles = getSampleStyleSheet()
title_style = ParagraphStyle(name='TitleStyle', fontName='Times New Roman', fontSize=20, leading=26, alignment=TA_CENTER, spaceAfter=16)
subtitle_style = ParagraphStyle(name='SubtitleStyle', fontName='Times New Roman', fontSize=12, leading=16, alignment=TA_CENTER, spaceAfter=24)
h1_style = ParagraphStyle(name='H1Style', fontName='Times New Roman', fontSize=14, leading=18, alignment=TA_LEFT, spaceBefore=14, spaceAfter=8)
h2_style = ParagraphStyle(name='H2Style', fontName='Times New Roman', fontSize=11, leading=14, alignment=TA_LEFT, spaceBefore=8, spaceAfter=5)
body_style = ParagraphStyle(name='BodyStyle', fontName='Times New Roman', fontSize=9.5, leading=13, alignment=TA_JUSTIFY, spaceAfter=5)
cell_style = ParagraphStyle(name='CellStyle', fontName='Times New Roman', fontSize=8, leading=10, alignment=TA_LEFT)
header_style = ParagraphStyle(name='HeaderStyle', fontName='Times New Roman', fontSize=8, leading=10, alignment=TA_CENTER, textColor=colors.white)

story = []
story.append(Spacer(1, 40))
story.append(Paragraph("<b>AI Agent Orchestrator Analysis</b>", title_style))
story.append(Paragraph("General Purpose AI Agents with OpenRouter Support<br/>Optimized for MacBook Pro 2017-2018", subtitle_style))
story.append(Spacer(1, 20))

story.append(Paragraph("<b>1. Executive Summary</b>", h1_style))
story.append(Paragraph(
    "This analysis identifies optimal AI agent orchestrators for general-purpose use with three key constraints: maximum free usage through OpenRouter integration, minimal hardware requirements compatible with MacBook Pro 2017-2018, and quality GUI interface suitable for non-power-users. The critical insight is that when using OpenRouter for cloud-based LLM inference, local hardware requirements drop dramatically—only the UI layer needs to run locally, not the AI models themselves. This enables even older hardware to provide excellent AI assistant experiences.",
    body_style
))

story.append(Paragraph("<b>2. Key Platforms Analyzed</b>", h1_style))
platform_data = [
    [Paragraph('<b>Platform</b>', header_style), Paragraph('<b>Type</b>', header_style), Paragraph('<b>RAM Req</b>', header_style), Paragraph('<b>OpenRouter</b>', header_style), Paragraph('<b>GUI</b>', header_style), Paragraph('<b>Free</b>', header_style)],
    [Paragraph('<b>PicoClaw</b>', cell_style), Paragraph('AI Assistant', cell_style), Paragraph('<b>10-20 MB</b>', cell_style), Paragraph('Likely', cell_style), Paragraph('Chat', cell_style), Paragraph('Yes', cell_style)],
    [Paragraph('<b>Open WebUI</b>', cell_style), Paragraph('Chat Platform', cell_style), Paragraph('300-500 MB', cell_style), Paragraph('Yes', cell_style), Paragraph('Web UI', cell_style), Paragraph('Yes', cell_style)],
    [Paragraph('<b>LibreChat</b>', cell_style), Paragraph('Chat Platform', cell_style), Paragraph('500 MB', cell_style), Paragraph('Yes', cell_style), Paragraph('Web UI', cell_style), Paragraph('Yes', cell_style)],
    [Paragraph('<b>Dify</b>', cell_style), Paragraph('Agent Builder', cell_style), Paragraph('1-2 GB', cell_style), Paragraph('Yes', cell_style), Paragraph('Visual', cell_style), Paragraph('Sandbox', cell_style)],
    [Paragraph('<b>Flowise</b>', cell_style), Paragraph('Agent Builder', cell_style), Paragraph('1-2 GB', cell_style), Paragraph('Yes', cell_style), Paragraph('Visual', cell_style), Paragraph('Yes', cell_style)],
    [Paragraph('<b>n8n</b>', cell_style), Paragraph('Workflow Auto', cell_style), Paragraph('512 MB', cell_style), Paragraph('Yes', cell_style), Paragraph('Visual', cell_style), Paragraph('Yes', cell_style)],
    [Paragraph('<b>OpenClaw</b>', cell_style), Paragraph('AI Assistant', cell_style), Paragraph('8-16 GB', cell_style), Paragraph('Yes', cell_style), Paragraph('Chat', cell_style), Paragraph('Yes', cell_style)]
]
platform_table = Table(platform_data, colWidths=[75, 65, 60, 60, 50, 50])
platform_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1F4E79')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('BACKGROUND', (0, 1), (-1, 1), colors.HexColor('#E8F4E8')),
    ('BACKGROUND', (0, 2), (-1, 2), colors.HexColor('#E8F4E8')),
    ('BACKGROUND', (0, 3), (-1, 3), colors.HexColor('#E8F4E8')),
    ('BACKGROUND', (0, 4), (-1, 4), colors.white),
    ('BACKGROUND', (0, 5), (-1, 5), colors.white),
    ('BACKGROUND', (0, 6), (-1, 6), colors.white),
    ('BACKGROUND', (0, 7), (-1, 7), colors.HexColor('#FFF3CD')),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('LEFTPADDING', (0, 0), (-1, -1), 4),
    ('RIGHTPADDING', (0, 0), (-1, -1), 4),
    ('TOPPADDING', (0, 0), (-1, -1), 3),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
]))
story.append(Spacer(1, 8))
story.append(platform_table)
story.append(Spacer(1, 4))
story.append(Paragraph("<i>Table 1: Platform comparison (green = optimal for constraints)</i>", ParagraphStyle(name='Caption', fontName='Times New Roman', fontSize=8, alignment=TA_CENTER)))
story.append(Spacer(1, 12))

story.append(Paragraph("<b>3. Detailed Platform Analysis</b>", h1_style))
story.append(Paragraph("<b>3.1 PicoClaw - Ultra-Lightweight Champion</b>", h2_style))
story.append(Paragraph(
    "PicoClaw is an ultra-lightweight personal AI assistant inspired by OpenClaw, designed to run on minimal hardware. It requires less than 10-20 MB of RAM and boots in approximately 1 second even on a 0.6 GHz processor. The architecture supports RISC-V, ARM64, and x86 platforms, making it incredibly versatile. PicoClaw is written in Go and distributed as a single binary, eliminating complex dependencies.",
    body_style
))
story.append(Paragraph(
    "<b>Hardware Fit:</b> Ideal for MacBook Pro 2017-2018. The 10-20 MB RAM footprint is negligible even on systems with 8 GB RAM. No GPU required as inference happens via API providers.",
    body_style
))
story.append(Paragraph(
    "<b>OpenRouter Status:</b> As a lightweight variant of OpenClaw, PicoClaw likely inherits OpenClaw's flexible LLM provider support. Users should verify OpenRouter configuration during setup.",
    body_style
))

story.append(Paragraph("<b>3.2 Open WebUI - The Polished Choice</b>", h2_style))
story.append(Paragraph(
    "Open WebUI (formerly Ollama WebUI) is one of the most popular self-hosted AI chat interfaces with 50K+ GitHub stars. It provides a ChatGPT-like experience with a polished web UI. The platform itself requires only 300-500 MB RAM when using external LLM providers—substantially less than running local models. For users connecting to OpenRouter, Open WebUI serves as an excellent front-end without the hardware burden of model inference.",
    body_style
))
story.append(Paragraph(
    "<b>Hardware Fit:</b> Excellent for MacBook Pro 2017-2018. With 8 GB RAM, running Open WebUI plus the operating system leaves ample headroom. The web interface is familiar and intuitive for users accustomed to ChatGPT.",
    body_style
))
story.append(Paragraph(
    "<b>OpenRouter Integration:</b> Fully supported. Open WebUI can connect to any OpenAI-compatible API, including OpenRouter. Configuration involves adding the OpenRouter API endpoint and key in settings.",
    body_style
))

story.append(Paragraph("<b>3.3 LibreChat - The Enterprise Option</b>", h2_style))
story.append(Paragraph(
    "LibreChat is an open-source AI chat platform with 35K+ GitHub stars that unifies all major AI providers in a single interface. It supports RAG (Retrieval Augmented Generation), plugins, and multi-modal capabilities. The platform is designed for self-hosting with privacy focus. Resource requirements are modest at approximately 500 MB RAM for the interface itself.",
    body_style
))
story.append(Paragraph(
    "<b>Hardware Fit:</b> Good for MacBook Pro 2017-2018. The platform runs as a Node.js application with MongoDB, which adds some overhead compared to simpler alternatives.",
    body_style
))
story.append(Paragraph(
    "<b>OpenRouter Integration:</b> Fully supported with dedicated documentation. OpenRouter is listed as a compatible provider in LibreChat's configuration options.",
    body_style
))

story.append(Paragraph("<b>3.4 Dify - Visual Agent Builder</b>", h2_style))
story.append(Paragraph(
    "Dify is a production-ready platform for building agentic workflows with visual tools. It supports RAG pipelines, multiple LLM providers, and has a plugin marketplace. Dify offers both cloud service (Sandbox plan with 200 free GPT-4 calls) and self-hosted Community Edition. The self-hosted version is completely free but requires Docker deployment.",
    body_style
))
story.append(Paragraph(
    "<b>Hardware Fit:</b> Moderate for MacBook Pro 2017-2018. Dify requires Docker which adds overhead. Recommended for systems with 16 GB RAM, though possible with 8 GB if other applications are minimal.",
    body_style
))
story.append(Paragraph(
    "<b>OpenRouter Integration:</b> Available through Dify's plugin marketplace. The OpenRouter plugin enables access to hundreds of models through Dify's visual workflow builder.",
    body_style
))

story.append(Paragraph("<b>3.5 n8n - Workflow Automation Platform</b>", h2_style))
story.append(Paragraph(
    "n8n is an open-source workflow automation platform (alternative to Zapier) with built-in AI capabilities. It has a dedicated OpenRouter node for LLM integration. The Self-hosted AI Starter Kit provides templates for quickly building AI workflows. n8n excels at orchestrating multi-step automations combining AI with other services.",
    body_style
))
story.append(Paragraph(
    "<b>Hardware Fit:</b> Good for MacBook Pro 2017-2018. The platform itself requires approximately 512 MB RAM. Self-hosting via Docker is straightforward.",
    body_style
))
story.append(Paragraph(
    "<b>OpenRouter Integration:</b> Native support with dedicated OpenRouter Chat Model node. Direct integration without custom configuration.",
    body_style
))

story.append(Paragraph("<b>4. Requirements Evaluation</b>", h1_style))
req_data = [
    [Paragraph('<b>Requirement</b>', header_style), Paragraph('<b>PicoClaw</b>', header_style), Paragraph('<b>Open WebUI</b>', header_style), Paragraph('<b>LibreChat</b>', header_style), Paragraph('<b>Dify</b>', header_style), Paragraph('<b>n8n</b>', header_style)],
    [Paragraph('Max Free Usage', cell_style), Paragraph('Likely', cell_style), Paragraph('Yes', cell_style), Paragraph('Yes', cell_style), Paragraph('Sandbox', cell_style), Paragraph('Yes', cell_style)],
    [Paragraph('OpenRouter', cell_style), Paragraph('Likely', cell_style), Paragraph('Yes', cell_style), Paragraph('Yes', cell_style), Paragraph('Plugin', cell_style), Paragraph('Native', cell_style)],
    [Paragraph('Min Hardware', cell_style), Paragraph('<b>Best</b>', cell_style), Paragraph('Excellent', cell_style), Paragraph('Good', cell_style), Paragraph('Moderate', cell_style), Paragraph('Good', cell_style)],
    [Paragraph('GUI Quality', cell_style), Paragraph('Basic', cell_style), Paragraph('<b>Excellent</b>', cell_style), Paragraph('Good', cell_style), Paragraph('<b>Excellent</b>', cell_style), Paragraph('Good', cell_style)],
    [Paragraph('Setup Ease', cell_style), Paragraph('Medium', cell_style), Paragraph('Easy', cell_style), Paragraph('Medium', cell_style), Paragraph('Complex', cell_style), Paragraph('Medium', cell_style)]
]
req_table = Table(req_data, colWidths=[70, 60, 70, 60, 55, 55])
req_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1F4E79')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('BACKGROUND', (0, 1), (0, -1), colors.HexColor('#E8EEF4')),
    ('BACKGROUND', (1, 1), (-1, 1), colors.white),
    ('BACKGROUND', (1, 2), (-1, 2), colors.HexColor('#F5F5F5')),
    ('BACKGROUND', (1, 3), (-1, 3), colors.HexColor('#E8F4E8')),
    ('BACKGROUND', (1, 4), (-1, 4), colors.white),
    ('BACKGROUND', (1, 5), (-1, 5), colors.HexColor('#F5F5F5')),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('LEFTPADDING', (0, 0), (-1, -1), 4),
    ('RIGHTPADDING', (0, 0), (-1, -1), 4),
    ('TOPPADDING', (0, 0), (-1, -1), 3),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
]))
story.append(Spacer(1, 8))
story.append(req_table)
story.append(Spacer(1, 4))
story.append(Paragraph("<i>Table 2: Requirements evaluation matrix</i>", ParagraphStyle(name='Caption', fontName='Times New Roman', fontSize=8, alignment=TA_CENTER)))
story.append(Spacer(1, 12))

story.append(Paragraph("<b>5. MacBook Pro 2017-2018 Considerations</b>", h1_style))
story.append(Paragraph(
    "MacBook Pro models from 2017-2018 typically feature Intel Core i5/i7 processors, 8-16 GB RAM, and integrated graphics. This hardware profile is well-suited for cloud-based AI solutions where only the interface runs locally. The key optimization is avoiding local model inference, which would require significant RAM and GPU resources.",
    body_style
))
story.append(Paragraph(
    "<b>RAM Allocation Strategy:</b> With 8 GB RAM, approximately 4-5 GB is available for applications after macOS overhead. Open WebUI (500 MB) or PicoClaw (20 MB) leave ample headroom for browser, email, and other daily applications. With 16 GB RAM, even Dify's Docker-based deployment becomes comfortable.",
    body_style
))
story.append(Paragraph(
    "<b>Running via OpenRouter:</b> All processing happens on OpenRouter's servers. The local machine only handles: rendering the chat interface, sending text prompts, receiving and displaying responses. This architecture means even minimal hardware provides snappy AI interactions.",
    body_style
))

story.append(Paragraph("<b>6. Recommendations</b>", h1_style))
story.append(Paragraph("<b>6.1 Best Overall: Open WebUI</b>", h2_style))
story.append(Paragraph(
    "Open WebUI provides the optimal balance for your requirements. It offers a polished, ChatGPT-like interface that feels familiar, requires only 300-500 MB RAM, has proven OpenRouter integration, and is completely free and open-source. The web UI means no terminal interaction, and setup via Docker is straightforward on macOS.",
    body_style
))

story.append(Paragraph("<b>6.2 Best for Minimal Hardware: PicoClaw</b>", h2_style))
story.append(Paragraph(
    "If your MacBook Pro has only 8 GB RAM or you want absolute minimal resource usage, PicoClaw is unmatched at 10-20 MB RAM. However, verify OpenRouter support before committing, and note that the interface may be more basic than Open WebUI.",
    body_style
))

story.append(Paragraph("<b>6.3 Best for Visual Workflows: Dify or n8n</b>", h2_style))
story.append(Paragraph(
    "If you need to build complex multi-step AI workflows with branching logic, tool integrations, and automation, Dify (visual agent builder) or n8n (workflow automation) are appropriate. These require more RAM but provide powerful orchestration capabilities.",
    body_style
))

story.append(Paragraph("<b>7. Installation Guides</b>", h1_style))
story.append(Paragraph("<b>7.1 Open WebUI with OpenRouter (Recommended)</b>", h2_style))
story.append(Paragraph(
    "Step 1: Install Docker Desktop for Mac from docker.com. Step 2: Create OpenRouter account at openrouter.ai and generate API key. Step 3: Run Open WebUI: 'docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui ghcr.io/open-webui/open-webui:main'. Step 4: Open browser at localhost:3000. Step 5: Go to Settings > Connections > OpenAI API, enter OpenRouter endpoint (https://openrouter.ai/api/v1) and your API key.",
    body_style
))

story.append(Paragraph("<b>7.2 PicoClaw (Ultra-Lightweight)</b>", h2_style))
story.append(Paragraph(
    "Step 1: Download binary from github.com/sipeed/picoclaw for macOS. Step 2: Make executable: 'chmod +x picoclaw'. Step 3: Run: './picoclaw'. Step 4: Configure LLM provider in settings (verify OpenRouter support). Step 5: Start chatting.",
    body_style
))

story.append(Paragraph("<b>8. Conclusion</b>", h1_style))
story.append(Paragraph(
    "For a MacBook Pro 2017-2018 user seeking a general-purpose AI assistant with maximum free usage, Open WebUI connected to OpenRouter's free models represents the optimal solution. This combination delivers: cloud-based inference (no local model resources), access to powerful free models like Llama 4 Maverick and DeepSeek R1, a polished ChatGPT-like GUI familiar to non-power-users, minimal local resource requirements (500 MB RAM), and complete open-source freedom. PicoClaw is a compelling alternative if absolute minimal resource usage is paramount, though OpenRouter integration should be verified. The key insight is that cloud-based LLM providers like OpenRouter fundamentally change hardware requirements—only the interface needs to run locally, making even older laptops perfectly capable AI assistant hosts.",
    body_style
))

doc.build(story)
print("PDF generated successfully!")
