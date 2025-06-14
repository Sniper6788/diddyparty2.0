#step-1 install required libraries
from twilio.rest import Client

#step-2 twilio credentials
account_sid = 'ACdce93d3f0acc0058651b0c3258f330e0'
auth_token = 'bc0debb85837d9e2165ebab8c7731d8f'

client =Client(account_sid, auth_token)

#step 3

def dr():
    recipient_number = +9779742410240
    message_body = "Alert! Fire/Gas detected"
    try:
        message = client.messages.create(
            from_="whatsapp:+14155238886",
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f'Message sent successfully! Message SID{message.sid}')
    except Exception as e:
        print('An error occured')

# # name= input('Enter the recipient name = ')
# name= "Bhairab"
# recipient_number = +9779742410240
# # recipient_number = input('Enter the recipient whatsapp number with country code(eg, +123) ')
# # message_body = input(f'enter the message you want to send to {name}')
# message_body = "Alert! Fire detected"
# # step 5 parse date/time and calculate delay
# # date_str = input('enter the date to send the message (YYYY-MM-DD): ')  # e.g., 2024-12-30
# date_str = "2025-6-14"
# time_str = input('enter the time to send the message (HH:MM in 24hour format): ')

# # datetime
# schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
# current_datetime = datetime.now()

# # # calculate delay
# time_difference = schedule_datetime - current_datetime
# delay_seconds = time_difference.total_seconds() 

# if delay_seconds <=0:
#     print('The specified time is in the past. Please enter a future data and time: ')
# else:
#     print(f'Message schedued to be sent to {name} at {schedule_datetime}.')

#     time.sleep(delay_seconds)

#     send_whatsapp_message(recipient_number, message_body)

dr()
