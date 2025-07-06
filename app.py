import streamlit as st
import time
from Neutrosophic_Cubic_Sets import NCS, NCN

# Page setup
st.set_page_config(page_title = "NCS Tool", layout = "wide")

# Custom CSS to hide all link icons

st.markdown("""
    <style>
        /* Hide all link icons and prevent link behavior */
        a {
            text-decoration: none !important;
            pointer-events: none !important;
            color: inherit !important;
        }

        /* Hide fullscreen buttons */
        button[title = "View fullscreen"] {
            display: none !important;
        }

        /* Hide markdown link icons */
        [data-testid = "stMarkdownContainer"] a {
            display: none !important;
        }

        /* Textarea styling */
        .stTextArea textarea {
            font-family: monospace;
        }

        /* Control page width */
        .stMainBlockContainer {
            max-width: 80rem;
        }
    </style>
    """, unsafe_allow_html = True)

st.markdown("<h1 style = 'text-align: center;'>Python Tool for Neutrosophic Cubic Sets</h1>", unsafe_allow_html = True)


# Session State Initialization
for key in ["ncs_list_A", "ncs_list_B", "message_A", "message_B"]:
    if key not in st.session_state:
        st.session_state[key] = [] if "list" in key else ""


# --- Input Columns for A and B ---
colA, colB = st.columns(2)

with colA:
    st.markdown("<h3 style = 'text-align: center;'>NCS A</h3>", unsafe_allow_html = True)
    T_A = tuple(round(v, 2) for v in st.slider("Lower Truth, Upper Truth", 0.0, 1.0, (0.2, 0.3), 0.01, key = "T_A"))
    I_A = tuple(round(v, 2) for v in st.slider("Lower Indeterminacy, Upper Indeterminacy", 0.0, 1.0, (0.3, 0.5), 0.01, key = "I_A"))
    F_A = tuple(round(v, 2) for v in st.slider("Lower Fallacy, Upper Fallacy", 0.0, 1.0, (0.7, 0.9), 0.01, key = "F_A"))
    t_A = round(st.number_input("Truth", 0.0, 1.0, 0.35, 0.01, key = "t_A"), 2)
    i_A = round(st.number_input("Indeterminacy", 0.0, 1.0, 0.25, 0.01, key = "i_A"), 2)
    f_A = round(st.number_input("Fallacy", 0.0, 1.0, 0.4, 0.01, key = "f_A"), 2)

    if st.button("Add this element to A"):
        if len(st.session_state.ncs_list_A) > len(st.session_state.ncs_list_B):
            st.warning("Add an element to B before adding more to A.")
        else:
            st.session_state.ncs_list_A.append([list(T_A), list(I_A), list(F_A), [t_A, i_A, f_A]])
            st.session_state.message_A = "Added element to NCS A."

    if st.session_state.message_A:
        st.success(st.session_state.message_A)
        time.sleep(0.5)
        st.session_state.message_A = ""
        st.rerun()

    if st.session_state.ncs_list_A:
        try:
            NCS_A = NCS()
            for item in st.session_state.ncs_list_A:
                NCS_A.add_element(NCN(*item[0], *item[1], *item[2], *item[3]))
            st.session_state.NCS_A_obj = NCS_A
            st.text_area("NCS A be displayed here...", value = str(NCS_A), height = 150)
        except Exception as e:
            st.error(f"Error creating NCS A: {e}")

    if st.button("Reset A"):
        st.session_state.ncs_list_A = []
        st.rerun()

with colB:
    st.markdown("<h3 style = 'text-align: center;'>NCS B</h3>", unsafe_allow_html = True)
    T_B = tuple(round(v, 2) for v in st.slider("Lower Truth, Upper Truth", 0.0, 1.0, (0.2, 0.3), 0.01, key = "T_B"))
    I_B = tuple(round(v, 2) for v in st.slider("Lower Indeterminacy, Upper Indeterminacy", 0.0, 1.0, (0.3, 0.5), 0.01, key = "I_B"))
    F_B = tuple(round(v, 2) for v in st.slider("Lower Fallacy, Upper Fallacy", 0.0, 1.0, (0.7, 0.9), 0.01, key = "F_B"))
    t_B = round(st.number_input("Truth", 0.0, 1.0, 0.35, 0.01, key = "t_B"), 2)
    i_B = round(st.number_input("Indeterminacy", 0.0, 1.0, 0.25, 0.01, key = "i_B"), 2)
    f_B = round(st.number_input("Fallacy", 0.0, 1.0, 0.4, 0.01, key = "f_B"), 2)

    if st.button("Add this element to B"):
        if len(st.session_state.ncs_list_B) > len(st.session_state.ncs_list_A):
            st.warning("Add an element to A before adding more to B.")
        else:
            st.session_state.ncs_list_B.append([list(T_B), list(I_B), list(F_B), [t_B, i_B, f_B]])
            st.session_state.message_B = "Added element to NCS B."

    if st.session_state.message_B:
        st.success(st.session_state.message_B)
        time.sleep(0.5)
        st.session_state.message_B = ""
        st.rerun()

    if st.session_state.ncs_list_B:
        try:
            NCS_B = NCS()
            for item in st.session_state.ncs_list_B:
                NCS_B.add_element(NCN(*item[0], *item[1], *item[2], *item[3]))
            st.session_state.NCS_B_obj = NCS_B
            st.text_area("NCS B be displayed here...", value = str(NCS_B), height = 150)
        except Exception as e:
            st.error(f"Error creating NCS B: {e}")

    if st.button("Reset B"):
        st.session_state.ncs_list_B = []
        st.rerun()

