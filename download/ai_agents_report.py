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
pdfmetrics.registerFont(TTFont('SimHei', '/usr/share/fonts/truetype/chinese/SimHei.ttf'))
registerFontFamily('Times New Roman', normal='Times New Roman', bold='Times New Roman')

# Create document
doc = SimpleDocTemplate(
    "/home/z/my-project/download/ai_agents_analysis.pdf",
    pagesize=A4,
    title="AI Coding Agents Analysis",
    author="Z.ai",
    creator="Z.ai",
    subject="Analysis of cloud-based AI coding agents with free tiers"
)

# Define styles
styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    name='TitleStyle',
    fontName='Times New Roman',
    fontSize=24,
    leading=30,
    alignment=TA_CENTER,
    spaceAfter=20
)

subtitle_style = ParagraphStyle(
    name='SubtitleStyle',
    fontName='Times New Roman',
    fontSize=14,
    leading=18,
    alignment=TA_CENTER,
    spaceAfter=30
)

h1_style = ParagraphStyle(
    name='H1Style',
    fontName='Times New Roman',
    fontSize=16,
    leading=20,
    alignment=TA_LEFT,
    spaceBefore=18,
    spaceAfter=12
)

h2_style = ParagraphStyle(
    name='H2Style',
    fontName='Times New Roman',
    fontSize=13,
    leading=16,
    alignment=TA_LEFT,
    spaceBefore=12,
    spaceAfter=8
)

body_style = ParagraphStyle(
    name='BodyStyle',
    fontName='Times New Roman',
    fontSize=10.5,
    leading=15,
    alignment=TA_JUSTIFY,
    spaceBefore=0,
    spaceAfter=8
)

