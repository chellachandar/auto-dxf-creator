import streamlit as st

st.set_page_config(page_title="DXF Creator", page_icon="⚡")

st.title("⚡ Electrical Symbol DXF Creator")

st.write("Simple DXF file generator")

# Create tabs
tab1, tab2, tab3 = st.tabs(["Home", "Symbols", "Create"])

with tab1:
    st.write("### Welcome")
    st.write("This app creates electrical drawing files.")

with tab2:
    st.write("### Available Symbols")
    st.write("""
    - CB: Circuit Breaker
    - DS: Disconnect Switch  
    - ES: Earthing Switch
    - LA: Lightning Arrester
    - L: Reactor
    """)

with tab3:
    st.write("### Create DXF File")
    
    title = st.text_input("Title:", "My Drawing")
    symbol1 = st.text_input("Symbol 1:", "CB")
    symbol2 = st.text_input("Symbol 2:", "DS")
    
    if st.button("Create DXF", use_container_width=True):
        # Create simple DXF content
        dxf_text = f"""  0
SECTION
  2
HEADER
  9
$ACADVER
  1
AC1021
  0
ENDSEC
  0
SECTION
  2
ENTITIES
  0
TEXT
  8
0
 10
10.0
 20
50.0
 40
5.0
  1
{title}
  0
TEXT
  8
0
 10
10.0
 20
35.0
 40
3.0
  1
{symbol1}
  0
TEXT
  8
0
 10
10.0
 20
25.0
 40
3.0
  1
{symbol2}
  0
ENDSEC
  0
EOF"""
        
        st.success("✓ File created!")
        
        st.download_button(
            label="📥 Download DXF",
            data=dxf_text,
            file_name=f"{title}.dxf",
            mime="text/plain",
            use_container_width=True
        )

st.write("---")
st.write("💡 No installation needed - runs on cloud!")