# NCS Operations

if not st.session_state["ncs_list_A"] and not st.session_state["ncs_list_B"]:
    st.warning("Please add at least one element to both NCS A and NCS B to continue.")

elif not st.session_state["ncs_list_A"]:
    st.warning("Please add at least one element to NCS A to continue.")

elif not st.session_state["ncs_list_B"]:
    st.warning("Please add at least one element to NCS B to continue.")

elif len(st.session_state["ncs_list_A"]) < len(st.session_state["ncs_list_B"]):
    st.warning("NCS A has fewer elements. Please add another element to NCS A.")

elif len(st.session_state["ncs_list_A"]) > len(st.session_state["ncs_list_B"]):
    st.warning("NCS B has fewer elements. Please add another element to NCS B.")

else:

    st.markdown("---")
    st.subheader("Operations on Neutrosophic Cubic Sets")
    result = ""

    # Unary operations
    c1, c2 = st.columns(2)
    st.markdown("<h5>Unary Operations</h5>", unsafe_allow_html = True)
    with c1:
        unary_target = st.radio("Select NCS for unary operations:", ["NCS A", "NCS B"], horizontal = True)
    with c2:
        scalar = st.number_input("Enter scalar (For Scalar Multiplication):", min_value = 0.0, value = 1.0, step = 0.1, key = "scalar_input")

    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        if st.button("COMPLEMENT"):
            try:
                obj = st.session_state.get(f"NCS_{unary_target[-1]}_obj")
                result = str(obj.complement())
            except Exception as e:
                st.error(f"Error in complement: {e}")

    with c2:
        if st.button("ACCURACY"):
            try:
                obj = st.session_state.get(f"NCS_{unary_target[-1]}_obj")
                result = str(obj.accuracy())
            except Exception as e:
                st.error(f"Error in accuracy: {e}")

    with c3:
        if st.button("SCORE"):
            try:
                obj = st.session_state.get(f"NCS_{unary_target[-1]}_obj")
                result = str(obj.score())
            except Exception as e:
                st.error(f"Error in score: {e}")

    with c4:
        if st.button("CERTAINTY"):
            try:
                obj = st.session_state.get(f"NCS_{unary_target[-1]}_obj")
                result = str(obj.certainty())
            except Exception as e:
                st.error(f"Error in certainty: {e}")

    with c5:
        if st.button("SCALAR MULTIPLICATION"):
            try:
                obj = st.session_state.get(f"NCS_{unary_target[-1]}_obj")
                result = str(obj.scalar_multiplication(scalar))
            except Exception as e:
                st.error(f"Error in scalar multiplication: {e}")

    # Binary operations
    st.markdown("<h5>Binary Operations</h5>", unsafe_allow_html = True)
    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:
        if st.button("P-UNION"):
            try:
                result = str(st.session_state.NCS_A_obj.p_union(st.session_state.NCS_B_obj))
            except Exception as e:
                st.error(f"Error in P-Union: {e}")

    with c2:
        if st.button("P-INTERSECTION"):
            try:
                result = str(st.session_state.NCS_A_obj.p_intersection(st.session_state.NCS_B_obj))
            except Exception as e:
                st.error(f"Error in P-Intersection: {e}")

    with c3:
        if st.button("R-UNION"):
            try:
                result = str(st.session_state.NCS_A_obj.r_union(st.session_state.NCS_B_obj))
            except Exception as e:
                st.error(f"Error in R-Union: {e}")

    with c4:
        if st.button("R-INTERSECTION"):
            try:
                result = str(st.session_state.NCS_A_obj.r_intersection(st.session_state.NCS_B_obj))
            except Exception as e:
                st.error(f"Error in R-Intersection: {e}")

    with c5:
        if st.button("DISTANCE MEASURE"):
            try:
                result = st.session_state.NCS_A_obj.distance_measure(st.session_state.NCS_B_obj)
            except Exception as e:
                st.error(f"Error in computing distance: {e}")

    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:
        if st.button("ADDITION"):
            try:
                result = str(st.session_state.NCS_A_obj + st.session_state.NCS_B_obj)
            except Exception as e:
                st.error(f"Error in addition: {e}")

    with c2:
        if st.button("MULTIPLICATION"):
            try:
                result = str(st.session_state.NCS_A_obj * st.session_state.NCS_B_obj)
            except Exception as e:
                st.error(f"Error in multiplication: {e}")

    with c3:
        if st.button("EQUALITY"):
            try:
                result = st.session_state.NCS_A_obj = st.session_state.NCS_B_obj
            except Exception as e:
                st.error(f"Error in equality: {e}")

    with c4:
        if st.button("CONTAINMENT"):
            try:
                result = st.session_state.NCS_A_obj.containment(st.session_state.NCS_B_obj)
            except Exception as e:
                st.error(f"Error in containment: {e}")
    
    with c5:
        if st.button("CORRELATION"):
            try:
                result = st.session_state.NCS_A_obj.correlation_measure(st.session_state.NCS_B_obj)
            except Exception as e:
                st.error(f"Error in correlation coefficient: {e}")

    # Result
    st.markdown("<h4>Result of the Operation</h4>", unsafe_allow_html = True)
    st.text_area("Result will be displayed here...", value = str(result), height = 150)