cell_style = ParagraphStyle(
    name='CellStyle',
    fontName='Times New Roman',
    fontSize=9,
    leading=12,
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
story.append(Spacer(1, 60))
story.append(Paragraph("<b>AI Coding Agents Analysis Report</b>", title_style))
story.append(Paragraph("Cloud-Based AI Agents for Software Development<br/>with Free Usage Tiers", subtitle_style))
story.append(Spacer(1, 40))

# Executive Summary
story.append(Paragraph("<b>1. Executive Summary</b>", h1_style))
story.append(Paragraph(
    "This comprehensive analysis examines cloud-based AI coding agents that operate without utilizing local computer resources, "
    "offer intelligent coding capabilities powered by top-tier AI models, and provide generous free usage tiers. "
    "The research covers platforms like Manus AI, Cursor, Windsurf, Google Gemini Code Assist, Amazon Kiro, Claude Code, "
    "Replit AI, Bolt.new, and v0 by Vercel. Each platform is evaluated against four key criteria: cloud-based operation, "
    "AI model quality, development capabilities with GitHub integration, and free tier limitations. "
    "The findings reveal that while several platforms offer free tiers, most have significant usage limitations, "
    "with Google Gemini Code Assist standing out for its exceptionally generous free offering of 180,000 monthly code completions.",
    body_style
))

# Requirements
story.append(Paragraph("<b>2. Search Requirements</b>", h1_style))
story.append(Paragraph(
    "The analysis focuses on identifying AI coding agents that meet four specific criteria essential for developers seeking "
    "accessible yet powerful AI-assisted development tools. First, the platform must operate entirely in the cloud without "
    "requiring local computational resources, though IDE plugin integration is acceptable if the AI inference occurs remotely. "
    "Second, the agent should leverage state-of-the-art AI models to ensure high-quality code generation and problem-solving capabilities. "
    "Third, strong development and coding competencies are essential, including the ability to work with GitHub repositories or "
    "other mechanisms for delivering work results to users. Fourth, and perhaps most critically for accessibility, "
    "the platform should offer a substantial free usage tier, ideally approaching unlimited availability.",
    body_style
))

# Manus AI
story.append(Paragraph("<b>3. Detailed Platform Analysis</b>", h1_style))
story.append(Paragraph("<b>3.1 Manus AI</b>", h2_style))
story.append(Paragraph(
    "Manus AI represents a sophisticated autonomous agent designed to bridge the gap between human intent and execution. "
    "Launched in early 2025 by Chinese startup Monica, Manus operates as a general-purpose AI agent capable of planning "
    "and executing complex tasks in cloud-based virtual machines. Each user task is assigned a fully functional cloud-based "
    "Linux virtual machine, with plans for Windows and Android support. The platform runs on Claude 3.5/3.7 and Alibaba's Qwen "
    "foundation models, providing powerful reasoning capabilities for development tasks. Manus excels in autonomous task execution, "
    "including code deployment, data analysis, web development, and content creation.",
    body_style
))
story.append(Paragraph(
    "<b>Pricing Structure:</b> Manus offers a free tier with 300 daily refresh credits, suitable for light experimentation. "
    "The Basic plan costs $19/month (1,900 monthly credits), while the Plus (Starter) plan is $39/month (3,900 credits). "
    "The Pro tier at $199/month provides 19,900 credits for intensive usage. While Manus provides excellent autonomous capabilities, "
    "the credit system can be unpredictable, and the free tier quickly reaches limits for serious development work. "
    "The platform supports GitHub integration for code delivery and repository management.",
    body_style
))

# Clawbot
story.append(Paragraph("<b>3.2 Clawbot (OpenClaw)</b>", h2_style))
story.append(Paragraph(
    "Clawbot, now known as OpenClaw, is an open-source personal AI assistant created by Peter Steinberger. "
    "Unlike other platforms in this analysis, Clawbot is designed to run on the user's own infrastructure, "
    "either locally or in a cloud environment of their choosing. This architecture means Clawbot does not inherently "
    "satisfy the cloud-based operation requirement as specified, since it requires users to provide their own computational "
    "resources. The platform can integrate with various AI models and offers capabilities for email management, calendar operations, "
    "and task automation through WhatsApp, Telegram, or other chat interfaces.",
    body_style
))
story.append(Paragraph(
    "<b>Limitations for Requirements:</b> While Clawbot offers excellent privacy and control advantages, "
    "it fundamentally requires local or self-hosted infrastructure resources, disqualifying it from meeting "
    "the first criterion of not using local computer resources. The platform is open-source and free to use, "
    "but users must provide their own AI model API keys and hosting environment, which introduces additional costs and complexity.",
    body_style
))

# Google Gemini Code Assist
story.append(Paragraph("<b>3.3 Google Gemini Code Assist</b>", h2_style))
story.append(Paragraph(
    "Google's Gemini Code Assist stands out as offering one of the most generous free tiers among AI coding assistants. "
    "The platform provides AI-powered coding assistance powered by Gemini 2.0, supporting all programming languages. "
    "The free tier offers an unprecedented 180,000 code completions per month at no cost, with a 1-million token context window "
    "that enables understanding of large codebases. Integration is available through IDE plugins (VS Code, JetBrains) and "
    "a CLI tool, with inference occurring entirely in Google Cloud. The platform also includes Gemini CLI, providing access "
    "to an open-source AI agent directly in the terminal with 60 requests per minute and 1,000 requests per day.",
    body_style
))
story.append(Paragraph(
    "<b>Key Advantages:</b> Gemini Code Assist excels in value proposition with its virtually unlimited free tier "
    "for individual developers. The platform supports over 20 programming languages including C, C++, C#, Go, Python, Java, "
    "JavaScript, Kotlin, and TypeScript. GitHub integration is available through Cloud Code extensions, enabling seamless "
    "repository workflows. The only consideration is Google's data usage terms, which by default allow code to be used for "
    "model improvement, though this can be disabled in settings. For developers prioritizing free access without compromise "
    "on model quality, Gemini Code Assist represents the optimal choice.",
    body_style
))

# Cursor
story.append(Paragraph("<b>3.4 Cursor AI</b>", h2_style))
story.append(Paragraph(
    "Cursor has emerged as one of the most popular AI-powered code editors, built as a fork of VS Code with native AI integration. "
    "The platform features an AI agent that can work autonomously, running in parallel to build, test, and demo features end-to-end "
    "for developer review. Cursor's cloud agent functionality enables background processing without consuming local resources for "
    "inference, though the editor itself runs locally. The platform supports multiple top-tier AI models including GPT-4, Claude, "
    "and Gemini, giving developers flexibility in model selection.",
    body_style
))
story.append(Paragraph(
    "<b>Pricing and Free Tier:</b> Cursor offers a free Hobby tier with limited agent requests and tab completions. "
    "The Pro plan at $20/month includes 500 fast premium requests per month with unlimited slow premium requests. "
    "Team plans at $40/user/month provide enhanced collaboration features. While the free tier allows basic usage, "
    "serious development work requires a paid subscription. Cursor integrates well with GitHub through its VS Code foundation, "
    "supporting standard Git workflows. The platform is particularly noted for its excellent code understanding and "
    "multi-file editing capabilities.",
    body_style
))

# Windsurf
story.append(Paragraph("<b>3.5 Windsurf (by Codeium)</b>", h2_style))
story.append(Paragraph(
    "Windsurf is an AI-powered IDE featuring Cascade, an agent that codes, fixes, and anticipates developer needs. "
    "The platform is built on Code OSS, allowing developers to maintain their VS Code settings and use Open VSX compatible plugins. "
    "Windsurf's Cascade agent provides autonomous code generation across multiple files, command execution, and agentic workflows. "
    "The AI flow paradigm enables seamless collaboration between developer and AI, with the system actively managing workflows "
    "rather than simply responding to prompts.",
    body_style
))
story.append(Paragraph(
    "<b>Pricing Structure:</b> Windsurf offers a free tier described as 'free forever for individuals.' "
    "The Pro plan costs $15/month, providing 500 User Prompt credits and 1,500 Flow Action credits (2,000 total steps). "
    "The Teams and Enterprise tiers provide enhanced features for organizational use. While the free tier provides access "
    "to the platform, users may encounter limits on advanced agent capabilities. GitHub integration is supported through "
    "standard Git functionality within the IDE. Windsurf is particularly noted for its ability to help developers write code quickly, "
    "with suggestions that significantly reduce typing and clicking.",
    body_style
))

# Amazon Kiro
story.append(Paragraph("<b>3.6 Amazon Kiro</b>", h2_style))
story.append(Paragraph(
    "Amazon Kiro is AWS's entry into the AI-powered IDE space, built to bridge the gap between rapid prototyping and production-ready code. "
    "The platform introduces a spec-driven development methodology, transforming ideas into production systems with structured AI assistance. "
    "Kiro is currently in preview and runs on Claude Sonnet 4.0, notably not Amazon's own models. The platform provides an AI-powered "
    "development experience with agents that can install, configure, and deploy applications autonomously through its CLI interface.",
    body_style
))
story.append(Paragraph(
    "<b>Pricing and Availability:</b> Kiro is free during its preview period, making it an attractive option for developers willing to "
    "adopt an early-stage platform. The planned pricing structure includes a free version with 50 agent interactions per month, "
    "Pro at $20/month, Pro+ at $40/month, and Power at $200/month. AWS offers one year of free Pro+ credits for qualifying startups. "
    "GitHub integration is available, and the platform integrates with AWS services for deployment. Developers should note that "
    "long-term pricing and feature stability remain uncertain as the platform exits preview.",
    body_style
))

# Claude Code
story.append(Paragraph("<b>3.7 Claude Code by Anthropic</b>", h2_style))
story.append(Paragraph(
    "Claude Code is Anthropic's official CLI coding agent, providing direct access to Claude's reasoning capabilities in the terminal. "
    "The platform operates as a terminal-based agent with IDE integration capabilities, handling complex coding tasks through "
    "natural language commands. Claude Code leverages Claude 3.5/4 models, known for their strong reasoning and code generation abilities. "
    "The tool excels at understanding large codebases and performing multi-step coding operations autonomously.",
    body_style
))
story.append(Paragraph(
    "<b>Pricing Considerations:</b> Claude Code requires at minimum a Claude Pro subscription at $20/month (or $17/month with annual billing), "
    "with no standalone free tier. The Max tier at $100/month provides extended usage, while Max 20x at $200/month offers the highest limits. "
    "Users report that the $20 Pro tier provides approximately 10-20 meaningful coding sessions per week, making it necessary to ration usage. "
    "For developers requiring extensive AI assistance, the cost can become substantial. GitHub integration is supported through "
    "standard Git commands within the CLI. While Claude Code offers excellent model quality, the lack of a free tier makes it "
    "less accessible than competitors.",
    body_style
))

# Replit AI
story.append(Paragraph("<b>3.8 Replit AI Agent</b>", h2_style))
story.append(Paragraph(
    "Replit provides a cloud-based development platform with integrated AI agent capabilities. The platform enables writing, running, "
    "and deploying code directly in the browser without local setup. The AI agent can write production-ready code, evolve it through iteration, "
    "and operate autonomously while developers focus on higher-level direction. Replit's 2025 updates expanded Agent functionality "
    "with Design Mode, Fast Build, and an expanded Free Tier for broader accessibility.",
    body_style
))
story.append(Paragraph(
    "<b>Pricing Structure:</b> The Starter plan is free, providing access to public projects and daily Agent usage with limited compute and storage. "
    "The Core plan at $25/month includes AI Agent credits for more extensive usage. Team plans are available at $40/user/month. "
    "The free tier allows creation of up to 10 development apps (public only), making it suitable for learning and experimentation. "
    "Replit offers GitHub integration and deployment capabilities directly from the browser environment. While the platform is excellent "
    "for beginners and rapid prototyping, advanced users may find the free tier limiting for substantial projects.",
    body_style
))

# Bolt.new
story.append(Paragraph("<b>3.9 Bolt.new by StackBlitz</b>", h2_style))
story.append(Paragraph(
    "Bolt.new is StackBlitz's AI-powered web development platform that generates full-stack applications from natural language prompts. "
    "The platform runs entirely in the browser using WebContainers technology, allowing users to prompt, run, edit, and deploy applications "
    "without leaving the browser. Bolt integrates frontier coding agents from major AI labs in a familiar visual interface, "
    "generating React applications with impressive speed and accuracy.",
    body_style
))
story.append(Paragraph(
    "<b>Pricing:</b> Bolt offers a free tier to start building, with premium plans unlocking advanced features. "
    "The platform achieved remarkable growth, reaching over $8 million ARR within two months of launch. "
    "GitHub integration is available for code export and repository management. Bolt is particularly suited for front-end "
    "development and rapid prototyping, though it may be less appropriate for complex backend systems. "
    "The free tier provides substantial value for developers building web applications and prototypes.",
    body_style
))

# v0 by Vercel
story.append(Paragraph("<b>3.10 v0 by Vercel</b>", h2_style))
story.append(Paragraph(
    "v0 (now v0.app) is Vercel's AI builder platform that generates working applications from natural language descriptions. "
    "The platform specializes in creating React components and full applications, publishing them as live websites in seconds. "
    "v0 has evolved from a UI generator to a comprehensive AI builder for founders, designers, developers, and other professionals. "
    "The platform features Design Mode for visual editing and seamless GitHub synchronization for code delivery.",
    body_style
))
story.append(Paragraph(
    "<b>Pricing Structure:</b> v0 offers four pricing tiers. The Free tier includes $5 of monthly credits with a 7 message per day limit, "
    "along with app deployment to Vercel and GitHub sync. The Premium tier at $20/month provides more extensive credits. "
    "While the free tier allows prototyping and experimentation, the daily message limit restricts intensive usage. "
    "v0 is particularly effective for React/Tailwind development and integrates deeply with Vercel's deployment infrastructure. "
    "For developers building modern web applications, v0 provides an efficient path from concept to deployment.",
    body_style
))

# Comparison Table
story.append(Paragraph("<b>4. Comparative Analysis</b>", h1_style))
story.append(Paragraph(
    "The following table provides a comprehensive comparison of all analyzed platforms across key evaluation criteria. "
    "This comparison enables direct assessment of each platform's strengths and limitations relative to the specified requirements.",
    body_style
))

# Table data
table_data = [
    [
        Paragraph('<b>Platform</b>', header_style),
        Paragraph('<b>Cloud-Based</b>', header_style),
        Paragraph('<b>Model Quality</b>', header_style),
        Paragraph('<b>Free Tier</b>', header_style),
        Paragraph('<b>GitHub Integration</b>', header_style)
    ],
    [
        Paragraph('Google Gemini Code Assist', cell_style),
        Paragraph('Yes', cell_style),
        Paragraph('Gemini 2.0', cell_style),
        Paragraph('180K completions/month', cell_style),
        Paragraph('Yes', cell_style)
    ],
    [
        Paragraph('Manus AI', cell_style),
        Paragraph('Yes (VM)', cell_style),
        Paragraph('Claude 3.5/3.7, Qwen', cell_style),
        Paragraph('300 daily credits', cell_style),
        Paragraph('Yes', cell_style)
    ],
    [
        Paragraph('Windsurf', cell_style),
        Paragraph('Hybrid', cell_style),
        Paragraph('Multiple models', cell_style),
        Paragraph('Free forever (limited)', cell_style),
        Paragraph('Yes (Git)', cell_style)
    ],
    [
        Paragraph('Cursor', cell_style),
        Paragraph('Hybrid', cell_style),
        Paragraph('GPT-4, Claude, Gemini', cell_style),
        Paragraph('Limited requests', cell_style),
        Paragraph('Yes', cell_style)
    ],
    [
        Paragraph('Amazon Kiro', cell_style),
        Paragraph('Yes', cell_style),
        Paragraph('Claude Sonnet 4.0', cell_style),
        Paragraph('Free preview (50/month)', cell_style),
        Paragraph('Yes', cell_style)
    ],
    [
        Paragraph('Replit AI', cell_style),
        Paragraph('Yes', cell_style),
        Paragraph('Proprietary', cell_style),
        Paragraph('Daily Agent access', cell_style),
        Paragraph('Yes', cell_style)
    ],
    [
        Paragraph('Bolt.new', cell_style),
        Paragraph('Yes (browser)', cell_style),
        Paragraph('Frontier models', cell_style),
        Paragraph('Start free', cell_style),
        Paragraph('Yes', cell_style)
    ],
    [
        Paragraph('v0 by Vercel', cell_style),
        Paragraph('Yes', cell_style),
        Paragraph('Vercel AI', cell_style),
        Paragraph('$5 credits, 7 msg/day', cell_style),
        Paragraph('Yes', cell_style)
    ],
    [
        Paragraph('Claude Code', cell_style),
        Paragraph('Yes (CLI)', cell_style),
        Paragraph('Claude 3.5/4', cell_style),
        Paragraph('None (requires Pro)', cell_style),
        Paragraph('Yes (Git)', cell_style)
    ],
    [
        Paragraph('Clawbot', cell_style),
        Paragraph('No (self-hosted)', cell_style),
        Paragraph('User-provided', cell_style),
        Paragraph('Free (bring own API)', cell_style),
        Paragraph('Limited', cell_style)
    ]
]

table = Table(table_data, colWidths=[100, 70, 90, 100, 70])
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1F4E79')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('BACKGROUND', (0, 1), (-1, 1), colors.white),
    ('BACKGROUND', (0, 2), (-1, 2), colors.HexColor('#F5F5F5')),
    ('BACKGROUND', (0, 3), (-1, 3), colors.white),
    ('BACKGROUND', (0, 4), (-1, 4), colors.HexColor('#F5F5F5')),
    ('BACKGROUND', (0, 5), (-1, 5), colors.white),
    ('BACKGROUND', (0, 6), (-1, 6), colors.HexColor('#F5F5F5')),
    ('BACKGROUND', (0, 7), (-1, 7), colors.white),
    ('BACKGROUND', (0, 8), (-1, 8), colors.HexColor('#F5F5F5')),
    ('BACKGROUND', (0, 9), (-1, 9), colors.white),
    ('BACKGROUND', (0, 10), (-1, 10), colors.HexColor('#F5F5F5')),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('LEFTPADDING', (0, 0), (-1, -1), 6),
    ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ('TOPPADDING', (0, 0), (-1, -1), 5),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
]))

