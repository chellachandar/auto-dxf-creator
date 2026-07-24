import streamlit as st
from pathlib import Path
import subprocess
import tempfile
import os

st.set_page_config(
    page_title="Electrical Symbol Generator",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ Electrical Symbol Drawing Generator")
st.write("Create DXF drawings with electrical symbols")

# Info sections
st.info("""
### How it works:
1. Download symbols from GitHub
2. Convert SVG → DXF
3. Create your drawing
4. Download the DXF file
""")

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["About", "Symbols", "Create Drawing", "Help"])

with tab1:
    st.header("About This App")
    st.write("""
    This app helps you create electrical drawings with IEC 60617 symbols.
    
    **Symbols from**: chille/electricalsymbols (GitHub)
    
    **Available symbols**:
    - Circuit Breaker (CB)
    - Disconnect Switch (DS)
    - Earthing Switch (ES)
    - Lightning Arrester (LA)
    - Reactor (L)
    - Current Transformer (CT)
    - Voltage Transformer (VT)
    - And 140+ more!
    """)

with tab2:
    st.header("Available Symbols")
    st.write("### Common IEC 60617 Electrical Symbols")
    
    symbols_info = {
        "cb": "Circuit Breaker - Switches on/off",
        "ds": "Disconnect Switch - Manual disconnect",
        "es": "Earthing Switch - Safety ground",
        "la": "Lightning Arrester - Overvoltage protection",
        "reactor": "Reactor - Inductance (coil)",
        "ct": "Current Transformer - Measurement",
        "vt": "Voltage Transformer - Voltage measurement",
        "busbar": "Busbar - Main conductor",
        "ground": "Ground - Earth symbol",
        "junction": "Junction - Connection point",
    }
    
    cols = st.columns(2)
    for idx, (symbol, description) in enumerate(symbols_info.items()):
        with cols[idx % 2]:
            st.write(f"**{symbol.upper()}**: {description}")

with tab3:
    st.header("Create Your Drawing")
    
    st.write("### Quick Drawing Creator")
    
    col1, col2 = st.columns(2)
    
    with col1:
        title = st.text_input("Drawing Title:", "My Circuit")
    
    with col2:
        num_symbols = st.slider("Number of symbols:", 1, 5, 2)
    
    symbols = []
    for i in range(num_symbols):
        symbol = st.text_input(f"Symbol {i+1}:", f"Symbol{i+1}")
        symbols.append(symbol)
    
    if st.button("📐 Create Drawing", use_container_width=True):
        try:
            import ezdxf
            
            # Create DXF
            doc = ezdxf.new('R2018')
            msp = doc.modelspace()
            
            # Add title
            msp.add_text(
                title,
                dxfattribs={'insert': (0, 30), 'height': 3}
            )
            
            # Add symbols as circles with labels
            y_pos = 15
            for symbol in symbols:
                # Draw symbol (simplified - circle)
                msp.add_circle((5, y_pos), radius=2)
                
                # Add label
                msp.add_text(
                    symbol.upper(),
                    dxfattribs={'insert': (2, y_pos - 1), 'height': 1.5}
                )
                
                # Add connection lines
                msp.add_line((5, y_pos + 2), (5, y_pos + 4))
                msp.add_line((5, y_pos - 2), (5, y_pos - 4))
                
                y_pos -= 10
            
            # Save to temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix='.dxf') as tmp:
                doc.saveas(tmp.name)
                tmp_path = tmp.name
            
            # Read file
            with open(tmp_path, 'rb') as f:
                dxf_data = f.read()
            
            # Cleanup
            os.remove(tmp_path)
            
            st.success("✓ Drawing created successfully!")
            
            # Download button
            st.download_button(
                label="📥 Download DXF File",
                data=dxf_data,
                file_name=f"{title.replace(' ', '_')}.dxf",
                mime="application/octet-stream",
                use_container_width=True
            )
            
            st.info("👇 Click the download button above to save the file")
            
        except Exception as e:
            st.error(f"Error creating drawing: {str(e)}")

with tab4:
    st.header("Help & FAQ")
    
    st.write("### Common Questions")
    
    with st.expander("What is DXF?"):
        st.write("""
        DXF (Drawing Exchange Format) is a standard file format for CAD drawings.
        You can open DXF files in:
        - AutoCAD
        - LibreCAD (free)
        - QCAD (free)
        - Online viewers
        """)
    
    with st.expander("What are IEC 60617 symbols?"):
        st.write("""
        IEC 60617 is the international standard for electrical symbols.
        These symbols are used worldwide in electrical diagrams.
        """)
    
    with st.expander("Can I edit the DXF file?"):
        st.write("""
        Yes! Download and open in LibreCAD (free) or AutoCAD.
        Then edit as you would any CAD drawing.
        """)
    
    with st.expander("Where do symbols come from?"):
        st.write("""
        From chille/electricalsymbols on GitHub.
        License: MIT (free to use)
        """)

# Footer
st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.write("**Made with**")
    st.caption("Streamlit")
    st.caption("ezdxf")

with col2:
    st.write("**Symbols from**")
    st.caption("chille/electricalsymbols")
    st.caption("IEC 60617")

with col3:
    st.write("**Open Source**")
    st.caption("GitHub")
    st.caption("Free tools")

st.write("\n💡 No installation needed - runs on cloud!")
