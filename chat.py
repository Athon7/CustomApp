import streamlit as st
import time
import json

async def chat(initialtext, category):
    container1 = st.container(border=False, height=430)
    container2 = st.container(border=False, height=70)

    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": initialtext}]
        st.session_state.clearcache = False

    with container2:
        if category=="food_delivery":
            options = ['I want to order Italian food in California',
                        'Get me the menu for FoodieSpot9',
                        'I want to eat EggPlant parmagiana',
                        'I want to add 2 items of Spaghetti',
                        'Yes I want to proceed with my order for payment']
            init_prompt = st.selectbox(options=options,
                index=None,
                label="",
                label_visibility="hidden"
            )
            system_messages = ["""Here’s a great Italian restaurant in California you can order from:\n\n **FoodieSpot9**  \n- Location: New house 
            road, California, DE 20622  \n- Cuisines: Italian, 
            American  \n- Suitable for: Vegetarian, Non-Vegetarian, Vegan  \n- Popular Meals:  \n  - Breakfast: 
            Calamari, Toasted Ravioli  \n  - Lunch Mains: Eggplant Parmigiana, Spaghetti, 
            Cheese Pizza  \n  - Dessert: Tiramisu  \n- Rating: 4.5  \n- Description: “Enjoy abundant 
            portions of classic entrees the whole family craves like the Tour of Italy. Gather together 
            with the people you love over a meal worth sharing. When you're here, you're family in a quiet
            and peaceful home.”\n\nWhat would you like to order from the menu, or would you like to see 
            more options?""", 
            """Here’s the menu for **FoodieSpot9**:\n\n**Breakfast**\n- Calamari: $50\n- Toasted 
            Ravioli: $40\n\n**Lunch**\n- Main Course:\n    - Eggplant Parmigiana: $210\n  - Spaghetti: $120\n    - Cheese 
            Pizza: $170\n- Dessert:\n    - Tiramisu: $100\n\nWhat would 
            you like to order from FoodieSpot9?""", 
            "Great! I have added the following to your order:\n\n**Eggplant Parmagiana** (x1) $210\n\nWould you like to proceed with your order?",
            "I have added Spaghetti to your order. Here is your updated order\n\n**EggPlant Parmagiana** (x1): $210\n**Spaghetti** (x2): $120\n\nWould you like to proceed with your order?",
            "[{'name': 'FoodieSpot9', 'selected_items': [['eggplant parmigiana', 210], ['spaghetti', 120], ['spaghetti', 120]], 'amount': 450}]"
            ]
        elif category=="grocery_delivery":
            options = ['I want to order bread, oranges and chips',
                       'I want to order multigrain bread, Tortilla chips and oranges',
                       'I want one multigrain bread, 2 tortilla chips and 1 pack of oranges',
                       'I want to remove 1 tortilla chips',
                       'Yes please proceed with my order of multigrain bread, Tortilla chips and oranges']
            init_prompt = st.selectbox(options=options,
                index=None,
                label="",
                label_visibility="hidden"
            )
            system_messages = ["""Here are available options from Incart:\n\n**Oranges:**\n- Oranges 
            (Spain), 1kg, ₹20.49\n\n**Bread:**\n- White Bread (Wonder), 400g, ₹1.99\n- Brown Bread (Modern),
             400g, ₹2.19\n- Multigrain Bread (Harvest Gold), 400g, ₹29.49\n- Breadsticks (Local Bakery), 
             100g, ₹1.79\n\n**Chips:**\n- Potato Chips (Lays), 150g, ₹2.99\n- Tortilla Chips (Doritos), 
             200g, ₹30.49\n- Banana Chips (Haldiram), 100g, ₹2.49\n\nPlease select your preferred bread and 
             chips from the above options. Would you like to proceed with all three (oranges, bread, and 
             chips), or do you want to modify your selection?""",
             "Can you let me know the quantities for multigrain bread, tortilla chips and oranges?",
             "I have added the following to your order:\n\n**Multigrain Bread (Harvest Gold)** (x1): ₹50\n\n**Tortilla Chips (Doritos) (x2)**: ₹40\n\n**Oranges (Spain)** (x1): ₹120\n\nWould you like to proceed with your order?",
             "I have updated your order:\n\n**Multigrain Bread (Harvest Gold)** (x1): ₹50\n\n**Tortilla Chips (Doritos) (x1)**: ₹40\n\n**Oranges (Spain)** (x1): ₹120\n\nWould you like to proceed with your order?",
             "[{'name': 'Incart', 'selected_items': [['Multigrain Bread', 50.0], ['Tortilla Chips', 40.0], ['Orange', 120.0]], 'amount': 210.0}]"
             ]
        elif category=="travel_booking":
            options = ['I want to book travel from Mumbai to Hyderabad',
                'I want to book the bus',
                'I want to change the seat type to Non-AC sleeper',
                'Please book the flight']
            init_prompt = st.selectbox(options=options,
                index=None,
                label="",
                label_visibility="hidden"
            )
            system_messages = ["""Here are your travel options from Mumbai to Hyderabad:\n\n**Bus:**\n- Sharma 
            Travels — Sleeper AC, ₹1270, 16 seats available, departs at 22:00\n\n**Airplane:**\n- Vistara — Premium 
            Economy, ₹9900, 50 seats available, departs at 12:50\n- Go First — Economy, 
            ₹4900, 10 seats available, departs at 11:25\n\n**Train:**\n- Indian Railways — 3A (AC 3 Tier), 
            ₹1990, 104 seats available, departs at 12:30\n\nPlease let me know which option you’d like to 
            book!""", 
            "I have booked the following:\n\n**Sharma Travels** — Sleeper AC, ₹1270",
            "I have updated your booking:\n\n**Sharma Travels** — Sleeper Non-AC, ₹1270",
            "[{'transport_mode': 'airplane', 'origin': 'Mumbai', 'destination': 'Hyderabad', 'seat_type': 'Premium Economy', 'ticket_price': 9900, 'selected_items': [['airplane Premium Economy', 9900]], 'amount': 9900}]"]
        elif category=="recurring_bills":
            options =['I want to recharge my mobile talktime',
                'I want to pay for the 365 day plan',
                'Yes I would like to make the payment']
            init_prompt = st.selectbox(options=options,
                index=None,
                label="",
                label_visibility="hidden"
            )
            system_messages = ["""Here are the available talktime recharge plans:\n\n1. **Plan 1:** Unlimited
             talktime, valid for 365 days, ₹2000\n2. **Plan 2:** Unlimited data, valid for 30 days, ₹200\n3. **Plan 3:** 
             Unlimited data, valid for 75 days, ₹375\n\nPlease let me know which plan you 
             would like to choose for your recharge!""", 
             "I have added the following bill to pay:\n\n**Unlimited talktime** - 365 days (₹2000)\n\nDo you want to proceed with your order?",
             "[{'bill_name': 'mobile_recharge_bill', 'bill_details': '365 day unlimited talktime', 'selected_items': [['365 day unlimited talktime', '2000']], 'amount': '2000'}]"]

        instr = 'Hi there! Enter what you want to let me know here.'
        prompt = init_prompt 
        
    with container1:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])

        if prompt:
            with st.chat_message("user"):
                st.markdown(prompt)
                st.session_state.messages.append({"role":"user", "content":prompt})
            
            with st.chat_message("assistant"):
                writespace = st.empty()
                with st.spinner("Generating response...", show_time=False):
                    time.sleep(3)
                    response = system_messages[options.index(init_prompt)]
                
                try:
                    response = response.replace("\'",'\"')
                    decodedresp = json.loads(response)
                    if (type(decodedresp)==list):
                        st.session_state.messages = [{"role": "assistant", "content": initialtext}]
                        st.session_state.messages.append({"role":"assistant", "content":str(decodedresp)})
                        st.switch_page(st.Page("./pages/checkout.py"))
                        return
                except Exception as e:
                    pass
                content = ""
                for c in str(response):
                    content += c
                    time.sleep(0.001)
                    writespace.markdown(content)
                writespace.markdown(content)
                st.session_state.messages.append({"role":"assistant", "content":str(content)})
    return container1, container2