story.append(Spacer(1, 12))
story.append(table)
story.append(Spacer(1, 6))
story.append(Paragraph("<i>Table 1: Comparative analysis of AI coding platforms</i>", 
    ParagraphStyle(name='Caption', fontName='Times New Roman', fontSize=9, alignment=TA_CENTER)))
story.append(Spacer(1, 18))

# Recommendations
story.append(Paragraph("<b>5. Recommendations by Use Case</b>", h1_style))

story.append(Paragraph("<b>5.1 Best Free Tier: Google Gemini Code Assist</b>", h2_style))
story.append(Paragraph(
    "For developers prioritizing maximum free usage without compromising on model quality, Google Gemini Code Assist is the clear leader. "
    "The platform offers 180,000 monthly code completions at no cost, with a 1-million token context window that rivals paid alternatives. "
    "The combination of cloud-based operation, high-quality Gemini 2.0 model, and exceptional free tier makes this the optimal choice "
    "for individual developers, students, and hobbyists. The platform's IDE plugins (VS Code, JetBrains) and CLI tool provide flexible "
    "integration options, while GitHub support ensures seamless repository workflows.",
    body_style
))

story.append(Paragraph("<b>5.2 Best for Autonomous Development: Manus AI</b>", h2_style))
story.append(Paragraph(
    "For developers seeking a truly autonomous agent capable of end-to-end task execution, Manus AI represents the cutting edge. "
    "The platform's cloud-based virtual machines provide isolated environments for each task, enabling safe execution of complex workflows. "
    "While the free tier is limited, the autonomous capabilities justify the cost for users who need an AI that can independently "
    "plan, execute, and deliver results. Manus is particularly suited for users who want to delegate entire projects rather than "
    "individual coding tasks.",
    body_style
))

