from datetime import datetime, timedelta

# ─── CONFIGURACIÓN ───────────────────────────────────────────
EMPRESA = "Blacknova"
WEB = "blacknova.es"
INICIO = datetime(2026, 4, 14)  # Lunes 14 abril
# ─────────────────────────────────────────────────────────────

CONTENIDO = [

    # ══════════════════════════════════════════════════════════
    # MES 1 — PRESENTACIÓN (semanas 1-2) + EDUCATIVO (semanas 3-4)
    # ══════════════════════════════════════════════════════════

    # SEMANA 1 — Quiénes somos
    {
        "semana": 1, "dia": "Lunes", "tipo": "Presentación",
        "titulo": "Bienvenidos a Blacknova",
        "imagen_prompt": "Modern industrial warehouse interior, dramatic lighting, dark tones, golden accents, professional architectural photography, Catalunya Spain, ultra realistic",
        "caption": """Bienvenidos a Blacknova.

Somos una consultora especializada en gestión de proyectos y activos inmobiliarios industriales en Catalunya.

Llevamos más de 10 años trabajando en proyectos de construcción e ingeniería industrial en toda Europa.

A partir de hoy compartimos aquí todo lo que sabemos sobre gestión de proyectos, naves industriales y selección de talento técnico.

📍 Catalunya · España
🌐 blacknova.es

#Blacknova #GestiónDeProyectos #NavesIndustriales #Catalunya #Ingeniería #PMI #ProjectManager #Construcción""",
    },
    {
        "semana": 1, "dia": "Miércoles", "tipo": "Presentación",
        "titulo": "Qué hace Blacknova",
        "imagen_prompt": "Professional project manager reviewing blueprints in modern industrial building, serious tone, dark professional environment, golden light, ultra realistic photography",
        "caption": """¿Qué hace exactamente Blacknova?

Tres cosas, y las hacemos muy bien:

𝟏. GESTIÓN DE PROYECTOS
Coordinamos proyectos de construcción e ingeniería industrial en Catalunya con metodología PMI. Desde la planificación hasta la entrega final.

𝟐. GESTIÓN DE ACTIVOS INMOBILIARIOS
Gestionamos naves industriales y activos inmobiliarios para que rindan al máximo sin que el propietario tenga que preocuparse.

𝟑. SELECCIÓN DE TALENTO
Conectamos empresas con los mejores project managers e ingenieros de Catalunya y Europa.

¿Necesitas alguno de estos servicios?
→ Escríbenos o visita blacknova.es

#Blacknova #GestiónDeProyectos #NavesIndustriales #Talento #Catalunya #PMI #Ingeniería #Construcción""",
    },
    {
        "semana": 1, "dia": "Viernes", "tipo": "Presentación",
        "titulo": "Nuestra metodología PMI",
        "imagen_prompt": "Clean modern office with project management charts and blueprints on wall, dark elegant interior, professional atmosphere, golden details, Catalunya Spain",
        "caption": """En Blacknova trabajamos con metodología PMI.

PMI (Project Management Institute) es el estándar internacional de gestión de proyectos utilizado por las empresas más exigentes del mundo.

¿Qué significa para ti?

→ Tu proyecto tiene un plan desde el día 1
→ Conoces el estado en tiempo real
→ Los costes están bajo control
→ Los plazos se cumplen
→ Los riesgos se anticipan antes de que aparezcan

No improvisamos. Gestionamos.

🌐 blacknova.es

#PMI #ProjectManagement #Blacknova #GestiónDeProyectos #Catalunya #Construcción #Ingeniería #Metodología""",
    },

    # SEMANA 2 — El equipo y los valores
    {
        "semana": 2, "dia": "Lunes", "tipo": "Presentación",
        "titulo": "Nuestro equipo",
        "imagen_prompt": "Professional team of engineers and project managers in modern industrial facility, serious and confident, dark professional atmosphere, golden tones, ultra realistic",
        "caption": """Detrás de Blacknova hay un equipo con más de 10 años de experiencia en proyectos industriales en Europa.

Project Managers certificados PMP.
Ingenieros industriales y de edificación.
Especialistas en gestión de activos inmobiliarios.

Todos con un objetivo común: que tu proyecto se entregue en plazo, dentro del presupuesto y con la calidad que merece.

📍 Basados en Catalunya · Red europea

#Blacknova #Equipo #ProjectManager #Ingeniería #Catalunya #PMI #Construcción #GestiónDeProyectos""",
    },
    {
        "semana": 2, "dia": "Miércoles", "tipo": "Presentación",
        "titulo": "Por qué Catalunya",
        "imagen_prompt": "Aerial view of industrial area near Barcelona Catalunya Spain, warehouses and logistics parks, dramatic sunset lighting, professional photography",
        "caption": """Catalunya es uno de los ecosistemas industriales más activos de Europa.

El corredor mediterráneo, el Puerto de Barcelona, los polígonos industriales de l'Hospitalet, Martorell, Tarragona y Girona concentran miles de millones en activos inmobiliarios industriales.

En Blacknova estamos aquí, en el centro de este ecosistema, para ayudar a empresas y propietarios a gestionar sus proyectos y activos de forma profesional.

¿Tienes un proyecto o activo industrial en Catalunya?
→ blacknova.es

#Catalunya #NavesIndustriales #Barcelona #Logística #ActivosIndustriales #Blacknova #GestiónDeProyectos #Construcción""",
    },
    {
        "semana": 2, "dia": "Viernes", "tipo": "Presentación",
        "titulo": "Nuestros valores",
        "imagen_prompt": "Modern industrial building exterior at dusk, dramatic sky, professional architectural photography, dark tones with golden light, Catalunya Spain",
        "caption": """En Blacknova nos guiamos por tres valores que no negociamos:

𝗧𝗥𝗔𝗡𝗦𝗣𝗔𝗥𝗘𝗡𝗖𝗜𝗔
El cliente siempre sabe qué está pasando en su proyecto. Sin sorpresas.

𝗥𝗜𝗚𝗢𝗥
Aplicamos metodología PMI en cada proyecto, sin atajos.

𝗖𝗢𝗠𝗣𝗥𝗢𝗠𝗜𝗦𝗢
No terminamos hasta que el proyecto está entregado correctamente.

Estos no son valores de marketing. Son la forma en que trabajamos cada día.

🌐 blacknova.es

#Blacknova #Valores #GestiónDeProyectos #PMI #Catalunya #Construcción #Ingeniería #ProjectManager""",
    },

    # ══════════════════════════════════════════════════════════
    # SEMANAS 3-4 — CONTENIDO EDUCATIVO (Gestión de proyectos)
    # ══════════════════════════════════════════════════════════
    {
        "semana": 3, "dia": "Lunes", "tipo": "Educativo",
        "titulo": "5 fases de un proyecto industrial",
        "imagen_prompt": "Project planning timeline on large screen in dark modern office, industrial project blueprints, professional atmosphere, golden lighting accents",
        "caption": """Todo proyecto industrial tiene 5 fases. Si falla una, falla todo.

𝟏. INICIO
Definición del alcance, objetivos y stakeholders.

𝟐. PLANIFICACIÓN
Cronograma, presupuesto, recursos y gestión de riesgos.

𝟑. EJECUCIÓN
Coordinación de equipos, proveedores y recursos.

𝟒. CONTROL
Seguimiento de plazos, costes y calidad en tiempo real.

𝟓. CIERRE
Entrega, documentación y lecciones aprendidas.

En Blacknova gestionamos las 5 fases para que tú solo tengas que aprobar y recibir resultados.

🌐 blacknova.es

#GestiónDeProyectos #PMI #ProjectManager #Construcción #Catalunya #Ingeniería #Blacknova #Industrial""",
    },
    {
        "semana": 3, "dia": "Miércoles", "tipo": "Educativo",
        "titulo": "Qué es el alcance de un proyecto",
        "imagen_prompt": "Engineer reviewing detailed construction plans in industrial warehouse, serious professional focus, dark industrial environment, dramatic lighting",
        "caption": """El error más caro en un proyecto industrial: no definir bien el alcance.

El alcance es exactamente qué incluye y qué NO incluye tu proyecto.

Sin alcance definido:
❌ Los costes se disparan
❌ Los plazos se alargan indefinidamente
❌ El cliente y el equipo tienen expectativas distintas
❌ Aparecen trabajos extra no presupuestados

Con alcance bien definido:
✅ Todos saben exactamente qué hay que hacer
✅ El presupuesto es realista
✅ El plazo es cumplible
✅ No hay sorpresas

En Blacknova definimos el alcance antes de empezar cualquier proyecto. Es la base de todo.

🌐 blacknova.es

#GestiónDeProyectos #ProjectManager #PMI #Construcción #Catalunya #Ingeniería #Blacknova #Alcance""",
    },
    {
        "semana": 3, "dia": "Viernes", "tipo": "Educativo",
        "titulo": "Cómo controlar el presupuesto de un proyecto",
        "imagen_prompt": "Financial project control dashboard on computer screen in dark modern office, industrial project data, professional serious atmosphere, golden accents",
        "caption": """El 43% de los proyectos industriales superan el presupuesto inicial.

¿Por qué? Porque no tienen un sistema de control de costes.

En Blacknova aplicamos estas 4 reglas:

𝟏. Presupuesto base detallado antes de empezar
Cada partida documentada y validada.

𝟐. Reserva de contingencia del 10-15%
Para imprevistos reales, no para cubrir mala planificación.

𝟑. Control semanal de desviaciones
Si algo se desvía, se corrige antes de que sea un problema.

𝟒. Reporting transparente al cliente
El cliente siempre sabe en qué se gasta su dinero.

¿Tu próximo proyecto necesita este nivel de control?
→ blacknova.es

#Presupuesto #GestiónDeProyectos #ProjectManager #PMI #Construcción #Catalunya #Blacknova #Costes""",
    },
    {
        "semana": 4, "dia": "Lunes", "tipo": "Educativo",
        "titulo": "Gestión de riesgos en proyectos industriales",
        "imagen_prompt": "Risk assessment matrix on whiteboard in professional industrial office, serious project management atmosphere, dark tones, golden light, Catalunya",
        "caption": """Los problemas en un proyecto no aparecen de la nada. Se pueden anticipar.

La gestión de riesgos es el proceso de identificar, analizar y responder a los problemas antes de que ocurran.

Los 5 riesgos más comunes en proyectos industriales en Catalunya:

⚠️ Retrasos en permisos y licencias
⚠️ Subcontratistas que no cumplen plazos
⚠️ Incremento de precios de materiales
⚠️ Cambios en el alcance del proyecto
⚠️ Problemas técnicos no detectados en la fase de planificación

En Blacknova identificamos estos riesgos en la fase de planificación y tenemos un plan de respuesta para cada uno.

🌐 blacknova.es

#GestiónDeRiesgos #ProjectManager #PMI #Construcción #Catalunya #Blacknova #Ingeniería #GestiónDeProyectos""",
    },
    {
        "semana": 4, "dia": "Miércoles", "tipo": "Educativo",
        "titulo": "Cuándo contratar un Project Manager",
        "imagen_prompt": "Professional project manager at construction site in Catalunya, hard hat, reviewing plans, serious confident posture, industrial warehouse background, golden hour light",
        "caption": """¿Cuándo necesitas un Project Manager externo?

Cuando uno o más de estos casos aplica a tu empresa:

✔ Tu proyecto supera los 500.000€ de inversión
✔ Implica más de 3 proveedores o subcontratas
✔ Tienes un plazo de entrega crítico que no puedes incumplir
✔ Tu equipo interno no tiene experiencia en gestión de proyectos industriales
✔ El proyecto tiene componentes técnicos complejos
✔ Necesitas reporting regular para inversores o dirección

Un Project Manager externo no es un gasto — es la garantía de que tu inversión se gestiona correctamente.

En Blacknova somos tu Project Manager en Catalunya.
→ blacknova.es

#ProjectManager #GestiónDeProyectos #Catalunya #PMI #Construcción #Ingeniería #Blacknova #Inversión""",
    },
    {
        "semana": 4, "dia": "Viernes", "tipo": "Educativo",
        "titulo": "La diferencia entre un jefe de obra y un Project Manager",
        "imagen_prompt": "Two professionals discussing construction project in industrial building, blueprints and project charts, dark professional atmosphere, dramatic lighting, Catalunya",
        "caption": """Mucha gente confunde el jefe de obra con el Project Manager. No son lo mismo.

𝗝𝗘𝗙𝗘 𝗗𝗘 𝗢𝗕𝗥𝗔
→ Gestiona la ejecución técnica de la obra
→ Coordina los trabajos en el campo
→ Controla la calidad de la construcción
→ Reporta al Project Manager

𝗣𝗥𝗢𝗝𝗘𝗖𝗧 𝗠𝗔𝗡𝗔𝗚𝗘𝗥
→ Gestiona todo el proyecto (no solo la obra)
→ Controla plazos, costes y alcance
→ Gestiona stakeholders y cliente
→ Anticipa y gestiona riesgos
→ Toma decisiones estratégicas

En proyectos industriales complejos necesitas los dos.
En Blacknova coordinamos ambos roles.

🌐 blacknova.es

#ProjectManager #JefeDeObra #GestiónDeProyectos #Construcción #Catalunya #PMI #Blacknova #Ingeniería""",
    },

    # ══════════════════════════════════════════════════════════
    # MES 2 — NAVES INDUSTRIALES (semanas 5-8)
    # ══════════════════════════════════════════════════════════
    {
        "semana": 5, "dia": "Lunes", "tipo": "Educativo — Naves",
        "titulo": "Qué es una nave industrial y tipos",
        "imagen_prompt": "Large modern industrial warehouse interior in Catalunya, high ceiling, dramatic industrial lighting, dark tones, professional architectural photography",
        "caption": """No todas las naves industriales son iguales. Conocer los tipos te ayuda a elegir bien.

𝗡𝗔𝗩𝗘 𝗟𝗢𝗚Í𝗦𝗧𝗜𝗖𝗔
Para almacenamiento y distribución. Alta rotación de mercancía. Necesita muelles de carga y buena accesibilidad.

𝗡𝗔𝗩𝗘 𝗣𝗥𝗢𝗗𝗨𝗖𝗧𝗜𝗩𝗔
Para fabricación e industria. Necesita alta potencia eléctrica, suelos reforzados y ventilación específica.

𝗡𝗔𝗩𝗘 𝗠𝗜𝗫𝗧𝗔
Combina producción y almacenamiento. La más habitual en Catalunya.

𝗡𝗔𝗩𝗘 𝗙𝗥𝗜𝗚𝗢𝗥Í𝗙𝗜𝗖𝗔
Para productos que requieren temperatura controlada.

¿Qué tipo necesita tu empresa?
→ blacknova.es

#NavesIndustriales #Logística #Catalunya #Almacén #Industria #Blacknova #ActivosIndustriales #GestiónInmobiliaria""",
    },
    {
        "semana": 5, "dia": "Miércoles", "tipo": "Educativo — Naves",
        "titulo": "Checklist para alquilar una nave industrial",
        "imagen_prompt": "Industrial warehouse inspection, professional engineer with clipboard checking facility, dark industrial space, dramatic lighting, Catalunya Spain",
        "caption": """Antes de firmar el contrato de alquiler de una nave industrial en Catalunya, revisa esto:

𝗘𝗦𝗧𝗥𝗨𝗖𝗧𝗨𝗥𝗔
☐ Altura libre mínima 8m (logística) o 6m (industria)
☐ Suelo sin grietas ni hundimientos
☐ Cubierta en buen estado sin filtraciones

𝗜𝗡𝗦𝗧𝗔𝗟𝗔𝗖𝗜𝗢𝗡𝗘𝗦
☐ Potencia eléctrica disponible suficiente
☐ Sistema contra incendios homologado
☐ Instalación de agua y saneamiento operativa

𝗔𝗖𝗖𝗘𝗦𝗢𝗦
☐ Muelles de carga suficientes
☐ Radio de giro para camiones
☐ Aparcamiento para personal

𝗟𝗘𝗚𝗔𝗟
☐ Licencia de actividad vigente
☐ Cédula de habitabilidad industrial
☐ Sin cargas urbanísticas pendientes

En Blacknova auditamos naves industriales antes de que firmes nada.
→ blacknova.es

#NavesIndustriales #Catalunya #Alquiler #Logística #Industria #Blacknova #ActivosIndustriales #Checklist""",
    },
    {
        "semana": 5, "dia": "Viernes", "tipo": "Educativo — Naves",
        "titulo": "Polígonos industriales clave en Catalunya",
        "imagen_prompt": "Aerial view of industrial logistics park near Barcelona, modern warehouses, highway access, dramatic golden hour sky, professional photography",
        "caption": """Los polígonos industriales más estratégicos de Catalunya para tu nave.

𝗖𝗢𝗥𝗥𝗘𝗗𝗢𝗥 𝗗𝗘𝗟 𝗕𝗔𝗜𝗫 𝗟𝗟𝗢𝗕𝗥𝗘𝗚𝗔𝗧
El Prat, Gavà, Viladecans. Acceso directo al aeropuerto y Puerto de Barcelona.

𝗠𝗔𝗥𝗧𝗢𝗥𝗘𝗟𝗟 / 𝗦𝗔𝗡𝗧 𝗔𝗡𝗗𝗥𝗘𝗨 𝗗𝗘 𝗟𝗔 𝗕𝗔𝗥𝗖𝗔
Gran concentración industrial. Acceso A-2 y autopistas.

𝗧𝗔𝗥𝗥𝗔𝗚𝗢𝗡𝗔
Hub petroquímico e industrial. Puerto propio.

𝗚𝗜𝗥𝗢𝗡𝗔
Crecimiento logístico fuerte. Acceso a Francia y norte de Europa.

𝗩𝗜𝗖 / 𝗠𝗔𝗡𝗥𝗘𝗦𝗔
Precios más competitivos. Buen acceso interior.

¿Buscas nave en alguna de estas zonas?
→ blacknova.es

#NavesIndustriales #Catalunya #Barcelona #Logística #Polígono #ActivosIndustriales #Blacknova #Inmobiliario""",
    },
    {
        "semana": 6, "dia": "Lunes", "tipo": "Educativo — Naves",
        "titulo": "Cómo optimizar una nave industrial",
        "imagen_prompt": "Optimized modern warehouse interior with organized storage systems, professional industrial photography, dramatic lighting, dark tones, Catalunya Spain",
        "caption": """Una nave mal optimizada pierde dinero cada día. Así se optimiza.

𝗘𝗦𝗣𝗔𝗖𝗜𝗢
→ Analiza el flujo de mercancía y reorganiza las zonas
→ Instala estanterías de altura máxima
→ Define zonas de trabajo, almacenaje y carga claramente

𝗘𝗡𝗘𝗥𝗚Í𝗔
→ Iluminación LED con sensores de movimiento
→ Paneles solares en cubierta (ROI en 5-7 años)
→ Auditoría energética obligatoria

𝗣𝗥𝗢𝗖𝗘𝗦𝗢𝗦
→ Sistema de gestión de almacén (SGA)
→ Trazabilidad de entradas y salidas
→ Mantenimiento preventivo programado

Una nave bien optimizada puede mejorar la productividad un 30%.

En Blacknova auditamos y optimizamos naves industriales en Catalunya.
→ blacknova.es

#NavesIndustriales #Optimización #Logística #Catalunya #Almacén #Industria #Blacknova #GestiónIndustrial""",
    },
    {
        "semana": 6, "dia": "Miércoles", "tipo": "Educativo — Naves",
        "titulo": "Mantenimiento preventivo de naves industriales",
        "imagen_prompt": "Industrial maintenance technician inspecting warehouse facility, professional equipment, dark industrial environment, serious technical atmosphere, Catalunya",
        "caption": """El mantenimiento correctivo cuesta 3 veces más que el preventivo.

Plan de mantenimiento preventivo para una nave industrial:

𝗠𝗘𝗡𝗦𝗨𝗔𝗟
→ Revisión de puertas seccionales y muelles
→ Comprobación del sistema de iluminación
→ Revisión de extintores y señalización

𝗧𝗥𝗜𝗠𝗘𝗦𝗧𝗥𝗔𝗟
→ Revisión de cubierta e impermeabilización
→ Inspección de instalación eléctrica
→ Mantenimiento de sistemas contra incendios

𝗔𝗡𝗨𝗔𝗟
→ Auditoría estructural completa
→ Revisión de licencias y normativa
→ Informe de estado del activo

En Blacknova gestionamos el mantenimiento de tu nave para que no tengas que preocuparte.
→ blacknova.es

#Mantenimiento #NavesIndustriales #Catalunya #GestiónIndustrial #Blacknova #ActivosIndustriales #Industria""",
    },
    {
        "semana": 6, "dia": "Viernes", "tipo": "Educativo — Naves",
        "titulo": "Invertir en naves industriales en Catalunya",
        "imagen_prompt": "Modern industrial real estate investment concept, warehouse exterior with financial data overlay, professional photography, dark dramatic tones, Catalunya Spain",
        "caption": """Las naves industriales en Catalunya son uno de los activos inmobiliarios más rentables de España.

¿Por qué?

📈 Rentabilidad bruta del 6-8% anual (vs 3-4% del residencial)
📦 Alta demanda logística por el corredor mediterráneo
🚢 Proximidad al Puerto de Barcelona
🛣️ Acceso a red de autopistas europea
🏭 Escasez de producto de calidad disponible

Pero invertir sin gestión profesional es un riesgo.

En Blacknova gestionamos tu activo industrial en Catalunya de forma integral — para que la inversión rinda sin que dediques tiempo.

¿Tienes o buscas una nave industrial en Catalunya como inversión?
→ blacknova.es

#InversiónInmobiliaria #NavesIndustriales #Catalunya #ActivosIndustriales #Blacknova #Logística #Inmobiliario #Rentabilidad""",
    },
    {
        "semana": 7, "dia": "Lunes", "tipo": "Educativo — Naves",
        "titulo": "Normativa para naves industriales en Catalunya",
        "imagen_prompt": "Professional reviewing legal documents and regulations in modern industrial office, serious atmosphere, dark professional environment, golden light accents",
        "caption": """Operar una nave industrial en Catalunya sin cumplir la normativa es un riesgo muy serio.

Lo que debes tener en orden:

📋 LICENCIA DE ACTIVIDAD
Específica para tu tipo de uso. Sin ella no puedes operar.

🔥 PROTECCIÓN CONTRA INCENDIOS
Normativa RSCIEI obligatoria según superficie y actividad.

⚡ INSTALACIÓN ELÉCTRICA
Certificado de instalación por OCA (Organisme de Control Autoritzat).

♻️ GESTIÓN DE RESIDUOS
Plan de gestión de residuos industriales registrado.

🏗️ NORMATIVA URBANÍSTICA
Plan de ordenación urbanística municipal compatible con tu uso.

En Blacknova verificamos que tu nave cumple toda la normativa antes de que empieces a operar.
→ blacknova.es

#Normativa #NavesIndustriales #Catalunya #LicenciaDeActividad #Industria #Blacknova #Cumplimiento #GestiónIndustrial""",
    },
    {
        "semana": 7, "dia": "Miércoles", "tipo": "Educativo — Naves",
        "titulo": "Reforma de nave industrial paso a paso",
        "imagen_prompt": "Industrial warehouse renovation in progress, construction workers and project managers, dramatic construction site photography, dark industrial tones, Catalunya",
        "caption": """Reformar una nave industrial en Catalunya tiene sus particularidades. Aquí el proceso correcto:

𝟏. AUDITORÍA PREVIA
Inspección técnica del estado actual. Identificación de problemas ocultos.

𝟐. PROYECTO TÉCNICO
Redacción del proyecto por arquitecto o ingeniero industrial.

𝟑. LICENCIA DE OBRAS
Solicitud al ayuntamiento. Puede tardar 2-6 meses según el municipio.

𝟒. EJECUCIÓN
Coordinación de industriales: estructura, electricidad, fontanería, contra incendios.

𝟓. LEGALIZACIÓN
Certificado final de obra y obtención de licencia de actividad.

𝟔. ENTREGA
Inspección final y documentación del activo.

En Blacknova gestionamos el proceso completo.
→ blacknova.es

#Reforma #NavesIndustriales #Construcción #Catalunya #ProjectManager #PMI #Blacknova #Industria""",
    },
    {
        "semana": 7, "dia": "Viernes", "tipo": "Educativo — Naves",
        "titulo": "Sostenibilidad en naves industriales",
        "imagen_prompt": "Sustainable industrial warehouse with solar panels on roof, green building concept, modern architecture, dramatic sky, Catalunya Spain, professional photography",
        "caption": """La sostenibilidad en naves industriales ya no es una opción — es una exigencia del mercado.

Las empresas que alquilan o compran naves en Catalunya cada vez exigen más:

☀️ Certificación energética B o superior
🌿 Paneles solares en cubierta
💧 Sistemas de recogida de agua de lluvia
🚗 Puntos de carga para vehículos eléctricos
♻️ Materiales de construcción sostenibles
📊 Monitorización del consumo energético en tiempo real

Una nave sostenible vale un 15-20% más en el mercado.

En Blacknova integramos criterios de sostenibilidad en la gestión de todos nuestros activos.
→ blacknova.es

#Sostenibilidad #NavesIndustriales #Catalunya #GreenBuilding #Energía #Blacknova #ActivosIndustriales #Construcción""",
    },
    {
        "semana": 8, "dia": "Lunes", "tipo": "Educativo — Naves",
        "titulo": "Cómo negociar el alquiler de una nave industrial",
        "imagen_prompt": "Professional business negotiation meeting in modern industrial office, serious atmosphere, dark professional tones, golden light, contracts on table",
        "caption": """Negociar el alquiler de una nave industrial en Catalunya correctamente puede ahorrarte miles de euros al año.

Lo que siempre debes negociar:

💰 PRECIO
El precio de salida siempre tiene margen. Empieza con una oferta un 10-15% inferior.

📅 PERÍODO DE CARENCIA
Pide 1-3 meses de alquiler gratuito para acondicionar la nave.

🔧 OBRAS DE ADECUACIÓN
¿Quién paga las obras necesarias para tu actividad? Negócialo antes de firmar.

⏳ DURACIÓN Y PRÓRROGAS
Mínimo 3 años con opción de prórroga. Estabilidad para tu operativa.

📈 REVISIÓN DE RENTA
IPC limitado o precio fijo los primeros años.

🔚 CONDICIONES DE SALIDA
Define claramente el estado de entrega al final del contrato.

En Blacknova negociamos por ti.
→ blacknova.es

#Negociación #NavesIndustriales #Catalunya #Alquiler #Logística #Blacknova #ActivosIndustriales #Inmobiliario""",
    },
    {
        "semana": 8, "dia": "Miércoles", "tipo": "Educativo — Naves",
        "titulo": "Gestión de activos inmobiliarios industriales",
        "imagen_prompt": "Asset management concept with industrial real estate portfolio, professional office environment, dark elegant tones, golden accents, data on screens",
        "caption": """Si tienes una nave industrial en Catalunya, tienes un activo que debe gestionarse profesionalmente.

La gestión de activos inmobiliarios industriales incluye:

📋 Gestión de contratos de arrendamiento
🔧 Coordinación del mantenimiento
📊 Reporting periódico al propietario
⚖️ Control de normativa y licencias
💰 Optimización de la rentabilidad
🔍 Auditorías técnicas periódicas
🤝 Relación con inquilinos

Sin gestión profesional, un activo industrial puede perder un 20-30% de su valor en 5 años por deterioro, conflictos con inquilinos o incumplimiento normativo.

En Blacknova somos tu gestor de activos industriales en Catalunya.
→ blacknova.es

#GestiónDeActivos #NavesIndustriales #Catalunya #ActivosIndustriales #Blacknova #Inmobiliario #Inversión #GestiónInmobiliaria""",
    },
    {
        "semana": 8, "dia": "Viernes", "tipo": "Educativo — Naves",
        "titulo": "El futuro de las naves industriales en Catalunya",
        "imagen_prompt": "Futuristic modern industrial warehouse with automation technology, robotic systems, dramatic lighting, dark high-tech atmosphere, Catalunya Spain",
        "caption": """Las naves industriales en Catalunya están evolucionando. Esto es lo que viene.

🤖 AUTOMATIZACIÓN
Cada vez más naves integran sistemas automatizados de almacenaje y picking. Las naves deben diseñarse para ello.

⚡ ELECTRIFICACIÓN
Crecimiento exponencial de vehículos eléctricos logísticos. Las naves necesitan infraestructura de carga.

☀️ AUTOCONSUMO ENERGÉTICO
Paneles solares + baterías de almacenamiento. El objetivo: nave de consumo casi cero.

🏙️ ÚLTIMA MILLA
Demanda creciente de naves urbanas pequeñas para entrega en 2 horas.

📦 FRÍO Y TEMPERATURA CONTROLADA
Crecimiento del e-commerce alimentario.

Las empresas y propietarios que anticipen estas tendencias ganarán posición en el mercado.

En Blacknova te ayudamos a posicionarte.
→ blacknova.es

#FuturoIndustrial #NavesIndustriales #Catalunya #Logística #Automatización #Blacknova #ActivosIndustriales #Tendencias""",
    },

    # ══════════════════════════════════════════════════════════
    # MES 3 — TALENTO + CASOS + LLAMADAS A LA ACCIÓN (semanas 9-12)
    # ══════════════════════════════════════════════════════════
    {
        "semana": 9, "dia": "Lunes", "tipo": "Talento",
        "titulo": "Selección de talento técnico en Catalunya",
        "imagen_prompt": "Professional job interview in modern industrial office, serious atmosphere, dark professional tones, golden light, two professionals talking",
        "caption": """Encontrar un buen Project Manager en Catalunya no es fácil.

En Blacknova lo hacemos diferente:

No publicamos ofertas y esperamos.
Buscamos activamente en nuestra red de más de 500 profesionales técnicos en Catalunya y Europa.

¿Qué perfiles tenemos?

→ Project Managers con certificación PMP/PMI
→ Ingenieros industriales y de edificación
→ Jefes de obra especializados en industrial
→ Arquitectos técnicos
→ Controllers financieros de proyecto
→ Coordinadores de seguridad y salud

Garantía de sustitución incluida.
Seguimiento post-incorporación garantizado.

¿Necesitas incorporar talento técnico a tu empresa en Catalunya?
→ blacknova.es

#Talento #ProjectManager #Ingeniería #Catalunya #Selección #Blacknova #RRHH #Construcción""",
    },
    {
        "semana": 9, "dia": "Miércoles", "tipo": "Talento",
        "titulo": "Por qué los ingenieros eligen Blacknova",
        "imagen_prompt": "Confident industrial engineer at project site in Catalunya, hard hat, professional posture, dramatic industrial background, golden light",
        "caption": """Si eres ingeniero o Project Manager en Catalunya, esto te interesa.

Los profesionales técnicos que trabajan con Blacknova valoran:

🎯 PROYECTOS REALES Y DESAFIANTES
No trabajos rutinarios. Proyectos industriales de verdad en Catalunya y Europa.

💼 METODOLOGÍA PROFESIONAL
Trabajamos con PMI. Aprenderás y aplicarás los mejores estándares.

🌍 RED EUROPEA
Acceso a proyectos en España, Francia, Alemania y más.

📈 DESARROLLO PROFESIONAL
Acompañamiento y formación continua.

🤝 RELACIÓN A LARGO PLAZO
No somos una ETT. Construimos relaciones profesionales duraderas.

¿Eres Project Manager o ingeniero industrial en Catalunya?
→ Mándanos tu perfil en blacknova.es

#Ingeniería #ProjectManager #Empleo #Catalunya #Oportunidades #Blacknova #PMI #Construcción""",
    },
    {
        "semana": 9, "dia": "Viernes", "tipo": "Llamada a la acción",
        "titulo": "¿Tienes un proyecto industrial en Catalunya?",
        "imagen_prompt": "Industrial construction project in Catalunya at sunset, project manager overlooking site, dramatic sky, professional photography, dark golden tones",
        "caption": """¿Tienes un proyecto industrial en Catalunya y no sabes por dónde empezar?

En Blacknova hacemos algo muy simple:

📞 Primera consulta gratuita
Analizamos tu proyecto o activo sin compromiso.

📋 Propuesta en 48 horas
Plan de acción detallado con alcance y honorarios.

✅ Empezamos cuando quieras
Sin burocracia, sin contratos kilométricos.

Gestionamos proyectos de:
→ Construcción y reforma de naves industriales
→ Gestión de activos inmobiliarios industriales
→ Coordinación de proyectos de ingeniería
→ Selección de talento técnico especializado

¿Hablamos?
📩 Escríbenos en blacknova.es

#Blacknova #GestiónDeProyectos #NavesIndustriales #Catalunya #ProjectManager #Contacto #Ingeniería #PMI""",
    },
    {
        "semana": 10, "dia": "Lunes", "tipo": "Educativo",
        "titulo": "Cómo elegir un buen consultor de proyectos",
        "imagen_prompt": "Professional consultant presentation in modern industrial boardroom, dark elegant atmosphere, professional serious tone, golden accents, Catalunya",
        "caption": """No todos los consultores de proyectos son iguales. Cómo elegir el correcto.

✅ DEBE TENER
→ Certificación PMP o equivalente
→ Experiencia real en tu sector (industrial, construcción)
→ Referencias verificables de proyectos anteriores
→ Metodología documentada y transparente
→ Sistema de reporting claro para el cliente

❌ SEÑALES DE ALARMA
→ No tiene proyectos de referencia en tu sector
→ No puede explicar su metodología claramente
→ Solo habla de precio, no de valor
→ No tiene equipo detrás
→ No ofrece garantías

En Blacknova cumplimos todos los criterios positivos.
→ Verifica nuestro trabajo en blacknova.es

#Consultoría #ProjectManager #GestiónDeProyectos #Catalunya #PMI #Blacknova #Construcción #Ingeniería""",
    },
    {
        "semana": 10, "dia": "Miércoles", "tipo": "Educativo",
        "titulo": "Digitalización en la gestión de proyectos industriales",
        "imagen_prompt": "Digital project management dashboard on multiple screens in dark modern industrial office, data visualization, professional atmosphere, golden light accents",
        "caption": """La gestión de proyectos industriales ha cambiado radicalmente en los últimos 5 años.

Las herramientas que usamos en Blacknova:

📊 PLANIFICACIÓN
Microsoft Project / Primavera P6 para cronogramas complejos.

📋 GESTIÓN DE TAREAS
Asana / Monday para coordinación de equipos.

💬 COMUNICACIÓN
Teams / Slack para comunicación en tiempo real con cliente y equipo.

📁 DOCUMENTACIÓN
SharePoint / Google Drive para gestión documental centralizada.

📈 REPORTING
Power BI para dashboards de estado del proyecto en tiempo real.

El cliente puede ver el estado de su proyecto en cualquier momento. Eso es transparencia real.

🌐 blacknova.es

#Digitalización #ProjectManager #GestiónDeProyectos #PMI #Catalunya #Blacknova #Tecnología #Construcción""",
    },
    {
        "semana": 10, "dia": "Viernes", "tipo": "Llamada a la acción",
        "titulo": "¿Tienes una nave industrial sin gestionar?",
        "imagen_prompt": "Empty industrial warehouse with potential, dramatic lighting, dark tones, golden light through windows, Catalunya Spain, professional photography",
        "caption": """¿Tienes una nave industrial en Catalunya que no está rindiendo todo lo que podría?

Puede deberse a:
→ Inquilino que no paga puntualmente
→ Mantenimiento que se acumula sin atender
→ Normativa que no está al día
→ Renta por debajo del mercado
→ Nave vacía sin comercialización activa

En Blacknova tomamos la gestión de tu nave de forma integral.

Tú eres el propietario.
Nosotros nos encargamos de todo lo demás.

📊 Reporting mensual
🔧 Mantenimiento coordinado
⚖️ Gestión de contratos
💰 Optimización de rentabilidad

Primera auditoría gratuita.
→ blacknova.es

#NavesIndustriales #GestiónDeActivos #Catalunya #Propietario #Blacknova #ActivosIndustriales #Inmobiliario #Rentabilidad""",
    },
    {
        "semana": 11, "dia": "Lunes", "tipo": "Educativo",
        "titulo": "ROI de contratar un Project Manager",
        "imagen_prompt": "ROI calculation and project success metrics on professional screen, modern industrial office, dark elegant atmosphere, golden accents, data visualization",
        "caption": """¿Cuánto cuesta no tener un Project Manager? Más de lo que crees.

Un proyecto industrial de 1M€ sin gestión profesional puede sufrir:

❌ Sobrecosto del 30-40% → 300.000-400.000€ adicionales
❌ Retraso de 3-6 meses → Costes de oportunidad enormes
❌ Problemas legales y técnicos no previstos
❌ Conflictos con subcontratas no resueltos

Los honorarios de un Project Manager representan entre el 3-8% del presupuesto total.

En un proyecto de 1M€: 30.000-80.000€.
Vs un sobrecosto potencial de 300.000-400.000€.

El ROI de contratar un buen Project Manager es evidente.

En Blacknova somos tu Project Manager en Catalunya.
→ blacknova.es

#ROI #ProjectManager #GestiónDeProyectos #Catalunya #PMI #Construcción #Blacknova #Inversión""",
    },
    {
        "semana": 11, "dia": "Miércoles", "tipo": "Educativo",
        "titulo": "Seguridad y salud en obras industriales",
        "imagen_prompt": "Safety coordinator in industrial construction site, hard hat and safety equipment, professional serious atmosphere, dark industrial environment, Catalunya",
        "caption": """La seguridad en obras industriales no es opcional. Es una obligación legal y ética.

En Catalunya, toda obra con más de 500m² o 30 días de duración necesita:

📋 Plan de seguridad y salud
Obligatorio antes del inicio de cualquier obra.

👷 Coordinador de seguridad y salud
Figura obligatoria por normativa española.

🦺 Formación de todos los trabajadores
Específica para el tipo de trabajo y riesgos del proyecto.

📊 Libro de incidencias
Registro de todas las incidencias y visitas de inspección.

🏥 Plan de emergencia
Protocolo claro en caso de accidente.

En Blacknova coordinamos la seguridad y salud en todos nuestros proyectos.
Porque la seguridad de las personas siempre es lo primero.

🌐 blacknova.es

#SeguridadYSalud #Construcción #Catalunya #Obra #ProjectManager #PMI #Blacknova #Normativa""",
    },
    {
        "semana": 11, "dia": "Viernes", "tipo": "Llamada a la acción",
        "titulo": "Únete al equipo Blacknova",
        "imagen_prompt": "Professional team collaboration in modern industrial office, serious confident atmosphere, dark elegant tones, golden light, Catalunya Spain",
        "caption": """¿Eres Project Manager o ingeniero industrial en Catalunya?

En Blacknova siempre buscamos profesionales con:

✔ Certificación PMP o experiencia equivalente
✔ Experiencia en proyectos industriales o de construcción
✔ Capacidad de gestión de equipos y subcontratas
✔ Orientación al cliente y a resultados
✔ Ganas de crecer en una empresa en expansión

Lo que ofrecemos:
→ Proyectos reales y desafiantes en Catalunya y Europa
→ Metodología PMI y formación continua
→ Red profesional europea
→ Relación profesional a largo plazo

¿Te identificas?
→ Envíanos tu perfil en blacknova.es

#Empleo #ProjectManager #Ingeniería #Catalunya #Trabajo #Blacknova #PMI #Oportunidades""",
    },
    {
        "semana": 12, "dia": "Lunes", "tipo": "Resumen",
        "titulo": "Todo lo que hace Blacknova",
        "imagen_prompt": "Comprehensive overview of industrial project management in Catalunya, professional team with blueprints and data, dark dramatic atmosphere, golden tones",
        "caption": """3 meses después de lanzar este perfil, queremos recordarte lo que hacemos en Blacknova.

𝗚𝗘𝗦𝗧𝗜Ó𝗡 𝗗𝗘 𝗣𝗥𝗢𝗬𝗘𝗖𝗧𝗢𝗦
Coordinamos proyectos de construcción e ingeniería industrial en Catalunya con metodología PMI.

𝗚𝗘𝗦𝗧𝗜Ó𝗡 𝗗𝗘 𝗔𝗖𝗧𝗜𝗩𝗢𝗦 𝗜𝗡𝗠𝗢𝗕𝗜𝗟𝗜𝗔𝗥𝗜𝗢𝗦
Gestionamos naves industriales para propietarios e inversores en Catalunya.

𝗦𝗘𝗟𝗘𝗖𝗖𝗜Ó𝗡 𝗗𝗘 𝗧𝗔𝗟𝗘𝗡𝗧𝗢
Conectamos empresas con los mejores ingenieros y Project Managers de Catalunya y Europa.

10+ años de experiencia.
Metodología PMI.
Red europea de profesionales.

¿Necesitas alguno de estos servicios?
→ Primera consulta gratuita en blacknova.es

#Blacknova #GestiónDeProyectos #NavesIndustriales #Talento #Catalunya #PMI #Ingeniería #Construcción""",
    },
    {
        "semana": 12, "dia": "Miércoles", "tipo": "Llamada a la acción",
        "titulo": "Primera consulta gratuita",
        "imagen_prompt": "Professional consultation meeting in modern industrial office, serious professional atmosphere, dark elegant tones, golden light, handshake moment",
        "caption": """Si llevas tiempo pensando en gestionar mejor tu proyecto o activo industrial en Catalunya, este es el momento.

Primera consulta con Blacknova: gratuita y sin compromiso.

En 45 minutos analizamos:
→ Tu proyecto o activo industrial
→ Los puntos de mejora
→ Cómo podemos ayudarte
→ Qué costaría y qué ahorrarías

Sin presión. Sin letra pequeña.
Solo una conversación profesional entre personas que quieren que tu proyecto funcione.

📩 Escríbenos en blacknova.es
O envíanos un mensaje directo aquí.

#Blacknova #ConsultaGratuita #GestiónDeProyectos #NavesIndustriales #Catalunya #PMI #Ingeniería #Construcción""",
    },
    {
        "semana": 12, "dia": "Viernes", "tipo": "Cierre",
        "titulo": "Gracias por seguirnos — el camino continúa",
        "imagen_prompt": "Successful industrial project completion in Catalunya, dramatic sunset over modern industrial building, professional photography, golden tones, achievement atmosphere",
        "caption": """3 meses, 36 publicaciones, todo lo que sabemos sobre gestión de proyectos y naves industriales en Catalunya.

Gracias por seguirnos.

Seguiremos compartiendo conocimiento, casos prácticos y todo lo que necesitas saber para gestionar mejor tus proyectos y activos industriales.

Porque creemos que el conocimiento compartido hace mejores proyectos.

Y los mejores proyectos hacen mejores empresas.

Si tienes un proyecto o activo industrial en Catalunya, ya sabes dónde encontrarnos.
→ blacknova.es

El camino continúa.

— El equipo Blacknova

#Blacknova #GestiónDeProyectos #NavesIndustriales #Catalunya #PMI #Ingeniería #Construcción #Gracias""",
    },
]

