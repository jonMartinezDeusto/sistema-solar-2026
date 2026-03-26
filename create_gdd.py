from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor, white, black
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY

# Colors
DARK_BLUE = HexColor('#0A0E2A')
SPACE_BLUE = HexColor('#0D1B4B')
ACCENT_BLUE = HexColor('#1E90FF')
LIGHT_BLUE = HexColor('#87CEEB')
GOLD = HexColor('#FFD700')
LIGHT_GRAY = HexColor('#E8EEF5')
MID_GRAY = HexColor('#B0BEC5')
TEXT_DARK = HexColor('#1A1A2E')

def build_pdf():
    doc = SimpleDocTemplate(
        "/Users/joninakimartinez/SistemaSolar2026/GDD_SistemaSolar2026.pdf",
        pagesize=A4,
        leftMargin=1.8*cm, rightMargin=1.8*cm,
        topMargin=1.5*cm, bottomMargin=1.5*cm
    )

    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle('Title', fontName='Helvetica-Bold', fontSize=26,
                                  textColor=GOLD, alignment=TA_CENTER, spaceAfter=4)
    subtitle_style = ParagraphStyle('Subtitle', fontName='Helvetica', fontSize=11,
                                     textColor=LIGHT_BLUE, alignment=TA_CENTER, spaceAfter=2)
    meta_style = ParagraphStyle('Meta', fontName='Helvetica', fontSize=9,
                                 textColor=MID_GRAY, alignment=TA_CENTER, spaceAfter=12)
    section_style = ParagraphStyle('Section', fontName='Helvetica-Bold', fontSize=13,
                                    textColor=GOLD, spaceBefore=10, spaceAfter=4)
    body_style = ParagraphStyle('Body', fontName='Helvetica', fontSize=9,
                                 textColor=TEXT_DARK, leading=14, spaceAfter=4, alignment=TA_JUSTIFY)
    bullet_style = ParagraphStyle('Bullet', fontName='Helvetica', fontSize=9,
                                   textColor=TEXT_DARK, leading=13, leftIndent=12,
                                   spaceAfter=2, bulletIndent=0)
    subsection_style = ParagraphStyle('Sub', fontName='Helvetica-Bold', fontSize=10,
                                       textColor=ACCENT_BLUE, spaceBefore=6, spaceAfter=3)

    story = []

    # ─── PAGE 1 ───────────────────────────────────────────────
    # Header banner (table used as colored block)
    header_data = [[Paragraph('<b>SISTEMA SOLAR 2026</b>', ParagraphStyle(
        'H', fontName='Helvetica-Bold', fontSize=28, textColor=GOLD, alignment=TA_CENTER))],
        [Paragraph('Game Design Document — v1.0', ParagraphStyle(
            'HS', fontName='Helvetica', fontSize=12, textColor=LIGHT_BLUE, alignment=TA_CENTER))],
        [Paragraph('Unity 3D &nbsp;|&nbsp; Plataforma: PC &nbsp;|&nbsp; Marzo 2026', ParagraphStyle(
            'HM', fontName='Helvetica', fontSize=9, textColor=MID_GRAY, alignment=TA_CENTER))]]

    header_table = Table(header_data, colWidths=[17.4*cm])
    header_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), DARK_BLUE),
        ('TOPPADDING', (0,0), (0,0), 18),
        ('BOTTOMPADDING', (0,-1), (-1,-1), 14),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('ROUNDEDCORNERS', [8]),
    ]))
    story.append(header_table)
    story.append(Spacer(1, 10))

    # Concept + Goals columns
    col1 = [
        Paragraph('CONCEPTO DEL JUEGO', section_style),
        HRFlowable(width="100%", thickness=1, color=ACCENT_BLUE, spaceAfter=6),
        Paragraph(
            'Sistema Solar 2026 es una experiencia interactiva 3D en Unity donde el jugador '
            'explora el sistema solar, aprende sobre cada planeta y puede interactuar con '
            'ellos en tiempo real. Combina divulgacion cientifica con exploracion espacial.',
            body_style),
        Spacer(1, 6),
        Paragraph('OBJETIVOS DEL PROYECTO', section_style),
        HRFlowable(width="100%", thickness=1, color=ACCENT_BLUE, spaceAfter=6),
        Paragraph('&#8226;  Construir una escena 3D del sistema solar a escala aproximada.', bullet_style),
        Paragraph('&#8226;  Orbitas planetarias animadas con velocidad ajustable.', bullet_style),
        Paragraph('&#8226;  Camara libre con zoom y rotacion (Mouse + Teclado).', bullet_style),
        Paragraph('&#8226;  Panel de informacion al seleccionar un planeta.', bullet_style),
        Paragraph('&#8226;  Iluminacion dinamica desde el Sol.', bullet_style),
        Paragraph('&#8226;  Fondo estelar inmersivo (Skybox espacial).', bullet_style),
    ]

    col2 = [
        Paragraph('GENERO Y PUBLICO', section_style),
        HRFlowable(width="100%", thickness=1, color=ACCENT_BLUE, spaceAfter=6),
        Paragraph('<b>Genero:</b> Simulacion / Educativo / Exploracion', body_style),
        Paragraph('<b>Publico:</b> Estudiantes, aficionados a la astronomia, publico general (+8 anos)', body_style),
        Paragraph('<b>Plataforma:</b> PC (Windows / macOS)', body_style),
        Spacer(1, 6),
        Paragraph('REFERENCIAS VISUALES', section_style),
        HRFlowable(width="100%", thickness=1, color=ACCENT_BLUE, spaceAfter=6),
        Paragraph('&#8226;  Solar System Scope (app web).', bullet_style),
        Paragraph('&#8226;  NASA Eyes on the Solar System.', bullet_style),
        Paragraph('&#8226;  Universe Sandbox 2.', bullet_style),
        Spacer(1, 6),
        Paragraph('TONO VISUAL', section_style),
        HRFlowable(width="100%", thickness=1, color=ACCENT_BLUE, spaceAfter=6),
        Paragraph(
            'Estilo realista-cientifico. Colores oscuros, espacio profundo negro/azul, '
            'planetas con texturas NASA. UI minimalista blanca sobre fondo oscuro.',
            body_style),
    ]

    # Two-column layout
    col_table = Table([[col1, col2]], colWidths=[8.5*cm, 8.5*cm], vAlign='TOP')
    col_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(col_table)
    story.append(Spacer(1, 8))

    # Planetas table
    story.append(Paragraph('CUERPOS CELESTES A INCLUIR', section_style))
    story.append(HRFlowable(width="100%", thickness=1, color=ACCENT_BLUE, spaceAfter=6))

    planet_data = [
        [Paragraph('<b>Cuerpo</b>', ParagraphStyle('th', fontName='Helvetica-Bold', fontSize=9, textColor=white, alignment=TA_CENTER)),
         Paragraph('<b>Tipo</b>', ParagraphStyle('th', fontName='Helvetica-Bold', fontSize=9, textColor=white, alignment=TA_CENTER)),
         Paragraph('<b>Detalle clave</b>', ParagraphStyle('th', fontName='Helvetica-Bold', fontSize=9, textColor=white, alignment=TA_CENTER)),
         Paragraph('<b>Prioridad</b>', ParagraphStyle('th', fontName='Helvetica-Bold', fontSize=9, textColor=white, alignment=TA_CENTER))],
        ['Sol', 'Estrella', 'Fuente de luz, efecto bloom', 'Alta'],
        ['Mercurio', 'Planeta', 'Orbita rapida, superficie gris', 'Alta'],
        ['Venus', 'Planeta', 'Atmosfera densa, rotacion inversa', 'Alta'],
        ['Tierra', 'Planeta', 'Textura nubes + luna', 'Alta'],
        ['Marte', 'Planeta', 'Color rojizo, Deimos & Fobos', 'Alta'],
        ['Jupiter', 'Planeta gigante', 'Gran mancha roja, anillos tenues', 'Media'],
        ['Saturno', 'Planeta gigante', 'Anillos prominentes', 'Alta'],
        ['Urano', 'Planeta gigante', 'Rotacion axial extrema', 'Media'],
        ['Neptuno', 'Planeta gigante', 'Azul intenso, vientos rapidos', 'Media'],
        ['Luna', 'satelite', 'Orbita la Tierra', 'Alta'],
    ]

    pt = Table(planet_data, colWidths=[3.5*cm, 3.5*cm, 7*cm, 2.9*cm])
    pt.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), SPACE_BLUE),
        ('TEXTCOLOR', (0,0), (-1,0), white),
        ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,0), (-1,-1), 8.5),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [LIGHT_GRAY, white]),
        ('GRID', (0,0), (-1,-1), 0.4, MID_GRAY),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('ALIGN', (0,0), (-1,0), 'CENTER'),
        ('ALIGN', (3,1), (3,-1), 'CENTER'),
    ]))
    story.append(pt)

    # ─── PAGE 2 ───────────────────────────────────────────────
    story.append(PageBreak())

    # Page 2 header
    p2_header = Table([[Paragraph('GUIA DE CONSTRUCCION EN UNITY', ParagraphStyle(
        'P2H', fontName='Helvetica-Bold', fontSize=18, textColor=GOLD, alignment=TA_CENTER))]],
        colWidths=[17.4*cm])
    p2_header.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), DARK_BLUE),
        ('TOPPADDING', (0,0), (-1,-1), 12),
        ('BOTTOMPADDING', (0,0), (-1,-1), 12),
        ('ROUNDEDCORNERS', [6]),
    ]))
    story.append(p2_header)
    story.append(Spacer(1, 10))

    # Two columns: milestones + technical
    milestones = [
        Paragraph('FASES DE DESARROLLO', section_style),
        HRFlowable(width="100%", thickness=1, color=ACCENT_BLUE, spaceAfter=6),
    ]

    phases = [
        ('Fase 1 — Escena Base', [
            'Crear proyecto Unity (URP recomendado).',
            'Importar Skybox espacial (Asset Store).',
            'Crear GameObject Sol con Light componente.',
            'Anadir planetas como esferas con texturas NASA.',
        ]),
        ('Fase 2 — Orbitas', [
            'Script PlanetOrbit.cs con velocidad configurable.',
            'Usar Transform.RotateAround() para orbitas.',
            'Exponer velocidad en Inspector para cada planeta.',
            'Anadir inclinacion axial por planeta.',
        ]),
        ('Fase 3 — Camara', [
            'Script CameraController.cs.',
            'Click + arrastrar para rotar; scroll para zoom.',
            'Limites de zoom min/max.',
            'Opcion de centrar camara en planeta seleccionado.',
        ]),
        ('Fase 4 — UI / Info', [
            'Canvas con Panel de informacion (TextMeshPro).',
            'Raycast al hacer clic en planeta.',
            'Mostrar: nombre, distancia al Sol, periodo orbital.',
            'Boton para pausar/reanudar orbitas.',
        ]),
        ('Fase 5 — Pulido', [
            'Post-processing: Bloom en el Sol.',
            'Particulas para cinturon de asteroides.',
            'Sonido ambiental espacial.',
            'Build final para PC.',
        ]),
    ]

    for title_phase, items in phases:
        milestones.append(Paragraph(title_phase, subsection_style))
        for item in items:
            milestones.append(Paragraph(f'&#8226;  {item}', bullet_style))
        milestones.append(Spacer(1, 2))

    # Technical column
    technical = [
        Paragraph('ARQUITECTURA TECNICA', section_style),
        HRFlowable(width="100%", thickness=1, color=ACCENT_BLUE, spaceAfter=6),
        Paragraph('Scripts principales:', subsection_style),
        Paragraph('&#8226;  <b>PlanetOrbit.cs</b> — Controla la traslacion.', bullet_style),
        Paragraph('&#8226;  <b>PlanetRotation.cs</b> — Rotacion sobre su eje.', bullet_style),
        Paragraph('&#8226;  <b>CameraController.cs</b> — Movimiento de camara.', bullet_style),
        Paragraph('&#8226;  <b>PlanetInfo.cs</b> — Datos y UI de cada planeta.', bullet_style),
        Paragraph('&#8226;  <b>SolarSystemManager.cs</b> — Control global.', bullet_style),
        Spacer(1, 6),
        Paragraph('Estructura de carpetas:', subsection_style),
        Paragraph('&#8226;  Assets/Scripts/', bullet_style),
        Paragraph('&#8226;  Assets/Textures/Planets/', bullet_style),
        Paragraph('&#8226;  Assets/Materials/', bullet_style),
        Paragraph('&#8226;  Assets/Prefabs/', bullet_style),
        Paragraph('&#8226;  Assets/UI/', bullet_style),
        Paragraph('&#8226;  Assets/Audio/', bullet_style),
        Spacer(1, 6),
        Paragraph('Recursos recomendados:', subsection_style),
        Paragraph('&#8226;  Texturas: <b>solarsystemscope.com/textures</b>', bullet_style),
        Paragraph('&#8226;  Skybox: <b>Unity Asset Store — Skybox Series</b>', bullet_style),
        Paragraph('&#8226;  Font UI: <b>TextMeshPro (incluido en Unity)</b>', bullet_style),
        Spacer(1, 6),
        Paragraph('Configuracion del proyecto:', subsection_style),
        Paragraph('&#8226;  Pipeline: <b>Universal Render Pipeline (URP)</b>', bullet_style),
        Paragraph('&#8226;  Unity version: <b>2022 LTS o superior</b>', bullet_style),
        Paragraph('&#8226;  Color Space: <b>Linear</b>', bullet_style),
        Paragraph('&#8226;  Target platform: <b>PC Standalone</b>', bullet_style),
        Spacer(1, 6),
        Paragraph('Metricas de exito:', subsection_style),
        Paragraph('&#8226;  60 FPS estables en escena completa.', bullet_style),
        Paragraph('&#8226;  Todos los planetas con textura y orbita.', bullet_style),
        Paragraph('&#8226;  UI funcional al clicar cada planeta.', bullet_style),
        Paragraph('&#8226;  Build ejecutable en PC sin errores.', bullet_style),
    ]

    page2_cols = Table([[milestones, technical]], colWidths=[8.8*cm, 8.2*cm], vAlign='TOP')
    page2_cols.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(page2_cols)

    # Footer
    story.append(Spacer(1, 10))
    story.append(HRFlowable(width="100%", thickness=0.5, color=MID_GRAY))
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        'Sistema Solar 2026 &nbsp;|&nbsp; GDD v1.0 &nbsp;|&nbsp; Marzo 2026 &nbsp;|&nbsp; '
        'Repositorio: github.com/jonMartinezDeusto/sistema-solar-2026',
        ParagraphStyle('Footer', fontName='Helvetica', fontSize=7.5,
                       textColor=MID_GRAY, alignment=TA_CENTER)))

    doc.build(story)
    print("PDF generado: GDD_SistemaSolar2026.pdf")

build_pdf()
