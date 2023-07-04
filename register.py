import streamlit as st
import pandas as pd
import currentCart



st.title("BEARDED PYRO ")
tax = 1.0625
st.divider()

input_placeholder = st.empty()

def submit():
    try:
        if st.session_state.widget.strip():  # check if the widget is not empty
            currentCart.addToCart(st.session_state.widget)
            
            st.session_state.widget = ''
    except Exception as e:
        
        st.write("An error occurred. Please enter manually.")



input_placeholder = st.empty()

if 'widget' not in st.session_state:
    st.session_state['widget'] = ''

input_placeholder.text_input("Enter", key='widget', value=st.session_state.widget, on_change=submit)

col1, col2, col3 = st.columns(3)

with col1:
    item_price = st.number_input('Enter Item price')
with col2:
    quantity = st.number_input('Enter Quantity', step=1, value=1)
with col3:
    if st.button('Add Item'):      
        currentCart.addToCartManual(quantity, item_price)
            
            
st.divider()
st.caption("CART")
df = pd.DataFrame(currentCart.currCart, columns=['Item ID', 'Price', 'Description', 'Quantity'])
editable_df = st.data_editor(df, use_container_width=True)

def reRun():
    global df
    global editable_df
    print(currentCart.currCart)
    currentCart.deleteCart()
    print(currentCart.currCart)
    df = pd.DataFrame(currentCart.currCart, columns=['Item ID', 'Price', 'Description', 'Quantity'])
    editable_df = st.data_editor(df, use_container_width=True)
    st.experimental_rerun()

if st.button('Update Total'):
        # Recalculate the total when the button is pressed.
    editable_df['Total Price'] = editable_df['Price'] * editable_df['Quantity']
    total_price = editable_df['Total Price'].sum()
    total_price_with_tax = total_price * tax

    st.header("TOTAL")
    st.subheader(f"${total_price:.2f} TOTAL")
    st.subheader(f"${total_price_with_tax:.2f} TOTAL + TAX")
st.write("##")
st.write("##")


col4, col5 = st.columns(2, gap="large")
with col4:
    if st.button('MILITARY'):
            editable_df['Total Price'] = editable_df['Price'] * editable_df['Quantity']
            total_price = editable_df['Total Price'].sum()
            discounted_price = total_price * 0.90
            total_price_with_tax = discounted_price * tax
            discount_amount = total_price - discounted_price
            tax = total_price_with_tax - discounted_price

            st.subheader(f"${total_price:.2f} TOTAL")
            st.subheader(f"${discount_amount:.2f} AMOUNT OFF")

            st.subheader(f"${discounted_price:.2f} TOTAL 10% OFF")
            st.subheader(f"${tax:.2f}  TAX")
            st.subheader(f"${total_price_with_tax:.2f} TOTAL + TAX")

with col5:
    if st.button('COUPON'):
            editable_df['Total Price'] = editable_df['Price'] * editable_df['Quantity']
            total_price = editable_df['Total Price'].sum()
            discounted_price = total_price * 0.85
            total_price = discounted_price * tax
            st.subheader(f"${discounted_price:.2f} TOTAL 15% OFF")
            st.subheader(f"${total_price:.2f} TOTAL + TAX")

st.divider()
if st.button("CLEAR ONLY/ NO SALE"):
    reRun()
    



