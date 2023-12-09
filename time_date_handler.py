import datetime

class TimeDateHandler:
    def get_time_date(self, query):
        # Check if the query is asking for the current time
        if 'time' in query:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            return current_time

        # Check if the query is asking for the current date
        elif 'date' in query:
            current_date = datetime.datetime.now().strftime("%B %d, %Y")
            return current_date

        else:
            return "Sorry, I didn't understand your query. Please try again."
