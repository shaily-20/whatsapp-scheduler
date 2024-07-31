import pywhatkit as kit
from datetime import datetime

now = datetime.now()

phone_number = input("Enter the phone number (in the form++at +1234567890): ")
message = input("Enter the message to send: ")
hour = int(input("Enter the hour (24-hour format) to send the message: "))
minute = int(input("Enter the minute to send the message: "))

if hour < now.hour or (hour == now.hour and minute <= now.minute):
    print("The time must be in the future. Please try again.")
else:
    # Send the message+91
    kit.sendwhatmsg(phone_number, message, hour, minute)
    print(f"Message will be sent to {phone_number} at {hour:02}:{minute:02}.")



'''Important Notes:
Make sure you have WhatsApp Web logged in on your default web browser.
The phone number should be in the international format, starting with + followed by the country code and the phone number.
The script opens a web browser tab for WhatsApp Web, waits for 20 seconds, and then sends the message. Adjustments to the script might be necessary based on your internet speed and system performance.
Example Usage:
Run the script.
Enter the phone number, message, hour, and minute when prompted.
Ensure the time is in the future; otherwise, it will prompt you to enter a valid time.
The script will automatically open WhatsApp Web and send the message at the specified time.
'''
