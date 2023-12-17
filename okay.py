import streamlit as st

def main123():
    st.title("Financial Input Form")

    # Input for Income earned (monthly)
    income_earned = st.number_input("Enter Income Earned (monthly)", min_value=0.0)

    # Input for Health cost
    health_cost = st.number_input("Enter Health Cost", min_value=0.0)

    # Input for Debt cost (monthly)
    debt_cost = st.number_input("Enter Debt Cost (monthly)", min_value=0.0)
    
    # Input for Expenses (monthly)
    exp = st.number_input("Enter the Expenses (monthly)", min_value=0.0)

    # Input for Risk tolerance
    risk_tolerance = st.number_input("Enter Risk Tolerance (in percentage)", min_value=0.0)

    # Display the inputs
    if st.button("Display Inputs"):
        EF = (((income_earned - (exp + health_cost + debt_cost)) / (income_earned * 12)) + (risk_tolerance / 100)) / 2
        # st.write(EF)
        t=(EF*income_earned)
        st.write("The Emergency fund in percentage is ",EF)
        st.write(f"The Emergency fund amount from {income_earned} is {t}")

if __name__ == "__main__":
    main123()