story.append(Paragraph("<b>5.3 Best for Web Development: Bolt.new or v0</b>", h2_style))
story.append(Paragraph(
    "For front-end and full-stack web development, Bolt.new and v0 by Vercel provide specialized capabilities. Bolt.new excels at "
    "generating complete React applications from prompts within the browser, while v0 specializes in React/Tailwind UI components "
    "with seamless Vercel deployment. Both platforms offer free tiers suitable for prototyping and learning. The choice between them "
    "depends on specific needs: Bolt.new for complete applications, v0 for component-focused development with Vercel ecosystem integration.",
    body_style
))

story.append(Paragraph("<b>5.4 Best for IDE Integration: Cursor or Windsurf</b>", h2_style))
story.append(Paragraph(
    "For developers who prefer working within a full-featured IDE environment, Cursor and Windsurf provide excellent AI integration. "
    "Cursor, built on VS Code, offers native AI features with multi-model support (GPT-4, Claude, Gemini). Windsurf, with its Cascade agent, "
    "provides a unique flow-based collaboration paradigm. Both platforms offer free tiers for basic usage, with paid plans for "
    "intensive development. The choice between them should be based on workflow preference: Cursor for traditional VS Code experience, "
    "Windsurf for AI-native flow-based development.",
    body_style
))

