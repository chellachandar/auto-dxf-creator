import streamlit as st

st.set_page_config(
    page_title="Electrical Symbol Generator",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ Electrical Symbol Drawing Generator")
st.write("Create DXF drawings with electrical symbols")

# Tabs
tab1, tab2, tab3 = st.tabs(["About", "Symbols", "Create Drawing"])

with tab1:
    st.header("About This App")
    st.write("""
    This app helps you create electrical drawings with IEC 60617 symbols.
    
    **Available symbols**:
    - CB: Circuit Breaker
    - DS: Disconnect Switch
    - ES: Earthing Switch
    - LA: Lightning Arrester
    - L: Reactor
    - CT: Current Transformer
    - VT: Voltage Transformer
    """)

with tab2:
    st.header("Available Symbols")
    st.write("""
    ### IEC 60617 Electrical Symbols
    
    | Symbol | Name |
    |--------|------|
    | CB | Circuit Breaker |
    | DS | Disconnect Switch |
    | ES | Earthing Switch |
    | LA | Lightning Arrester |
    | L | Reactor |
    | CT | Current Transformer |
    | VT | Voltage Transformer |
    | GND | Ground |
    """)

with tab3:
    st.header("Create DXF Drawing")
    st.write("### Quick Drawing Creator")
    
    col1, col2 = st.columns(2)
    
    with col1:
        title = st.text_input("Drawing Title:", "My Circuit")
    
    with col2:
        num_symbols = st.slider("Number of symbols:", 1, 5, 2)
    
    symbols_list = []
    for i in range(num_symbols):
        sym = st.text_input(f"Symbol {i+1}:", "CB")
        symbols_list.append(sym)
    
    if st.button("📐 Create Drawing", use_container_width=True):
        # Create simple DXF file
        dxf_content = create_simple_dxf(title, symbols_list)
        
        st.success("✓ Drawing created!")
        
        st.download_button(
            label="📥 Download DXF File",
            data=dxf_content,
            file_name=f"{title.replace(' ', '_')}.dxf",
            mime="application/octet-stream",
            use_container_width=True
        )

def create_simple_dxf(title, symbols):
    """Create a simple DXF file content as text"""
    
    dxf = """  0
SECTION
  2
HEADER
  9
$ACADVER
  1
AC1021
  9
$EXTMIN
 10
0.0
 20
0.0
  9
$EXTMAX
 10
100.0
 20
100.0
  0
ENDSEC
  0
SECTION
  2
ENTITIES
"""
    
    # Add title text
    dxf += f"""  0
TEXT
  8
0
 10
10.0
 20
80.0
 40
5.0
  1
{title}
  0
"""
    
    # Add symbols as text
    y_pos = 60
    for i, symbol in enumerate(symbols):
        dxf += f"""TEXT
  8
0
 10
10.0
 20
{y_pos}
 40
3.0
  1
{symbol}
  0
"""
        y_pos -= 15
    
    # End of DXF
    dxf += """ENDSEC
  0
EOF
"""
    
    return dxf

# Footer
st.divider()
st.write("💡 Simple DXF creator - no installation needed!")
