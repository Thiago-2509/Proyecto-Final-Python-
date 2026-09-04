import streamlit as st

# ==========================================
# CONFIGURACIÓN
# ==========================================

st.set_page_config(
    page_title="Smart Training",
    page_icon="💪"
)

st.title("💪 Smart Training")
st.write("Sistema de seguimiento de ejercicios")

# Guardar ejercicios durante la sesión
if "ejercicios" not in st.session_state:
    st.session_state.ejercicios = []


# ==========================================
# OPCIÓN 1: AGREGAR EJERCICIO
# ==========================================

def agregarEjercicio():
    st.header("➕ Agregar ejercicio")

    with st.form("formulario_ejercicio"):

        semana = st.number_input(
            "¿En qué semana desea agregar el ejercicio?",
            min_value=1,
            step=1
        )

        nombre = st.text_input(
            "¿Qué ejercicio desea agregar?"
        )

        series = st.number_input(
            "¿Cuántas series son?",
            min_value=1,
            step=1
        )

        repeticiones = st.number_input(
            "¿Cuántas repeticiones son?",
            min_value=1,
            step=1
        )

        enviar = st.form_submit_button("Agregar ejercicio")

        if enviar:

            if nombre.strip() == "":
                st.error("Debe ingresar el nombre del ejercicio.")

            else:

                ejercicio = {
                    "semana": semana,
                    "nombre": nombre,
                    "series": series,
                    "repeticiones": repeticiones
                }

                st.session_state.ejercicios.append(ejercicio)

                st.success("✅ Ejercicio agregado correctamente")


# ==========================================
# OPCIÓN 2: VER HISTORIAL
# ==========================================

def verHistorial():

    st.header("📋 Historial semanal")

    ejercicios = st.session_state.ejercicios

    if len(ejercicios) == 0:

        st.info("No hay ejercicios registrados.")

    else:

        for ejercicio in ejercicios:

            st.subheader(ejercicio["nombre"])

            st.write("**Semana:**", ejercicio["semana"])
            st.write("**Series:**", ejercicio["series"])
            st.write("**Repeticiones:**", ejercicio["repeticiones"])

            st.divider()


# ==========================================
# OPCIÓN 3: CALCULAR PROGRESO
# ==========================================

def calcularProgreso():

    st.header("📈 Calcular progreso")

    ejercicios = st.session_state.ejercicios

    if len(ejercicios) == 0:

        st.info("No hay ejercicios registrados.")

    else:

        st.write(
            "Cantidad de ejercicios registrados:",
            len(ejercicios)
        )

        for ejercicio in ejercicios:

            total = (
                ejercicio["series"] *
                ejercicio["repeticiones"]
            )

            st.subheader(ejercicio["nombre"])

            st.write(
                "Semana:",
                ejercicio["semana"]
            )

            st.write(
                "Repeticiones totales:",
                total
            )

            st.divider()


# ==========================================
# OPCIÓN 4: BUSCAR EJERCICIO
# ==========================================

def buscarEjercicio():

    st.header("🔎 Buscar ejercicio")

    ejercicios = st.session_state.ejercicios

    nombre = st.text_input(
        "¿Qué ejercicio desea buscar?"
    )

    if st.button("Buscar"):

        encontrado = False

        for ejercicio in ejercicios:

            if ejercicio["nombre"].lower() == nombre.lower():

                st.success("Ejercicio encontrado")

                st.write(
                    "**Semana:**",
                    ejercicio["semana"]
                )

                st.write(
                    "**Ejercicio:**",
                    ejercicio["nombre"]
                )

                st.write(
                    "**Series:**",
                    ejercicio["series"]
                )

                st.write(
                    "**Repeticiones:**",
                    ejercicio["repeticiones"]
                )

                encontrado = True

        if not encontrado:
            st.warning("No se encontró ese ejercicio.")


# ==========================================
# MENÚ PRINCIPAL
# ==========================================

st.sidebar.title("📋 Menú")

opcion = st.sidebar.selectbox(
    "¿Qué deseas hacer?",
    [
        "Inicio",
        "Agregar ejercicio",
        "Ver historial",
        "Calcular progreso",
        "Buscar ejercicio"
    ]
)


# ==========================================
# EJECUTAR OPCIÓN
# ==========================================

if opcion == "Inicio":

    st.subheader("Bienvenido a Smart Training")

    st.write(
        "Selecciona una opción en el menú "
        "para comenzar."
    )

    st.metric(
        "Ejercicios registrados",
        len(st.session_state.ejercicios)
    )


elif opcion == "Agregar ejercicio":

    agregarEjercicio()


elif opcion == "Ver historial":

    verHistorial()


elif opcion == "Calcular progreso":

    calcularProgreso()


elif opcion == "Buscar ejercicio":

    buscarEjercicio()