def generar_calendario():
    calendario = []
    dias_semana = {"Lunes": 0, "Miércoles": 2, "Viernes": 4}

    for post in CONTENIDO:
        semana = post["semana"]
        dia = post["dia"]
        offset_dias = (semana - 1) * 7 + dias_semana[dia]
        fecha = INICIO + timedelta(days=offset_dias)

        calendario.append({
            **post,
            "fecha": fecha.strftime("%d/%m/%Y"),
            "fecha_dt": fecha,
        })

    return sorted(calendario, key=lambda x: x["fecha_dt"])

def guardar_txt(calendario):
    with open("blacknova_instagram_3meses.txt", "w", encoding="utf-8") as f:
        f.write("=" * 70 + "\n")
        f.write("BLACKNOVA — INSTAGRAM 3 MESES COMPLETO\n")
        f.write(f"36 publicaciones · Abril — Junio 2026\n")
        f.write("=" * 70 + "\n\n")

        f.write("ESTRUCTURA DEL PLAN:\n")
        f.write("─" * 40 + "\n")
        f.write("MES 1 (Semanas 1-2): Presentación de Blacknova\n")
        f.write("MES 1 (Semanas 3-4): Gestión de proyectos industriales\n")
        f.write("MES 2 (Semanas 5-8): Naves industriales en Catalunya\n")
        f.write("MES 3 (Semanas 9-12): Talento + Llamadas a la acción\n\n")

        semana_actual = 0
        for entrada in calendario:
            if entrada["semana"] != semana_actual:
                semana_actual = entrada["semana"]
                f.write(f"\n{'═' * 70}\n")
                f.write(f"SEMANA {semana_actual}\n")
                f.write(f"{'═' * 70}\n\n")

            f.write(f"📅 {entrada['fecha']} ({entrada['dia']}) — {entrada['tipo'].upper()}\n")
            f.write(f"🎯 {entrada['titulo']}\n\n")

            f.write("🖼️  PROMPT PARA IMAGEN IA:\n")
            f.write(f"{entrada['imagen_prompt']}\n\n")

            f.write("📝 CAPTION INSTAGRAM:\n")
            f.write("─" * 50 + "\n")
            f.write(entrada["caption"] + "\n")
            f.write("─" * 50 + "\n\n")

        f.write("\n" + "=" * 70 + "\n")
        f.write("INSTRUCCIONES DE USO:\n")
        f.write("─" * 40 + "\n")
        f.write("1. Copia el PROMPT de cada post y pégalo en:\n")
        f.write("   → Claude (gratis con Pro) para generar la imagen\n")
        f.write("   → Midjourney (10€/mes) para mayor calidad\n")
        f.write("   → DALL-E en ChatGPT (20€/mes)\n\n")
        f.write("2. Descarga la imagen generada\n\n")
        f.write("3. Copia el CAPTION y publícalo en Instagram junto a la imagen\n\n")
        f.write("4. Publica en los horarios óptimos:\n")
        f.write("   → Lunes: 9:00-11:00h\n")
        f.write("   → Miércoles: 18:00-20:00h\n")
        f.write("   → Viernes: 12:00-14:00h\n\n")
        f.write("5. Responde a todos los comentarios en las primeras 2 horas\n")

    print("✅ blacknova_instagram_3meses.txt generado")

if __name__ == "__main__":
    print("📸 Generando plan Instagram 3 meses para Blacknova...\n")
    calendario = generar_calendario()

    meses = {}
    for e in calendario:
        mes = e["fecha_dt"].strftime("%B %Y")
        meses[mes] = meses.get(mes, 0) + 1

    print(f"   📅 Período: {calendario[0]['fecha']} → {calendario[-1]['fecha']}")
    print(f"   📸 Total publicaciones: {len(calendario)}")
    for mes, total in meses.items():
        print(f"   → {mes}: {total} posts")

    tipos = {}
    for e in calendario:
        tipos[e["tipo"]] = tipos.get(e["tipo"], 0) + 1
    print(f"\n   Tipos de contenido:")
    for tipo, total in sorted(tipos.items()):
        print(f"   → {tipo}: {total} posts")

    print()
    guardar_txt(calendario)
    print("\n📌 Abre blacknova_instagram_3meses.txt para ver todo el contenido")
    print("   Cada post incluye el prompt para generar la imagen con IA")