# Conclusion
story.append(Paragraph("<b>6. Conclusion</b>", h1_style))
story.append(Paragraph(
    "The landscape of cloud-based AI coding agents has matured significantly in 2025, with multiple platforms offering compelling "
    "combinations of intelligent capabilities and accessible pricing. Among the analyzed platforms, Google Gemini Code Assist stands out "
    "for its exceptional free tier offering, providing 180,000 monthly completions powered by the advanced Gemini 2.0 model. "
    "For developers requiring autonomous task execution, Manus AI provides sophisticated agent capabilities in cloud-based virtual machines. "
    "Cursor and Windsurf offer excellent IDE-integrated experiences with multi-model support. For web development specifically, "
    "Bolt.new and v0 provide specialized capabilities for rapid application generation.",
    body_style
))
story.append(Paragraph(
    "It is important to note that truly 'unlimited' free AI coding assistance does not exist among cloud-based platforms. "
    "All services incur computational costs that must be covered through subscription revenue, usage limits, or data utilization. "
    "Google Gemini Code Assist comes closest to the ideal with its 180,000 monthly completions, which represents practical "
    "near-unlimited usage for most individual developers. For those willing to manage their own infrastructure, open-source "
    "alternatives like Clawbot provide cost control at the expense of convenience. The optimal choice depends on balancing "
    "requirements for autonomy, model quality, integration needs, and budget constraints.",
    body_style
))

# Build PDF
doc.build(story)
print("PDF generated successfully!")
